# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Corrigido
- `read_csv_smart` relê sem tratar aspas os CSVs em que elas fazem parte do texto
  ("Spin-off" da Contax, no Assunto do IPE); antes, cerca de 250 arquivos falhavam com
  "could not parse" ou "CSV malformed".
- `read_csv_smart` infere o esquema a partir do arquivo inteiro: na CDA de fundos,
  `CD_SELIC` é numérico nas primeiras linhas e traz texto ("PDD") mais adiante.

## [0.2.0] - 2026-10-27

### Adicionado
- Módulo `cvm_fetcher.lake` e entry point `quantilica.lake`: conversão direta dos arquivos abertos da CVM (CSV e ZIP) para o lake Parquet particionado no formato Hive (`ano=/mes=` para séries mensais/diárias de fundos, `ano=` para anuais e sem partição para cadastros estáticos).
- Comandos CLI `convert` e `pipeline` integrados via SDK do `FetcherApp`, com suporte a `--lake`, `--dataset` e `--force`.
- Extra `analysis` atualizado para `quantilica-analytics>=0.5.0`.
- Dependência `quantilica-core` atualizada para `>=0.13.0`, primeira versão com o contrato do lake.

## [0.1.1] - 2026-10-20

### Corrigido
- Testes com fake HTTP isolado (`transport`, `emulate_browser` e `__exit__`).
- Compatibilidade de testes de storage em ambiente Windows.
- `.gitignore`: cabeçalho do bloco de IA de volta ao canônico `# Claude`.
- `plugin.py` (`cmd_convert`): comentário documentando que o `ImportError`
  de polars/analysis é tratado pelo SDK (`command_convert`); sem mudança de
  comportamento.

### Alterado

- `cli.py` protege o import do plugin; sem o host a CLI standalone sai com
  código 1 e orienta `quantilica install cvm`.
- `analysis`: extração de `reader` e `wrangling` do plugin, com metadados canônicos de proveniência Parquet.
- Dependências atualizadas: `quantilica-core>=0.12.0` e `quantilica-analytics>=0.4.0`.

## [0.1.0] - 2026-10-04

Primeira release do `cvm-fetcher`. Catálogo determinístico sobre o espelho
`https://dados.cvm.gov.br/dados/`, CLI dupla (standalone + plugin do
`quantilica-cli`) e conversão para Parquet.

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
- Testes com fake HTTP isolado (`transport`, `emulate_browser` e `__exit__`).
- Compatibilidade de testes de storage em ambiente Windows.
- `sync` total não planeja mais 33 arquivos duplicados: o hook do SDK consultava
  o catálogo reexpandindo o macro-alias `ofertas` (que também é grupo canônico),
  duplicando `securit-cra` (2×) e `securit-cri` (2×).
- Informe trimestral de FIP encerra em 2023 — a série foi descontinuada e
  substituída pela quadrimestral a partir de 2024, o que gerava 3 URLs com
  HTTP 404 permanente.
- Filtro de meses da série mensal passa a valer só no ano de estreia: o
  recorte de estreia do FIAGRO (2025-05) não omite mais janeiro–abril de 2027+
  (`_catalog_base.monthly_datasets`).
