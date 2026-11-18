"""O build do lake pula, sem ler o bruto, o que já está em dia."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

import cvm_fetcher.lake as lake_mod  # noqa: E402
from cvm_fetcher.lake import converter  # noqa: E402

_CAD = "CNPJ_CIA;DENOM_SOCIAL\n00.000.000/0001-91;BANCO TESTE\n"
_FI = "CNPJ_FUNDO;DT_COMPTC;VL_TOTAL\n11.111.111/0001-11;2024-05-02;1000000.00\n"


def _bruto(tmp_path: Path) -> Path:
    raw = tmp_path / "raw"
    (raw / "cia-cad").mkdir(parents=True)
    (raw / "cia-cad" / "cad_cia_aberta@20240601.csv").write_text(_CAD)
    (raw / "fi-inf-diario").mkdir()
    with zipfile.ZipFile(
        raw / "fi-inf-diario" / "inf_diario_fi_2024-05@2.zip", "w"
    ) as z:
        z.writestr("inf_diario_fi_202405.csv", _FI)
        z.writestr("inf_diario_fi_202405_b.csv", _FI)
    return raw


@pytest.fixture
def leituras(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Registra toda leitura do bruto: CSV, cabeçalho, ZIP e extração."""
    vistas: list[str] = []

    def espia(nome: str, original):  # noqa: ANN001, ANN202
        def _f(*args, **kwargs):  # noqa: ANN002, ANN003
            vistas.append(nome)
            return original(*args, **kwargs)

        return _f

    monkeypatch.setattr(
        lake_mod, "_read_csv_with_codes", espia("csv", lake_mod._read_csv_with_codes)
    )
    monkeypatch.setattr(
        lake_mod, "decompress_archive", espia("zip", lake_mod.decompress_archive)
    )
    monkeypatch.setattr(
        lake_mod,
        "_detect_code_overrides",
        espia("cab", lake_mod._detect_code_overrides),
    )
    monkeypatch.setattr(zipfile, "ZipFile", espia("zipfile", zipfile.ZipFile))
    return vistas


@pytest.mark.parametrize(("dataset", "membros"), [("cia-cad", 1), ("fi-inf-diario", 2)])
def test_segunda_rodada_nao_le_o_bruto(
    tmp_path: Path, leituras: list[str], dataset: str, membros: int
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake, datasets=[dataset])
    assert not res.errors, res.errors
    assert (res.converted, res.skipped) == (membros, 0)
    assert leituras

    leituras.clear()
    res2 = converter.convert(raw, lake, datasets=[dataset])
    assert (res2.converted, res2.skipped, res2.errors) == (0, membros, [])
    assert leituras == []


def test_force_reconverte_lendo_o_bruto(tmp_path: Path, leituras: list[str]) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=["fi-inf-diario", "cia-cad"])

    leituras.clear()
    res = converter.convert(
        raw, lake, datasets=["fi-inf-diario", "cia-cad"], force=True
    )
    assert (res.converted, res.skipped, res.errors) == (3, 0, [])
    assert "csv" in leituras and "zip" in leituras


def test_bruto_novo_e_convertido_e_o_resto_pulado(
    tmp_path: Path, leituras: list[str]
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake)

    # CSV novo (conteúdo diferente, mesma chave) e ZIP novo de outro mês
    (raw / "cia-cad" / "cad_cia_aberta@20240602.csv").write_text(_CAD + _CAD[22:])
    with zipfile.ZipFile(
        raw / "fi-inf-diario" / "inf_diario_fi_2024-06@3.zip", "w"
    ) as z:
        z.writestr("inf_diario_fi_202406.csv", _FI)

    leituras.clear()
    res = converter.convert(raw, lake)
    assert not res.errors, res.errors
    # novo CSV e novo ZIP convertem; o ZIP de maio (2 membros) e o CSV velho pulam
    assert (res.converted, res.skipped) == (2, 3)
    assert leituras.count("zip") == 1  # só o ZIP de junho


def test_zip_com_conteudo_alterado_e_reconvertido(
    tmp_path: Path, leituras: list[str]
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=["fi-inf-diario"])
    zip_path = raw / "fi-inf-diario" / "inf_diario_fi_2024-05@2.zip"
    with zipfile.ZipFile(zip_path, "w") as z:  # mesmo nome, outro conteúdo
        z.writestr("inf_diario_fi_202405.csv", _FI + _FI.splitlines()[1] + "\n")

    leituras.clear()
    res = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert not res.errors, res.errors
    assert res.converted == 1
    assert "zip" in leituras
