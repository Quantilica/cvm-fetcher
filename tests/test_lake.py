"""Tests for Hive lake conversion of CVM open data."""

from __future__ import annotations

import zipfile
from importlib.metadata import entry_points
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402
from typer.testing import CliRunner  # noqa: E402

from cvm_fetcher.lake import (  # noqa: E402
    SOURCE_ID,
    converter,
    resolve_group,
    resolve_partitions,
)
from cvm_fetcher.plugin import app  # noqa: E402


def test_entry_point_registered() -> None:
    eps = entry_points(group="quantilica.lake")
    matches = [ep for ep in eps if ep.name == "cvm"]
    assert len(matches) == 1
    loaded = matches[0].load()
    assert loaded is converter
    assert loaded.source_id == SOURCE_ID


def test_resolve_group() -> None:
    p = Path("fi-inf-diario/inf_diario_fi_2026-10@20261003.zip")
    assert resolve_group(p) == "fi-inf-diario"
    assert resolve_group(Path("cia-cad/cad_cia_aberta@20261003.csv")) == "cia-cad"
    assert resolve_group(Path("unknown/file.csv")) is None


def test_resolve_partitions() -> None:
    keys_ym, vals_ym = resolve_partitions(Path("inf_diario_fi_2024-05@20240601.zip"))
    assert keys_ym == ["ano", "mes"]
    assert vals_ym == {"ano": "2024", "mes": "05"}

    keys_y, vals_y = resolve_partitions(Path("dfp_cia_aberta_2024@20240601.zip"))
    assert keys_y == ["ano"]
    assert vals_y == {"ano": "2024"}

    keys_empty, vals_empty = resolve_partitions(Path("cad_cia_aberta@20240601.csv"))
    assert keys_empty == []
    assert vals_empty == {}


def test_converter_datasets() -> None:
    datasets = converter.datasets()
    assert "fi-inf-diario" in datasets
    assert "cia-dfp" in datasets
    assert "cia-cad" in datasets


def test_convert_end_to_end(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"

    # 1. Unpartitioned CSV in cia-cad
    cad_dir = raw_dir / "cia-cad"
    cad_dir.mkdir(parents=True)
    cad_csv = cad_dir / "cad_cia_aberta@20240601.csv"
    cad_csv.write_text(
        "CNPJ_CIA;DENOM_SOCIAL;SIT\n00.000.000/0001-91;BANCO TESTE;ATIVO\n",
        encoding="utf-8",
    )

    # 2. Partitioned ZIP with inner CSV in fi-inf-diario
    fi_dir = raw_dir / "fi-inf-diario"
    fi_dir.mkdir(parents=True)
    fi_zip = fi_dir / "inf_diario_fi_2024-05@20240601.zip"
    with zipfile.ZipFile(fi_zip, "w") as z:
        z.writestr(
            "inf_diario_fi_202405.csv",
            "CNPJ_FUNDO;DT_COMPTC;VL_TOTAL\n11.111.111/0001-11;2024-05-02;1000000.00\n",
        )

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors, res.errors
    assert res.converted == 2
    assert res.skipped == 0

    # Check unpartitioned cia-cad
    cad_lake = lake_dir / SOURCE_ID / "cia-cad"
    assert check_dataset(cad_lake) == []
    df_cad = scan_dataset(cad_lake).collect()
    assert df_cad.height == 1
    assert "CNPJ_CIA" in df_cad.columns

    # Check partitioned fi-inf-diario
    fi_lake = lake_dir / SOURCE_ID / "fi-inf-diario"
    assert check_dataset(fi_lake) == []
    df_fi = scan_dataset(fi_lake).collect()
    assert df_fi.height == 1
    assert "ano" in df_fi.columns
    assert "mes" in df_fi.columns
    assert df_fi["ano"][0] == 2024
    assert df_fi["mes"][0] == "05"

    # Second pass skips
    res2 = converter.convert(raw_dir, lake_dir)
    assert not res2.errors
    assert res2.converted == 0
    assert res2.skipped == 2


def test_cli_convert(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    cad_dir = raw_dir / "cia-cad"
    cad_dir.mkdir(parents=True)
    (cad_dir / "cad_cia_aberta@20240601.csv").write_text(
        "CNPJ_CIA;DENOM_SOCIAL\n00.000.000/0001-91;TESTE\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "convert",
            "-i",
            str(raw_dir),
            "--lake",
            str(lake_dir),
            "--dataset",
            "cia-cad",
        ],
    )
    assert result.exit_code == 0, result.output
    assert (lake_dir / SOURCE_ID / "cia-cad").exists()


def _zip(path: Path, members: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as z:
        for name, text in members.items():
            z.writestr(name, text)


def test_cadastro_com_varios_snapshots_converte_so_o_mais_novo(
    tmp_path: Path,
) -> None:
    """Cadastro (ZIP com vários CSVs, sem partição) guardado em três datas."""
    raw = tmp_path / "raw" / "adm-cart-cad"
    for day, nome in (("27", "ANTIGO"), ("28", "MEIO"), ("29", "NOVO")):
        _zip(
            raw / f"cad_adm_cart@202610{day}.zip",
            {
                "cad_adm_cart_pf.csv": f"CPF;NOME\n1;{nome}\n",
                "cad_adm_cart_pj.csv": f"CNPJ;NOME\n2;{nome}\n",
            },
        )
    lake = tmp_path / "lake"

    res1 = converter.convert(tmp_path / "raw", lake)
    assert not res1.errors, res1.errors
    assert res1.converted == 2  # dois CSVs do snapshot vigente
    assert res1.skipped == 2  # dois snapshots superados

    res2 = converter.convert(tmp_path / "raw", lake)
    assert not res2.errors, res2.errors
    assert res2.converted == 0
    assert res2.skipped == 4

    df = scan_dataset(lake / SOURCE_ID / "adm-cart-cad").collect()
    assert set(df["NOME"].to_list()) == {"NOVO"}


def test_historico_com_snapshots_na_mesma_particao(tmp_path: Path) -> None:
    """Série mensal baixada em duas datas e um mês só com uma data."""
    raw = tmp_path / "raw" / "fi-entrega"
    _zip(
        raw / "fi_entrega_documento_2026-09@20261027.zip",
        {"fi_entrega_documento_202609.csv": "CNPJ;DOC\n1;velho\n"},
    )
    _zip(
        raw / "fi_entrega_documento_2026-09@20261029.zip",
        {"fi_entrega_documento_202609.csv": "CNPJ;DOC\n1;novo\n"},
    )
    _zip(
        raw / "fi_entrega_documento_2026-08@20261024.zip",
        {"fi_entrega_documento_202608.csv": "CNPJ;DOC\n2;unico\n"},
    )
    lake = tmp_path / "lake"

    res1 = converter.convert(tmp_path / "raw", lake)
    assert not res1.errors, res1.errors
    assert (res1.converted, res1.skipped) == (2, 1)

    res2 = converter.convert(tmp_path / "raw", lake)
    assert not res2.errors, res2.errors
    assert (res2.converted, res2.skipped) == (0, 3)

    df = scan_dataset(lake / SOURCE_ID / "fi-entrega").collect()
    assert sorted(df["DOC"].to_list()) == ["novo", "unico"]


def test_snapshot_novo_substitui_o_anterior_uma_vez(tmp_path: Path) -> None:
    """Quando sai um snapshot novo, ele é convertido uma vez e depois pulado."""
    raw = tmp_path / "raw" / "cia-cad"
    raw.mkdir(parents=True)
    (raw / "cad_cia_aberta@20261027.csv").write_text("CNPJ;SIT\n1;A\n")
    lake = tmp_path / "lake"
    assert converter.convert(tmp_path / "raw", lake).converted == 1

    (raw / "cad_cia_aberta@20261028.csv").write_text("CNPJ;SIT\n1;B\n")
    res = converter.convert(tmp_path / "raw", lake)
    assert (res.converted, res.skipped) == (1, 1)
    res = converter.convert(tmp_path / "raw", lake)
    assert (res.converted, res.skipped) == (0, 2)

    df = scan_dataset(lake / SOURCE_ID / "cia-cad").collect()
    assert df["SIT"].to_list() == ["B"]


def test_securit_cri_alias_and_code_columns(tmp_path: Path) -> None:
    import polars as pl
    from quantilica.core.lake import DatasetDescriptor

    raw = tmp_path / "raw" / "securit-cri"
    raw.mkdir(parents=True)
    (raw / "securit_cri_2024@20240601.csv").write_text(
        "CNPJ_EMISSOR;CD_CVM;CODIGO_ISIN;DENOM_SOCIAL\n"
        "00123456000199;01234;BRCRI0000001;EMISSORA TESTE\n",
        encoding="utf-8",
    )
    lake = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake, datasets=["securit-cri"])
    assert not res.errors, res.errors
    assert res.converted == 1

    ds_dir = lake / SOURCE_ID / "securit-cri"
    assert check_dataset(ds_dir) == []
    desc = DatasetDescriptor.load(ds_dir)
    assert desc.alias == "securitizacao_cri"

    df = scan_dataset(ds_dir).collect()
    assert df["CNPJ_EMISSOR"].dtype == pl.String
    assert df["CD_CVM"].dtype == pl.String
    assert df["CODIGO_ISIN"].dtype == pl.String
    assert df["CD_CVM"][0] == "01234"


def test_convert_by_canonical_alias_cvm(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "securit-cri"
    raw.mkdir(parents=True)
    (raw / "securit_cri_2023@20240101.csv").write_text(
        "CNPJ_EMISSOR;CD_CVM;CODIGO_ISIN;DENOM_SOCIAL\n"
        "00123456000199;01234;BRCRI0000001;EMISSORA TESTE\n",
        encoding="utf-8",
    )
    lake = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake, datasets=["securitizacao_cri"])
    assert not res.errors, res.errors
    assert res.converted == 1


def test_convert_unknown_dataset_cvm(tmp_path: Path) -> None:
    res = converter.convert(tmp_path, tmp_path, datasets=["desconhecido_cvm"])
    assert len(res.errors) == 1
    assert "dataset desconhecido: desconhecido_cvm" in res.errors[0]
