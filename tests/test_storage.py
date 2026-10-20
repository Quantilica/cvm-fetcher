"""Testes do repositório de dados (storage) do cvm-fetcher."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from cvm_fetcher.catalog import list_datasets
from cvm_fetcher.storage import DataRepository, build_stamped_filename, stamp_filename

_STAMP = dt.date(2026, 10, 3)


def test_static_path(tmp_path: Path) -> None:
    """Entradas estáticas recebem ``{slug}@{stamp}.{ext}``."""
    entry = next(e for e in list_datasets("cia-cad") if e.id == "cad_cia_aberta")
    repo = DataRepository(tmp_path)
    path = repo.path_for_entry(entry.to_dict(), last_modified=_STAMP)
    assert path == tmp_path / "cia-cad/cad_cia_aberta@20261003.csv"


def test_static_path_without_last_modified(tmp_path: Path) -> None:
    """Sem carimbo, o nome fica ``{slug}.{ext}``."""
    entry = next(e for e in list_datasets("ofertas") if e.id == "oferta_distribuicao")
    repo = DataRepository(tmp_path)
    path = repo.path_for_entry(entry.to_dict(), last_modified=None)
    assert path == tmp_path / "ofertas/oferta_distribuicao.zip"


def test_annual_path(tmp_path: Path) -> None:
    """Entradas anuais recebem ``{slug}_{ano}@{stamp}.{ext}``."""
    entry = next(e for e in list_datasets("cia-dfp") if e.year == 2026)
    repo = DataRepository(tmp_path)
    path = repo.path_for_entry(entry.to_dict(), last_modified=_STAMP)
    assert path == tmp_path / "cia-dfp/dfp_cia_aberta_2026@20261003.zip"


def test_monthly_path(tmp_path: Path) -> None:
    """Entradas mensais recebem ``{slug}_{ano}-{mes:02d}@{stamp}.{ext}``."""
    entry = next(
        e for e in list_datasets("fi-inf-diario") if e.year == 2026 and e.month == 10
    )
    repo = DataRepository(tmp_path)
    path = repo.path_for_entry(entry.to_dict(), last_modified=_STAMP)
    assert path == tmp_path / "fi-inf-diario/inf_diario_fi_2026-10@20261003.zip"


def test_quarterly_fii_monthly_zip_annual_partition(tmp_path: Path) -> None:
    """FII mensal (ZIP anual) usa particionamento anual no repositório."""
    entry = next(e for e in list_datasets("fii-inf-mensal") if e.year == 2026)
    repo = DataRepository(tmp_path)
    path = repo.path_for_entry(entry.to_dict(), last_modified=_STAMP)
    assert path == tmp_path / "fii-inf-mensal/inf_mensal_fii_2026@20261003.zip"


def test_helpers_reexport() -> None:
    """Reexports de stamp helpers continuam disponíveis no módulo."""
    assert stamp_filename("cad_fi", "csv", _STAMP) == "cad_fi@20261003.csv"
    assert (
        build_stamped_filename("extrato_fi", 2026, ext="csv", timestamp=_STAMP)
        == "extrato_fi_2026@20261003.csv"
    )


def test_entry_without_partition_fields_defaults(tmp_path: Path) -> None:
    """Faltando campos, o path degrada graciosamente (defaults)."""
    repo = DataRepository(tmp_path)
    path = repo.path_for_entry({"id": "foo", "ext": "csv"}, last_modified=None)
    # Sem "group", a raiz passa a agrupar em "datasets" por contrato do SDK.
    assert path == tmp_path / "foo/foo.csv"


def test_targets_are_disjoint_by_group_directory(tmp_path: Path) -> None:
    """Grupos mapeiam para subdiretórios distintos."""
    repo = DataRepository(tmp_path)
    dfp = next(e for e in list_datasets("cia-dfp") if e.year == 2026)
    itr = next(e for e in list_datasets("cia-itr") if e.year == 2026)
    assert repo.path_for_entry(dfp.to_dict()).parent.name == "cia-dfp"
    assert repo.path_for_entry(itr.to_dict()).parent.name == "cia-itr"
    assert (
        repo.path_for_entry(dfp.to_dict()).parent
        != repo.path_for_entry(itr.to_dict()).parent
    )


def test_invalid_root_raises(tmp_path: Path) -> None:
    """Repositório recusa raiz inválida (arquivo não diretório)."""
    file_root = tmp_path / "arquivo.txt"
    file_root.write_text("x")
    with pytest.raises((FileExistsError, NotADirectoryError, OSError)):
        DataRepository(file_root)
