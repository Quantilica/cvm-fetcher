---
dataset:
  id: fi-inf-diario
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Informe Diário (CVM)"
  resumo: "Informe diário dos fundos de investimento: o valor da cota, o patrimônio líquido, a captação, os resgates e o número de cotistas de cada fundo, classe ou subclasse em cada dia útil."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-inf_diario
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-inf_diario"
  periodicidade: "mensal (um arquivo por mês, com um registro por dia útil); o portal declara atualização diária para os dois meses mais recentes e semanal para os demais"
  cobertura: {inicio: 2021-01, fim: em-curso}
  unidade: "o informe de um fundo, classe ou subclasse em um dia"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "diária (dia útil, `DT_COMPTC`), em arquivos mensais"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [CNPJ_FUNDO_CLASSE, ID_SUBCLASSE, DT_COMPTC], colunas: 12}
  unidades_de_medida:
    VL_TOTAL: "moeda (R$)"
    VL_QUOTA: "moeda (R$ por cota)"
    VL_PATRIM_LIQ: "moeda (R$)"
    CAPTC_DIA: "moeda (R$)"
    RESG_DIA: "moeda (R$)"
    NR_COTST: "quantidade (cotistas)"
  dados_pessoais: nenhum
  eras:
    - {desde: 2023-12, mudanca: "`CNPJ_FUNDO` e `TP_FUNDO` viram `CNPJ_FUNDO_CLASSE` e `TP_FUNDO_CLASSE`, e entra `ID_SUBCLASSE` (adaptação à Resolução CVM 175)"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Informe Diário

## Resumo

Informe diário dos fundos de investimento: o valor da cota, o patrimônio líquido, a captação, os resgates e o número de cotistas de cada fundo, classe ou subclasse em cada dia útil.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-inf-diario` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-inf_diario |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-inf_diario |
| Periodicidade | mensal (um arquivo por mês, com um registro por dia útil); o portal declara atualização diária para os dois meses mais recentes e semanal para os demais |
| Cobertura | 2021-01 a em-curso |
| Unidade (uma linha) | o informe de um fundo, classe ou subclasse em um dia |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: diária (dia útil, `DT_COMPTC`), em arquivos mensais |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `CNPJ_FUNDO_CLASSE`, `ID_SUBCLASSE`, `DT_COMPTC` |
| Colunas | 12 |
| Unidades de medida | `VL_TOTAL`: moeda (R$); `VL_QUOTA`: moeda (R$ por cota); `VL_PATRIM_LIQ`: moeda (R$); `CAPTC_DIA`: moeda (R$); `RESG_DIA`: moeda (R$); `NR_COTST`: quantidade (cotistas) |
| Dados pessoais | nenhum |
| Eras | 2023-12: `CNPJ_FUNDO` e `TP_FUNDO` viram `CNPJ_FUNDO_CLASSE` e `TP_FUNDO_CLASSE`, e entra `ID_SUBCLASSE` (adaptação à Resolução CVM 175) |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-inf_diario). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/`.
- O catálogo do fetcher lista 71 arquivo(s): de `inf_diario_fi_202101.zip` a `inf_diario_fi_202611.zip`.
- Em 2026-11-16 conferimos 3 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2021-01, 2023-12, 2026-10).
- No bruto, o arquivo fica em `fi-inf-diario/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe de um fundo, classe ou subclasse em um dia.
- Particionado por `ano` e `mes`; o catálogo cobre 2021-01 a 2026-11, e conferimos as amostras 2021-01, 2023-12, 2026-10.
- Em 2026-10 o arquivo tem 538.270 linhas em 22 dias úteis (2026-10-01 a 2026-10-30); em 2023-12, 514.295 linhas em 21 dias; em 2021-01, 389.625 linhas em 21 dias. O valor `TP_FUNDO_CLASSE` mais comum em 2026-10 é `CLASSES - FIF` (537.835 linhas); os demais são `FI` (162) e `CLASSE FIF/FAPI` (273).
- A chave `CNPJ_FUNDO_CLASSE` + `ID_SUBCLASSE` + `DT_COMPTC` é única em 2026-10; em 2023-12 há uma linha repetida (mesmo fundo e dia, mesmos valores). `ID_SUBCLASSE` é nulo em 516.662 das 538.270 linhas de 2026-10 (a maioria é classe sem subclasse) e nulo em todas as linhas de 2023-12.
- Uma tabela, com 12 colunas; o maior arquivo convertido tem 538.270 linhas. Chave candidata (única no arquivo mais recente convertido): `CNPJ_FUNDO_CLASSE`, `ID_SUBCLASSE`, `DT_COMPTC`.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `TP_FUNDO` | `TP_FUNDO` | texto | Tipo de fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `TP_FUNDO_CLASSE`) | — | 2021-01 |
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE`) | — | 2021-01 |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `VL_TOTAL` | `VL_TOTAL` | decimal | Valor total da carteira | moeda (R$) | todo |
| `VL_QUOTA` | `VL_QUOTA` | decimal | Valor da cota | moeda (R$ por cota) | todo |
| `VL_PATRIM_LIQ` | `VL_PATRIM_LIQ` | decimal | Valor do patrimônio líquido | moeda (R$) | todo |
| `CAPTC_DIA` | `CAPTC_DIA` | decimal | Captação do dia | moeda (R$) | todo |
| `RESG_DIA` | `RESG_DIA` | decimal | Resgate no dia | moeda (R$) | todo |
| `NR_COTST` | `NR_COTST` | inteiro | Número de cotistas | quantidade (cotistas) | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe | — | 2023-12 a 2026-10 |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe | — | 2023-12 a 2026-10 |
| `ID_SUBCLASSE` | `ID_SUBCLASSE` | texto | Identificador da subclasse | — | 2023-12 a 2026-10 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-inf-diario`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Troca de coluna de identificação em 2023-12.** Os arquivos até 2023-11 trazem `CNPJ_FUNDO` e `TP_FUNDO`; os de 2023-12 em diante, `CNPJ_FUNDO_CLASSE`, `TP_FUNDO_CLASSE` e `ID_SUBCLASSE`. Ao ler vários meses, coalesça `CNPJ_FUNDO` e `CNPJ_FUNDO_CLASSE`.
- **Valores de `TP_FUNDO_CLASSE` mudam de uma era para outra.** Em 2021 a coluna `TP_FUNDO` tem `FI`, `FAPI`, `FMP-FGTS`, `FMP-FGTS CL`, `FIF` e `FACFIF`; em 2026, `TP_FUNDO_CLASSE` tem `CLASSES - FIF`, `CLASSE FIF/FAPI` e `FI`.
- **Valores extremos e negativos.** `VL_QUOTA` tem mínimo negativo em todos os meses amostrados (-16.194 em 2026-10) e `VL_TOTAL` chega a 3,4e14 em 2026-10, contra 3,0e11 no máximo de `VL_PATRIM_LIQ`; trate outliers antes de calcular rentabilidade ou somar.
- **Soma de patrimônio pode contar em dobro.** Os fundos que aplicam em cotas de outros fundos (FIC) aparecem no arquivo junto com os fundos em que investem; somar `VL_PATRIM_LIQ` de todas as linhas conta duas vezes o patrimônio investido entre fundos.
- **Janela de doze meses.** O portal mantém os últimos doze meses atualizados; o catálogo do fetcher parte de 2021-01 e lista 71 arquivos.

## Exemplos

Patrimônio líquido e captação líquida por dia em um mês (esquema desde 2023-12).

```python
import duckdb

duckdb.sql("""
    SELECT DT_COMPTC, count(*) AS classes, sum(VL_PATRIM_LIQ) AS pl, sum(CAPTC_DIA - RESG_DIA) AS captacao_liquida
    FROM read_parquet('lake/cvm/fi-inf-diario/ano=2026/mes=10/*.parquet')
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-inf_diario
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/
