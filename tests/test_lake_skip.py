"""O build do lake pula, sem ler o bruto, o que já está em dia."""

from __future__ import annotations

import builtins
import hashlib
import io
import json
import zipfile
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

import quantilica.core.manifests as manifests_mod  # noqa: E402
from quantilica.analytics.lake import LakeWriter  # noqa: E402

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
    _sidecars(raw)
    return raw


def _sidecars(raiz: Path) -> None:
    """Sidecar ``.manifest.json`` com o sha256 de cada bruto, como o fetcher grava:
    o hash do bruto sai dele, sem ler o arquivo."""
    for f in sorted(raiz.rglob("*")):
        if f.is_file() and not f.name.endswith(".manifest.json"):
            Path(f"{f}.manifest.json").write_text(
                json.dumps(
                    {
                        "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                        "size_bytes": f.stat().st_size,
                    }
                ),
                encoding="utf-8",
            )


@pytest.fixture
def leituras(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> list[str]:
    """Registra toda leitura do bruto: CSV, cabeçalho, ZIP, extração, abertura de
    arquivo do bruto (menos o sidecar, que se lê de propósito) e hash por leitura."""
    vistas: list[str] = []
    raiz = str(tmp_path / "raw")

    def do_bruto(arquivo) -> bool:  # noqa: ANN001
        nome = str(arquivo)
        return nome.startswith(raiz) and not nome.endswith(".manifest.json")

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
    monkeypatch.setattr(
        manifests_mod, "sha256_file", espia("hash", manifests_mod.sha256_file)
    )

    original_open = builtins.open
    original_io_open = io.open
    original_path_open = Path.open

    def open_espiado(file, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003, ANN202
        if do_bruto(file):
            vistas.append(f"open:{file}")
        return original_open(file, *args, **kwargs)

    def io_open_espiado(file, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003, ANN202
        if do_bruto(file):
            vistas.append(f"io.open:{file}")
        return original_io_open(file, *args, **kwargs)

    def path_open_espiado(self, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003, ANN202
        if do_bruto(self):
            vistas.append(f"Path.open:{self}")
        return original_path_open(self, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", open_espiado)
    monkeypatch.setattr(io, "open", io_open_espiado)
    monkeypatch.setattr(Path, "open", path_open_espiado)
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
    _sidecars(raw)

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
    _sidecars(raw)

    leituras.clear()
    res = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert not res.errors, res.errors
    assert res.converted == 1
    assert "zip" in leituras


def test_sem_sidecar_o_espiao_de_hash_dispara(
    tmp_path: Path, leituras: list[str]
) -> None:
    # Prova de que o espião funciona: sem sidecar o bruto é hasheado lendo-o.
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=["cia-cad"])
    for sidecar in raw.rglob("*.manifest.json"):
        sidecar.unlink()
    leituras.clear()
    converter.convert(raw, lake, datasets=["cia-cad"])
    assert "hash" in leituras


def test_zip_interrompido_completa_na_rodada_seguinte(
    tmp_path: Path, leituras: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """Falha no segundo membro na rodada 1; a 2 completa; a 3 pula sem ler o bruto."""
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    original = lake_mod._read_csv_with_codes

    def falha_no_b(path):  # noqa: ANN001, ANN202
        if path.name.endswith("_b.csv"):
            raise RuntimeError("disco cheio")
        return original(path)

    monkeypatch.setattr(lake_mod, "_read_csv_with_codes", falha_no_b)
    r1 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r1.converted, r1.skipped, len(r1.errors)) == (1, 0, 1)

    # sem a declaração, o Parquet do primeiro membro viraria pulo permanente
    monkeypatch.setattr(lake_mod, "_read_csv_with_codes", original)
    leituras.clear()
    r2 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r2.converted, r2.skipped, r2.errors) == (1, 1, [])
    assert leituras

    leituras.clear()
    r3 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r3.converted, r3.skipped, r3.errors) == (0, 2, [])
    assert leituras == []


def test_erro_deterministico_de_zip_volta_a_cada_build(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    original = lake_mod._read_csv_with_codes

    def falha_no_b(path):  # noqa: ANN001, ANN202
        if path.name.endswith("_b.csv"):
            raise ValueError("coluna inválida")
        return original(path)

    monkeypatch.setattr(lake_mod, "_read_csv_with_codes", falha_no_b)
    r1 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    r2 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert len(r1.errors) == len(r2.errors) == 1
    assert (r2.converted, r2.skipped) == (0, 1)


def test_lake_sem_declaracao_reconverte_uma_vez_e_depois_pula(
    tmp_path: Path, leituras: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    with monkeypatch.context() as m:  # lake gravado antes da declaração
        escrever = LakeWriter.write_polars
        conferir = LakeWriter.is_current

        def sem_decl(self, *a, **kw):  # noqa: ANN001, ANN002, ANN003, ANN202
            kw.pop("origin_outputs", None)
            return escrever(self, *a, **kw)

        def sem_decl_atual(self, *a, **kw):  # noqa: ANN001, ANN002, ANN003, ANN202
            kw.pop("origin_outputs", None)
            return conferir(self, *a, **kw)

        m.setattr(LakeWriter, "write_polars", sem_decl)
        m.setattr(LakeWriter, "is_current", sem_decl_atual)
        r0 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r0.converted, r0.skipped) == (2, 0)

    r1 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r1.converted, r1.skipped, r1.errors) == (2, 0, [])

    leituras.clear()
    r2 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r2.converted, r2.skipped, r2.errors) == (0, 2, [])
    assert leituras == []


def test_particao_do_nome_mudou_reconverte(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=["fi-inf-diario"])
    monkeypatch.setattr(
        lake_mod,
        "resolve_partitions",
        lambda _p: (["ano", "mes"], {"ano": "2024", "mes": "07"}),
    )
    r = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r.converted, r.skipped, r.errors) == (2, 0, [])


def _tags_do_lake(lake: Path) -> set[str]:
    import pyarrow.parquet as pq

    return {
        pq.read_metadata(f).metadata[b"quantilica.converter"].decode()
        for f in (lake / "cvm" / "fi-inf-diario").rglob("*.parquet")
    }


def test_revisao_do_layout_diferente_reconverte_o_zip(
    tmp_path: Path, leituras: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """Outra ``LAKE_LAYOUT_REVISION`` no rodapé: o ZIP é aberto e regravado (e o
    rodapé passa à nova revisão); com a mesma, pula sem ler o bruto."""
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    r1 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r1.converted, r1.skipped, r1.errors) == (2, 0, [])
    assert _tags_do_lake(lake) == {
        f"cvm-fetcher layout-{lake_mod.LAKE_LAYOUT_REVISION}"
    }

    leituras.clear()
    r2 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r2.converted, r2.skipped, r2.errors) == (0, 2, [])
    assert leituras == []

    monkeypatch.setattr(
        lake_mod, "LAKE_LAYOUT_REVISION", lake_mod.LAKE_LAYOUT_REVISION + 1
    )
    r3 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r3.converted, r3.skipped, r3.errors) == (2, 0, [])
    assert leituras
    assert _tags_do_lake(lake) == {
        f"cvm-fetcher layout-{lake_mod.LAKE_LAYOUT_REVISION}"
    }

    leituras.clear()
    r4 = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r4.converted, r4.skipped, r4.errors) == (0, 2, [])
    assert leituras == []


def test_versao_do_pacote_nao_reconverte(
    tmp_path: Path, leituras: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=["fi-inf-diario"])
    monkeypatch.setattr(lake_mod, "__version__", "99.0.0")
    leituras.clear()
    r = converter.convert(raw, lake, datasets=["fi-inf-diario"])
    assert (r.converted, r.skipped, r.errors) == (0, 2, [])
    assert leituras == []
