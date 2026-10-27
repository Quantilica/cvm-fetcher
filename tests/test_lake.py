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
    assert df_fi["ano"][0] == "2024"
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
