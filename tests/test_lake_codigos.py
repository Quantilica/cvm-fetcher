"""Leitura de CSV da CVM com colunas de código preservadas como texto."""

from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

import polars as pl  # noqa: E402

from cvm_fetcher.lake import (  # noqa: E402
    _cast_code_columns,
    _detect_code_overrides,
    _read_csv_with_codes,
)
from cvm_fetcher.reader import read_csv_smart  # noqa: E402


def _csv(tmp_path: Path) -> Path:
    path = tmp_path / "cad_fi.csv"
    path.write_text(
        "CNPJ_FUNDO;CD_CVM;ISIN;VL_QUOTA\n"
        "00.123.456/0001-00;000123;BRABCDE12345;1,5\n"
        "11.222.333/0001-44;004567;BRXYZWV98765;2,5\n",
        encoding="latin-1",
    )
    return path


def test_helper_equivale_as_duas_etapas_antigas(tmp_path: Path) -> None:
    path = _csv(tmp_path)
    antigo = _cast_code_columns(
        read_csv_smart(path, schema_overrides=_detect_code_overrides(path))
    )
    novo = _read_csv_with_codes(path)
    assert novo.schema == antigo.schema
    assert novo.equals(antigo)


def test_codigos_mantem_zeros_a_esquerda(tmp_path: Path) -> None:
    df = _read_csv_with_codes(_csv(tmp_path))
    assert df.schema["CD_CVM"] == pl.String
    assert df["CD_CVM"].to_list() == ["000123", "004567"]
    assert df["CNPJ_FUNDO"][0] == "00.123.456/0001-00"
