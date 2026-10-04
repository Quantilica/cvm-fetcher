"""Catálogo de ofertas públicas e securitização.

Macro-domínio ``mercado``: ofertas públicas de distribuição de valores
mobiliários (oferta_distribuicao) e informes de securitização (CRA e CRI).
"""

from __future__ import annotations

from ._catalog_base import annual_datasets, static_dataset
from .contracts import DatasetEntry, GroupInfo

macro = "mercado"

# Primeiro ano publicado no espelho (confirmado via servidor).
_DFIN_CRA_START = 2019
_DFIN_CRI_START = 2018
_INF_MENSAL_CRA_START = 2019
_INF_MENSAL_CRI_START = 2019

_OFERTAS: list[DatasetEntry] = [
    static_dataset(
        "ofertas",
        slug="oferta_distribuicao",
        path="OFERTA/DISTRIB/DADOS/oferta_distribuicao.zip",
        description="Ofertas públicas de distribuição (IPOs, debêntures).",
    ),
]

_CRA: list[DatasetEntry] = [
    *annual_datasets(
        "securit-cra",
        slug="dfin_cra",
        path_pattern="SECURIT/DOC/DFIN_CRA/DADOS/dfin_cra_{year}.csv",
        start_year=_DFIN_CRA_START,
        description="Demonstrações financeiras das CRAs (CSV anual).",
    ),
    *annual_datasets(
        "securit-cra",
        slug="inf_mensal_cra",
        path_pattern="SECURIT/DOC/INF_MENSAL_CRA/DADOS/inf_mensal_cra_{year}.zip",
        start_year=_INF_MENSAL_CRA_START,
        description="Informe mensal das CRAs (ZIP anual).",
    ),
]

_CRI: list[DatasetEntry] = [
    *annual_datasets(
        "securit-cri",
        slug="dfin_cri",
        path_pattern="SECURIT/DOC/DFIN_CRI/DADOS/dfin_cri_{year}.csv",
        start_year=_DFIN_CRI_START,
        description="Demonstrações financeiras das CRIs (CSV anual).",
    ),
    *annual_datasets(
        "securit-cri",
        slug="inf_mensal_cri",
        path_pattern="SECURIT/DOC/INF_MENSAL_CRI/DADOS/inf_mensal_cri_{year}.zip",
        start_year=_INF_MENSAL_CRI_START,
        description="Informe mensal das CRIs (ZIP anual).",
    ),
]

_ENTRIES: dict[str, list[DatasetEntry]] = {
    "ofertas": _OFERTAS,
    "securit-cra": _CRA,
    "securit-cri": _CRI,
}

GROUPS: dict[str, GroupInfo] = {
    "ofertas": GroupInfo(
        id="ofertas",
        name="Ofertas Públicas de Distribuição",
        description="Coordenadores e distribuição de ofertas desde 2000.",
        macro=macro,
        partition="static",
    ),
    "securit-cra": GroupInfo(
        id="securit-cra",
        name="Securitização — CRA",
        description="Certificados de Recebíveis do Agronegócio.",
        macro=macro,
        partition="annual",
    ),
    "securit-cri": GroupInfo(
        id="securit-cri",
        name="Securitização — CRI",
        description="Certificados de Recebíveis Imobiliários.",
        macro=macro,
        partition="annual",
    ),
}


def list_datasets(group: str) -> list[DatasetEntry]:
    """Listar as entradas de um grupo do macro-domínio mercado.

    Args:
        group: Grupo canônico (ex.: ``"ofertas"``).

    Returns:
        list[DatasetEntry]: Entradas do grupo.

    Raises:
        ValueError: Se o grupo não pertencer a este domínio.
    """
    try:
        return list(_ENTRIES[group])
    except KeyError:
        raise ValueError(f"Unknown group: {group!r}") from None
