---
dataset:
  id: fi-cda
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Composição e Diversificação das Aplicações (CVM)"
  resumo: "Composição e Diversificação das Aplicações (CDA) dos fundos de investimento: as posições de cada fundo ou classe por bloco de ativo (títulos públicos, cotas de fundos, swaps, ativos codificados, depósitos, crédito privado, exterior e outros), em 13 tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-cda
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-cda"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização diária para os três meses mais recentes e semanal para os demais"
  cobertura: {inicio: 2023-01, fim: em-curso}
  unidade: "uma posição de um ativo na carteira de um fundo ou classe em uma competência (nas tabelas de blocos); o patrimônio líquido de um fundo (em `cda_fi_pl`)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (competência, `DT_COMPTC`)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [], colunas: 63}
  unidades_de_medida:
    QT_VENDA_NEGOC: "quantidade"
    VL_VENDA_NEGOC: "moeda (R$)"
    QT_AQUIS_NEGOC: "quantidade"
    VL_AQUIS_NEGOC: "moeda (R$)"
    QT_POS_FINAL: "quantidade"
    VL_MERC_POS_FINAL: "moeda (R$)"
    VL_CUSTO_POS_FINAL: "moeda (R$)"
    CD_SELIC: "código ou número de identificação (sem unidade)"
    PR_INDEXADOR_POSFX: "percentual (%)"
    PR_CUPOM_POSFX: "percentual (%)"
    PR_TAXA_PREFX: "percentual (%)"
    CD_PAIS: "código ou número de identificação (sem unidade)"
    QT_ATIVO_EXTERIOR: "quantidade"
    VL_ATIVO_EXTERIOR: "moeda (R$)"
    VL_PATRIM_LIQ: "moeda (R$)"
    ID_DOC: "código ou número de identificação (sem unidade)"
  dados_pessoais:
    - {coluna: CPF_CNPJ_EMISSOR, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras:
    - {desde: 2023-12, mudanca: "`CNPJ_FUNDO` e `TP_FUNDO` viram `CNPJ_FUNDO_CLASSE` e `TP_FUNDO_CLASSE` (adaptação à Resolução CVM 175)"}
    - {desde: 2024-03, mudanca: "as aplicações dos fundos de índice de mercado (competência 2018-06 em diante) passam a vir em `cda_fiim`, independentemente do bloco"}
    - {desde: 2025-11, mudanca: "`cda_fiim` passa a se chamar `cda_fie` e a incluir os FIDC e os FIAGRO"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Composição e Diversificação das Aplicações

## Resumo

Composição e Diversificação das Aplicações (CDA) dos fundos de investimento: as posições de cada fundo ou classe por bloco de ativo (títulos públicos, cotas de fundos, swaps, ativos codificados, depósitos, crédito privado, exterior e outros), em 13 tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-cda` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-cda |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-cda |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização diária para os três meses mais recentes e semanal para os demais |
| Cobertura | 2023-01 a em-curso |
| Unidade (uma linha) | uma posição de um ativo na carteira de um fundo ou classe em uma competência (nas tabelas de blocos); o patrimônio líquido de um fundo (em `cda_fi_pl`) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (competência, `DT_COMPTC`) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 63 |
| Unidades de medida | `QT_VENDA_NEGOC`: quantidade; `VL_VENDA_NEGOC`: moeda (R$); `QT_AQUIS_NEGOC`: quantidade; `VL_AQUIS_NEGOC`: moeda (R$); `QT_POS_FINAL`: quantidade; `VL_MERC_POS_FINAL`: moeda (R$); `VL_CUSTO_POS_FINAL`: moeda (R$); `CD_SELIC`: código ou número de identificação (sem unidade); `PR_INDEXADOR_POSFX`: percentual (%); `PR_CUPOM_POSFX`: percentual (%); `PR_TAXA_PREFX`: percentual (%); `CD_PAIS`: código ou número de identificação (sem unidade); `QT_ATIVO_EXTERIOR`: quantidade; `VL_ATIVO_EXTERIOR`: moeda (R$); `VL_PATRIM_LIQ`: moeda (R$); `ID_DOC`: código ou número de identificação (sem unidade) |
| Dados pessoais | `CPF_CNPJ_EMISSOR` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | 2023-12: `CNPJ_FUNDO` e `TP_FUNDO` viram `CNPJ_FUNDO_CLASSE` e `TP_FUNDO_CLASSE` (adaptação à Resolução CVM 175); 2024-03: as aplicações dos fundos de índice de mercado (competência 2018-06 em diante) passam a vir em `cda_fiim`, independentemente do bloco; 2025-11: `cda_fiim` passa a se chamar `cda_fie` e a incluir os FIDC e os FIAGRO |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-cda). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/CDA/DADOS/`.
- O catálogo do fetcher lista 47 arquivo(s): de `cda_fi_202301.zip` a `cda_fi_202611.zip`.
- Em 2026-11-16 conferimos 32 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2023-01, 2024-12, 2026-10).
- No bruto, o arquivo fica em `fi-cda/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma posição de um ativo na carteira de um fundo ou classe em uma competência (nas tabelas de blocos); o patrimônio líquido de um fundo (em `cda_fi_pl`).
- Particionado por `ano` e `mes`; o catálogo cobre 2023-01 a 2026-11, e conferimos as amostras 2023-01, 2024-12, 2026-10.
- Os blocos seguem o padrão XML do Informe CDA. As tabelas `cda_fiim` e `cda_fie` repetem as colunas de todos os blocos (31 colunas) numa só tabela; no lake, cada arquivo de origem traz uma ou outra conforme a data em que a CVM o regravou (o arquivo de 2023-01 tem `cda_fiim`; os de 2024-12 e 2026-10, `cda_fie`).
- As posições confidenciais só aparecem em `cda_fi_confid` e `cda_fie_confid`, de forma consolidada (sem o ativo), até expirar o prazo de confidencialidade; o arquivo de 2026-10 tem 55.037 linhas em `cda_fi_confid` e 770 em `cda_fie_confid`.
- Tamanho no arquivo de 2026-10: `cda_fi_blc_4` (demais ativos codificados) tem 132.385 linhas, `cda_fi_blc_8` 141.808, `cda_fi_blc_7` 55.567 e `cda_fi_pl` 24.775 fundos ou classes. O catálogo do fetcher parte de 2023-01 (o portal tem histórico desde 2021-01).
- Este dataset reúne 13 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `cda_fi_blc_1` | 23 | 44.689 | `CNPJ_FUNDO_CLASSE`, `EMISSOR_LIGADO`, `TP_NEGOC`, `CD_ISIN` | bloco 1: títulos públicos do Selic |
| `cda_fi_blc_2` | 23 | 182.884 | `CNPJ_FUNDO_CLASSE`, `CNPJ_FUNDO_CLASSE_COTA`, `ID_SUBCLASSE` | bloco 2: cotas de fundos de investimento |
| `cda_fi_blc_3` | 20 | 308 | `CNPJ_FUNDO_CLASSE`, `TP_APLIC`, `CD_SWAP` | bloco 3: swaps |
| `cda_fi_blc_4` | 23 | 237.292 | `CNPJ_FUNDO_CLASSE`, `TP_APLIC`, `TP_NEGOC`, `CD_ATIVO` | bloco 4: demais ativos codificados (ações, debêntures, opções e outros) |
| `cda_fi_blc_5` | 31 | 70.622 | não determinada | bloco 5: depósitos a prazo e outros títulos de instituições financeiras |
| `cda_fi_blc_6` | 31 | 11.144 | não determinada | bloco 6: títulos do agronegócio e de crédito privado |
| `cda_fi_blc_7` | 34 | 59.691 | `CNPJ_FUNDO_CLASSE`, `EMISSOR`, `DT_VENC`, `CD_ATIVO_BV_MERC` | bloco 7: investimentos no exterior |
| `cda_fi_blc_8` | 22 | 223.365 | não determinada | bloco 8: demais ativos não codificados |
| `cda_fi_confid` | 10 | 55.037 | `CNPJ_FUNDO_CLASSE`, `TP_APLIC` | aplicações sob prazo de confidencialidade, só em forma consolidada |
| `cda_fi_pl` | 7 | 26.304 | `CNPJ_FUNDO_CLASSE` | patrimônio líquido de cada fundo ou classe na competência |
| `cda_fie` | 31 | 15.390 | não determinada | aplicações dos fundos estruturados (índice de mercado, FIDC e FIAGRO), em qualquer bloco; nome usado desde 2025-11 (antes, `cda_fiim`) |
| `cda_fie_confid` | 11 | 770 | `CNPJ_FUNDO_CLASSE`, `VL_MERC_POS_FINAL` | aplicações dos fundos estruturados sob prazo de confidencialidade |
| `cda_fiim` | 31 | 4.467 | não determinada | aplicações dos fundos de índice de mercado (FIIM), em qualquer bloco; nome usado de 2024-03 a 2025-11 (depois, `cda_fie`) |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `TP_FUNDO` | `TP_FUNDO` | texto | Tipo de fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `TP_FUNDO_CLASSE`) (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | — | 2023-01 |
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE`) (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | — | 2023-01 |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `TP_APLIC` | `TP_APLIC` | texto | Tipo de aplicação (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | — | todo |
| `TP_ATIVO` | `TP_ATIVO` | texto | Tipo de ativo (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | — | todo |
| `EMISSOR_LIGADO` | `EMISSOR_LIGADO` | texto | Indica se o emissor da aplicação é ligado ao gestor ou administrador do fundo de investimento (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | S/N | todo |
| `TP_NEGOC` | `TP_NEGOC` | texto | Tipo de negociação (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | Para negociação/Mantido até o vencimento | todo |
| `QT_VENDA_NEGOC` | `QT_VENDA_NEGOC` | decimal / texto | Quantidade de vendas dos negócios realizados no mês (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | quantidade | todo |
| `VL_VENDA_NEGOC` | `VL_VENDA_NEGOC` | decimal / inteiro / texto | Valor das vendas dos negócios realizados no mês (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | moeda (R$) | todo |
| `QT_AQUIS_NEGOC` | `QT_AQUIS_NEGOC` | decimal / texto | Quantidade de aquisições dos negócios realizados no mês (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | quantidade | todo |
| `VL_AQUIS_NEGOC` | `VL_AQUIS_NEGOC` | decimal / inteiro / texto | Valor das aquisições dos negócios realizados no mês (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | moeda (R$) | todo |
| `QT_POS_FINAL` | `QT_POS_FINAL` | decimal / texto | Quantidade da posição final (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 6) | quantidade | todo |
| `VL_MERC_POS_FINAL` | `VL_MERC_POS_FINAL` | decimal / inteiro | Valor de mercado da posição final (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | moeda (R$) | todo |
| `VL_CUSTO_POS_FINAL` | `VL_CUSTO_POS_FINAL` | decimal / texto | Valor de custo da posição final (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | moeda (R$) | todo |
| `DT_CONFID_APLIC` | `DT_CONFID_APLIC` | texto | Prazo de confidencialidade da aplicação (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | — | todo |
| `TP_TITPUB` | `TP_TITPUB` | texto | Tipo de título público (só em: `cda_fi_blc_1`) | — | todo |
| `CD_ISIN` | `CD_ISIN` | texto | Código ISIN (International Securities Identification Number) (só em: `cda_fi_blc_1`, `cda_fi_blc_4`) | — | todo |
| `CD_SELIC` | `CD_SELIC` | inteiro | Código SELIC (só em: `cda_fi_blc_1`, `cda_fie`, `cda_fiim`) | código ou número de identificação (sem unidade) | todo |
| `DT_EMISSAO` | `DT_EMISSAO` | texto | Data de emissão (só em: `cda_fi_blc_1`) | — | todo |
| `DT_VENC` | `DT_VENC` | texto | Data de vencimento (só em: `cda_fi_blc_1`, `cda_fi_blc_5`, `cda_fi_blc_6`, `cda_fi_blc_7` e mais 2) | — | todo |
| `CNPJ_FUNDO_COTA` | `CNPJ_FUNDO_COTA` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE_COTA`) (só em: `cda_fi_blc_2`) | — | 2023-01 |
| `NM_FUNDO_COTA` | `NM_FUNDO_COTA` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nm fundo cota (só em: `cda_fi_blc_2`) | — | 2023-01 |
| `CD_SWAP` | `CD_SWAP` | texto | Código SWAP (só em: `cda_fi_blc_3`) | — | todo |
| `DS_SWAP` | `DS_SWAP` | texto | Descrição do tipo de ativo SWAP (só em: `cda_fi_blc_3`) | — | todo |
| `CD_ATIVO` | `CD_ATIVO` | texto | Código do ativo (só em: `cda_fi_blc_4`, `cda_fie`, `cda_fiim`) | — | todo |
| `DS_ATIVO` | `DS_ATIVO` | texto | Descrição do ativo (só em: `cda_fi_blc_4`, `cda_fi_blc_8`, `cda_fie`, `cda_fiim`) | — | todo |
| `DT_INI_VIGENCIA` | `DT_INI_VIGENCIA` | texto | Data início da vigência (só em: `cda_fi_blc_4`, `cda_fie`, `cda_fiim`) | — | todo |
| `DT_FIM_VIGENCIA` | `DT_FIM_VIGENCIA` | texto | Data fim da vigência (só em: `cda_fi_blc_4`) | — | todo |
| `CNPJ_EMISSOR` | `CNPJ_EMISSOR` | texto | CNPJ do emissor (só em: `cda_fi_blc_5`) | — | todo |
| `EMISSOR` | `EMISSOR` | texto | Nome do Emissor (só em: `cda_fi_blc_5`, `cda_fi_blc_6`, `cda_fi_blc_7`, `cda_fi_blc_8` e mais 2) | — | todo |
| `TITULO_POSFX` | `TITULO_POSFX` | texto | Indica se é título pós-fixado (só em: `cda_fi_blc_5`, `cda_fi_blc_6`) | S/N | todo |
| `CD_INDEXADOR_POSFX` | `CD_INDEXADOR_POSFX` | texto | Código do indexador (somente pós-fixados) (só em: `cda_fi_blc_5`, `cda_fi_blc_6`) | — | todo |
| `DS_INDEXADOR_POSFX` | `DS_INDEXADOR_POSFX` | texto | Descrição do indexador (somente pós-fixados) (só em: `cda_fi_blc_5`, `cda_fi_blc_6`) | — | todo |
| `PR_INDEXADOR_POSFX` | `PR_INDEXADOR_POSFX` | decimal | Percentual do indexador (somente pós-fixados) (só em: `cda_fi_blc_5`, `cda_fi_blc_6`) | percentual (%) | todo |
| `PR_CUPOM_POSFX` | `PR_CUPOM_POSFX` | decimal | Percentual do cupom (somente pós-fixados) (só em: `cda_fi_blc_5`, `cda_fi_blc_6`) | percentual (%) | todo |
| `PR_TAXA_PREFX` | `PR_TAXA_PREFX` | decimal | Percentual da taxa contratada (somente pré-fixados) (só em: `cda_fi_blc_5`, `cda_fi_blc_6`) | percentual (%) | todo |
| `RISCO_EMISSOR` | `RISCO_EMISSOR` | texto | Indica se o emissor do título possui classificação de risco (só em: `cda_fi_blc_5`, `cda_fi_blc_7`, `cda_fie`, `cda_fiim`) | S/N | todo |
| `AG_RISCO` | `AG_RISCO` | texto | Nome da agência de classificação de risco (só em: `cda_fi_blc_5`, `cda_fi_blc_7`) | — | todo |
| `DT_RISCO` | `DT_RISCO` | texto | Data da classificação de risco (só em: `cda_fi_blc_5`, `cda_fi_blc_7`) | — | todo |
| `GRAU_RISCO` | `GRAU_RISCO` | texto | Grau de risco atribuído (só em: `cda_fi_blc_5`, `cda_fi_blc_7`) | — | todo |
| `PF_PJ_EMISSOR` | `PF_PJ_EMISSOR` | texto | Indica se o emissor é pessoa física ou jurídica (só em: `cda_fi_blc_6`, `cda_fi_blc_8`, `cda_fie`, `cda_fiim`) | PF/PJ | todo |
| `CPF_CNPJ_EMISSOR` | `CPF_CNPJ_EMISSOR` | texto | Informa o código de identificação do emissor, pessoa física ou jurídica (só em: `cda_fi_blc_6`, `cda_fi_blc_8`, `cda_fie`, `cda_fiim`) | — | todo |
| `TITULO_CETIP` | `TITULO_CETIP` | texto | Indica se é título registrado na CETIP (só em: `cda_fi_blc_6`) | S/N | todo |
| `TITULO_GARANTIA` | `TITULO_GARANTIA` | texto | Indica se o título possui garantia ou seguro (só em: `cda_fi_blc_6`) | S/N | todo |
| `CNPJ_INSTITUICAO_FINANC_COOBR` | `CNPJ_INSTITUICAO_FINANC_COOBR` | texto | CNPJ da instituição financeira com coobrigação (só em: `cda_fi_blc_6`) | — | todo |
| `INVEST_COLETIVO` | `INVEST_COLETIVO` | texto | Indica se é veículo de investimento coletivo (só em: `cda_fi_blc_7`) | S/N | todo |
| `INVEST_COLETIVO_GESTOR` | `INVEST_COLETIVO_GESTOR` | texto | Indica se a gestão da carteira do veículo de investimento coletivo conta com influência, direta ou indireta, do gestor (só em: `cda_fi_blc_7`) | S/N | todo |
| `CD_PAIS` | `CD_PAIS` | inteiro / texto | Código do país (só em: `cda_fi_blc_7`, `cda_fie`, `cda_fiim`) | código ou número de identificação (sem unidade) | todo |
| `PAIS` | `PAIS` | texto | País (só em: `cda_fi_blc_7`, `cda_fie`, `cda_fiim`) | — | todo |
| `CD_BV_MERC` | `CD_BV_MERC` | texto | Código da Bolsa ou Mercado de balcão (só em: `cda_fi_blc_7`, `cda_fie`, `cda_fiim`) | — | todo |
| `BV_MERC` | `BV_MERC` | texto | Bolsa ou Mercado de balcão (só em: `cda_fi_blc_7`, `cda_fie`, `cda_fiim`) | — | todo |
| `CD_ATIVO_BV_MERC` | `CD_ATIVO_BV_MERC` | texto | Código do ativo na Bolsa ou Mercado de balcão onde foi adquirido (só em: `cda_fi_blc_7`) | — | todo |
| `DS_ATIVO_EXTERIOR` | `DS_ATIVO_EXTERIOR` | texto | Descrição do ativo no exterior (só em: `cda_fi_blc_7`) | — | todo |
| `QT_ATIVO_EXTERIOR` | `QT_ATIVO_EXTERIOR` | inteiro | Quantidade de ativos no exterior (só em: `cda_fi_blc_7`) | quantidade | todo |
| `VL_ATIVO_EXTERIOR` | `VL_ATIVO_EXTERIOR` | decimal | Valor do ativo no exterior (só em: `cda_fi_blc_7`) | moeda (R$) | todo |
| `VL_PATRIM_LIQ` | `VL_PATRIM_LIQ` | decimal | Valor do patrimônio líquido (só em: `cda_fi_pl`, `cda_fie`, `cda_fiim`) | moeda (R$) | todo |
| `ID_DOC` | `ID_DOC` | inteiro | Identificador do documento (só em: `cda_fie`, `cda_fie_confid`, `cda_fiim`) | código ou número de identificação (sem unidade) | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | — | 2024-12 a 2026-10 |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe (só em: `cda_fi_blc_1`, `cda_fi_blc_2`, `cda_fi_blc_3`, `cda_fi_blc_4` e mais 8) | — | 2024-12 a 2026-10 |
| `CNPJ_FUNDO_CLASSE_COTA` | `CNPJ_FUNDO_CLASSE_COTA` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj fundo classe cota (só em: `cda_fi_blc_2`) | — | 2024-12 a 2026-10 |
| `ID_SUBCLASSE` | `ID_SUBCLASSE` | texto | Identificador da subclasse (só em: `cda_fi_blc_2`) | — | 2024-12 a 2026-10 |
| `NM_FUNDO_CLASSE_SUBCLASSE_COTA` | `NM_FUNDO_CLASSE_SUBCLASSE_COTA` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nm fundo classe subclasse cota (só em: `cda_fi_blc_2`) | — | 2024-12 a 2026-10 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-cda`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Troca de coluna de identificação em 2023-12.** Até 2023-11 o CNPJ do fundo está em `CNPJ_FUNDO` (e há `TP_FUNDO`); de 2023-12 em diante, em `CNPJ_FUNDO_CLASSE` e `TP_FUNDO_CLASSE`. Nos blocos de cotas (`cda_fi_blc_2`), a coluna da cota investida também muda (`CNPJ_FUNDO_COTA` para `CNPJ_FUNDO_CLASSE_COTA`).
- **Fundos de índice, FIDC e FIAGRO ficam fora dos blocos.** Nenhum dos 689 CNPJ de `cda_fie` (arquivo de 2026-10) aparece nos blocos 1 a 8 do mesmo mês: a carteira desses fundos está só em `cda_fie` (antes, `cda_fiim`), e a dos demais fundos, só nos blocos. Junte as tabelas para ter a carteira completa; `cda_fi_pl` traz o patrimônio líquido de cada fundo.
- **Colunas quase vazias.** `VL_CUSTO_POS_FINAL` e `DT_CONFID_APLIC` têm mais de 98% de nulos na maioria dos blocos do arquivo de 2026-10 (a coluna de custo existe em todos os blocos, mas só alguns fundos a preenchem).
- **`CPF_CNPJ_EMISSOR` mistura CPF e CNPJ.** Em `cda_fi_blc_6` do arquivo de 2026-10, 1.542 das 1.547 linhas preenchidas são CNPJ e 5 são CPF (11 dígitos); o formato varia entre tabelas (com e sem máscara). O fetcher e o lake preservam o que a fonte publica.
- **Tipo inferido varia entre arquivos.** 8 coluna(s) (`QT_VENDA_NEGOC`, `VL_VENDA_NEGOC`, `QT_AQUIS_NEGOC`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Patrimônio líquido total informado no CDA por competência (esquema desde 2023-12).

```python
import duckdb

duckdb.sql("""
    SELECT DT_COMPTC, count(*) AS fundos_e_classes, sum(VL_PATRIM_LIQ) AS pl
    FROM read_parquet('lake/cvm/fi-cda/**/*__cda_fi_pl_*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-cda
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/CDA/
