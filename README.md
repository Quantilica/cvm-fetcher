# cvm-fetcher

Coletor de dados abertos da **Comissão de Valores Mobiliários (CVM)** para o
ecossistema Quantilica.

Consome o espelho determinístico `https://dados.cvm.gov.br/dados/` (Nginx
auto-index) — sem dependência da API CKAN em tempo de sincronização — e cobre
mais de 50 conjuntos de dados organizados em 5 macro-domínios:

| Macro-domínio | Conteúdo |
|---|---|
| `cadastros` | Cias abertas, fundos de investimento (ICVM 555 / RCVM 175), intermediários, auditores, agentes autônomos, consultores e administradores de carteira |
| `cias` | Demonstrações Financeiras Padronizadas (DFP), Informações Trimestrais (ITR), FRE, FCA, IPE e CGVN |
| `fundos` | Informe diário, CDA (carteiras), extratos, lâminas, perfil mensal e balancetes |
| `estruturados` | FII, FIDC, FIAGRO e FIP |
| `mercado` | Ofertas públicas de distribuição e securitização (CRI/CRA) |

> **Instalação (ecossistema Quantilica):**
>
> ```bash
> quantilica install cvm
> ```

## Uso

```bash
# Listar todos os grupos e datasets do catálogo
cvm-fetcher list

# Planejar (dry-run) o download do informe diário de fundos de 2026-09
cvm-fetcher sync fundos -y 2026 -m 9 --dry-run -o /data/cvm

# Baixar DFPs de 2025
cvm-fetcher sync cias -y 2025

# Baixar apenas cadastros (com macro-alias)
cvm-fetcher sync cadastros

# Converter CSV/ZIP brutos para Parquet (requer extras de análise)
cvm-fetcher convert -i /data/cvm -o /data/cvm/parquet
```

Comandos equivalentes via CLI do ecossistema: `quantilica cvm <comando> ...`.

## Armazenamento e proveniência

Arquivos são gravados atomicamente em `/data/cvm/{grupo}/` com carimbo temporal:

- `cad_cia_aberta@20261003.csv` (estático)
- `dfp_cia_aberta_2026@20261003.zip` (partição anual)
- `inf_diario_fi_2026-10@20261003.zip` (partição mensal)

Cada download gera um manifesto sidecar `*.manifest.json` com SHA-256, URL de
origem e data de coleta (`DownloadManifest` de `quantilica-core`).

## Arquitetura

`cvm-fetcher` é um **adaptador de fonte puro**: apenas extração HTTP, catálogo
de URLs determinísticos e manifestos de proveniência. A representação analítica
(DataFrames/Parquet/SQL) pertence às camadas ETL e analíticas do ecossistema.
Dependência de runtime única: `quantilica-core`.

## Desenvolvimento

```bash
uv sync --all-packages
uv run --package cvm-fetcher pytest cvm-fetcher/tests/ -v
uv run ruff check cvm-fetcher/
uv run ruff format --check cvm-fetcher/
```

## Licença

MIT — consulte [LICENSE](LICENSE).
