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
    errors = []
    # A CVM não delimita campos com aspas: elas fazem parte do texto ("Spin-off" da
    # Contax, no Assunto do IPE). Lidas como delimitador, desalinham as colunas.
    for quote in ('"', None):
        for encoding in ("utf-8", "latin-1"):
            try:
                return pl.read_csv(
                    path, separator=";", encoding=encoding, quote_char=quote
                )
            except Exception as exc:  # noqa: BLE001 - próxima combinação
                errors.append(exc)
    raise errors[-1]
