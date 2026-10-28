"""CSVs da CVM com aspas que fazem parte do texto."""

from pathlib import Path

import pytest

pl = pytest.importorskip("polars")

from cvm_fetcher.reader import read_csv_smart  # noqa: E402


def test_aspas_no_meio_do_texto(tmp_path: Path) -> None:
    src = tmp_path / "ipe_cia_aberta_2004.csv"
    src.write_text(
        "CNPJ_Companhia;Assunto;Data_Entrega\n"
        '00.000.000/0001-91;"Spin-off" da Contax;2004-05-10\n'
        '33.000.167/0001-01;Pagamento de "Juros sobre Capital Próprio";2004-06-01\n',
        encoding="latin-1",
    )
    df = read_csv_smart(src)
    assert df.height == 2
    assert df["Assunto"].to_list() == [
        '"Spin-off" da Contax',
        'Pagamento de "Juros sobre Capital Próprio"',
    ]
    assert df["Data_Entrega"].to_list() == ["2004-05-10", "2004-06-01"]


def test_csv_comum_continua_igual(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_text('a;b\n1;"x;y"\n', encoding="utf-8")
    assert read_csv_smart(src)["b"].to_list() == ["x;y"]
