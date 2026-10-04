# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Adicionado
- Catálogo modular de 5 macro-domínios da CVM: `cadastros`, `cias`, `fundos`,
  `estruturados` e `mercado`, com resolução por grupo, alias e macro-alias.
- CLI dupla canônica: `plugin.py` (Typer via `FetcherApp` do `quantilica.cli.sdk`)
  e `cli.py` standalone fina, com comandos `sync` (concorrente, `--dry-run`,
  filtros de grupo/ano/mês), `list` e `convert` (Parquet via extra `analysis`).
- Armazenamento com carimbos temporais (`{slug}@{YYYYMMDD}.{ext}`,
  `{slug}_{particao}@{YYYYMMDD}.{ext}`) e layout `{raiz}/{grupo}/{arquivo}`.
- Cliente HTTP `CvmClient` sobre o espelho determinístico
  `https://dados.cvm.gov.br/dados/` com gravação atômica e manifesto sidecar
  SHA-256 (`DownloadManifest` de `quantilica-core`).
