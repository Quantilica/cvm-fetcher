"""Catálogo de fundos estruturados (FII, FIDC, FIAGRO e FIP).

Macro-domínio ``estruturados``: informes mensais, trimestrais, anuais e
demonstrações financeiras de Fundos Imobiliários (FII), Direitos Creditórios
(FIDC), Cadeias Agroindustriais (FIAGRO) e Participações (FIP).
"""

from __future__ import annotations

from ._catalog_base import annual_datasets, monthly_datasets
from .contracts import DatasetEntry, GroupInfo

macro = "estruturados"

# Primeiro ano/mês publicado no espelho (confirmado via servidor).
_FII_START = 2016
_FIDC_START = (2025, 1)
_FIAGRO_START = (2025, 5)
_FIP_TRIM_START = 2010
# A série trimestral foi descontinuada ao fim de 2023: a partir de 2024 a CVM
# publica apenas a quadrimestral (``_FIP_QUADRIM``). Estender a trimestral até
# o ano corrente geraria URLs com HTTP 404 permanente.
_FIP_TRIM_END = 2023
_FIP_QUADRIM_START = 2024

_FII_INF_MENSAL: list[DatasetEntry] = annual_datasets(
    "fii-inf-mensal",
    slug="inf_mensal_fii",
    path_pattern="FII/DOC/INF_MENSAL/DADOS/inf_mensal_fii_{year}.zip",
    start_year=_FII_START,
    description="Informe mensal dos fundos imobiliários (ZIP anual).",
)

_FII_INF_TRIM: list[DatasetEntry] = annual_datasets(
    "fii-inf-trim",
    slug="inf_trimestral_fii",
    path_pattern="FII/DOC/INF_TRIMESTRAL/DADOS/inf_trimestral_fii_{year}.zip",
    start_year=_FII_START,
    description="Informe trimestral dos fundos imobiliários (ZIP anual).",
)

_FII_INF_ANUAL: list[DatasetEntry] = annual_datasets(
    "fii-inf-anual",
    slug="inf_anual_fii",
    path_pattern="FII/DOC/INF_ANUAL/DADOS/inf_anual_fii_{year}.zip",
    start_year=_FII_START,
    description="Informe anual dos fundos imobiliários (ZIP anual).",
)

_FII_DFIN: list[DatasetEntry] = annual_datasets(
    "fii-dfin",
    slug="dfin_fii",
    path_pattern="FII/DOC/DFIN/DADOS/dfin_fii_{year}.csv",
    start_year=_FII_START,
    description="Demonstrações financeiras dos fundos imobiliários.",
)

_FIDC_INF_MENSAL: list[DatasetEntry] = monthly_datasets(
    "fidc-inf-mensal",
    slug="inf_mensal_fidc",
    path_pattern="FIDC/DOC/INF_MENSAL/DADOS/inf_mensal_fidc_{year}{month:02d}.zip",
    start_year=_FIDC_START[0],
    months=tuple(range(_FIDC_START[1], 13)),
    description="Informe mensal dos fundos de direitos creditórios.",
)

_FIAGRO_INF_MENSAL: list[DatasetEntry] = monthly_datasets(
    "fiagro-inf-mensal",
    slug="inf_mensal_fiagro",
    path_pattern=(
        "FIAGRO/DOC/INF_MENSAL/DADOS/inf_mensal_fiagro_{year}{month:02d}.zip"
    ),
    start_year=_FIAGRO_START[0],
    months=tuple(range(_FIAGRO_START[1], 13)),
    description="Informe mensal das cadeias agroindustriais (FIAGRO).",
)

_FIP_TRIM: list[DatasetEntry] = annual_datasets(
    "fip-inf",
    slug="inf_trimestral_fip",
    path_pattern="FIP/DOC/INF_TRIMESTRAL/DADOS/inf_trimestral_fip_{year}.csv",
    start_year=_FIP_TRIM_START,
    end_year=_FIP_TRIM_END,
    description="Informe trimestral dos fundos de participação (CSV).",
)

_FIP_QUADRIM: list[DatasetEntry] = annual_datasets(
    "fip-inf",
    slug="inf_quadrimestral_fip",
    path_pattern=("FIP/DOC/INF_QUADRIMESTRAL/DADOS/inf_quadrimestral_fip_{year}.csv"),
    start_year=_FIP_QUADRIM_START,
    description="Informe quadrimestral dos fundos de participação (CSV).",
)

_ENTRIES: dict[str, list[DatasetEntry]] = {
    "fii-inf-mensal": _FII_INF_MENSAL,
    "fii-inf-trim": _FII_INF_TRIM,
    "fii-inf-anual": _FII_INF_ANUAL,
    "fii-dfin": _FII_DFIN,
    "fidc-inf-mensal": _FIDC_INF_MENSAL,
    "fiagro-inf-mensal": _FIAGRO_INF_MENSAL,
    "fip-inf": [*dict.fromkeys(_FIP_TRIM + _FIP_QUADRIM)],
}

GROUPS: dict[str, GroupInfo] = {
    "fii-inf-mensal": GroupInfo(
        id="fii-inf-mensal",
        name="Informe Mensal de FII",
        description="Informe mensal consolidado por ano (ZIP).",
        macro=macro,
        partition="annual",
    ),
    "fii-inf-trim": GroupInfo(
        id="fii-inf-trim",
        name="Informe Trimestral de FII",
        description="Informe trimestral consolidado por ano (ZIP).",
        macro=macro,
        partition="annual",
    ),
    "fii-inf-anual": GroupInfo(
        id="fii-inf-anual",
        name="Informe Anual de FII",
        description="Informe anual consolidado dos fundos imobiliários.",
        macro=macro,
        partition="annual",
    ),
    "fii-dfin": GroupInfo(
        id="fii-dfin",
        name="Demonstrações Financeiras de FII",
        description="Balanços de fundos imobiliários (CSV anual).",
        macro=macro,
        partition="annual",
    ),
    "fidc-inf-mensal": GroupInfo(
        id="fidc-inf-mensal",
        name="Informe Mensal de FIDC",
        description="Informe mensal dos fundos de direitos creditórios.",
        macro=macro,
        partition="monthly",
    ),
    "fiagro-inf-mensal": GroupInfo(
        id="fiagro-inf-mensal",
        name="Informe Mensal de FIAGRO",
        description="Informe mensal das cadeias agroindustriais.",
        macro=macro,
        partition="monthly",
    ),
    "fip-inf": GroupInfo(
        id="fip-inf",
        name="Informes de Fundos de Participação",
        description="Informes trimestrais e quadrimestrais de FIP (CSV).",
        macro=macro,
        partition="annual",
    ),
}


def list_datasets(group: str) -> list[DatasetEntry]:
    """Listar as entradas de um grupo do macro-domínio estruturados.

    Args:
        group: Grupo canônico (ex.: ``"fii-inf-mensal"``).

    Returns:
        list[DatasetEntry]: Entradas do grupo.

    Raises:
        ValueError: Se o grupo não pertencer a este domínio.
    """
    try:
        return list(_ENTRIES[group])
    except KeyError:
        raise ValueError(f"Unknown group: {group!r}") from None
