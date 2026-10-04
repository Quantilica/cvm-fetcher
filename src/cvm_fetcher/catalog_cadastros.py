"""Catálogo de cadastros de entidades reguladas pela CVM.

Macro-domínio ``cadastros``: companhias abertas, fundos de investimento
(ICVM 555 / RCVM 175), intermediários financeiros, auditores, agentes
autônomos, consultores, administradores de carteira e agentes fiduciários.
Todos os conjuntos são estáticos (arquivo único por cadastro).
"""

from __future__ import annotations

from ._catalog_base import static_dataset
from .contracts import DatasetEntry, GroupInfo

macro = "cadastros"

_CIA_CAD: list[DatasetEntry] = [
    static_dataset(
        "cia-cad",
        slug="cad_cia_aberta",
        path="CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv",
        description="Cadastro de companhias abertas.",
    ),
]

_FI_CAD: list[DatasetEntry] = [
    static_dataset(
        "fi-cad",
        slug="cad_fi",
        path="FI/CAD/DADOS/cad_fi.csv",
        description="Cadastro de fundos de investimento (versão vigente).",
    ),
    static_dataset(
        "fi-cad",
        slug="cad_fi_hist",
        path="FI/CAD/DADOS/cad_fi_hist.zip",
        description="Histórico de cadastro de fundos de investimento.",
    ),
    static_dataset(
        "fi-cad",
        slug="registro_fundo_classe",
        path="FI/CAD/DADOS/registro_fundo_classe.zip",
        description="Registro de fundos por classe (RCVM 175).",
    ),
]

_INTERMED_CAD: list[DatasetEntry] = [
    static_dataset(
        "intermed-cad",
        slug="cad_intermed",
        path="INTERMED/CAD/DADOS/cad_intermed.zip",
        description="Cadastro de intermediários financeiros.",
    ),
]

_AUDITOR_CAD: list[DatasetEntry] = [
    static_dataset(
        "auditor-cad",
        slug="cad_auditor",
        path="AUDITOR/CAD/DADOS/cad_auditor.zip",
        description="Cadastro de auditores independentes.",
    ),
]

_AGENTE_AUTON_CAD: list[DatasetEntry] = [
    static_dataset(
        "agente-auton-cad",
        slug="cad_agente_auton",
        path="AGENTE_AUTON/CAD/DADOS/cad_agente_auton.zip",
        description="Cadastro de agentes autônomos de investimento.",
    ),
]

_CONSULTOR_CAD: list[DatasetEntry] = [
    static_dataset(
        "consultor-cad",
        slug="cad_consultor_vlmob",
        path="CONSULTOR_VLMOB/CAD/DADOS/cad_consultor_vlmob.zip",
        description="Cadastro de consultores de valores mobiliários.",
    ),
]

_ADM_CART_CAD: list[DatasetEntry] = [
    static_dataset(
        "adm-cart-cad",
        slug="cad_adm_cart",
        path="ADM_CART/CAD/DADOS/cad_adm_cart.zip",
        description="Cadastro de administradores de carteira.",
    ),
]

_AGENTE_FIDUC_CAD: list[DatasetEntry] = [
    static_dataset(
        "agente-fiduc-cad",
        slug="cad_agente_fiduc",
        path="AGENTE_FIDUC/CAD/DADOS/cad_agente_fiduc.zip",
        description="Cadastro de agentes fiduciários.",
    ),
]

_ENTRIES: dict[str, list[DatasetEntry]] = {
    "cia-cad": _CIA_CAD,
    "fi-cad": _FI_CAD,
    "intermed-cad": _INTERMED_CAD,
    "auditor-cad": _AUDITOR_CAD,
    "agente-auton-cad": _AGENTE_AUTON_CAD,
    "consultor-cad": _CONSULTOR_CAD,
    "adm-cart-cad": _ADM_CART_CAD,
    "agente-fiduc-cad": _AGENTE_FIDUC_CAD,
}

GROUPS: dict[str, GroupInfo] = {
    "cia-cad": GroupInfo(
        id="cia-cad",
        name="Cadastro de Companhias Abertas",
        description="Cadastro vigente de companhias abertas (CVM).",
        macro=macro,
        partition="static",
    ),
    "fi-cad": GroupInfo(
        id="fi-cad",
        name="Cadastro de Fundos de Investimento",
        description="Cadastro e histórico de fundos de investimento "
        "(ICVM 555 / RCVM 175).",
        macro=macro,
        partition="static",
    ),
    "intermed-cad": GroupInfo(
        id="intermed-cad",
        name="Cadastro de Intermediários Financeiros",
        description="Corretoras, distribuidoras e demais intermediários.",
        macro=macro,
        partition="static",
    ),
    "auditor-cad": GroupInfo(
        id="auditor-cad",
        name="Cadastro de Auditores Independentes",
        description="Auditoras independentes registradas na CVM.",
        macro=macro,
        partition="static",
    ),
    "agente-auton-cad": GroupInfo(
        id="agente-auton-cad",
        name="Cadastro de Agentes Autônomos",
        description="Agentes autônomos de investimento.",
        macro=macro,
        partition="static",
    ),
    "consultor-cad": GroupInfo(
        id="consultor-cad",
        name="Cadastro de Consultores de Valores Mobiliários",
        description="Consultores de valores mobiliários.",
        macro=macro,
        partition="static",
    ),
    "adm-cart-cad": GroupInfo(
        id="adm-cart-cad",
        name="Cadastro de Administradores de Carteira",
        description="Administradoras de carteira de terceiros.",
        macro=macro,
        partition="static",
    ),
    "agente-fiduc-cad": GroupInfo(
        id="agente-fiduc-cad",
        name="Cadastro de Agentes Fiduciários",
        description="Agentes fiduciários (RCVM 35).",
        macro=macro,
        partition="static",
    ),
}


def list_datasets(group: str) -> list[DatasetEntry]:
    """Listar as entradas de um grupo do macro-domínio cadastros.

    Args:
        group: Grupo canônico (ex.: ``"fi-cad"``).

    Returns:
        list[DatasetEntry]: Entradas do grupo.

    Raises:
        ValueError: Se o grupo não pertencer a este domínio.
    """
    try:
        return list(_ENTRIES[group])
    except KeyError:
        raise ValueError(f"Unknown group: {group!r}") from None
