---
dataset:
  id: fi-entrega
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Entrega (CVM)"
  resumo: "Registro das entregas de documentos pelos fundos de investimento à CVM: o tipo de documento, a competência, o momento da entrega e se a entrega está ativa, em duas tabelas (documentos periódicos e eventuais, e documentos diários)."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-entrega
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-entrega"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização diária para os dois meses mais recentes e semanal para os demais"
  cobertura: {inicio: 2025-01, fim: em-curso}
  unidade: "uma entrega de documento de um fundo, classe ou subclasse"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (arquivo por mês); a data e a hora da entrega estão em `Data_Hora_Entrega`"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [], colunas: 11}
  unidades_de_medida:
    ID_Documento: "código ou número de identificação (sem unidade)"
  dados_pessoais: nenhum
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Entrega

## Resumo

Registro das entregas de documentos pelos fundos de investimento à CVM: o tipo de documento, a competência, o momento da entrega e se a entrega está ativa, em duas tabelas (documentos periódicos e eventuais, e documentos diários).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-entrega` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-entrega |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-entrega |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização diária para os dois meses mais recentes e semanal para os demais |
| Cobertura | 2025-01 a em-curso |
| Unidade (uma linha) | uma entrega de documento de um fundo, classe ou subclasse |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (arquivo por mês); a data e a hora da entrega estão em `Data_Hora_Entrega` |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 11 |
| Unidades de medida | `ID_Documento`: código ou número de identificação (sem unidade) |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-entrega). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/ENTREGA/DADOS/`.
- O catálogo do fetcher lista 23 arquivo(s): de `fi_entrega_documento_202501.zip` a `fi_entrega_documento_202611.zip`.
- Em 2026-11-16 conferimos 4 arquivos Parquet convertidos de 2 arquivo(s) de origem (amostra: 2025-01, 2026-10).
- No bruto, o arquivo fica em `fi-entrega/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma entrega de documento de um fundo, classe ou subclasse.
- Particionado por `ano` e `mes`; o catálogo cobre 2025-01 a 2026-11, e conferimos as amostras 2025-01, 2026-10.
- Em 2026-10, `fi_entrega_documento` tem 85.804 linhas e `fi_entrega_documento_diario` 1.395.474. Os tipos mais frequentes de `Tipo_Documento` na primeira tabela são `CDA` (29.563), `BALANCETE` (24.028), `PERFIL` (16.792) e `INF MENS FIDC` (4.565) no arquivo de 2026-10, e `DIÁRIO FUNDOS` na segunda.
- `ID_Documento` identifica o documento entregue; `Ativo` assume `S` ou `N` e o dicionário da CVM não o descreve; no arquivo diário de 2026-10, para um mesmo fundo, tipo de documento e competência com mais de uma entrega, o padrão dominante é uma só entrega `S` e as demais `N` (535.912 + 316.431 linhas `N` contra 543.131 `S`).
- Este dataset reúne 2 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `fi_entrega_documento` | 11 | 114.558 | `ID_Subclasse`, `ID_Documento` | documentos periódicos e eventuais (CDA, balancete, perfil, lâmina, regulamento e outros) |
| `fi_entrega_documento_diario` | 11 | 1.395.474 | `ID_Subclasse`, `ID_Documento` | documentos diários (informe diário), um por dia de competência |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Tipo_Fundo_Classe` | `Tipo_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo fundo classe | — | todo |
| `CNPJ_Fundo_Classe` | `CNPJ_Fundo_Classe` | texto | CNPJ do fundo/classe | — | todo |
| `ID_Subclasse` | `ID_Subclasse` | texto | Identificador da subclasse | — | todo |
| `Tipo_Documento` | `Tipo_Documento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo documento | — | todo |
| `Data_Inicio_Competencia` | `Data_Inicio_Competencia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data inicio competencia | — | todo |
| `Data_Fim_Competencia` | `Data_Fim_Competencia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data fim competencia | — | todo |
| `ID_Documento` | `ID_Documento` | inteiro | Identificador do documento | código ou número de identificação (sem unidade) | todo |
| `Data_Hora_Entrega` | `Data_Hora_Entrega` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data hora entrega | — | todo |
| `Tipo_Apresentacao` | `Tipo_Apresentacao` | texto | Tipo de Apresentação | — | todo |
| `Ativo` | `Ativo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo | — | todo |
| `Sistema_Origem` | `Sistema_Origem` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: sistema origem | — | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-entrega`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **CNPJ só com dígitos.** `CNPJ_Fundo_Classe` vem com os 14 dígitos, sem máscara, ao contrário dos conjuntos de informes e balancetes (`00.000.000/0000-00`); normalize antes de juntar.
- **Reapresentações.** Uma competência pode ter várias entregas (`Tipo_Apresentacao`: apresentação ou reapresentação); `Ativo` marca com `S` a entrega que prevalece e com `N` as demais (o dicionário da CVM não o descreve; é o padrão observado no arquivo de 2026-10). Filtre `Ativo = 'S'` antes de contar entregas.
- **Janela de doze meses.** O portal publica os últimos doze meses e arquivos históricos desde 2021; o catálogo do fetcher parte de 2025-01 e lista 23 arquivos.
- **`ID_Subclasse` quase sempre vazio.** A coluna é nula em mais de 98% das linhas da tabela de documentos: a entrega é por fundo ou classe, raramente por subclasse.

## Exemplos

Entregas por tipo de documento e mês, só as ativas.

```python
import duckdb

duckdb.sql("""
    SELECT ano, mes, Tipo_Documento, count(*) AS entregas
    FROM read_parquet('lake/cvm/fi-entrega/**/fi_entrega_documento_20*__fi_entrega_documento_20*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE Ativo = 'S'
    GROUP BY ALL
    ORDER BY ano, mes, entregas DESC
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-entrega
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/ENTREGA/
