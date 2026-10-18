"""Leitura de CSVs da CVM (requer o extra ``analysis``)."""

from __future__ import annotations

from pathlib import Path

try:
    import polars as pl
except ImportError as exc:
    raise ImportError(
        "cvm_fetcher.reader requer o extra 'analysis': "
        "uv add 'cvm-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

__all__ = ["read_csv_smart"]


def read_csv_smart(path: Path) -> pl.DataFrame:
    """Ler CSV da CVM com separador ``;`` e fallback de encoding.

    Args:
        path: Arquivo CSV.

    Returns:
        pl.DataFrame: Conteúdo do CSV (tenta UTF-8, depois latin-1).
    """
    try:
        return pl.read_csv(path, separator=";", encoding="utf-8")
    except Exception:
        return pl.read_csv(path, separator=";", encoding="latin-1")
