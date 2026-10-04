"""Catálogo unificado dos datasets da CVM.

Agrega os 5 macro-domínios canônicos (``cadastros``, ``cias``, ``fundos``,
``estruturados`` e ``mercado``) com grupo canônico, aliases e macro-aliases.

- GROUPS: grupo canônico → GroupInfo (metadados + entradas resolvidas por
  :func:`list_datasets`).
- GROUP_ALIASES: macro-alias → lista de grupos canônicos (ex. ``fundos`` →
  todos os grupos de fundos de investimento).
"""

from __future__ import annotations

from . import catalog_cadastros, catalog_cias, catalog_fundos
from . import catalog_estruturados as _estruturados
from . import catalog_mercado as _mercado
from ._catalog_base import CVM_BASE_URL, dataset_url
from .contracts import DatasetEntry, GroupInfo

__all__ = [
    "CVM_BASE_URL",
    "GROUPS",
    "GROUP_ALIASES",
    "MACRO_ALIASES",
    "ALL_GROUP_KEYS",
    "dataset_url",
    "expand_group",
    "resolve_group",
    "list_datasets",
]

# Grupos canônicos agregados por ordem de macro-domínio.
_MODULES = [
    catalog_cadastros,
    catalog_cias,
    catalog_fundos,
    _estruturados,
    _mercado,
]

GROUPS: dict[str, GroupInfo] = {
    **{gid: info for mod in _MODULES for gid, info in mod.GROUPS.items()}
}

# Macro-aliases: um apelido que engloba vários grupos canônicos de uma vez.
MACRO_ALIASES: dict[str, list[str]] = {
    "cadastros": [
        "cia-cad",
        "fi-cad",
        "intermed-cad",
        "auditor-cad",
        "agente-auton-cad",
        "consultor-cad",
        "adm-cart-cad",
        "agente-fiduc-cad",
    ],
    "cias": ["cia-dfp", "cia-itr", "cia-fre", "cia-fca", "cia-ipe", "cia-cgvn"],
    "fundos": [
        "fi-inf-diario",
        "fi-cda",
        "fi-extrato",
        "fi-lamina",
        "fi-perfil",
        "fi-balancete",
        "fi-entrega",
    ],
    "estruturados": [
        "fii-inf-mensal",
        "fii-inf-trim",
        "fii-inf-anual",
        "fii-dfin",
        "fidc-inf-mensal",
        "fiagro-inf-mensal",
        "fip-inf",
    ],
    "ofertas": ["ofertas", "securit-cra", "securit-cri"],
}

# Alias listado no ADR como macro-domínio "fundos-estruturados" — mantido como
# alias canônico retrocompatível para os grupos de estruturados.
MACRO_ALIASES["fundos-estruturados"] = MACRO_ALIASES["estruturados"]

# Alias de oferta singular → grupo "ofertas" (plural).
GROUP_ALIASES: dict[str, list[str]] = {
    **MACRO_ALIASES,
    "oferta": ["ofertas"],
}

ALL_GROUP_KEYS: list[str] = list(GROUPS)


def expand_group(key: str) -> list[str]:
    """Expandir um grupo, alias ou macro-alias em ids canônicos.

    Args:
        key: Nome do grupo ou alias (ex.: ``"ofertas"``, ``"fundos"``).

    Returns:
        list[str]: Ids canônicos em ordem de declaração; lista vazia se o
            nome não for reconhecido.
    """
    resolved: list[str] = []
    for canon in GROUP_ALIASES.get(key, [key]):
        if canon in GROUPS and canon not in resolved:
            resolved.append(canon)
    return resolved


def resolve_group(key: str) -> str | None:
    """Resolver um grupo ou alias simples para um único id canônico.

    Não expande macro-aliases (que mapeiam para vários grupos); use
    :func:`expand_group` para isso.

    Args:
        key: Nome do grupo ou alias.

    Returns:
        str | None: Id canônico, ou None se desconhecido.
    """
    if key in GROUPS:
        return key
    matched = GROUP_ALIASES.get(key)
    if matched and len(matched) == 1:
        return matched[0]
    return None


def _list_group_datasets(group: str) -> list[DatasetEntry]:
    """Listar entradas de um grupo canônico consultando os módulos."""
    for mod in _MODULES:
        if group in mod.GROUPS:
            return mod.list_datasets(group)
    raise ValueError(f"Unknown group: {group!r}")


def list_datasets(group: str | None = None) -> list[DatasetEntry]:
    """Listar todas as entradas do catálogo, opcionalmente filtradas.

    Args:
        group: Grupo, alias ou macro-alias. None lista todos.

    Returns:
        list[DatasetEntry]: Entradas correspondentes.

    Raises:
        ValueError: Se ``group`` for fornecido e não for reconhecido.
    """
    if group is None:
        return [entry for gid in GROUPS for entry in _list_group_datasets(gid)]
    canon = expand_group(group)
    if not canon:
        raise ValueError(f"Unknown group: {group!r}")
    return [entry for gid in canon for entry in _list_group_datasets(gid)]
