---
dataset:
  id: fi-lamina
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Lâmina de Informações Essenciais (CVM)"
  resumo: "Lâmina de informações essenciais dos fundos de investimento (ICVM 555): perfil de risco, objetivo, política de investimento, taxas, rentabilidade histórica e cenários de simulação, em quatro tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-lamina
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-lamina"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização semanal (os arquivos recentes foram regravados em 2026-11-14)"
  cobertura: {inicio: 2019-01, fim: em-curso}
  unidade: "a lâmina de um fundo em um mês (tabela `lamina_fi`); uma linha de carteira, de rentabilidade anual ou de rentabilidade mensal da lâmina (nas demais tabelas)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (fim do mês, `DT_COMPTC`)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [], colunas: 91}
  unidades_de_medida:
    PR_PL_ATIVO_EXTERIOR: "percentual (%)"
    PR_PL_ATIVO_CRED_PRIV: "percentual (%)"
    PR_PL_ALAVANC: "percentual (%)"
    PR_ATIVO_EMISSOR: "percentual (%)"
    PR_PL_APLIC_MAX_FUNDO_UNICO: "percentual (%)"
    INVEST_INICIAL_MIN: "moeda (R$)"
    INVEST_ADIC: "moeda (R$)"
    RESGATE_MIN: "moeda (R$)"
    VL_MIN_PERMAN: "moeda (R$)"
    QT_DIA_CAREN: "dias"
    QT_DIA_CONVERSAO_COTA_COMPRA: "dias"
    QT_DIA_CONVERSAO_COTA_RESGATE: "dias"
    QT_DIA_PAGTO_RESGATE: "dias"
    TAXA_ADM: "percentual (%)"
    TAXA_ADM_MIN: "percentual (%)"
    TAXA_ADM_MAX: "percentual (%)"
    TAXA_ENTR: "percentual (%)"
    QT_DIA_SAIDA: "dias"
    TAXA_SAIDA: "percentual (%)"
    PR_PL_DESPESA: "percentual (%)"
    VL_PATRIM_LIQ: "moeda (R$)"
    CLASSE_RISCO_ADMIN: "escala de 1 a 5 (sem unidade)"
    PR_RENTAB_FUNDO_5ANO: "percentual (%)"
    PR_VARIACAO_INDICE_REFER_5ANO: "percentual (%)"
    QT_ANO_PERDA: "anos"
    PR_VARIACAO_PERFM: "percentual (%)"
    ANO_EXEMPLO: "ano"
    ANO_ANTER_EXEMPLO: "ano"
    VL_RESGATE_EXEMPLO: "moeda (R$)"
    VL_IMPOSTO_EXEMPLO: "moeda (R$)"
    VL_TAXA_ENTR_EXEMPLO: "percentual (%)"
    VL_TAXA_SAIDA_EXEMPLO: "percentual (%)"
    VL_AJUSTE_PERFM_EXEMPLO: "moeda (R$)"
    VL_DESPESA_EXEMPLO: "moeda (R$)"
    VL_DESPESA_3ANO: "moeda (R$)"
    VL_DESPESA_5ANO: "moeda (R$)"
    VL_RETORNO_3ANO: "moeda (R$)"
    VL_RETORNO_5ANO: "moeda (R$)"
    TEL_SAC: "código ou número de identificação (sem unidade)"
    PR_PL_ATIVO: "percentual (%)"
    ANO_RENTAB: "ano"
    PR_RENTAB_ANO: "percentual (%)"
    PR_VARIACAO_INDICE_REFER_ANO: "percentual (%)"
    PR_PERFM_INDICE_REFER_ANO: "percentual (%)"
    MES_RENTAB: "mês (1 a 12)"
    PR_RENTAB_MES: "percentual (%)"
    PR_VARIACAO_INDICE_REFER_MES: "percentual (%)"
    PR_PERFM_INDICE_REFER_MES: "percentual (%)"
  dados_pessoais:
    - {coluna: ENDER_ELETRONICO, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: ENDER_ELETRONICO_DESPESA, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TEL_SAC, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: ENDER_ELETRONICO_RECLAMACAO, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras:
    - {desde: 2023-11, mudanca: "`CNPJ_FUNDO` vira `CNPJ_FUNDO_CLASSE`, e entram `TP_FUNDO_CLASSE` e `ID_SUBCLASSE` (adaptação à Resolução CVM 175)"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Lâmina de Informações Essenciais

## Resumo

Lâmina de informações essenciais dos fundos de investimento (ICVM 555): perfil de risco, objetivo, política de investimento, taxas, rentabilidade histórica e cenários de simulação, em quatro tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-lamina` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-lamina |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-lamina |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização semanal (os arquivos recentes foram regravados em 2026-11-14) |
| Cobertura | 2019-01 a em-curso |
| Unidade (uma linha) | a lâmina de um fundo em um mês (tabela `lamina_fi`); uma linha de carteira, de rentabilidade anual ou de rentabilidade mensal da lâmina (nas demais tabelas) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (fim do mês, `DT_COMPTC`) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 91 |
| Unidades de medida | `PR_PL_ATIVO_EXTERIOR`: percentual (%); `PR_PL_ATIVO_CRED_PRIV`: percentual (%); `PR_PL_ALAVANC`: percentual (%); `PR_ATIVO_EMISSOR`: percentual (%); `PR_PL_APLIC_MAX_FUNDO_UNICO`: percentual (%); `INVEST_INICIAL_MIN`: moeda (R$); `INVEST_ADIC`: moeda (R$); `RESGATE_MIN`: moeda (R$); `VL_MIN_PERMAN`: moeda (R$); `QT_DIA_CAREN`: dias; `QT_DIA_CONVERSAO_COTA_COMPRA`: dias; `QT_DIA_CONVERSAO_COTA_RESGATE`: dias; `QT_DIA_PAGTO_RESGATE`: dias; `TAXA_ADM`: percentual (%); `TAXA_ADM_MIN`: percentual (%); `TAXA_ADM_MAX`: percentual (%); `TAXA_ENTR`: percentual (%); `QT_DIA_SAIDA`: dias; `TAXA_SAIDA`: percentual (%); `PR_PL_DESPESA`: percentual (%); `VL_PATRIM_LIQ`: moeda (R$); `CLASSE_RISCO_ADMIN`: escala de 1 a 5 (sem unidade); `PR_RENTAB_FUNDO_5ANO`: percentual (%); `PR_VARIACAO_INDICE_REFER_5ANO`: percentual (%); `QT_ANO_PERDA`: anos; `PR_VARIACAO_PERFM`: percentual (%); `ANO_EXEMPLO`: ano; `ANO_ANTER_EXEMPLO`: ano; `VL_RESGATE_EXEMPLO`: moeda (R$); `VL_IMPOSTO_EXEMPLO`: moeda (R$); `VL_TAXA_ENTR_EXEMPLO`: percentual (%); `VL_TAXA_SAIDA_EXEMPLO`: percentual (%); `VL_AJUSTE_PERFM_EXEMPLO`: moeda (R$); `VL_DESPESA_EXEMPLO`: moeda (R$); `VL_DESPESA_3ANO`: moeda (R$); `VL_DESPESA_5ANO`: moeda (R$); `VL_RETORNO_3ANO`: moeda (R$); `VL_RETORNO_5ANO`: moeda (R$); `TEL_SAC`: código ou número de identificação (sem unidade); `PR_PL_ATIVO`: percentual (%); `ANO_RENTAB`: ano; `PR_RENTAB_ANO`: percentual (%); `PR_VARIACAO_INDICE_REFER_ANO`: percentual (%); `PR_PERFM_INDICE_REFER_ANO`: percentual (%); `MES_RENTAB`: mês (1 a 12); `PR_RENTAB_MES`: percentual (%); `PR_VARIACAO_INDICE_REFER_MES`: percentual (%); `PR_PERFM_INDICE_REFER_MES`: percentual (%) |
| Dados pessoais | `ENDER_ELETRONICO` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `ENDER_ELETRONICO_DESPESA` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TEL_SAC` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `ENDER_ELETRONICO_RECLAMACAO` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | 2023-11: `CNPJ_FUNDO` vira `CNPJ_FUNDO_CLASSE`, e entram `TP_FUNDO_CLASSE` e `ID_SUBCLASSE` (adaptação à Resolução CVM 175) |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-lamina). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/LAMINA/DADOS/`.
- O catálogo do fetcher lista 95 arquivo(s): de `lamina_fi_201901.zip` a `lamina_fi_202611.zip`.
- Em 2026-11-16 conferimos 12 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2019-01, 2022-12, 2026-10).
- No bruto, o arquivo fica em `fi-lamina/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: a lâmina de um fundo em um mês (tabela `lamina_fi`); uma linha de carteira, de rentabilidade anual ou de rentabilidade mensal da lâmina (nas demais tabelas).
- Particionado por `ano` e `mes`; o catálogo cobre 2019-01 a 2026-11, e conferimos as amostras 2019-01, 2022-12, 2026-10.
- O arquivo de 2022-12 tem 5.469 lâminas (uma por fundo, `CNPJ_FUNDO` único), o de 2019-01 tem 3.412 e o de 2026-10 tem 968 linhas (967 CNPJ): o número de lâminas cai (968 em 2026-10 contra 5.469 em 2022-12) e a fonte não explica a queda.
- As tabelas `lamina_fi_carteira`, `lamina_fi_rentab_ano` e `lamina_fi_rentab_mes` ligam-se a `lamina_fi` pelo CNPJ (e `ID_SUBCLASSE`, quando houver) na mesma competência.
- Este dataset reúne 4 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `lamina_fi` | 79 | 5.469 | não determinada | a lâmina: perfil, objetivo, taxas, condições de aplicação e resgate, cenários (79 colunas) |
| `lamina_fi_carteira` | 8 | 17.401 | `CNPJ_FUNDO_CLASSE`, `TP_ATIVO` | a carteira do fundo por tipo de ativo, em percentual do patrimônio líquido |
| `lamina_fi_rentab_ano` | 11 | 20.613 | `CNPJ_FUNDO_CLASSE`, `ANO_RENTAB` | a rentabilidade anual do fundo e do benchmark |
| `lamina_fi_rentab_mes` | 11 | 59.040 | `CNPJ_FUNDO_CLASSE`, `MES_RENTAB` | a rentabilidade mensal do fundo e do benchmark |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE`) | — | 2019-01 a 2022-12 |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `NM_FANTASIA` | `NM_FANTASIA` | texto | Nome fantasia do fundo (só em: `lamina_fi`) | — | todo |
| `ENDER_ELETRONICO` | `ENDER_ELETRONICO` | texto | Endereço eletrônico (só em: `lamina_fi`) | — | todo |
| `PUBLICO_ALVO` | `PUBLICO_ALVO` | texto | Público-alvo (só em: `lamina_fi`) | — | todo |
| `RESTR_INVEST` | `RESTR_INVEST` | texto | Restrições de investimento (só em: `lamina_fi`) | — | todo |
| `OBJETIVO` | `OBJETIVO` | texto | Objetivos do fundo (só em: `lamina_fi`) | — | todo |
| `POLIT_INVEST` | `POLIT_INVEST` | texto | Política de investimento (só em: `lamina_fi`) | — | todo |
| `PR_PL_ATIVO_EXTERIOR` | `PR_PL_ATIVO_EXTERIOR` | decimal | Percentual do PL que pode ser aplicado em ativos do exterior (só em: `lamina_fi`) | percentual (%) | todo |
| `PR_PL_ATIVO_CRED_PRIV` | `PR_PL_ATIVO_CRED_PRIV` | decimal | Percentual do PL que pode ser aplicado em crédito privado (só em: `lamina_fi`) | percentual (%) | todo |
| `PR_PL_ALAVANC` | `PR_PL_ALAVANC` | decimal | Limite de alavancagem (% em relação ao PL) (só em: `lamina_fi`) | percentual (%) | todo |
| `PR_ATIVO_EMISSOR` | `PR_ATIVO_EMISSOR` | decimal / texto | Limite de concentração em ativos de um só emissor que não seja a União Federal (só em: `lamina_fi`) | percentual (%) | todo |
| `DERIV_PROTECAO_CARTEIRA` | `DERIV_PROTECAO_CARTEIRA` | texto | Indica se o fundo utiliza derivativos apenas para proteção da carteira (só em: `lamina_fi`) | S/N | todo |
| `RISCO_PERDA` | `RISCO_PERDA` | texto | Indica se as estratégias de investimento do fundo podem resultar em perdas patrimoniais significativas para seus cotistas (só em: `lamina_fi`) | S/N | todo |
| `RISCO_PERDA_NEGATIVO` | `RISCO_PERDA_NEGATIVO` | texto | Indica se as estratégias de investimento do fundo podem resultar em perdas superiores ao capital aplicado e a consequente obrigação do cotista de aportar recursos adicionais para cobrir o prejuízo do fundo (só em: `lamina_fi`) | S/N | todo |
| `PR_PL_APLIC_MAX_FUNDO_UNICO` | `PR_PL_APLIC_MAX_FUNDO_UNICO` | decimal | Percentual máximo do PL que pode ser aplicado em um só fundo de investimento (só em: `lamina_fi`) | percentual (%) | todo |
| `INVEST_INICIAL_MIN` | `INVEST_INICIAL_MIN` | decimal | Investimento inicial mínimo (só em: `lamina_fi`) | moeda (R$) | todo |
| `INVEST_ADIC` | `INVEST_ADIC` | decimal | Investimento adicional (só em: `lamina_fi`) | moeda (R$) | todo |
| `RESGATE_MIN` | `RESGATE_MIN` | decimal | Resgate mínimo (só em: `lamina_fi`) | moeda (R$) | todo |
| `HORA_APLIC_RESGATE` | `HORA_APLIC_RESGATE` | texto | Horário para aplicação e resgate (só em: `lamina_fi`) | — | todo |
| `VL_MIN_PERMAN` | `VL_MIN_PERMAN` | decimal | Valor mínimo para permanência (só em: `lamina_fi`) | moeda (R$) | todo |
| `QT_DIA_CAREN` | `QT_DIA_CAREN` | inteiro | Número de dias de carência (só em: `lamina_fi`) | dias | todo |
| `CONDIC_CAREN` | `CONDIC_CAREN` | texto | Condições do período de carência (só em: `lamina_fi`) | — | todo |
| `CONVERSAO_COTA_COMPRA` | `CONVERSAO_COTA_COMPRA` | texto | Evento considerado para o cálculo do valor das cotas compradas (só em: `lamina_fi`) | — | todo |
| `QT_DIA_CONVERSAO_COTA_COMPRA` | `QT_DIA_CONVERSAO_COTA_COMPRA` | inteiro | Número de dias para conversão de cotas contado da data da aplicação (só em: `lamina_fi`) | dias | todo |
| `CONVERSAO_COTA_CANC` | `CONVERSAO_COTA_CANC` | texto | Evento considerado para o cálculo do valor das cotas canceladas (só em: `lamina_fi`) | — | todo |
| `QT_DIA_CONVERSAO_COTA_RESGATE` | `QT_DIA_CONVERSAO_COTA_RESGATE` | inteiro | Número de dias para conversão de cotas após o pedido de resgate (só em: `lamina_fi`) | dias | todo |
| `TP_DIA_PAGTO_RESGATE` | `TP_DIA_PAGTO_RESGATE` | texto | Tipo de prazo para o efetivo pagamento dos resgates (só em: `lamina_fi`) | — | todo |
| `QT_DIA_PAGTO_RESGATE` | `QT_DIA_PAGTO_RESGATE` | inteiro | Prazo para o efetivo pagamento dos resgates, contado a partir da data do pedido (só em: `lamina_fi`) | dias | todo |
| `TP_TAXA_ADM` | `TP_TAXA_ADM` | texto | Tipo da taxa de administração (só em: `lamina_fi`) | — | todo |
| `TAXA_ADM` | `TAXA_ADM` | decimal | Taxa de administração (só em: `lamina_fi`) | percentual (%) | todo |
| `TAXA_ADM_MIN` | `TAXA_ADM_MIN` | decimal | Taxa de administração mínima (quando variável) (só em: `lamina_fi`) | percentual (%) | todo |
| `TAXA_ADM_MAX` | `TAXA_ADM_MAX` | decimal | Taxa de administração máxima (quando variável) (só em: `lamina_fi`) | percentual (%) | todo |
| `TAXA_ADM_OBS` | `TAXA_ADM_OBS` | texto | Comentários ou esclarecimentos sobre a taxa de administração (só em: `lamina_fi`) | — | todo |
| `TAXA_ENTR` | `TAXA_ENTR` | decimal | Taxa de entrada (só em: `lamina_fi`) | percentual (%) | todo |
| `CONDIC_ENTR` | `CONDIC_ENTR` | texto | Condições de entrada (só em: `lamina_fi`) | — | todo |
| `QT_DIA_SAIDA` | `QT_DIA_SAIDA` | inteiro | Número de dias de saída para resgatar suas cotas do fundo (só em: `lamina_fi`) | dias | todo |
| `TAXA_SAIDA` | `TAXA_SAIDA` | decimal | Taxa de saída (só em: `lamina_fi`) | percentual (%) | todo |
| `CONDIC_SAIDA` | `CONDIC_SAIDA` | texto | Condições de saída (só em: `lamina_fi`) | — | todo |
| `TAXA_PERFM` | `TAXA_PERFM` | texto | Taxa de performance (só em: `lamina_fi`) | — | todo |
| `PR_PL_DESPESA` | `PR_PL_DESPESA` | decimal | Despesas pagas pelo fundo (em % do PL diário médio) (só em: `lamina_fi`) | percentual (%) | todo |
| `DT_INI_DESPESA` | `DT_INI_DESPESA` | texto | Início do período considerado para o cálculo das despesas (só em: `lamina_fi`) | — | todo |
| `DT_FIM_DESPESA` | `DT_FIM_DESPESA` | texto | Fim do período considerado para o cálculo das despesas (só em: `lamina_fi`) | — | todo |
| `ENDER_ELETRONICO_DESPESA` | `ENDER_ELETRONICO_DESPESA` | texto | Endereço eletrônico do administrador onde a descrição das despesas do fundo pode ser encontrada (só em: `lamina_fi`) | — | todo |
| `VL_PATRIM_LIQ` | `VL_PATRIM_LIQ` | decimal | Valor do patrimônio líquido (só em: `lamina_fi`) | moeda (R$) | todo |
| `CLASSE_RISCO_ADMIN` | `CLASSE_RISCO_ADMIN` | inteiro | Risco do fundo de acordo com a classificação do administrador (escala de 1 a 5) (só em: `lamina_fi`) | escala de 1 a 5 (sem unidade) | todo |
| `PR_RENTAB_FUNDO_5ANO` | `PR_RENTAB_FUNDO_5ANO` | decimal | Rentabilidade acumulada nos últimos 5 anos (valor percentual) (só em: `lamina_fi`) | percentual (%) | todo |
| `INDICE_REFER` | `INDICE_REFER` | texto | Índice de referência do fundo (só em: `lamina_fi`) | — | todo |
| `PR_VARIACAO_INDICE_REFER_5ANO` | `PR_VARIACAO_INDICE_REFER_5ANO` | decimal | Variação do índice de referência do fundo, nos últimos 5 anos (valor percentual) (só em: `lamina_fi`) | percentual (%) | todo |
| `QT_ANO_PERDA` | `QT_ANO_PERDA` | inteiro | Número de anos em que o fundo perdeu parte do patrimônio que detinha no início do respectivo ano (só em: `lamina_fi`) | anos | todo |
| `DT_INI_ATIV_5ANO` | `DT_INI_ATIV_5ANO` | texto | Data de início do funcionamento do fundo (quando o fundo tiver sido constituído há menos de 5 anos) (só em: `lamina_fi`) | — | todo |
| `ANO_SEM_RENTAB` | `ANO_SEM_RENTAB` | texto | Anos em que não foram apresentados dados de rentabilidade (só em: `lamina_fi`) | — | todo |
| `CALC_RENTAB_FUNDO_GATILHO` | `CALC_RENTAB_FUNDO_GATILHO` | texto | Descrição da fórmula de cálculo da rentabilidade do fundo, incluindo todas as condições (gatilhos) e cláusulas que afetarão o desempenho (só em: `lamina_fi`) | — | todo |
| `PR_VARIACAO_PERFM` | `PR_VARIACAO_PERFM` | decimal | Variação do desempenho do fundo (valor percentual) (só em: `lamina_fi`) | percentual (%) | todo |
| `CALC_RENTAB_FUNDO` | `CALC_RENTAB_FUNDO` | texto | Fórmula de cálculo de sua rentabilidade (só em: `lamina_fi`) | — | todo |
| `RENTAB_GATILHO` | `RENTAB_GATILHO` | texto | Indicação dos valores dos cenários ou gatilhos que afetam a rentabilidade (só em: `lamina_fi`) | — | todo |
| `DS_RENTAB_GATILHO` | `DS_RENTAB_GATILHO` | texto | Descrição de como o cenário/gatilho afeta a variação do desempenho do fundo (só em: `lamina_fi`) | — | todo |
| `ANO_EXEMPLO` | `ANO_EXEMPLO` | inteiro | Ano de referência (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | ano | todo |
| `ANO_ANTER_EXEMPLO` | `ANO_ANTER_EXEMPLO` | inteiro | Ano anterior ao de referência (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | ano | todo |
| `VL_RESGATE_EXEMPLO` | `VL_RESGATE_EXEMPLO` | decimal | Valor que poderia ser resgatado já deduzido dos impostos (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_IMPOSTO_EXEMPLO` | `VL_IMPOSTO_EXEMPLO` | decimal | Valor dos impostos que seriam pagos (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_TAXA_ENTR_EXEMPLO` | `VL_TAXA_ENTR_EXEMPLO` | decimal | Valor da taxa de ingresso (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | percentual (%) | todo |
| `VL_TAXA_SAIDA_EXEMPLO` | `VL_TAXA_SAIDA_EXEMPLO` | decimal | Valor da taxa de saída (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | percentual (%) | todo |
| `VL_AJUSTE_PERFM_EXEMPLO` | `VL_AJUSTE_PERFM_EXEMPLO` | decimal | Valor do ajuste sobre performance individual (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_DESPESA_EXEMPLO` | `VL_DESPESA_EXEMPLO` | decimal | Valor total das despesas do fundo (exemplo para comparar custos e benefícios de se investir no fundo) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_DESPESA_3ANO` | `VL_DESPESA_3ANO` | decimal | Despesas previstas para 3 anos (se a taxa total de despesas se mantiver constante) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_DESPESA_5ANO` | `VL_DESPESA_5ANO` | decimal | Despesas previstas para 5 anos (se a taxa total de despesas se mantiver constante) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_RETORNO_3ANO` | `VL_RETORNO_3ANO` | decimal | Retorno bruto hipotético para 3 anos após dedução das despesas e do valor do investimento original (antes da incidência de impostos, de taxas de ingresso e/ou saída, ou de taxa de performance) (só em: `lamina_fi`) | moeda (R$) | todo |
| `VL_RETORNO_5ANO` | `VL_RETORNO_5ANO` | decimal | Retorno bruto hipotético para 5 anos após dedução das despesas e do valor do investimento original (antes da incidência de impostos, de taxas de ingresso e/ou saída, ou de taxa de performance) (só em: `lamina_fi`) | moeda (R$) | todo |
| `REMUN_DISTRIB` | `REMUN_DISTRIB` | texto | Descrição da forma de remuneração dos distribuidores (só em: `lamina_fi`) | — | todo |
| `DISTRIB_GESTOR_UNICO` | `DISTRIB_GESTOR_UNICO` | texto | Informa se o principal distribuidor oferta, para o público alvo do fundo, preponderantemente fundos geridos por um único gestor, ou por gestores ligados a um mesmo grupo econômico (só em: `lamina_fi`) | — | todo |
| `CONFLITO_VENDA` | `CONFLITO_VENDA` | texto | Informa se existe conflito de interesses no esforço de venda (só em: `lamina_fi`) | — | todo |
| `TEL_SAC` | `TEL_SAC` | inteiro | Telefone do serviço de atendimento ao cotista (só em: `lamina_fi`) | código ou número de identificação (sem unidade) | todo |
| `ENDER_ELETRONICO_RECLAMACAO` | `ENDER_ELETRONICO_RECLAMACAO` | texto | Endereço eletrônico e demais canais disponíveis para o encaminhamento de reclamações (só em: `lamina_fi`) | — | todo |
| `INF_SAC` | `INF_SAC` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: inf sac (só em: `lamina_fi`) | — | todo |
| `TP_ATIVO` | `TP_ATIVO` | texto | Tipo de ativo (só em: `lamina_fi_carteira`) | — | todo |
| `PR_PL_ATIVO` | `PR_PL_ATIVO` | decimal | Concentração dos investimentos do fundo por tipo de ativo (em % do PL) (só em: `lamina_fi_carteira`) | percentual (%) | todo |
| `ANO_RENTAB` | `ANO_RENTAB` | inteiro | Ano referente à rentabilidade do fundo (só em: `lamina_fi_rentab_ano`) | ano | todo |
| `PR_RENTAB_ANO` | `PR_RENTAB_ANO` | decimal | Rentabilidade (líquida de despesas, mas não de impostos) do fundo no ano de referência (valor percentual) (só em: `lamina_fi_rentab_ano`) | percentual (%) | todo |
| `PR_VARIACAO_INDICE_REFER_ANO` | `PR_VARIACAO_INDICE_REFER_ANO` | decimal | Variação anual do índice de referência do fundo (valor percentual) (só em: `lamina_fi_rentab_ano`) | percentual (%) | todo |
| `PR_PERFM_INDICE_REFER_ANO` | `PR_PERFM_INDICE_REFER_ANO` | decimal | Desempenho anual do fundo como percentual do índice de referência (só em: `lamina_fi_rentab_ano`) | percentual (%) | todo |
| `RENTAB_ANO_OBS` | `RENTAB_ANO_OBS` | texto | Comentários ou esclarecimentos sobre a rentabilidade do fundo no ano de referência (só em: `lamina_fi_rentab_ano`) | — | todo |
| `MES_RENTAB` | `MES_RENTAB` | inteiro | Mês referente à rentabilidade do fundo (só em: `lamina_fi_rentab_mes`) | mês (1 a 12) | todo |
| `PR_RENTAB_MES` | `PR_RENTAB_MES` | decimal | Rentabilidade (líquida de despesas, mas não de impostos) do fundo no mês de referência (valor percentual) (só em: `lamina_fi_rentab_mes`) | percentual (%) | todo |
| `PR_VARIACAO_INDICE_REFER_MES` | `PR_VARIACAO_INDICE_REFER_MES` | decimal | Variação mensal do índice de referência do fundo (valor percentual) (só em: `lamina_fi_rentab_mes`) | percentual (%) | todo |
| `PR_PERFM_INDICE_REFER_MES` | `PR_PERFM_INDICE_REFER_MES` | decimal | Desempenho mensal do fundo como percentual do índice de referência (só em: `lamina_fi_rentab_mes`) | percentual (%) | todo |
| `RENTAB_MES_OBS` | `RENTAB_MES_OBS` | texto | Comentários ou esclarecimentos sobre a rentabilidade do fundo no mês de referência (só em: `lamina_fi_rentab_mes`) | — | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe | — | 2026-10 |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe | — | 2026-10 |
| `ID_SUBCLASSE` | `ID_SUBCLASSE` | texto | Identificador da subclasse | — | 2026-10 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-lamina`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Troca de coluna de identificação em 2023-11.** Até 2023-10 o CNPJ está em `CNPJ_FUNDO`; depois, em `CNPJ_FUNDO_CLASSE`, com `TP_FUNDO_CLASSE` e `ID_SUBCLASSE`. Coalesça as duas colunas ao ler vários meses.
- **Texto livre com espaços nas pontas.** Colunas como `OBJETIVO`, `POLIT_INVEST`, `DISTRIB_GESTOR_UNICO` e `CONFLITO_VENDA` têm espaços no início ou no fim do texto; aplique `trim` antes de comparar.
- **Percentuais fora de 0 a 100.** `PR_PL_ATIVO` (carteira) vai de -282 a 2.407 em 2026-10, porque um ativo (um derivativo, por exemplo) pode superar o patrimônio ou ter sinal negativo; as rentabilidades e `PR_ATIVO_EMISSOR` também vêm em pontos percentuais, não em fração.
- **Tipo inferido varia entre arquivos.** 1 coluna(s) (`PR_ATIVO_EMISSOR`) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.
- **CEP, DDD, telefone e CPF viram número.** O conversor infere o tipo de cada CSV e lê `TEL_SAC` como inteiro, o que descarta zeros à esquerda; reconstrua o texto com `lpad` quando precisar do código.

## Exemplos

Lâminas por competência (esquema desde 2023-11 usa `CNPJ_FUNDO_CLASSE`).

```python
import duckdb

duckdb.sql("""
    SELECT ano, mes, count(*) AS laminas
    FROM read_parquet('lake/cvm/fi-lamina/**/lamina_fi_20*__lamina_fi_20*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-lamina
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/LAMINA/
