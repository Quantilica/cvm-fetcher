"""Catálogo da indústria de fundos de investimento (ICVM 555 / RCVM 175).

Macro-domínio ``fundos``: informe diário de cotas e patrimônio líquido,
composição e diversificação das aplicações (CDA), extratos de documentos,
lâminas, perfil mensal, balancetes e controle de entregas.
"""

from __future__ import annotations

from ._catalog_base import annual_datasets, monthly_datasets
from .contracts import DatasetEntry, GroupInfo

macro = "fundos"

# Primeiro mês/ano publicado no espelho (confirmado via servidor).
_INF_DIARIO_START = (2021, 1)
_CDA_START = (2023, 1)
_LAMINA_START = (2019, 1)
_PERFIL_START = (2019, 1)
_BALANCETE_START = (2015, 1)
_ENTREGA_START = (2025, 1)
_EXTRATO_START = 2015


_INF_DIARIO: list[DatasetEntry] = monthly_datasets(
    "fi-inf-diario",
    slug="inf_diario_fi",
    path_pattern="FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year}{month:02d}.zip",
    start_year=_INF_DIARIO_START[0],
    months=tuple(range(_INF_DIARIO_START[1], 13)),
    description="Informe diário de cotas e patrimônio líquido.",
)

_CDA: list[DatasetEntry] = monthly_datasets(
    "fi-cda",
    slug="cda_fi",
    path_pattern="FI/DOC/CDA/DADOS/cda_fi_{year}{month:02d}.zip",
    start_year=_CDA_START[0],
    months=tuple(range(_CDA_START[1], 13)),
    description="Composição e Diversificação das Aplicações (carteiras).",
)

_LAMINA: list[DatasetEntry] = monthly_datasets(
    "fi-lamina",
    slug="lamina_fi",
    path_pattern="FI/DOC/LAMINA/DADOS/lamina_fi_{year}{month:02d}.zip",
    start_year=_LAMINA_START[0],
    months=tuple(range(_LAMINA_START[1], 13)),
    description="Lâminas dos fundos de investimento.",
)

_PERFIL: list[DatasetEntry] = monthly_datasets(
    "fi-perfil",
    slug="perfil_mensal_fi",
    path_pattern="FI/DOC/PERFIL_MENSAL/DADOS/perfil_mensal_fi_{year}{month:02d}.csv",
    start_year=_PERFIL_START[0],
    months=tuple(range(_PERFIL_START[1], 13)),
    description="Perfil mensal dos fundos de investimento.",
)

_BALANCETE: list[DatasetEntry] = monthly_datasets(
    "fi-balancete",
    slug="balancete_fi",
    path_pattern="FI/DOC/BALANCETE/DADOS/balancete_fi_{year}{month:02d}.zip",
    start_year=_BALANCETE_START[0],
    months=tuple(range(_BALANCETE_START[1], 13)),
    description="Balancetes mensais dos fundos de investimento.",
)

_ENTREGA: list[DatasetEntry] = monthly_datasets(
    "fi-entrega",
    slug="fi_entrega_documento",
    path_pattern=("FI/DOC/ENTREGA/DADOS/fi_entrega_documento_{year}{month:02d}.zip"),
    start_year=_ENTREGA_START[0],
    months=tuple(range(_ENTREGA_START[1], 13)),
    description="Documentos entregues pelos fundos (controle de entregas).",
)

_EXTRATO: list[DatasetEntry] = annual_datasets(
    "fi-extrato",
    slug="extrato_fi",
    path_pattern="FI/DOC/EXTRATO/DADOS/extrato_fi_{year}.csv",
    start_year=_EXTRATO_START,
    description="Extrato de documentos entregues (anual, CSV).",
)

_ENTRIES: dict[str, list[DatasetEntry]] = {
    "fi-inf-diario": _INF_DIARIO,
    "fi-cda": _CDA,
    "fi-extrato": _EXTRATO,
    "fi-lamina": _LAMINA,
    "fi-perfil": _PERFIL,
    "fi-balancete": _BALANCETE,
    "fi-entrega": _ENTREGA,
}

GROUPS: dict[str, GroupInfo] = {
    "fi-inf-diario": GroupInfo(
        id="fi-inf-diario",
        name="Informe Diário de Fundos",
        description="Cotas e patrimônio líquido diários (mensal em ZIP).",
        macro=macro,
        partition="monthly",
    ),
    "fi-cda": GroupInfo(
        id="fi-cda",
        name="Composição da Carteira (CDA)",
        description="Composição e diversificação das aplicações (mensal).",
        macro=macro,
        partition="monthly",
    ),
    "fi-extrato": GroupInfo(
        id="fi-extrato",
        name="Extrato de Documentos Entregues",
        description="Extrato anual de documentos entregues por gestores.",
        macro=macro,
        partition="annual",
    ),
    "fi-lamina": GroupInfo(
        id="fi-lamina",
        name="Lâminas dos Fundos",
        description="Lâminas de divulgação dos fundos de investimento.",
        macro=macro,
        partition="monthly",
    ),
    "fi-perfil": GroupInfo(
        id="fi-perfil",
        name="Perfil Mensal dos Fundos",
        description="Perfil de investimento dos fundos (CSV mensal).",
        macro=macro,
        partition="monthly",
    ),
    "fi-balancete": GroupInfo(
        id="fi-balancete",
        name="Balancetes Mensais",
        description="Balancetes dos fundos de investimento (mensal em ZIP).",
        macro=macro,
        partition="monthly",
    ),
    "fi-entrega": GroupInfo(
        id="fi-entrega",
        name="Entregas de Documentos",
        description="Controle de entregas de documentos por fundos (mensal).",
        macro=macro,
        partition="monthly",
    ),
}


def list_datasets(group: str) -> list[DatasetEntry]:
    """Listar as entradas de um grupo do macro-domínio fundos.

    Args:
        group: Grupo canônico (ex.: ``"fi-inf-diario"``).

    Returns:
        list[DatasetEntry]: Entradas do grupo.

    Raises:
        ValueError: Se o grupo não pertencer a este domínio.
    """
    try:
        return list(_ENTRIES[group])
    except KeyError:
        raise ValueError(f"Unknown group: {group!r}") from None
