"""Testes do catálogo unificado do cvm-fetcher."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pytest

from cvm_fetcher import (
    catalog_cadastros,
    catalog_cias,
    catalog_estruturados,
    catalog_fundos,
    catalog_mercado,
)
from cvm_fetcher._catalog_base import (
    CVM_BASE_URL,
    annual_datasets,
    dataset_url,
    monthly_datasets,
)
from cvm_fetcher.catalog import (
    ALL_GROUP_KEYS,
    GROUP_ALIASES,
    GROUPS,
    MACRO_ALIASES,
    expand_group,
    list_canonical_datasets,
    list_datasets,
    resolve_group,
)

_DOMAIN_MODULES = (
    catalog_cadastros,
    catalog_cias,
    catalog_fundos,
    catalog_estruturados,
    catalog_mercado,
)

_EXPECTED_GROUPS = {
    # cadastros
    "cia-cad",
    "fi-cad",
    "intermed-cad",
    "auditor-cad",
    "agente-auton-cad",
    "consultor-cad",
    "adm-cart-cad",
    "agente-fiduc-cad",
    # cias
    "cia-dfp",
    "cia-itr",
    "cia-fre",
    "cia-fca",
    "cia-ipe",
    "cia-cgvn",
    # fundos
    "fi-inf-diario",
    "fi-cda",
    "fi-extrato",
    "fi-lamina",
    "fi-perfil",
    "fi-balancete",
    "fi-entrega",
    # estruturados
    "fii-inf-mensal",
    "fii-inf-trim",
    "fii-inf-anual",
    "fii-dfin",
    "fidc-inf-mensal",
    "fiagro-inf-mensal",
    "fip-inf",
    # mercado
    "ofertas",
    "securit-cra",
    "securit-cri",
}


def test_groups_aggregation_and_macros() -> None:
    """GROUPS agrega os grupos de todos os módulos de domínio."""
    assert set(GROUPS) == _EXPECTED_GROUPS
    assert set(ALL_GROUP_KEYS) == _EXPECTED_GROUPS
    module_groups: set[str] = set()
    for mod in _DOMAIN_MODULES:
        module_groups |= set(mod.GROUPS)
    assert module_groups == _EXPECTED_GROUPS


def test_macro_aliases_cover_every_group() -> None:
    """Cada macro-domínio cobre exatamente os grupos do módulo."""
    assert set(MACRO_ALIASES["cadastros"]) == set(catalog_cadastros.GROUPS)
    assert set(MACRO_ALIASES["cias"]) == set(catalog_cias.GROUPS)
    assert set(MACRO_ALIASES["fundos"]) == set(catalog_fundos.GROUPS)
    assert set(MACRO_ALIASES["estruturados"]) == set(catalog_estruturados.GROUPS)
    assert set(MACRO_ALIASES["ofertas"]) == set(catalog_mercado.GROUPS)
    # ADR permite "fundos-estruturados" como alias canônico retrocompatível.
    assert GROUP_ALIASES["fundos-estruturados"] == MACRO_ALIASES["estruturados"]


def test_expand_and_resolve_groups() -> None:
    """Resolução de grupo simples e macro-aliases via expand_group."""
    assert expand_group("cia-dfp") == ["cia-dfp"]
    assert expand_group("cadastros") == MACRO_ALIASES["cadastros"]
    assert expand_group("fundos") == MACRO_ALIASES["fundos"]
    assert expand_group("estruturados") == MACRO_ALIASES["estruturados"]
    assert expand_group("ofertas") == MACRO_ALIASES["ofertas"]
    assert expand_group("grupo-inexistente") == []
    # resolve_group (um único alvo)
    assert resolve_group("cia-dfp") == "cia-dfp"
    assert resolve_group("cias") is None  # macro-alias → múltiplos grupos
    assert resolve_group("oferta") == "ofertas"  # alias simples
    assert resolve_group("desconhecido") is None


def test_list_datasets_all_and_filtered() -> None:
    """list_datasets(None) cobre todos; por grupo, filtra corretamente."""
    everything = list_datasets()
    total_by_modules = sum(
        len(mod.list_datasets(gid)) for mod in _DOMAIN_MODULES for gid in mod.GROUPS
    )
    assert len(everything) == total_by_modules
    diarios = list_datasets("fi-inf-diario")
    assert all(e.group == "fi-inf-diario" for e in diarios)
    with pytest.raises(ValueError, match="Unknown group"):
        list_datasets("grupo-inexistente")


def test_list_canonical_datasets_nao_expande_alias() -> None:
    """list_canonical_datasets exige id canônico e não expande macro-alias."""
    total_by_modules = sum(
        len(mod.list_datasets(gid)) for mod in _DOMAIN_MODULES for gid in mod.GROUPS
    )
    for gid in ALL_GROUP_KEYS:
        canonical = list_canonical_datasets(gid)
        assert canonical, f"Grupo canônico sem entradas: {gid}"
        assert all(entry.group == gid for entry in canonical)
    assert sum(len(list_canonical_datasets(gid)) for gid in ALL_GROUP_KEYS) == (
        total_by_modules
    )
    # "ofertas" é simultaneamente grupo canônico e macro-alias: as duas
    # leituras são legítimas e deliberadamente diferentes.
    assert expand_group("ofertas") == ["ofertas", "securit-cra", "securit-cri"]
    assert len(list_datasets("ofertas")) > len(list_canonical_datasets("ofertas"))
    # Aliases (simples ou macro) não são ids canônicos.
    for alias in ("cadastros", "oferta", "grupo-inexistente"):
        with pytest.raises(ValueError, match="Unknown group"):
            list_canonical_datasets(alias)


def test_fip_trimestral_encerrado_em_2023() -> None:
    """Série trimestral de FIP termina em 2023; a quadrimestral cobre 2024+."""
    fip = list_datasets("fip-inf")
    trim = sorted(e.year for e in fip if e.id == "inf_trimestral_fip")
    quadrim = sorted(e.year for e in fip if e.id == "inf_quadrimestral_fip")
    assert trim[-1] == 2023
    assert quadrim[0] == 2024
    # Contíguas e sem sobreposição entre as duas séries.
    assert trim == list(range(trim[0], 2024))
    assert quadrim == list(range(2024, quadrim[-1] + 1))
    assert not [year for year in trim if year >= 2024]


def test_monthly_meses_apenas_no_ano_de_estreia() -> None:
    """``months`` corta o calendário só na estreia; anos seguintes são completos."""
    custom = monthly_datasets(
        "fiagro-inf-mensal",
        slug="inf_mensal_fiagro",
        path_pattern=(
            "FIAGRO/DOC/INF_MENSAL/DADOS/inf_mensal_fiagro_{year}{month:02d}.zip"
        ),
        start_year=2025,
        end_year=2026,
        months=tuple(range(5, 13)),
    )
    debut = sorted(e.month for e in custom if e.year == 2025)
    assert debut == list(range(5, 13))
    following = sorted(e.month for e in custom if e.year == 2026)
    # Janeiro do ano seguinte não pode faltar (o mês de estreia é do recorte).
    assert following[:4] == [1, 2, 3, 4]
    filenames = {e.url.rsplit("/", 1)[-1] for e in custom}
    assert "inf_mensal_fiagro_202601.zip" in filenames
    # Jan-ab do ano de estreia seguem fora do catálogo.
    fora_da_estreia = {
        f"inf_mensal_fiagro_2025{month:02d}.zip" for month in range(1, 5)
    }
    assert not filenames & fora_da_estreia


@pytest.mark.parametrize("group", ["fiagro-inf-mensal", "fidc-inf-mensal"])
def test_serie_mensal_completa_apos_estreia(group: str) -> None:
    """Grupos mensais do catálogo cobrem janeiro em todos os anos pós-estreia."""
    entries = list_datasets(group)
    debut = min(e.year for e in entries)
    for year in range(debut + 1, max(e.year for e in entries) + 1):
        months = sorted(e.month for e in entries if e.year == year)
        assert months and months[0] == 1, f"{group}: {year} sem janeiro"


def test_entry_schema_sdk() -> None:
    """Entradas serializadas seguem o schema canônico do SDK."""
    entry = list_datasets("fii-dfin")[0]
    data = entry.to_dict()
    assert data["group"] == "fii-dfin"
    assert data["id"] == "dfin_fii"
    assert data["ext"] == "csv"
    assert data["url"].startswith(CVM_BASE_URL)


def test_static_urls_deterministic() -> None:
    """URLs estáticas são exatamente as do espelho determinístico."""
    expected: dict[str, str] = {
        "cad_cia_aberta": (
            "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"
        ),
        "cad_fi": "https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv",
        "cad_fi_hist": "https://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi_hist.zip",
        "registro_fundo_classe": (
            "https://dados.cvm.gov.br/dados/FI/CAD/DADOS/registro_fundo_classe.zip"
        ),
        "cad_intermed": (
            "https://dados.cvm.gov.br/dados/INTERMED/CAD/DADOS/cad_intermed.zip"
        ),
        "cad_auditor": (
            "https://dados.cvm.gov.br/dados/AUDITOR/CAD/DADOS/cad_auditor.zip"
        ),
        "cad_agente_auton": (
            "https://dados.cvm.gov.br/dados/AGENTE_AUTON/CAD/DADOS/cad_agente_auton.zip"
        ),
        "cad_consultor_vlmob": (
            "https://dados.cvm.gov.br/dados/CONSULTOR_VLMOB/CAD/DADOS/"
            "cad_consultor_vlmob.zip"
        ),
        "cad_adm_cart": (
            "https://dados.cvm.gov.br/dados/ADM_CART/CAD/DADOS/cad_adm_cart.zip"
        ),
        "cad_agente_fiduc": (
            "https://dados.cvm.gov.br/dados/AGENTE_FIDUC/CAD/DADOS/cad_agente_fiduc.zip"
        ),
        "oferta_distribuicao": (
            "https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/"
            "oferta_distribuicao.zip"
        ),
    }
    for entry in list_datasets("cadastros") + list_datasets("oferta"):
        assert entry.url == expected[entry.id], (
            f"URL divergente para {entry.id}: {entry.url}"
        )


def test_annual_cia_urls_deterministic() -> None:
    """Partições anuais de companhias abertas montam o padrão do espelho."""
    dfp = list_datasets("cia-dfp")
    first, last = dfp[0], dfp[-1]
    assert first.year == 2010
    assert first.url == (
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/"
        "dfp_cia_aberta_2010.zip"
    )
    # Janela contígua até o ano corrente (sem lacunas).
    assert last.url.endswith(f"dfp_cia_aberta_{last.year}.zip")
    assert [e.year for e in dfp] == list(range(2010, last.year + 1))
    itr_url = annual_datasets(
        "cia-itr",
        slug="itr_cia_aberta",
        path_pattern="CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_{year}.zip",
        start_year=2011,
        end_year=2012,
    )[1].url
    assert itr_url == (
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"
        "itr_cia_aberta_2012.zip"
    )


def test_monthly_fundo_urls_deterministic() -> None:
    """Partições mensais de fundos seguem o padrão {prefixo}_{ano}{mes}."""
    mensal = list_datasets("fi-inf-diario")
    assert mensal[0].year == 2021 and mensal[0].month == 1
    assert mensal[0].url == (
        "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/"
        "inf_diario_fi_202101.zip"
    )
    custom = monthly_datasets(
        "fi-inf-diario",
        slug="inf_diario_fi",
        path_pattern="FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year}{month:02d}.zip",
        start_year=2021,
        end_year=2021,
        months=(3, 5),
    )
    assert [e.url for e in custom] == [
        "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/"
        "inf_diario_fi_202103.zip",
        "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/"
        "inf_diario_fi_202105.zip",
    ]


def test_dataset_url_builder() -> None:
    """dataset_url junta segmentos e descarta barras duplicadas."""
    assert (
        dataset_url("CIA_ABERTA", "/DOC/DFP/DADOS/", "dfp_cia_aberta_2026.zip")
        == "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/"
        "dfp_cia_aberta_2026.zip"
    )


@pytest.mark.parametrize(
    "group_factory",
    [
        lambda: list_datasets("cadastros"),
        lambda: list_datasets("cias"),
        lambda: list_datasets("fundos"),
        lambda: list_datasets("estruturados"),
        lambda: list_datasets("ofertas"),
    ],
)
def test_catalog_consistency(group_factory: Callable[[], list[Any]]) -> None:
    """Invariantes estruturais do catálogo por macro-domínio."""
    seen: set[tuple[str, int, int]] = set()
    for entry in group_factory():
        assert GROUPS[entry.group].macro
        assert entry.id and entry.ext in {"csv", "zip"}
        assert entry.url.startswith(CVM_BASE_URL)
        # (id, mês, ano) únicos por entrada para carimbos consistentes
        key = (f"{entry.group}:{entry.id}", entry.year or 0, entry.month or 0)
        assert key not in seen, f"Entrada duplicada: {key}"
        seen.add(key)


def test_monthly_window_future_months_excluded() -> None:
    """Janela mensal do ano corrente descarta meses futuros."""
    custom = monthly_datasets(
        "fi-inf-diario",
        slug="inf_diario_fi",
        path_pattern="FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year}{month:02d}.zip",
        start_year=2021,
        end_year=2024,  # fixado no passado: força gerar o calendário completo
        months=tuple(range(1, 13)),
    )
    calendars = {e.year for e in custom}
    assert 2021 in calendars and 2024 in calendars
    assert all(e.month is not None for e in custom)
