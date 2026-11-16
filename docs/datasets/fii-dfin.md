---
dataset:
  id: fii-dfin
  fonte: cvm
  titulo: "FII: Documentos: Demonstrações Financeiras (CVM)"
  resumo: "Demonstrações financeiras anuais dos Fundos de Investimento Imobiliário (FII): o índice dos documentos entregues, com a data de referência, a versão, a data de entrega, o parecer do auditor e o link do documento."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fii-doc-dfin
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-dfin"
  periodicidade: "anual (um arquivo por ano); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2016, fim: em-curso}
  unidade: "uma demonstração financeira entregue por um FII (um documento, identificado pelo link)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (arquivo por ano de entrega; `Data_Referencia` é a data-base da demonstração)"}
  formato_bruto: "CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [Link_Download], colunas: 10}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
  dados_pessoais: nenhum
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# FII: Documentos: Demonstrações Financeiras

## Resumo

Demonstrações financeiras anuais dos Fundos de Investimento Imobiliário (FII): o índice dos documentos entregues, com a data de referência, a versão, a data de entrega, o parecer do auditor e o link do documento.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fii-dfin` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fii-doc-dfin |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-dfin |
| Periodicidade | anual (um arquivo por ano); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2016 a em-curso |
| Unidade (uma linha) | uma demonstração financeira entregue por um FII (um documento, identificado pelo link) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (arquivo por ano de entrega; `Data_Referencia` é a data-base da demonstração) |
| Formato bruto | CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | `Link_Download` |
| Colunas | 10 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade) |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fii-doc-dfin). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FII/DOC/DFIN/DADOS/`.
- O catálogo do fetcher lista 11 arquivo(s): de `dfin_fii_2016.csv` a `dfin_fii_2026.csv`.
- Em 2026-11-16 conferimos 3 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2016, 2021, 2026).
- No bruto, o arquivo fica em `fii-dfin/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma demonstração financeira entregue por um FII (um documento, identificado pelo link).
- Particionado por `ano`; o catálogo cobre 2016 a 2026, e conferimos as amostras 2016, 2021, 2026.
- O arquivo traz o índice (`Link_Download` leva ao documento no FNET), não o conteúdo das demonstrações. O arquivo de 2026 tem 430 documentos (`Link_Download` único) e `Data_Referencia` de 2026-01-14 em diante; o de 2021 tem 662 e o de 2016 tem 298.
- `Parecer_Auditor` descreve o tipo de parecer (por exemplo, `Com ressalva` no primeiro registro de 2026).
- Uma tabela, com 10 colunas; o maior arquivo convertido tem 662 linhas. Chave candidata (única no arquivo mais recente convertido): `Link_Download`.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Fundo` | `CNPJ_Fundo` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_Fundo_Classe`) | — | 2016 |
| `Nome_Fundo` | `Nome_Fundo` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Nome_Fundo_Classe`) | — | 2016 |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento | — | todo |
| `Link_Download` | `Link_Download` | texto | Endereço para download do documento | — | todo |
| `Parecer_Auditor` | `Parecer_Auditor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: parecer auditor | — | todo |
| `Tipo_Fundo_Classe` | `Tipo_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo fundo classe | — | 2021 a 2026 |
| `CNPJ_Fundo_Classe` | `CNPJ_Fundo_Classe` | texto | CNPJ do fundo/classe | — | 2021 a 2026 |
| `Nome_Fundo_Classe` | `Nome_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome fundo classe | — | 2021 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fii-dfin`, particionado por `ano`; um arquivo Parquet por arquivo CSV de origem.
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Troca de colunas entre arquivos.** Os arquivos de 2016 usam `CNPJ_Fundo` e `Nome_Fundo`; o de 2026, `CNPJ_Fundo_Classe`, `Nome_Fundo_Classe` e `Tipo_Fundo_Classe` (os de 2021 e 2026 foram regravados em 2025-12 e 2026-11). Coalesça as colunas ao ler vários anos.
- **Índice, não valores.** Para os valores das demonstrações é preciso baixar o documento de `Link_Download`; o dataset não traz contas nem saldos.
- **Texto do parecer com caixa diferente.** No arquivo de 2016, `Parecer_Auditor` tem `ABSTENÇÃO DE OPNIÃO` (3 linhas) e `Abstenção de opinião` (1 linha); em 2026 há 6 valores (`Sem ressalva e sem ênfase` 276, `Sem ressalva e com ênfase` 71, `Abstenção de opinião` 39, `Com ressalva` 29, `Dispensado - art.23, §6º ICVM 516/11` 14 e `Adverso` 1). Padronize a caixa antes de agrupar.
- **Janela de cinco anos.** O portal publica os últimos cinco anos e o histórico desde 2016; o catálogo do fetcher lista 11 arquivos (2016 a 2026).

## Exemplos

Demonstrações entregues por ano e tipo de parecer.

```python
import duckdb

duckdb.sql("""
    SELECT ano, Parecer_Auditor, count(*) AS documentos
    FROM read_parquet('lake/cvm/fii-dfin/**/*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-dfin
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FII/DOC/DFIN/
