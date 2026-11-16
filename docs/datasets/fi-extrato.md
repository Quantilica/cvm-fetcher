---
dataset:
  id: fi-extrato
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Extrato das Informações (CVM)"
  resumo: "Extrato anual das informações dos fundos de investimento (versão 2.0): dados cadastrais, taxas, prazos, limites de aplicação e regras de investimento declaradas pelo fundo, uma linha por fundo e competência, com 118 colunas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-extrato
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-extrato"
  periodicidade: "anual (um arquivo por ano); o portal declara atualização diária do arquivo mais recente e semanal dos demais (os arquivos de 2024 a 2026 foram regravados em 2026-11-14)"
  cobertura: {inicio: 2015, fim: em-curso}
  unidade: "o extrato de informações de um fundo (ou classe) em uma data de competência"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (arquivo por ano, com várias datas de competência)"}
  formato_bruto: "CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [CNPJ_FUNDO_CLASSE, DT_COMPTC], colunas: 118}
  unidades_de_medida:
    APLIC_MAX_FUNDO_LIGADO: "percentual (%)"
    APLIC_MIN: "moeda (R$)"
    PRAZO_ATUALIZ_COTA: "prazo (a unidade não consta do dicionário da CVM)"
    QT_DIA_CONVERSAO_COTA: "dias"
    QT_DIA_PAGTO_COTA: "dias"
    QT_DIA_RESGATE_COTAS: "dias"
    QT_DIA_PAGTO_RESGATE: "dias"
    TAXA_ADM: "percentual (%)"
    TAXA_CUSTODIA_MAX: "percentual (%)"
    TAXA_PERFM: "percentual (%)"
    PR_INDICE_REFER_TAXA_PERFM: "percentual (%)"
    VL_CUPOM: "moeda (R$)"
    TAXA_INGRESSO_REAL: "percentual (%)"
    TAXA_INGRESSO_PR: "percentual (%)"
    TAXA_SAIDA_REAL: "percentual (%)"
    TAXA_SAIDA_PR: "percentual (%)"
    FATOR_OPER_VL_SUPERIOR_PL: "fator (razão ao patrimônio líquido)"
    APLIC_MAX_ATIVO_EXTERIOR: "percentual do patrimônio líquido (%)"
    APLIC_MAX_ATIVO_CRED_PRIV: "percentual do patrimônio líquido (%)"
    PR_INSTITUICAO_FINANC_MIN: "percentual (%)"
    PR_INSTITUICAO_FINANC_MAX: "percentual (%)"
    PR_CIA_MIN: "percentual (%)"
    PR_CIA_MAX: "percentual (%)"
    PR_FI_MIN: "percentual (%)"
    PR_FI_MAX: "percentual (%)"
    PR_UNIAO_MIN: "percentual (%)"
    PR_UNIAO_MAX: "percentual (%)"
    PR_ADMIN_GESTOR_MIN: "percentual (%)"
    PR_ADMIN_GESTOR_MAX: "percentual (%)"
    PR_EMISSOR_OUTRO_MIN: "percentual (%)"
    PR_EMISSOR_OUTRO_MAX: "percentual (%)"
    PR_COTA_FI_MIN: "percentual (%)"
    PR_COTA_FI_MAX: "percentual (%)"
    PR_COTA_FIC_MIN: "percentual (%)"
    PR_COTA_FIC_MAX: "percentual (%)"
    PR_COTA_FI_QUALIF_MIN: "percentual (%)"
    PR_COTA_FI_QUALIF_MAX: "percentual (%)"
    PR_COTA_FIC_QUALIF_MIN: "percentual (%)"
    PR_COTA_FIC_QUALIF_MAX: "percentual (%)"
    PR_COTA_FI_PROF_MIN: "percentual (%)"
    PR_COTA_FI_PROF_MAX: "percentual (%)"
    PR_COTA_FIC_PROF_MIN: "percentual (%)"
    PR_COTA_FIC_PROF_MAX: "percentual (%)"
    PR_COTA_FII_MIN: "percentual (%)"
    PR_COTA_FII_MAX: "percentual (%)"
    PR_COTA_FIDC_MIN: "percentual (%)"
    PR_COTA_FIDC_MAX: "percentual (%)"
    PR_COTA_FICFIDC_MIN: "percentual (%)"
    PR_COTA_FICFIDC_MAX: "percentual (%)"
    PR_COTA_FIDC_NP_MIN: "percentual (%)"
    PR_COTA_FIDC_NP_MAX: "percentual (%)"
    PR_COTA_FICFIDC_NP_MIN: "percentual (%)"
    PR_COTA_FICFIDC_NP_MAX: "percentual (%)"
    PR_COTA_ETF_MIN: "percentual (%)"
    PR_COTA_ETF_MAX: "percentual (%)"
    PR_CRI_MIN: "percentual (%)"
    PR_CRI_MAX: "percentual (%)"
    PR_TITPUB_MIN: "percentual (%)"
    PR_TITPUB_MAX: "percentual (%)"
    PR_OURO_MIN: "percentual (%)"
    PR_OURO_MAX: "percentual (%)"
    PR_TIT_INSTITUICAO_FINANC_BACEN_MIN: "percentual (%)"
    PR_TIT_INSTITUICAO_FINANC_BACEN_MAX: "percentual (%)"
    PR_VLMOB_MIN: "percentual (%)"
    PR_VLMOB_MAX: "percentual (%)"
    PR_ACAO_MIN: "percentual (%)"
    PR_ACAO_MAX: "percentual (%)"
    PR_DEBENTURE_MIN: "percentual (%)"
    PR_DEBENTURE_MAX: "percentual (%)"
    PR_NP_MIN: "percentual (%)"
    PR_NP_MAX: "percentual (%)"
    PR_COMPROM_MIN: "percentual (%)"
    PR_COMPROM_MAX: "percentual (%)"
    PR_DERIV_MIN: "percentual (%)"
    PR_DERIV_MAX: "percentual (%)"
    PR_ATIVO_OUTRO_MIN: "percentual (%)"
    PR_ATIVO_OUTRO_MAX: "percentual (%)"
    PR_COTA_FMIEE_MIN: "percentual (%)"
    PR_COTA_FMIEE_MAX: "percentual (%)"
    PR_COTA_FIP_MIN: "percentual (%)"
    PR_COTA_FIP_MAX: "percentual (%)"
    PR_COTA_FICFIP_MIN: "percentual (%)"
    PR_COTA_FICFIP_MAX: "percentual (%)"
  dados_pessoais: nenhum
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Extrato das Informações

## Resumo

Extrato anual das informações dos fundos de investimento (versão 2.0): dados cadastrais, taxas, prazos, limites de aplicação e regras de investimento declaradas pelo fundo, uma linha por fundo e competência, com 118 colunas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-extrato` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-extrato |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-extrato |
| Periodicidade | anual (um arquivo por ano); o portal declara atualização diária do arquivo mais recente e semanal dos demais (os arquivos de 2024 a 2026 foram regravados em 2026-11-14) |
| Cobertura | 2015 a em-curso |
| Unidade (uma linha) | o extrato de informações de um fundo (ou classe) em uma data de competência |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (arquivo por ano, com várias datas de competência) |
| Formato bruto | CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | `CNPJ_FUNDO_CLASSE`, `DT_COMPTC` |
| Colunas | 118 |
| Unidades de medida | `APLIC_MAX_FUNDO_LIGADO`: percentual (%); `APLIC_MIN`: moeda (R$); `PRAZO_ATUALIZ_COTA`: prazo (a unidade não consta do dicionário da CVM); `QT_DIA_CONVERSAO_COTA`: dias; `QT_DIA_PAGTO_COTA`: dias; `QT_DIA_RESGATE_COTAS`: dias; `QT_DIA_PAGTO_RESGATE`: dias; `TAXA_ADM`: percentual (%); `TAXA_CUSTODIA_MAX`: percentual (%); `TAXA_PERFM`: percentual (%); `PR_INDICE_REFER_TAXA_PERFM`: percentual (%); `VL_CUPOM`: moeda (R$); `TAXA_INGRESSO_REAL`: percentual (%); `TAXA_INGRESSO_PR`: percentual (%); `TAXA_SAIDA_REAL`: percentual (%); `TAXA_SAIDA_PR`: percentual (%); `FATOR_OPER_VL_SUPERIOR_PL`: fator (razão ao patrimônio líquido); `APLIC_MAX_ATIVO_EXTERIOR`: percentual do patrimônio líquido (%); `APLIC_MAX_ATIVO_CRED_PRIV`: percentual do patrimônio líquido (%); `PR_INSTITUICAO_FINANC_MIN`: percentual (%); `PR_INSTITUICAO_FINANC_MAX`: percentual (%); `PR_CIA_MIN`: percentual (%); `PR_CIA_MAX`: percentual (%); `PR_FI_MIN`: percentual (%); `PR_FI_MAX`: percentual (%); `PR_UNIAO_MIN`: percentual (%); `PR_UNIAO_MAX`: percentual (%); `PR_ADMIN_GESTOR_MIN`: percentual (%); `PR_ADMIN_GESTOR_MAX`: percentual (%); `PR_EMISSOR_OUTRO_MIN`: percentual (%); `PR_EMISSOR_OUTRO_MAX`: percentual (%); `PR_COTA_FI_MIN`: percentual (%); `PR_COTA_FI_MAX`: percentual (%); `PR_COTA_FIC_MIN`: percentual (%); `PR_COTA_FIC_MAX`: percentual (%); `PR_COTA_FI_QUALIF_MIN`: percentual (%); `PR_COTA_FI_QUALIF_MAX`: percentual (%); `PR_COTA_FIC_QUALIF_MIN`: percentual (%); `PR_COTA_FIC_QUALIF_MAX`: percentual (%); `PR_COTA_FI_PROF_MIN`: percentual (%); `PR_COTA_FI_PROF_MAX`: percentual (%); `PR_COTA_FIC_PROF_MIN`: percentual (%); `PR_COTA_FIC_PROF_MAX`: percentual (%); `PR_COTA_FII_MIN`: percentual (%); `PR_COTA_FII_MAX`: percentual (%); `PR_COTA_FIDC_MIN`: percentual (%); `PR_COTA_FIDC_MAX`: percentual (%); `PR_COTA_FICFIDC_MIN`: percentual (%); `PR_COTA_FICFIDC_MAX`: percentual (%); `PR_COTA_FIDC_NP_MIN`: percentual (%); `PR_COTA_FIDC_NP_MAX`: percentual (%); `PR_COTA_FICFIDC_NP_MIN`: percentual (%); `PR_COTA_FICFIDC_NP_MAX`: percentual (%); `PR_COTA_ETF_MIN`: percentual (%); `PR_COTA_ETF_MAX`: percentual (%); `PR_CRI_MIN`: percentual (%); `PR_CRI_MAX`: percentual (%); `PR_TITPUB_MIN`: percentual (%); `PR_TITPUB_MAX`: percentual (%); `PR_OURO_MIN`: percentual (%); `PR_OURO_MAX`: percentual (%); `PR_TIT_INSTITUICAO_FINANC_BACEN_MIN`: percentual (%); `PR_TIT_INSTITUICAO_FINANC_BACEN_MAX`: percentual (%); `PR_VLMOB_MIN`: percentual (%); `PR_VLMOB_MAX`: percentual (%); `PR_ACAO_MIN`: percentual (%); `PR_ACAO_MAX`: percentual (%); `PR_DEBENTURE_MIN`: percentual (%); `PR_DEBENTURE_MAX`: percentual (%); `PR_NP_MIN`: percentual (%); `PR_NP_MAX`: percentual (%); `PR_COMPROM_MIN`: percentual (%); `PR_COMPROM_MAX`: percentual (%); `PR_DERIV_MIN`: percentual (%); `PR_DERIV_MAX`: percentual (%); `PR_ATIVO_OUTRO_MIN`: percentual (%); `PR_ATIVO_OUTRO_MAX`: percentual (%); `PR_COTA_FMIEE_MIN`: percentual (%); `PR_COTA_FMIEE_MAX`: percentual (%); `PR_COTA_FIP_MIN`: percentual (%); `PR_COTA_FIP_MAX`: percentual (%); `PR_COTA_FICFIP_MIN`: percentual (%); `PR_COTA_FICFIP_MAX`: percentual (%) |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-extrato). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/EXTRATO/DADOS/`.
- O catálogo do fetcher lista 12 arquivo(s): de `extrato_fi_2015.csv` a `extrato_fi_2026.csv`.
- Em 2026-11-16 conferimos 3 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2015, 2021, 2026).
- No bruto, o arquivo fica em `fi-extrato/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o extrato de informações de um fundo (ou classe) em uma data de competência.
- Particionado por `ano`; o catálogo cobre 2015 a 2026, e conferimos as amostras 2015, 2021, 2026.
- O arquivo de 2026 tem 7.748 linhas, 5.929 CNPJ e 213 datas de competência entre 2026-01-02 e 2026-11-13; o de 2021 tem 12.860 linhas e 9.813 CNPJ; o de 2015 tem 967 linhas (de 2015-10-01 a 2015-12-30). As datas de competência não são fins de mês (213 datas distintas em 2026).
- O portal publica os extratos dos últimos cinco anos; o histórico desde 2015 existe, mas só os últimos arquivos são regravados.
- Uma tabela, com 118 colunas; o maior arquivo convertido tem 12.860 linhas. Chave candidata (única no arquivo mais recente convertido): `CNPJ_FUNDO_CLASSE`, `DT_COMPTC`.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE`) | — | 2015 |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `CONDOM` | `CONDOM` | texto | Forma de condomínio | Aberto/Fechado | todo |
| `NEGOC_MERC` | `NEGOC_MERC` | texto | Indica se as cotas do fundo são admitidas à negociação em mercado organizado | S/N | todo |
| `MERCADO` | `MERCADO` | texto | Nome do Mercado | — | todo |
| `TP_PRAZO` | `TP_PRAZO` | texto | Tipo de prazo | — | todo |
| `PRAZO` | `PRAZO` | texto | Detalhamento sobre o prazo | — | todo |
| `PUBLICO_ALVO` | `PUBLICO_ALVO` | texto | Público-alvo | — | todo |
| `REG_ANBIMA` | `REG_ANBIMA` | texto | Indica se o fundo é registrado na ANBIMA | S/N | todo |
| `CLASSE_ANBIMA` | `CLASSE_ANBIMA` | texto | Classificação de Fundos regulados ANBIMA | — | todo |
| `DISTRIB` | `DISTRIB` | texto | Forma de distribuição | — | todo |
| `POLIT_INVEST` | `POLIT_INVEST` | texto | Política de investimento | — | todo |
| `APLIC_MAX_FUNDO_LIGADO` | `APLIC_MAX_FUNDO_LIGADO` | decimal | Percentual máximo de aplicação em cotas de fundos de investimento com o mesmo administrador, gestor ou empresas a eles ligadas | percentual (%) | todo |
| `RESULT_CART_INCORP_PL` | `RESULT_CART_INCORP_PL` | texto | Indica se os resultados atrelados à carteira de ativos (dividendos, JSCP, etc) são incorporados ao patrimônio líquido do fundo | S/N | todo |
| `FUNDO_COTAS` | `FUNDO_COTAS` | texto | Indica se é fundo de cotas | S/N | todo |
| `FUNDO_ESPELHO` | `FUNDO_ESPELHO` | texto | Indica se é fundo-espelho | S/N | todo |
| `APLIC_MIN` | `APLIC_MIN` | decimal | Aplicação mínima | moeda (R$) | todo |
| `ATUALIZ_DIARIA_COTA` | `ATUALIZ_DIARIA_COTA` | texto | Indica se o valor da cota será atualizado e informado diariamente | S/N | todo |
| `PRAZO_ATUALIZ_COTA` | `PRAZO_ATUALIZ_COTA` | inteiro / texto | Prazo de atualização do valor da cota | prazo (a unidade não consta do dicionário da CVM) | todo |
| `COTA_EMISSAO` | `COTA_EMISSAO` | texto | Valor da cota utilizado na emissão de cotas | — | todo |
| `COTA_PL` | `COTA_PL` | texto | Patrimônio Líquido base para o cálculo do valor da cota | — | todo |
| `QT_DIA_CONVERSAO_COTA` | `QT_DIA_CONVERSAO_COTA` | inteiro | Prazo em dias úteis para conversão de cotas após o pedido de resgate | dias | todo |
| `QT_DIA_PAGTO_COTA` | `QT_DIA_PAGTO_COTA` | inteiro | Prazo em dias úteis para pagamento de resgates após a conversão de cotas | dias | todo |
| `QT_DIA_RESGATE_COTAS` | `QT_DIA_RESGATE_COTAS` | inteiro | Dias de carência para o resgate de cotas | dias | todo |
| `QT_DIA_PAGTO_RESGATE` | `QT_DIA_PAGTO_RESGATE` | inteiro | Prazo para o efetivo pagamento dos resgates, contado a partir da data do pedido | dias | todo |
| `TP_DIA_PAGTO_RESGATE` | `TP_DIA_PAGTO_RESGATE` | texto | Tipo de prazo para o efetivo pagamento dos resgates | — | todo |
| `TAXA_SAIDA_PAGTO_RESGATE` | `TAXA_SAIDA_PAGTO_RESGATE` | texto | Indica se, para o efetivo pagamento dos resgates, há cobrança de taxa de saída | S/N | todo |
| `TAXA_ADM` | `TAXA_ADM` | decimal | Taxa de administração | percentual (%) | todo |
| `TAXA_CUSTODIA_MAX` | `TAXA_CUSTODIA_MAX` | decimal | Taxa máxima de custódia | percentual (%) | todo |
| `EXISTE_TAXA_PERFM` | `EXISTE_TAXA_PERFM` | texto | Indica se o fundo cobra taxa de performance | S/N | todo |
| `TAXA_PERFM` | `TAXA_PERFM` | decimal | Taxa de performance | percentual (%) | todo |
| `PARAM_TAXA_PERFM` | `PARAM_TAXA_PERFM` | texto | Parâmetro utilizado para cobrança de taxa de performance | — | todo |
| `PR_INDICE_REFER_TAXA_PERFM` | `PR_INDICE_REFER_TAXA_PERFM` | decimal | Percentual do Índice de Referência (Taxa de performance) | percentual (%) | todo |
| `VL_CUPOM` | `VL_CUPOM` | decimal | Valor do Cupom | moeda (R$) | todo |
| `CALC_TAXA_PERFM` | `CALC_TAXA_PERFM` | texto | Método de cálculo da taxa de performance | — | todo |
| `INF_TAXA_PERFM` | `INF_TAXA_PERFM` | texto | Informações Adicionais (Taxa de performance) | — | todo |
| `EXISTE_TAXA_INGRESSO` | `EXISTE_TAXA_INGRESSO` | texto | Indica se o fundo cobra taxa de ingresso | S/N | todo |
| `TAXA_INGRESSO_REAL` | `TAXA_INGRESSO_REAL` | decimal | Taxa de ingresso (Real) | percentual (%) | todo |
| `TAXA_INGRESSO_PR` | `TAXA_INGRESSO_PR` | decimal | Taxa de ingresso (Percentagem) | percentual (%) | todo |
| `EXISTE_TAXA_SAIDA` | `EXISTE_TAXA_SAIDA` | texto | Indica se o fundo cobra taxa de saída | S/N | todo |
| `TAXA_SAIDA_REAL` | `TAXA_SAIDA_REAL` | decimal | Taxa de saída (Real) | percentual (%) | todo |
| `TAXA_SAIDA_PR` | `TAXA_SAIDA_PR` | decimal | Taxa de saída (Percentagem) | percentual (%) | todo |
| `OPER_DERIV` | `OPER_DERIV` | texto | Indica se o fundo pode realizar operações com derivativos | S/N | todo |
| `FINALIDADE_OPER_DERIV` | `FINALIDADE_OPER_DERIV` | texto | Finalidade das operações com derivativos | — | todo |
| `OPER_VL_SUPERIOR_PL` | `OPER_VL_SUPERIOR_PL` | texto | Indica se o fundo pode realizar operações em valor superior ao seu patrimônio líquido | S/N | todo |
| `FATOR_OPER_VL_SUPERIOR_PL` | `FATOR_OPER_VL_SUPERIOR_PL` | decimal | Fator limite para o valor total das operações, em relação ao patrimônio líquido | fator (razão ao patrimônio líquido) | todo |
| `CONTRAP_LIGADO` | `CONTRAP_LIGADO` | texto | Indica se o regulamento permite que, em mercado sem contraparte central, o fundo tenha como contraparte o administrador, gestor, fundos de investimento por eles administrados ou geridos, conforme o caso, ou pessoas ligadas | S/N | todo |
| `INVEST_EXTERIOR` | `INVEST_EXTERIOR` | texto | Indica se o fundo pode realizar investimentos no exterior | S/N | todo |
| `APLIC_MAX_ATIVO_EXTERIOR` | `APLIC_MAX_ATIVO_EXTERIOR` | decimal | Limite máximo, em relação ao Patrimônio Líquido do fundo, que pode ser aplicado em ativos no exterior | percentual do patrimônio líquido (%) | todo |
| `ATIVO_CRED_PRIV` | `ATIVO_CRED_PRIV` | texto | Indica se o regulamento permite que o fundo adquira ativos de crédito privado | S/N | todo |
| `APLIC_MAX_ATIVO_CRED_PRIV` | `APLIC_MAX_ATIVO_CRED_PRIV` | decimal | Limite máximo, em relação ao Patrimônio Líquido do fundo, que pode ser aplicado em ativos de crédito privado | percentual do patrimônio líquido (%) | todo |
| `PR_INSTITUICAO_FINANC_MIN` | `PR_INSTITUICAO_FINANC_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para emissor do tipo Instituições Financeiras | percentual (%) | todo |
| `PR_INSTITUICAO_FINANC_MAX` | `PR_INSTITUICAO_FINANC_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para emissor do tipo Instituições Financeiras | percentual (%) | todo |
| `PR_CIA_MIN` | `PR_CIA_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para emissor do tipo Companhias Abertas | percentual (%) | todo |
| `PR_CIA_MAX` | `PR_CIA_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para emissor do tipo Companhias Abertas | percentual (%) | todo |
| `PR_FI_MIN` | `PR_FI_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para emissor do tipo Fundos de Investimento | percentual (%) | todo |
| `PR_FI_MAX` | `PR_FI_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para emissor do tipo Fundos de Investimento | percentual (%) | todo |
| `PR_UNIAO_MIN` | `PR_UNIAO_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para emissor do tipo União Federal | percentual (%) | todo |
| `PR_UNIAO_MAX` | `PR_UNIAO_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para emissor do tipo União Federal | percentual (%) | todo |
| `PR_ADMIN_GESTOR_MIN` | `PR_ADMIN_GESTOR_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para emissor do tipo Administrador, Gestor ou Pessoas Ligadas | percentual (%) | todo |
| `PR_ADMIN_GESTOR_MAX` | `PR_ADMIN_GESTOR_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para emissor do tipo Administrador, Gestor ou Pessoas Ligadas | percentual (%) | todo |
| `PR_EMISSOR_OUTRO_MIN` | `PR_EMISSOR_OUTRO_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para emissor do tipo Outros (art. 102, IV, ICVM 555) | percentual (%) | todo |
| `PR_EMISSOR_OUTRO_MAX` | `PR_EMISSOR_OUTRO_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para emissor do tipo Outros (art. 102, IV, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FI_MIN` | `PR_COTA_FI_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FI 555 | percentual (%) | todo |
| `PR_COTA_FI_MAX` | `PR_COTA_FI_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FI 555 | percentual (%) | todo |
| `PR_COTA_FIC_MIN` | `PR_COTA_FIC_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIC 555 | percentual (%) | todo |
| `PR_COTA_FIC_MAX` | `PR_COTA_FIC_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIC 555 | percentual (%) | todo |
| `PR_COTA_FI_QUALIF_MIN` | `PR_COTA_FI_QUALIF_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FI 555 para investidores qualificados | percentual (%) | todo |
| `PR_COTA_FI_QUALIF_MAX` | `PR_COTA_FI_QUALIF_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FI 555 para investidores qualificados | percentual (%) | todo |
| `PR_COTA_FIC_QUALIF_MIN` | `PR_COTA_FIC_QUALIF_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIC 555 para investidores qualificados | percentual (%) | todo |
| `PR_COTA_FIC_QUALIF_MAX` | `PR_COTA_FIC_QUALIF_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIC 555 para investidores qualificados | percentual (%) | todo |
| `PR_COTA_FI_PROF_MIN` | `PR_COTA_FI_PROF_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FI 555 para investidores profissionais | percentual (%) | todo |
| `PR_COTA_FI_PROF_MAX` | `PR_COTA_FI_PROF_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FI 555 para investidores profissionais | percentual (%) | todo |
| `PR_COTA_FIC_PROF_MIN` | `PR_COTA_FIC_PROF_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIC 555 para investidores profissionais | percentual (%) | todo |
| `PR_COTA_FIC_PROF_MAX` | `PR_COTA_FIC_PROF_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIC 555 para investidores profissionais | percentual (%) | todo |
| `PR_COTA_FII_MIN` | `PR_COTA_FII_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FII | percentual (%) | todo |
| `PR_COTA_FII_MAX` | `PR_COTA_FII_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FII | percentual (%) | todo |
| `PR_COTA_FIDC_MIN` | `PR_COTA_FIDC_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIDC | percentual (%) | todo |
| `PR_COTA_FIDC_MAX` | `PR_COTA_FIDC_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIDC | percentual (%) | todo |
| `PR_COTA_FICFIDC_MIN` | `PR_COTA_FICFIDC_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FICFIDC | percentual (%) | todo |
| `PR_COTA_FICFIDC_MAX` | `PR_COTA_FICFIDC_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FICFIDC | percentual (%) | todo |
| `PR_COTA_FIDC_NP_MIN` | `PR_COTA_FIDC_NP_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIDC-NP | percentual (%) | todo |
| `PR_COTA_FIDC_NP_MAX` | `PR_COTA_FIDC_NP_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIDC-NP | percentual (%) | todo |
| `PR_COTA_FICFIDC_NP_MIN` | `PR_COTA_FICFIDC_NP_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FICFIDC-NP | percentual (%) | todo |
| `PR_COTA_FICFIDC_NP_MAX` | `PR_COTA_FICFIDC_NP_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FICFIDC-NP | percentual (%) | todo |
| `PR_COTA_ETF_MIN` | `PR_COTA_ETF_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de Fundos de Índice de Mercado (ETF) | percentual (%) | todo |
| `PR_COTA_ETF_MAX` | `PR_COTA_ETF_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de Fundos de Índice de Mercado (ETF) | percentual (%) | todo |
| `PR_CRI_MIN` | `PR_CRI_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo CRI | percentual (%) | todo |
| `PR_CRI_MAX` | `PR_CRI_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo CRI | percentual (%) | todo |
| `PR_TITPUB_MIN` | `PR_TITPUB_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Títulos públicos e operações compromissadas lastreadas nestes títulos | percentual (%) | todo |
| `PR_TITPUB_MAX` | `PR_TITPUB_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Títulos públicos e operações compromissadas lastreadas nestes títulos | percentual (%) | todo |
| `PR_OURO_MIN` | `PR_OURO_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Ouro | percentual (%) | todo |
| `PR_OURO_MAX` | `PR_OURO_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Ouro | percentual (%) | todo |
| `PR_TIT_INSTITUICAO_FINANC_BACEN_MIN` | `PR_TIT_INSTITUICAO_FINANC_BACEN_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Títulos de emissão ou coobrigação de instituição financeira autorizada a funcionar pelo Banco Central do Brasil e operações compromissadas lastreadas nestes títulos | percentual (%) | todo |
| `PR_TIT_INSTITUICAO_FINANC_BACEN_MAX` | `PR_TIT_INSTITUICAO_FINANC_BACEN_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Títulos de emissão ou coobrigação de instituição financeira autorizada a funcionar pelo Banco Central do Brasil e operações compromissadas lastreadas nestes títulos | percentual (%) | todo |
| `PR_VLMOB_MIN` | `PR_VLMOB_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Valores mobiliários previstos na alínea (d) do inciso III do art. 103 da ICVM 555 | percentual (%) | todo |
| `PR_VLMOB_MAX` | `PR_VLMOB_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Valores mobiliários previstos na alínea (d) do inciso III do art. 103 da ICVM 555 | percentual (%) | todo |
| `PR_ACAO_MIN` | `PR_ACAO_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Ações ou Certificados de Depósito de Ações | percentual (%) | todo |
| `PR_ACAO_MAX` | `PR_ACAO_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Ações ou Certificados de Depósito de Ações | percentual (%) | todo |
| `PR_DEBENTURE_MIN` | `PR_DEBENTURE_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Debêntures | percentual (%) | todo |
| `PR_DEBENTURE_MAX` | `PR_DEBENTURE_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Debêntures | percentual (%) | todo |
| `PR_NP_MIN` | `PR_NP_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Notas promissórias | percentual (%) | todo |
| `PR_NP_MAX` | `PR_NP_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Notas promissórias | percentual (%) | todo |
| `PR_COMPROM_MIN` | `PR_COMPROM_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Operações compromissadas lastreadas em títulos de crédito privado | percentual (%) | todo |
| `PR_COMPROM_MAX` | `PR_COMPROM_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Operações compromissadas lastreadas em títulos de crédito privado | percentual (%) | todo |
| `PR_DERIV_MIN` | `PR_DERIV_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Derivativos | percentual (%) | todo |
| `PR_DERIV_MAX` | `PR_DERIV_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Derivativos | percentual (%) | todo |
| `PR_ATIVO_OUTRO_MIN` | `PR_ATIVO_OUTRO_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Outros (art. 103, I, j, ICVM 555) | percentual (%) | todo |
| `PR_ATIVO_OUTRO_MAX` | `PR_ATIVO_OUTRO_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Outros (art. 103, I, j, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FMIEE_MIN` | `PR_COTA_FMIEE_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FMIEE (art. 109, §8º, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FMIEE_MAX` | `PR_COTA_FMIEE_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FMIEE (art. 109, §8º, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FIP_MIN` | `PR_COTA_FIP_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIP (art. 109, §8º, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FIP_MAX` | `PR_COTA_FIP_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FIP (art. 109, §8º, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FICFIP_MIN` | `PR_COTA_FICFIP_MIN` | decimal | Exposição mínima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FICFIP (art. 109, §8º, ICVM 555) | percentual (%) | todo |
| `PR_COTA_FICFIP_MAX` | `PR_COTA_FICFIP_MAX` | decimal | Exposição máxima (em percentual) permitida pelo Regulamento para ativo do tipo Cotas de FICFIP (art. 109, §8º, ICVM 555) | percentual (%) | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe | — | 2021 a 2026 |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe | — | 2021 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-extrato`, particionado por `ano`; um arquivo Parquet por arquivo CSV de origem.
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Colunas de CNPJ por arquivo.** O arquivo de 2015 usa `CNPJ_FUNDO`; os de 2021 e 2026 (regravados em 2025-12 e 2026-11) usam `CNPJ_FUNDO_CLASSE` e trazem `TP_FUNDO_CLASSE`. Arquivos antigos que a CVM não regrava mantêm o layout anterior; coalesça as duas colunas.
- **Várias versões por fundo.** Um fundo aparece em várias datas de competência no mesmo ano: para o extrato vigente, tome a maior `DT_COMPTC` de cada CNPJ.
- **Taxas com valores absurdos.** `TAXA_ADM` do arquivo de 2026 chega a 262.600 (mediana de 0,09); trate valores muito acima de 100 como erro de preenchimento antes de agregar.
- **Colunas quase vazias.** `PRAZO_ATUALIZ_COTA`, `QT_DIA_RESGATE_COTAS`, `TAXA_INGRESSO_REAL` e `TAXA_INGRESSO_PR` têm mais de 98% de nulos no arquivo de 2026; os limites de aplicação (`PR_*_MIN`, `PR_*_MAX`) valem como declarados no regulamento, não como posição da carteira.
- **Tipo inferido varia entre arquivos.** 1 coluna(s) (`PRAZO_ATUALIZ_COTA`) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Último extrato de cada classe em 2026.

```python
import duckdb

duckdb.sql("""
    SELECT CNPJ_FUNDO_CLASSE, max(DT_COMPTC) AS ultima_competencia, any_value(TAXA_ADM) AS taxa_adm
    FROM read_parquet('lake/cvm/fi-extrato/ano=2026/*.parquet')
    GROUP BY 1
    ORDER BY 1
    LIMIT 10
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-extrato
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/EXTRATO/
