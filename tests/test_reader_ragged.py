"""CSVs da CVM com ``;`` dentro de um campo de texto, sem aspas."""

from __future__ import annotations

import logging
import zipfile
from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402

from cvm_fetcher.lake import SOURCE_ID, converter  # noqa: E402
from cvm_fetcher.reader import read_csv_smart  # noqa: E402

# Recorte real de inf_mensal_cra_cedente_devedor_2026.csv (CVM, CRA): o campo CNPJ
# é texto livre e uma linha traz "; " no meio dele.
CEDENTE_DEVEDOR = (
    "CNPJ_Emissora;Codigo_Identificacao_Certificado;Data_Referencia;Versao;Tipo;"
    "CNPJ;Percentual\r\n"
    "02.773.542/0001-22;BRRBRACRA1Z6;2026-04-01;1;Devedor;"
    "Assembleia publicada em 06042026, 13042026, 170420;1.00000000000000000000\r\n"
    "02.773.542/0001-22;BRRBRACRA1Z6;2026-05-01;1;Cedente;"
    "93071116934 0058907599303461921963;1.00000000000000000000\r\n"
    "02.773.542/0001-22;BRRBRACRA1Z6;2026-05-01;1;Devedor;"
    "Ata da Assembleia (27052026, 04052026); Sumário da;1.00000000000000000000\r\n"
    "02.773.542/0001-22;BRRBRACRA1Z6;2026-06-01;1;Cedente;"
    "12.345.678/0001-95;0.5\r\n"
)


def test_ponto_e_virgula_no_texto_volta_para_a_coluna(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    src = tmp_path / "inf_mensal_cra_cedente_devedor_2026.csv"
    src.write_bytes(CEDENTE_DEVEDOR.encode("latin-1"))

    with caplog.at_level(logging.WARNING, logger="cvm_fetcher.reader"):
        df = read_csv_smart(src)

    assert df.columns == [
        "CNPJ_Emissora",
        "Codigo_Identificacao_Certificado",
        "Data_Referencia",
        "Versao",
        "Tipo",
        "CNPJ",
        "Percentual",
    ]
    assert df.height == 4  # nenhuma linha descartada
    assert df["CNPJ"].to_list() == [
        "Assembleia publicada em 06042026, 13042026, 170420",
        "93071116934 0058907599303461921963",
        "Ata da Assembleia (27052026, 04052026); Sumário da",
        "12.345.678/0001-95",
    ]
    assert df["Tipo"].to_list() == ["Devedor", "Cedente", "Devedor", "Cedente"]
    assert df["Percentual"].to_list() == [1.0, 1.0, 1.0, 0.5]
    assert df["Versao"].dtype == pl.Int64
    assert df["Percentual"].dtype == pl.Float64
    assert any(
        "1 linha(s) com campos a mais" in r.message and "CNPJ" in r.message
        for r in caplog.records
    )


def test_excesso_na_coluna_de_texto_com_valores_numericos_e_data(
    tmp_path: Path,
) -> None:
    src = tmp_path / "x.csv"
    src.write_text(
        "id;obs;valor;data\n"
        "1;ok;10.5;2026-01-01\n"
        "2;com;ponto;e;virgula;3.0;2026-01-02\n"
        "3;outra;7;2026-01-03\n",
        encoding="utf-8",
    )
    df = read_csv_smart(src)
    assert df["obs"].to_list() == ["ok", "com;ponto;e;virgula", "outra"]
    assert df["valor"].to_list() == [10.5, 3.0, 7.0]
    assert df["data"].to_list() == ["2026-01-01", "2026-01-02", "2026-01-03"]


def test_zip_com_varios_csvs_converte_todos_inclusive_o_defeituoso(
    tmp_path: Path,
) -> None:
    raw = tmp_path / "raw" / "securit-cra"
    raw.mkdir(parents=True)
    with zipfile.ZipFile(raw / "inf_mensal_cra_2026@20261025.zip", "w") as z:
        z.writestr("inf_mensal_cra_geral_2026.csv", "CNPJ;NOME\n1;A\n2;B\n")
        z.writestr(
            "inf_mensal_cra_cedente_devedor_2026.csv",
            CEDENTE_DEVEDOR.encode("latin-1"),
        )
    lake = tmp_path / "lake"

    res = converter.convert(tmp_path / "raw", lake)

    assert not res.errors, res.errors
    assert res.converted == 2
    dataset = lake / SOURCE_ID / "securit-cra"
    assert check_dataset(dataset) == []
    df = scan_dataset(dataset).collect()
    assert df.height == 6  # 2 do geral + 4 do cedente_devedor
