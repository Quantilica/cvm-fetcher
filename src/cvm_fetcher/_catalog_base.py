"""Funções construtoras auxiliares do catálogo CVM.

Centraliza a construção de URLs determinísticas sobre o espelho Nginx
``https://dados.cvm.gov.br/dados/`` e a geração de entradas estáticas,
anuais e mensais (com janelas de cobertura plausíveis).
"""

from __future__ import annotations

import datetime as dt
from typing import Any

from .contracts import DatasetEntry

CVM_BASE_URL = "https://dados.cvm.gov.br/dados"
DEFAULT_END_YEAR_PAD = 1

# Janelas de cobertura por prefixo de arquivo (derivadas do espelho público).
WINDOW = 3  # anos/meses de janela padrão quando não especificado


def dataset_url(*path_segments: str) -> str:
    """Montar a URL determinística do arquivo no espelho da CVM.

    Args:
        *path_segments: Segmentos do caminho relativo a ``dados/``.

    Returns:
        str: URL absoluta do arquivo.
    """
    return f"{CVM_BASE_URL}/{'/'.join(s.strip('/') for s in path_segments)}"


def _partition_start_year(start: int | None) -> int:
    """Resolver o primeiro ano de cobertura da partição."""
    if start is not None:
        return start
    return dt.date.today().year - DEFAULT_END_YEAR_PAD


def static_dataset(
    group: str,
    *,
    slug: str,
    path: str,
    description: str = "",
) -> DatasetEntry:
    """Construir uma entrada estática (arquivo único sem partição).

    Args:
        group: Grupo canônico ao qual a entrada pertence.
        slug: Base do nome de arquivo (ex.: ``"cad_cia_aberta"``).
        path: Caminho relativo do arquivo no espelho (ex.:
            ``"CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"``).
        description: Descrição opcional.

    Returns:
        DatasetEntry: A entrada estática gerada.
    """
    filename = path.rsplit("/", 1)[-1]
    ext = filename.rsplit(".", 1)[-1] if "." in filename else "csv"
    return DatasetEntry(
        group=group,
        id=slug,
        url=dataset_url(path),
        ext=ext,
        description=description,
    )


def annual_datasets(
    group: str,
    *,
    slug: str,
    path_pattern: str,
    start_year: int | None = None,
    end_year: int | None = None,
    description: str = "",
    **extra: Any,
) -> list[DatasetEntry]:
    """Construir entradas com partição anual (``{prefixo}_{ano}.{ext}``).

    Args:
        group: Grupo canônico ao qual as entradas pertencem.
        slug: Base do nome de arquivo (ex.: ``"dfp_cia_aberta"``).
        path_pattern: Padrão do diretório/arquivo. Pode conter ``{year}``
            no nome do arquivo ou ser apenas o diretório ``DADOS/``.
        start_year: Primeiro ano coberto (padrão: ano atual - janela).
        end_year: Último ano coberto (padrão: ano atual).
        description: Descrição opcional aplicada às entradas.
        **extra: Metadados extras encaminhados às entradas.

    Returns:
        list[DatasetEntry]: Entradas anuais em ordem crescente de ano.

    Raises:
        ValueError: Se a janela ficar vazia ou negativa.
    """
    end = end_year or dt.date.today().year
    start = _partition_start_year(start_year)
    if end < start:
        msg = f"Janela anual inválida: {start} > {end}"
        raise ValueError(msg)

    entries = []
    for year in range(start, end + 1):
        if "{year}" in path_pattern:
            url = dataset_url(path_pattern.format(year=year))
        else:
            url = dataset_url(f"{path_pattern}/{slug}_{year}.zip")
        ext = url.rsplit(".", 1)[-1]
        entries.append(
            DatasetEntry(
                group=group,
                id=slug,
                url=url,
                ext=ext,
                description=description,
                year=year,
                **extra,
            )
        )
    return entries


def monthly_datasets(
    group: str,
    *,
    slug: str,
    path_pattern: str,
    start_year: int | None = None,
    end_year: int | None = None,
    months: tuple[int, ...] | None = None,
    description: str = "",
    **extra: Any,
) -> list[DatasetEntry]:
    """Construir entradas com partição mensal (``{prefixo}_{ano}{mes}.zip``).

    Args:
        group: Grupo canônico ao qual as entradas pertencem.
        slug: Base do nome de arquivo (ex.: ``"inf_diario_fi"``).
        path_pattern: Padrão do diretório ``DADOS/`` junto ao prefixo de
            arquivo com ``{year}`` e ``{month:02d}``, ou apenas o diretório
            do espelho.
        start_year: Primeiro ano coberto (padrão: ano atual - janela).
        end_year: Último ano coberto (padrão: ano atual).
        months: Meses a gerar **no ano de estreia** (``start_year``), 1-12.
            A partir do ano seguinte a série cobre o calendário completo —
            use-o para séries que nasceram no meio de um ano (ex.: FIAGRO em
            2025-05). Se None, todos os meses em todos os anos.
        description: Descrição opcional aplicada às entradas.
        **extra: Metadados extras encaminhados às entradas.

    Returns:
        list[DatasetEntry]: Entradas mensais em ordem cronológica.

    Raises:
        ValueError: Se a janela ficar vazia ou negativa.
    """
    today = dt.date.today()
    end = end_year or today.year
    start = _partition_start_year(start_year)
    if end < start:
        msg = f"Janela mensal inválida: {start} > {end}"
        raise ValueError(msg)

    full_year = tuple(range(1, 13))
    debut_months = full_year if months is None else tuple(months)

    entries = []
    cursor = dt.date(start, 1, 1)
    last = dt.date(end, 12, 1)
    while cursor <= last:
        year = cursor.year
        month = cursor.month
        # ``months`` descreve a estreia da série, não uma estação: só o ano
        # inicial é incompleto. Os anos seguintes geram os 12 meses.
        allowed = debut_months if year == start else full_year
        if year == today.year:
            last_month = min(max(allowed), today.month)
            if month > last_month:
                break
        if month not in allowed:
            cursor = dt.date(year + (month // 12), (month % 12) + 1, 1)
            continue
        if "{year}" in path_pattern:
            filename = path_pattern.format(year=year, month=month)
        else:
            filename = f"{path_pattern}/{slug}_{year}{month:02d}.zip"
        url = dataset_url(filename)
        ext = url.rsplit(".", 1)[-1]
        entries.append(
            DatasetEntry(
                group=group,
                id=slug,
                url=url,
                ext=ext,
                description=description,
                year=year,
                month=month,
                **extra,
            )
        )
        cursor = dt.date(year + (month // 12), (month % 12) + 1, 1)
    return entries
