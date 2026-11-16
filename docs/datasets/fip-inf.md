---
dataset:
  id: fip-inf
  fonte: cvm
  titulo: "Fundos de Investimento em Participações: Documentos: Informes Trimestral e Quadrimestral (CVM)"
  resumo: "Informes dos Fundos de Investimento em Participações (FIP): trimestral de 2010 a 2023 e quadrimestral desde 2024, com patrimônio, cotas, cotistas, capital comprometido e demais itens, em duas tabelas (uma por periodicidade)."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fip-doc-inf_trimestral
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fip-doc-inf_trimestral"
  periodicidade: "anual (um arquivo por ano); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2010, fim: em-curso}
  unidade: "o informe de um FIP (fundo ou classe) em uma data de competência"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "trimestral até 2023 e quadrimestral desde 2024 (`DT_COMPTC`), em arquivos anuais"}
  formato_bruto: "CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 56}
  unidades_de_medida:
    VL_PATRIM_LIQ: "moeda (R$)"
    QT_COTA: "quantidade"
    VL_PATRIM_COTA: "moeda (R$ por cota)"
    NR_COTST: "quantidade"
    VL_CAP_COMPROM: "moeda (R$)"
    QT_COTA_SUBSCR: "quantidade"
    VL_CAP_SUBSCR: "moeda (R$)"
    QT_COTA_INTEGR: "quantidade"
    VL_CAP_INTEGR: "moeda (R$)"
    VL_INVEST_FIP_COTA: "moeda (R$)"
    NR_COTST_SUBSCR_PF: "quantidade"
    PR_COTA_SUBSCR_PF: "percentual (%)"
    NR_COTST_SUBSCR_PJ_NAO_FINANC: "quantidade"
    PR_COTA_SUBSCR_PJ_NAO_FINANC: "percentual (%)"
    NR_COTST_SUBSCR_BANCO: "quantidade"
    PR_COTA_SUBSCR_BANCO: "percentual (%)"
    NR_COTST_SUBSCR_CORRETORA_DISTRIB: "quantidade"
    PR_COTA_SUBSCR_CORRETORA_DISTRIB: "percentual (%)"
    NR_COTST_SUBSCR_PJ_FINANC: "quantidade"
    PR_COTA_SUBSCR_PJ_FINANC: "percentual (%)"
    NR_COTST_SUBSCR_INVNR: "quantidade"
    PR_COTA_SUBSCR_INVNR: "percentual (%)"
    NR_COTST_SUBSCR_EAPC: "quantidade"
    PR_COTA_SUBSCR_EAPC: "percentual (%)"
    NR_COTST_SUBSCR_EFPC: "quantidade"
    PR_COTA_SUBSCR_EFPC: "percentual (%)"
    NR_COTST_SUBSCR_RPPS: "quantidade"
    PR_COTA_SUBSCR_RPPS: "percentual (%)"
    NR_COTST_SUBSCR_SEGUR: "quantidade"
    PR_COTA_SUBSCR_SEGUR: "percentual (%)"
    NR_COTST_SUBSCR_CAPITALIZ: "quantidade"
    PR_COTA_SUBSCR_CAPITALIZ: "percentual (%)"
    NR_COTST_SUBSCR_FII: "quantidade"
    PR_COTA_SUBSCR_FII: "percentual (%)"
    NR_COTST_SUBSCR_FI: "quantidade"
    PR_COTA_SUBSCR_FI: "percentual (%)"
    NR_COTST_SUBSCR_DISTRIB: "quantidade"
    PR_COTA_SUBSCR_DISTRIB: "percentual (%)"
    NR_COTST_SUBSCR_OUTRO: "quantidade"
    PR_COTA_SUBSCR_OUTRO: "percentual (%)"
    NR_TOTAL_COTST_SUBSCR: "quantidade"
    PR_TOTAL_COTA_SUBSCR: "percentual (%)"
    NR_COTST_SUBSCR_CLASSE: "quantidade"
    QT_COTA_SUBSCR_CLASSE: "quantidade"
    QT_COTA_INTEGR_CLASSE: "quantidade"
    VL_QUOTA_CLASSE: "moeda (R$ por cota)"
  dados_pessoais: nenhum
  eras:
    - {desde: 2024-01, mudanca: "o informe, antes trimestral, passa a quadrimestral (o arquivo trimestral de 2024 foi descontinuado em 2025-01-27 e substituído pelo quadrimestral)"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento em Participações: Documentos: Informes Trimestral e Quadrimestral

## Resumo

Informes dos Fundos de Investimento em Participações (FIP): trimestral de 2010 a 2023 e quadrimestral desde 2024, com patrimônio, cotas, cotistas, capital comprometido e demais itens, em duas tabelas (uma por periodicidade).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fip-inf` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fip-doc-inf_trimestral |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fip-doc-inf_trimestral |
| Periodicidade | anual (um arquivo por ano); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2010 a em-curso |
| Unidade (uma linha) | o informe de um FIP (fundo ou classe) em uma data de competência |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: trimestral até 2023 e quadrimestral desde 2024 (`DT_COMPTC`), em arquivos anuais |
| Formato bruto | CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 56 |
| Unidades de medida | `VL_PATRIM_LIQ`: moeda (R$); `QT_COTA`: quantidade; `VL_PATRIM_COTA`: moeda (R$ por cota); `NR_COTST`: quantidade; `VL_CAP_COMPROM`: moeda (R$); `QT_COTA_SUBSCR`: quantidade; `VL_CAP_SUBSCR`: moeda (R$); `QT_COTA_INTEGR`: quantidade; `VL_CAP_INTEGR`: moeda (R$); `VL_INVEST_FIP_COTA`: moeda (R$); `NR_COTST_SUBSCR_PF`: quantidade; `PR_COTA_SUBSCR_PF`: percentual (%); `NR_COTST_SUBSCR_PJ_NAO_FINANC`: quantidade; `PR_COTA_SUBSCR_PJ_NAO_FINANC`: percentual (%); `NR_COTST_SUBSCR_BANCO`: quantidade; `PR_COTA_SUBSCR_BANCO`: percentual (%); `NR_COTST_SUBSCR_CORRETORA_DISTRIB`: quantidade; `PR_COTA_SUBSCR_CORRETORA_DISTRIB`: percentual (%); `NR_COTST_SUBSCR_PJ_FINANC`: quantidade; `PR_COTA_SUBSCR_PJ_FINANC`: percentual (%); `NR_COTST_SUBSCR_INVNR`: quantidade; `PR_COTA_SUBSCR_INVNR`: percentual (%); `NR_COTST_SUBSCR_EAPC`: quantidade; `PR_COTA_SUBSCR_EAPC`: percentual (%); `NR_COTST_SUBSCR_EFPC`: quantidade; `PR_COTA_SUBSCR_EFPC`: percentual (%); `NR_COTST_SUBSCR_RPPS`: quantidade; `PR_COTA_SUBSCR_RPPS`: percentual (%); `NR_COTST_SUBSCR_SEGUR`: quantidade; `PR_COTA_SUBSCR_SEGUR`: percentual (%); `NR_COTST_SUBSCR_CAPITALIZ`: quantidade; `PR_COTA_SUBSCR_CAPITALIZ`: percentual (%); `NR_COTST_SUBSCR_FII`: quantidade; `PR_COTA_SUBSCR_FII`: percentual (%); `NR_COTST_SUBSCR_FI`: quantidade; `PR_COTA_SUBSCR_FI`: percentual (%); `NR_COTST_SUBSCR_DISTRIB`: quantidade; `PR_COTA_SUBSCR_DISTRIB`: percentual (%); `NR_COTST_SUBSCR_OUTRO`: quantidade; `PR_COTA_SUBSCR_OUTRO`: percentual (%); `NR_TOTAL_COTST_SUBSCR`: quantidade; `PR_TOTAL_COTA_SUBSCR`: percentual (%); `NR_COTST_SUBSCR_CLASSE`: quantidade; `QT_COTA_SUBSCR_CLASSE`: quantidade; `QT_COTA_INTEGR_CLASSE`: quantidade; `VL_QUOTA_CLASSE`: moeda (R$ por cota) |
| Dados pessoais | nenhum |
| Eras | 2024-01: o informe, antes trimestral, passa a quadrimestral (o arquivo trimestral de 2024 foi descontinuado em 2025-01-27 e substituído pelo quadrimestral) |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fip-doc-inf_trimestral, https://dados.cvm.gov.br/dataset/fip-doc-inf_quadrimestral). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FIP/DOC/INF_QUADRIMESTRAL/DADOS/`, `https://dados.cvm.gov.br/dados/FIP/DOC/INF_TRIMESTRAL/DADOS/`.
- O catálogo do fetcher lista 17 arquivo(s), em 2 séries: `inf_trimestral_fip` (de `inf_trimestral_fip_2010.csv` a `inf_trimestral_fip_2023.csv`); `inf_quadrimestral_fip` (de `inf_quadrimestral_fip_2024.csv` a `inf_quadrimestral_fip_2026.csv`).
- Em 2026-11-16 conferimos 5 arquivos Parquet convertidos de 5 arquivo(s) de origem (amostra: 2010, 2018, 2023, 2024, 2026).
- No bruto, o arquivo fica em `fip-inf/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe de um FIP (fundo ou classe) em uma data de competência.
- Particionado por `ano`; o catálogo cobre 2010 a 2026, e conferimos as amostras 2010, 2018, 2023, 2024, 2026.
- O arquivo trimestral de 2023 tem 7.847 linhas, 1.787 fundos e 8 datas de competência (de 2023-01-31 a 2023-12-31); o de 2018 tem 3.934 linhas e o de 2010 tem 1.102. O quadrimestral de 2024 tem 6.821 linhas e 1.986 fundos em 4 datas (2024-03-31 a 2024-12-31) e o de 2026 tem 5.754 linhas em 3 datas (2026-04-30, 2026-08-31 e 2026-12-31).
- O portal avisa que, desde 2017-09, `QT_COTA` e `VL_PATRIM_COTA` foram descontinuados no informe trimestral; as duas colunas continuam nos arquivos, quase sempre vazias.
- Este dataset reúne 2 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `inf_quadrimestral_fip` | 55 | 6.821 | não determinada | informes quadrimestrais, de 2024 em diante |
| `inf_trimestral_fip` | 54 | 7.847 | não determinada | informes trimestrais, de 2010 a 2023 |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo (só em: `inf_trimestral_fip`) | — | todo |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `VL_PATRIM_LIQ` | `VL_PATRIM_LIQ` | decimal | Valor do patrimônio líquido | moeda (R$) | todo |
| `QT_COTA` | `QT_COTA` | decimal / texto | Quantidade de Cotas | quantidade | todo |
| `VL_PATRIM_COTA` | `VL_PATRIM_COTA` | decimal / texto | Valor Patrimonial da Cota | moeda (R$ por cota) | todo |
| `NR_COTST` | `NR_COTST` | inteiro / texto | Número de cotistas | quantidade | todo |
| `ENTID_INVEST` | `ENTID_INVEST` | texto | Indica se o fundo é entidade de investimento | S/N | todo |
| `PUBLICO_ALVO` | `PUBLICO_ALVO` | texto | Público-alvo | — | todo |
| `VL_CAP_COMPROM` | `VL_CAP_COMPROM` | decimal / texto | Valor total do capital comprometido | moeda (R$) | todo |
| `QT_COTA_SUBSCR` | `QT_COTA_SUBSCR` | decimal / texto | Quantidade de cotas subscritas | quantidade | todo |
| `VL_CAP_SUBSCR` | `VL_CAP_SUBSCR` | decimal / texto | Valor total do capital subscrito | moeda (R$) | todo |
| `QT_COTA_INTEGR` | `QT_COTA_INTEGR` | decimal / texto | Quantidade de cotas integralizadas | quantidade | todo |
| `VL_CAP_INTEGR` | `VL_CAP_INTEGR` | decimal / texto | Valor total do capital integralizado | moeda (R$) | todo |
| `VL_INVEST_FIP_COTA` | `VL_INVEST_FIP_COTA` | decimal / texto | Valor total investido em cotas de outros FIP | moeda (R$) | todo |
| `NR_COTST_SUBSCR_PF` | `NR_COTST_SUBSCR_PF` | decimal / texto | Número de cotistas subscritores na categoria Pessoa Física | quantidade | todo |
| `PR_COTA_SUBSCR_PF` | `PR_COTA_SUBSCR_PF` | decimal / texto | Percentual das cotas subscritas na categoria Pessoa Física | percentual (%) | todo |
| `NR_COTST_SUBSCR_PJ_NAO_FINANC` | `NR_COTST_SUBSCR_PJ_NAO_FINANC` | decimal / texto | Número de cotistas subscritores na categoria Pessoa Jurídica Não Financeira | quantidade | todo |
| `PR_COTA_SUBSCR_PJ_NAO_FINANC` | `PR_COTA_SUBSCR_PJ_NAO_FINANC` | decimal / texto | Percentual das cotas subscritas na categoria Pessoa Jurídica Não Financeira | percentual (%) | todo |
| `NR_COTST_SUBSCR_BANCO` | `NR_COTST_SUBSCR_BANCO` | decimal / texto | Número de cotistas subscritores na categoria Banco Comercial | quantidade | todo |
| `PR_COTA_SUBSCR_BANCO` | `PR_COTA_SUBSCR_BANCO` | decimal / texto | Percentual das cotas subscritas na categoria Banco Comercial | percentual (%) | todo |
| `NR_COTST_SUBSCR_CORRETORA_DISTRIB` | `NR_COTST_SUBSCR_CORRETORA_DISTRIB` | decimal / texto | Número de cotistas subscritores na categoria Corretora ou Distribuidora | quantidade | todo |
| `PR_COTA_SUBSCR_CORRETORA_DISTRIB` | `PR_COTA_SUBSCR_CORRETORA_DISTRIB` | decimal / texto | Percentual das cotas subscritas na categoria Corretora ou Distribuidora | percentual (%) | todo |
| `NR_COTST_SUBSCR_PJ_FINANC` | `NR_COTST_SUBSCR_PJ_FINANC` | decimal / texto | Número de cotistas subscritores na categoria Outras Pessoas Jurídicas Financeiras | quantidade | todo |
| `PR_COTA_SUBSCR_PJ_FINANC` | `PR_COTA_SUBSCR_PJ_FINANC` | decimal / texto | Percentual das cotas subscritas na categoria Outras Pessoas Jurídicas Financeiras | percentual (%) | todo |
| `NR_COTST_SUBSCR_INVNR` | `NR_COTST_SUBSCR_INVNR` | decimal / texto | Número de cotistas subscritores na categoria Investidores Não Residentes | quantidade | todo |
| `PR_COTA_SUBSCR_INVNR` | `PR_COTA_SUBSCR_INVNR` | decimal / texto | Percentual das cotas subscritas na categoria Investidores Não Residentes | percentual (%) | todo |
| `NR_COTST_SUBSCR_EAPC` | `NR_COTST_SUBSCR_EAPC` | decimal / texto | Número de cotistas subscritores na categoria Entidade Aberta de Previdência Complementar | quantidade | todo |
| `PR_COTA_SUBSCR_EAPC` | `PR_COTA_SUBSCR_EAPC` | decimal / texto | Percentual das cotas subscritas na categoria Entidade Aberta de Previdência Complementar | percentual (%) | todo |
| `NR_COTST_SUBSCR_EFPC` | `NR_COTST_SUBSCR_EFPC` | decimal / texto | Número de cotistas subscritores na categoria Entidade Fechada de Previdência Complementar | quantidade | todo |
| `PR_COTA_SUBSCR_EFPC` | `PR_COTA_SUBSCR_EFPC` | decimal / texto | Percentual das cotas subscritas na categoria Entidade Fechada de Previdência Complementar | percentual (%) | todo |
| `NR_COTST_SUBSCR_RPPS` | `NR_COTST_SUBSCR_RPPS` | decimal / texto | Número de cotistas subscritores na categoria Regime Próprio de Previdência dos Servidores Públicos | quantidade | todo |
| `PR_COTA_SUBSCR_RPPS` | `PR_COTA_SUBSCR_RPPS` | decimal / texto | Percentual das cotas subscritas na categoria Regime Próprio de Previdência dos Servidores Públicos | percentual (%) | todo |
| `NR_COTST_SUBSCR_SEGUR` | `NR_COTST_SUBSCR_SEGUR` | decimal / texto | Número de cotistas subscritores na categoria Sociedade Seguradora ou Resseguradora | quantidade | todo |
| `PR_COTA_SUBSCR_SEGUR` | `PR_COTA_SUBSCR_SEGUR` | decimal / texto | Percentual das cotas subscritas na categoria Sociedade Seguradora ou Resseguradora | percentual (%) | todo |
| `NR_COTST_SUBSCR_CAPITALIZ` | `NR_COTST_SUBSCR_CAPITALIZ` | decimal / texto | Número de cotistas subscritores na categoria Sociedade de Capitalização e de Arrendamento Mercantil | quantidade | todo |
| `PR_COTA_SUBSCR_CAPITALIZ` | `PR_COTA_SUBSCR_CAPITALIZ` | decimal / texto | Percentual das cotas subscritas na categoria Sociedade de Capitalização e de Arrendamento Mercantil | percentual (%) | todo |
| `NR_COTST_SUBSCR_FII` | `NR_COTST_SUBSCR_FII` | decimal / texto | Número de cotistas subscritores na categoria Fundos de Investimento Imobiliário | quantidade | todo |
| `PR_COTA_SUBSCR_FII` | `PR_COTA_SUBSCR_FII` | decimal / texto | Percentual das cotas subscritas na categoria Fundos de Investimento Imobiliário | percentual (%) | todo |
| `NR_COTST_SUBSCR_FI` | `NR_COTST_SUBSCR_FI` | decimal / texto | Número de cotistas subscritores na categoria Outros Fundos de Investimento | quantidade | todo |
| `PR_COTA_SUBSCR_FI` | `PR_COTA_SUBSCR_FI` | decimal / texto | Percentual das cotas subscritas na categoria Outros Fundos de Investimento | percentual (%) | todo |
| `NR_COTST_SUBSCR_DISTRIB` | `NR_COTST_SUBSCR_DISTRIB` | decimal / texto | Número de cotistas subscritores na categoria Cotistas de Distribuidores do Fundo | quantidade | todo |
| `PR_COTA_SUBSCR_DISTRIB` | `PR_COTA_SUBSCR_DISTRIB` | decimal / texto | Percentual das cotas subscritas na categoria Cotistas de Distribuidores do Fundo | percentual (%) | todo |
| `NR_COTST_SUBSCR_OUTRO` | `NR_COTST_SUBSCR_OUTRO` | decimal / texto | Número de cotistas subscritores na categoria Outros Tipos de Cotistas Não Relacionados | quantidade | todo |
| `PR_COTA_SUBSCR_OUTRO` | `PR_COTA_SUBSCR_OUTRO` | decimal / texto | Percentual das cotas subscritas na categoria Outros Tipos de Cotistas Não Relacionados | percentual (%) | todo |
| `NR_TOTAL_COTST_SUBSCR` | `NR_TOTAL_COTST_SUBSCR` | decimal / texto | Número total de cotistas subscritores | quantidade | todo |
| `PR_TOTAL_COTA_SUBSCR` | `PR_TOTAL_COTA_SUBSCR` | decimal / texto | Percentual total das cotas subscritas | percentual (%) | todo |
| `CLASSE_COTA` | `CLASSE_COTA` | texto | Classe de cotas | — | todo |
| `NR_COTST_SUBSCR_CLASSE` | `NR_COTST_SUBSCR_CLASSE` | decimal / texto | Número de cotistas subscritores na classe | quantidade | todo |
| `QT_COTA_SUBSCR_CLASSE` | `QT_COTA_SUBSCR_CLASSE` | decimal / texto | Quantidade de cotas subscritas na classe | quantidade | todo |
| `QT_COTA_INTEGR_CLASSE` | `QT_COTA_INTEGR_CLASSE` | decimal / texto | Quantidade de cotas integralizadas na classe | quantidade | todo |
| `VL_QUOTA_CLASSE` | `VL_QUOTA_CLASSE` | decimal / texto | Valor da cota da classe | moeda (R$ por cota) | todo |
| `DIREITO_POLIT_CLASSE` | `DIREITO_POLIT_CLASSE` | texto | Indica se a classe de cotas possui direitos políticos especiais | S/N | todo |
| `DIREITO_ECON_CLASSE` | `DIREITO_ECON_CLASSE` | texto | Indica se a classe de cotas possui distintos direitos econômico-financeiros | S/N | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe (só em: `inf_quadrimestral_fip`) | — | todo |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe (só em: `inf_quadrimestral_fip`) | — | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fip-inf`, particionado por `ano`; um arquivo Parquet por arquivo CSV de origem.
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Datas de competência no futuro.** O arquivo quadrimestral de 2026, coletado em 2026-11-16, traz 2 linhas com `DT_COMPTC` = 2026-12-31 (ainda não ocorrida); trate-as como erro de preenchimento ou entrega antecipada.
- **Último trimestre no arquivo quadrimestral.** O arquivo quadrimestral de 2024 traz 156 linhas de `DT_COMPTC` = 2024-03-31 (o último trimestre, entregue no layout anterior), seguidas de 2024-04-30, 2024-08-31 e 2024-12-31 (2.177, 2.258 e 2.230 linhas).
- **Duas séries, duas tabelas.** Para a série contínua de 2010 a 2026, junte `inf_trimestral_fip` e `inf_quadrimestral_fip` pelas colunas em comum e lembre que a periodicidade mudou.
- **Tipos inferidos varia muito entre arquivos de FIP.** O trimestral tem dezenas de colunas com tipo diferente entre arquivos (por exemplo `QT_COTA`, `VL_PATRIM_COTA`, `NR_COTST` e `VL_CAP_COMPROM`), porque as colunas vazias viram texto; converta com `CAST`.
- **Linhas repetidas.** O quadrimestral de 2026 tem 6 linhas inteiramente repetidas; remova duplicatas antes de contar fundos.
- **Tipo inferido varia entre arquivos.** 45 coluna(s) (`QT_COTA`, `VL_PATRIM_COTA`, `NR_COTST`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.
- **Linhas repetidas.** No arquivo mais recente convertido há linhas inteiramente repetidas em: `inf_quadrimestral_fip` (6). Remova as duplicatas antes de contar ou somar.

## Exemplos

Fundos informantes por data de competência no informe quadrimestral.

```python
import duckdb

duckdb.sql("""
    SELECT DT_COMPTC, count(DISTINCT CNPJ_FUNDO_CLASSE) AS fundos
    FROM read_parquet('lake/cvm/fip-inf/**/*inf_quadrimestral_fip_*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fip-doc-inf_trimestral
- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fip-doc-inf_quadrimestral
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FIP/DOC/INF_QUADRIMESTRAL/
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FIP/DOC/INF_TRIMESTRAL/
