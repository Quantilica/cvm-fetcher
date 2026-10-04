# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Adicionado
- Catálogo modular de 5 macro-domínios da CVM: `cadastros`, `cias`, `fundos`,
  `estruturados` e `mercado`, com resolução por grupo, alias e macro-alias.
- `catalog.list_canonical_datasets(grupo)`: entradas de um id canônico sem
  expansão de alias — para hooks que já receberam o grupo resolvido.
- CLI dupla canônica: `plugin.py` (Typer via `FetcherApp` do `quantilica.cli.sdk`)
  e `cli.py` standalone fina, com comandos `sync` (concorrente, `--dry-run`,
  filtros de grupo/ano/mês), `list` e `convert` (Parquet via extra `analysis`).
- Armazenamento com carimbos temporais (`{slug}@{YYYYMMDD}.{ext}`,
  `{slug}_{particao}@{YYYYMMDD}.{ext}`) e layout `{raiz}/{grupo}/{arquivo}`.
- Cliente HTTP `CvmClient` sobre o espelho determinístico
  `https://dados.cvm.gov.br/dados/` com gravação atômica e manifesto sidecar
  SHA-256 (`DownloadManifest` de `quantilica-core`).

### Corrigido
- `sync` total não planeja mais 33 arquivos duplicados: o hook do SDK consultava
  o catálogo reexpandindo o macro-alias `ofertas` (que também é grupo canônico),
  duplicando `securit-cra` (2×) e `securit-cri` (2×).
- Informe trimestral de FIP encerra em 2023 — a série foi descontinuada e
  substituída pela quadrimestral a partir de 2024, o que gerava 3 URLs com
  HTTP 404 permanente.
- Filtro de meses da série mensal passa a valer só no ano de estreia: o
  recorte de estreia do FIAGRO (2025-05) não omite mais janeiro–abril de 2027+
  (`_catalog_base.monthly_datasets`).
