"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

from quantilica.cli.sdk import FetcherApp, make_resolve_groups

from .catalog import GROUP_ALIASES as CATALOG_GROUP_ALIASES
from .catalog import GROUPS, MACRO_ALIASES, list_canonical_datasets
from .contracts import DatasetEntry
from .storage import DEFAULT_OUTPUT, DataRepository

__all__ = ["app", "fetcher", "path_builder", "resolve_groups"]

# Resolver canônico — make_resolve_groups espera alias -> lista de ids canônicos.
resolve_groups = make_resolve_groups(
    {gid: info.to_dict() for gid, info in GROUPS.items()},
    MACRO_ALIASES,
)


def sdk_list_datasets(group: str) -> list[dict[str, Any]]:
    """Hook de catálogo exigido pelo ``FetcherApp``.

    Recebe sempre um id canônico (o ``FetcherApp`` resolve alias → grupos),
    então consulta o catálogo sem expansão de macro-alias — expandir aqui
    duplicaria entradas de grupos que também são macro (``ofertas``).

    Args:
        group: Grupo canônico (id já resolvido pelo SDK).

    Returns:
        list[dict[str, Any]]: Entradas no schema canônico do SDK.
    """
    entries: list[DatasetEntry] = list_canonical_datasets(group)
    return [entry.to_dict() for entry in entries]


def path_builder(
    output_dir: Path, entry: dict[str, Any], last_modified: dt.date | None
) -> Path:
    """Construir o caminho de destino de uma entrada.

    Args:
        output_dir: Diretório raiz de saída.
        entry: Entrada de dataset no schema do SDK.
        last_modified: Data de modificação remota (carimbo).

    Returns:
        Path: Caminho destino ``{output}/{grupo}/{arquivo carimbado}``.
    """
    return DataRepository(output_dir).path_for_entry(entry, last_modified=last_modified)


fetcher = FetcherApp(
    name="cvm-fetcher",
    help="Dados abertos da CVM (Comissão de Valores Mobiliários).",
    groups_dict={gid: info.to_dict() for gid, info in GROUPS.items()},
    aliases_dict=CATALOG_GROUP_ALIASES,
    list_datasets=sdk_list_datasets,
    path_builder=path_builder,
    default_output=Path(DEFAULT_OUTPUT),
)

app = fetcher.app


def _convert_impl(input_dir: Path, output_dir: Path) -> int:
    """Converter CSVs (diretos ou dentro de ZIPs) para Parquet.

    Args:
        input_dir: Diretório de origem com dados brutos (``--output`` do
            ``sync``).
        output_dir: Diretório de destino dos Parquet.

    Returns:
        int: Quantidade de Parquet gerados.

    Raises:
        ImportError: Se o extra ``analysis`` não estiver instalado.
    """
    from .wrangling import convert_all

    return convert_all(input_dir, output_dir)


@fetcher.command_convert
def cmd_convert(input: Path, output: Path) -> None:
    """Corpo de conversão chamado pelo ``convert`` gerado pelo SDK.

    Args:
        input: Diretório de origem com arquivos brutos.
        output: Diretório de destino para os Parquet.
    """
    # O ImportError de polars/analysis não é tratado aqui: o SDK já o
    # converte em saída amigável (sdk.py, ``command_convert``).
    converted = _convert_impl(input, output)
    from quantilica.cli.ui import get_console

    get_console().print(
        f"[bold]{converted}[/bold] Parquet(s) gerado(s) em [dim]{output}[/dim]."
    )
