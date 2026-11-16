---
dataset:
  id: fi-balancete
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Balancete (CVM)"
  resumo: "Balancetes mensais dos fundos de investimento: o saldo de cada conta do plano contábil do fundo (plano COFI), no fim de cada mês."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-balancete
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-balancete"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização semanal (os arquivos de 2026-09 e 2026-10 foram regravados em 2026-11-14)"
  cobertura: {inicio: 2015-01, fim: em-curso}
  unidade: "o saldo de uma conta contábil de um fundo (ou classe) em um mês"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (último dia do mês, `DT_COMPTC`)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [CNPJ_FUNDO_CLASSE, CD_CONTA_BALCTE], colunas: 7}
  unidades_de_medida:
    VL_SALDO_BALCTE: "moeda (R$)"
  dados_pessoais: nenhum
  eras:
    - {desde: 2023-11, mudanca: "`CNPJ_FUNDO` vira `CNPJ_FUNDO_CLASSE` e entra `TP_FUNDO_CLASSE` (adaptação à Resolução CVM 175)"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Balancete

## Resumo

Balancetes mensais dos fundos de investimento: o saldo de cada conta do plano contábil do fundo (plano COFI), no fim de cada mês.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-balancete` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-balancete |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-balancete |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização semanal (os arquivos de 2026-09 e 2026-10 foram regravados em 2026-11-14) |
| Cobertura | 2015-01 a em-curso |
| Unidade (uma linha) | o saldo de uma conta contábil de um fundo (ou classe) em um mês |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (último dia do mês, `DT_COMPTC`) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `CNPJ_FUNDO_CLASSE`, `CD_CONTA_BALCTE` |
| Colunas | 7 |
| Unidades de medida | `VL_SALDO_BALCTE`: moeda (R$) |
| Dados pessoais | nenhum |
| Eras | 2023-11: `CNPJ_FUNDO` vira `CNPJ_FUNDO_CLASSE` e entra `TP_FUNDO_CLASSE` (adaptação à Resolução CVM 175) |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-balancete). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/BALANCETE/DADOS/`.
- O catálogo do fetcher lista 143 arquivo(s): de `balancete_fi_201501.zip` a `balancete_fi_202611.zip`.
- Em 2026-11-16 conferimos 3 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2015-01, 2020-12, 2026-10).
- No bruto, o arquivo fica em `fi-balancete/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o saldo de uma conta contábil de um fundo (ou classe) em um mês.
- Particionado por `ano` e `mes`; o catálogo cobre 2015-01 a 2026-11, e conferimos as amostras 2015-01, 2020-12, 2026-10.
- O arquivo de 2026-10 tem 1.954.887 linhas, 374 contas distintas (`CD_CONTA_BALCTE`) e um único `DT_COMPTC` (2026-10-31); o plano de contas (`PLANO_CONTA_BALCTE`) é o COFI. A chave `CNPJ_FUNDO_CLASSE` + `CD_CONTA_BALCTE` (em 2015-01 e 2020-12, `CNPJ_FUNDO` + `CD_CONTA_BALCTE`) é única nos três arquivos amostrados.
- O portal disponibiliza os balancetes dos últimos doze meses com atualização semanal, e o histórico desde 2015-01 em arquivos que não são mais atualizados.
- Uma tabela, com 7 colunas; o maior arquivo convertido tem 1.954.887 linhas. Chave candidata (única no arquivo mais recente convertido): `CNPJ_FUNDO_CLASSE`, `CD_CONTA_BALCTE`.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE`) | — | 2015-01 a 2020-12 |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `PLANO_CONTA_BALCTE` | `PLANO_CONTA_BALCTE` | texto | Plano contábil utilizado no balancete | — | todo |
| `CD_CONTA_BALCTE` | `CD_CONTA_BALCTE` | inteiro | Código da conta | código ou número de identificação (sem unidade) | todo |
| `VL_SALDO_BALCTE` | `VL_SALDO_BALCTE` | decimal | Saldo da conta | moeda (R$) | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe | — | 2026-10 |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe | — | 2026-10 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-balancete`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Troca de coluna de identificação.** Até 2023-10 o CNPJ está em `CNPJ_FUNDO` e o arquivo não tem `TP_FUNDO_CLASSE`; desde 2023-11 o CNPJ está em `CNPJ_FUNDO_CLASSE`. Ao ler vários meses com `union_by_name`, coalesça as duas colunas.
- **O saldo não traz descrição da conta.** O arquivo traz só o código (`CD_CONTA_BALCTE`) e o plano; a descrição de cada conta está no plano COFI, fora do dataset.
- **Saldos com sinal.** `VL_SALDO_BALCTE` é negativo em cerca de 19% das linhas (377.113 de 1.954.887 em 2026-10); o sinal segue a natureza da conta no plano, então confira o código antes de somar contas.

## Exemplos

Saldo por conta de uma classe em um mês.

```python
import duckdb

duckdb.sql("""
    SELECT CD_CONTA_BALCTE, VL_SALDO_BALCTE
    FROM read_parquet('lake/cvm/fi-balancete/ano=2026/mes=10/*.parquet')
    WHERE CNPJ_FUNDO_CLASSE = '00.017.024/0001-53'
    ORDER BY CD_CONTA_BALCTE
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-balancete
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/BALANCETE/
