"""Catálogo de demonstrações e formulários de companhias abertas.

Macro-domínio ``cias``: DFP (demonstrações financeiras padronizadas),
ITR (informações trimestrais), FRE (formulário de referência — demonstrações
financeiras e remuneração), FCA (formulário cadastral), IPE (informações
periódicas e eventuais) e CGVN (consultas de governança).
Todos particionados anualmente em ZIPs no espelho da CVM.
"""

from __future__ import annotations

from ._catalog_base import annual_datasets
from .contracts import DatasetEntry, GroupInfo

macro = "cias"

# Primeiro ano publicado no espelho (confirmado via servidor).
_DFP_START = 2010
_ITR_START = 2011
_FRE_START = 2010
_FCA_START = 2010
_IPE_START = 2003
_CGVN_START = 2018

_ENTRIES: dict[str, list[DatasetEntry]] = {
    "cia-dfp": annual_datasets(
        "cia-dfp",
        slug="dfp_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_{year}.zip",
        start_year=_DFP_START,
        description="Demonstrações Financeiras Padronizadas (annual).",
    ),
    "cia-itr": annual_datasets(
        "cia-itr",
        slug="itr_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_{year}.zip",
        start_year=_ITR_START,
        description="Informações Trimestrais (ITR).",
    ),
    "cia-fre": annual_datasets(
        "cia-fre",
        slug="fre_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/FRE/DADOS/fre_cia_aberta_{year}.zip",
        start_year=_FRE_START,
        description="Formulário de Referência — demonstrações financeiras.",
    ),
    "cia-fca": annual_datasets(
        "cia-fca",
        slug="fca_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/FCA/DADOS/fca_cia_aberta_{year}.zip",
        start_year=_FCA_START,
        description="Formulário Cadastral.",
    ),
    "cia-ipe": annual_datasets(
        "cia-ipe",
        slug="ipe_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/IPE/DADOS/ipe_cia_aberta_{year}.zip",
        start_year=_IPE_START,
        description="Informações Periódicas e Eventuais (IPO, fatos relevantes).",
    ),
    "cia-cgvn": annual_datasets(
        "cia-cgvn",
        slug="cgvn_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/CGVN/DADOS/cgvn_cia_aberta_{year}.zip",
        start_year=_CGVN_START,
        description="Consultas e Junta de Governança Corporativa (CGVN).",
    ),
}

GROUPS: dict[str, GroupInfo] = {
    "cia-dfp": GroupInfo(
        id="cia-dfp",
        name="Demonstrações Financeiras Padronizadas (DFP)",
        description="Balanço, DRE, DFC, DMPL e DVA de companhias abertas (anual).",
        macro=macro,
        partition="annual",
    ),
    "cia-itr": GroupInfo(
        id="cia-itr",
        name="Informações Trimestrais (ITR)",
        description="Balanço e DRE trimestrais de companhias abertas.",
        macro=macro,
        partition="annual",
    ),
    "cia-fre": GroupInfo(
        id="cia-fre",
        name="Formulário de Referência (FRE)",
        description="Governança, remuneração e demonstrações financeiras.",
        macro=macro,
        partition="annual",
    ),
    "cia-fca": GroupInfo(
        id="cia-fca",
        name="Formulário Cadastral (FCA)",
        description="Informações cadastrais de companhias abertas.",
        macro=macro,
        partition="annual",
    ),
    "cia-ipe": GroupInfo(
        id="cia-ipe",
        name="Informações Periódicas e Eventuais (IPE)",
        description="Publicações como IPOs e fatos relevantes.",
        macro=macro,
        partition="annual",
    ),
    "cia-cgvn": GroupInfo(
        id="cia-cgvn",
        name="Consultas CGVN",
        description="Consultas à Comissão de Relações com Investidores.",
        macro=macro,
        partition="annual",
    ),
}


def list_datasets(group: str) -> list[DatasetEntry]:
    """Listar as entradas de um grupo do macro-domínio companhias abertas.

    Args:
        group: Grupo canônico (ex.: ``"cia-dfp"``).

    Returns:
        list[DatasetEntry]: Entradas do grupo.

    Raises:
        ValueError: Se o grupo não pertencer a este domínio.
    """
    try:
        return list(_ENTRIES[group])
    except KeyError:
        raise ValueError(f"Unknown group: {group!r}") from None
