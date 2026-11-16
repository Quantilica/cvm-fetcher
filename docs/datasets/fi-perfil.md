---
dataset:
  id: fi-perfil
  fonte: cvm
  titulo: "Fundos de Investimento: Documentos: Perfil Mensal (CVM)"
  resumo: "Perfil mensal dos fundos de investimento (ICVM 555): o número de cotistas e a participação no patrimônio por tipo de investidor, a liquidez, os principais comitentes e emissores, os cenários de estresse e outras características da carteira, com 108 colunas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-doc-perfil_mensal
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-perfil_mensal"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização semanal (os arquivos recentes foram regravados em 2026-11-14)"
  cobertura: {inicio: 2019-01, fim: em-curso}
  unidade: "o perfil mensal de um fundo ou classe em um mês"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (fim do mês, `DT_COMPTC`)"}
  formato_bruto: "CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [CNPJ_FUNDO_CLASSE], colunas: 108}
  unidades_de_medida:
    VERSAO: "código ou número de identificação (sem unidade)"
    NR_COTST_PF_PB: "quantidade"
    NR_COTST_PF_VAREJO: "quantidade"
    NR_COTST_PJ_NAO_FINANC_PB: "quantidade"
    NR_COTST_PJ_NAO_FINANC_VAREJO: "quantidade"
    NR_COTST_BANCO: "quantidade"
    NR_COTST_CORRETORA_DISTRIB: "quantidade"
    NR_COTST_PJ_FINANC: "quantidade"
    NR_COTST_INVNR: "quantidade"
    NR_COTST_EAPC: "quantidade"
    NR_COTST_EFPC: "quantidade"
    NR_COTST_RPPS: "quantidade"
    NR_COTST_SEGUR: "quantidade"
    NR_COTST_CAPITALIZ: "quantidade"
    NR_COTST_FI_CLUBE: "quantidade"
    NR_COTST_DISTRIB: "quantidade"
    NR_COTST_OUTRO: "quantidade"
    PR_PL_COTST_PF_PB: "percentual (%)"
    PR_PL_COTST_PF_VAREJO: "percentual (%)"
    PR_PL_COTST_PJ_NAO_FINANC_PB: "percentual (%)"
    PR_PL_COTST_PJ_NAO_FINANC_VAREJO: "percentual (%)"
    PR_PL_COTST_BANCO: "percentual (%)"
    PR_PL_COTST_CORRETORA_DISTRIB: "percentual (%)"
    PR_PL_COTST_PJ_FINANC: "percentual (%)"
    PR_PL_COTST_INVNR: "percentual (%)"
    PR_PL_COTST_EAPC: "percentual (%)"
    PR_PL_COTST_EFPC: "percentual (%)"
    PR_PL_COTST_RPPS: "percentual (%)"
    PR_PL_COTST_SEGUR: "percentual (%)"
    PR_PL_COTST_CAPITALIZ: "percentual (%)"
    PR_PL_COTST_FI_CLUBE: "percentual (%)"
    PR_PL_COTST_DISTRIB: "percentual (%)"
    PR_PL_COTST_OUTRO: "percentual (%)"
    PR_VAR_CARTEIRA: "percentual (%)"
    PRAZO_CARTEIRA_TITULO: "meses"
    VL_CONTRATO_COMPRA_DOLAR: "moeda (o dicionário não informa a moeda; a descrição fala em US$)"
    VL_CONTRATO_VENDA_DOLAR: "moeda (o dicionário não informa a moeda; a descrição fala em US$)"
    PR_VARIACAO_DIARIA_COTA: "percentual (%)"
    PR_VARIACAO_DIARIA_COTA_ESTRESSE: "percentual (%)"
    PR_VARIACAO_DIARIA_PL_TAXA_ANUAL: "percentual (%)"
    PR_VARIACAO_DIARIA_PL_TAXA_CAMBIO: "percentual (%)"
    PR_VARIACAO_DIARIA_PL_IBOVESPA: "percentual (%)"
    PR_VARIACAO_DIARIA_OUTRO: "percentual (%)"
    PR_COLATERAL_DERIV: "percentual (%)"
    VL_FATOR_RISCO_NOCIONAL_LONG_IBOVESPA: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_LONG_JUROS: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_LONG_CUPOM: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_LONG_DOLAR: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_LONG_OUTRO: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_SHORT_IBOVESPA: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_SHORT_JUROS: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_SHORT_CUPOM: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_SHORT_DOLAR: "moeda (R$)"
    VL_FATOR_RISCO_NOCIONAL_SHORT_OUTRO: "moeda (R$)"
    PR_COMITENTE_1: "percentual (%)"
    PR_COMITENTE_2: "percentual (%)"
    PR_COMITENTE_3: "percentual (%)"
    PR_ATIVO_EMISSOR_LIGADO: "percentual (%)"
    PR_EMISSOR_1: "percentual (%)"
    PR_EMISSOR_2: "percentual (%)"
    PR_EMISSOR_3: "percentual (%)"
    PR_ATIVO_CRED_PRIV: "percentual (%)"
    VL_COTA_TAXA_PERFM: "percentual (%)"
    VL_DIREITO_DISTRIB: "moeda (R$)"
    PR_PATRIM_LIQ_MAIOR_COTST: "percentual (%)"
  dados_pessoais:
    - {coluna: CPF_CNPJ_COMITENTE_1, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_COMITENTE_2, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_COMITENTE_3, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_EMISSOR_1, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_EMISSOR_2, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_EMISSOR_3, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras:
    - {desde: 2023-12, mudanca: "`CNPJ_FUNDO` vira `CNPJ_FUNDO_CLASSE` e entra `TP_FUNDO_CLASSE` (adaptação à Resolução CVM 175)"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Documentos: Perfil Mensal

## Resumo

Perfil mensal dos fundos de investimento (ICVM 555): o número de cotistas e a participação no patrimônio por tipo de investidor, a liquidez, os principais comitentes e emissores, os cenários de estresse e outras características da carteira, com 108 colunas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-perfil` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-doc-perfil_mensal |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-perfil_mensal |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização semanal (os arquivos recentes foram regravados em 2026-11-14) |
| Cobertura | 2019-01 a em-curso |
| Unidade (uma linha) | o perfil mensal de um fundo ou classe em um mês |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (fim do mês, `DT_COMPTC`) |
| Formato bruto | CSV com ponto e vírgula, um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `CNPJ_FUNDO_CLASSE` |
| Colunas | 108 |
| Unidades de medida | `VERSAO`: código ou número de identificação (sem unidade); `NR_COTST_PF_PB`: quantidade; `NR_COTST_PF_VAREJO`: quantidade; `NR_COTST_PJ_NAO_FINANC_PB`: quantidade; `NR_COTST_PJ_NAO_FINANC_VAREJO`: quantidade; `NR_COTST_BANCO`: quantidade; `NR_COTST_CORRETORA_DISTRIB`: quantidade; `NR_COTST_PJ_FINANC`: quantidade; `NR_COTST_INVNR`: quantidade; `NR_COTST_EAPC`: quantidade; `NR_COTST_EFPC`: quantidade; `NR_COTST_RPPS`: quantidade; `NR_COTST_SEGUR`: quantidade; `NR_COTST_CAPITALIZ`: quantidade; `NR_COTST_FI_CLUBE`: quantidade; `NR_COTST_DISTRIB`: quantidade; `NR_COTST_OUTRO`: quantidade; `PR_PL_COTST_PF_PB`: percentual (%); `PR_PL_COTST_PF_VAREJO`: percentual (%); `PR_PL_COTST_PJ_NAO_FINANC_PB`: percentual (%); `PR_PL_COTST_PJ_NAO_FINANC_VAREJO`: percentual (%); `PR_PL_COTST_BANCO`: percentual (%); `PR_PL_COTST_CORRETORA_DISTRIB`: percentual (%); `PR_PL_COTST_PJ_FINANC`: percentual (%); `PR_PL_COTST_INVNR`: percentual (%); `PR_PL_COTST_EAPC`: percentual (%); `PR_PL_COTST_EFPC`: percentual (%); `PR_PL_COTST_RPPS`: percentual (%); `PR_PL_COTST_SEGUR`: percentual (%); `PR_PL_COTST_CAPITALIZ`: percentual (%); `PR_PL_COTST_FI_CLUBE`: percentual (%); `PR_PL_COTST_DISTRIB`: percentual (%); `PR_PL_COTST_OUTRO`: percentual (%); `PR_VAR_CARTEIRA`: percentual (%); `PRAZO_CARTEIRA_TITULO`: meses; `VL_CONTRATO_COMPRA_DOLAR`: moeda (o dicionário não informa a moeda; a descrição fala em US$); `VL_CONTRATO_VENDA_DOLAR`: moeda (o dicionário não informa a moeda; a descrição fala em US$); `PR_VARIACAO_DIARIA_COTA`: percentual (%); `PR_VARIACAO_DIARIA_COTA_ESTRESSE`: percentual (%); `PR_VARIACAO_DIARIA_PL_TAXA_ANUAL`: percentual (%); `PR_VARIACAO_DIARIA_PL_TAXA_CAMBIO`: percentual (%); `PR_VARIACAO_DIARIA_PL_IBOVESPA`: percentual (%); `PR_VARIACAO_DIARIA_OUTRO`: percentual (%); `PR_COLATERAL_DERIV`: percentual (%); `VL_FATOR_RISCO_NOCIONAL_LONG_IBOVESPA`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_LONG_JUROS`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_LONG_CUPOM`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_LONG_DOLAR`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_LONG_OUTRO`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_SHORT_IBOVESPA`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_SHORT_JUROS`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_SHORT_CUPOM`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_SHORT_DOLAR`: moeda (R$); `VL_FATOR_RISCO_NOCIONAL_SHORT_OUTRO`: moeda (R$); `PR_COMITENTE_1`: percentual (%); `PR_COMITENTE_2`: percentual (%); `PR_COMITENTE_3`: percentual (%); `PR_ATIVO_EMISSOR_LIGADO`: percentual (%); `PR_EMISSOR_1`: percentual (%); `PR_EMISSOR_2`: percentual (%); `PR_EMISSOR_3`: percentual (%); `PR_ATIVO_CRED_PRIV`: percentual (%); `VL_COTA_TAXA_PERFM`: percentual (%); `VL_DIREITO_DISTRIB`: moeda (R$); `PR_PATRIM_LIQ_MAIOR_COTST`: percentual (%) |
| Dados pessoais | `CPF_CNPJ_COMITENTE_1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_COMITENTE_2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_COMITENTE_3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_EMISSOR_1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_EMISSOR_2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_EMISSOR_3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | 2023-12: `CNPJ_FUNDO` vira `CNPJ_FUNDO_CLASSE` e entra `TP_FUNDO_CLASSE` (adaptação à Resolução CVM 175) |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-doc-perfil_mensal). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/DOC/PERFIL_MENSAL/DADOS/`.
- O catálogo do fetcher lista 95 arquivo(s): de `perfil_mensal_fi_201901.csv` a `perfil_mensal_fi_202611.csv`.
- Em 2026-11-16 conferimos 3 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2019-01, 2022-12, 2026-10).
- No bruto, o arquivo fica em `fi-perfil/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o perfil mensal de um fundo ou classe em um mês.
- Particionado por `ano` e `mes`; o catálogo cobre 2019-01 a 2026-11, e conferimos as amostras 2019-01, 2022-12, 2026-10.
- Os arquivos amostrados têm 11.620 linhas em 2019-01, 24.392 em 2022-12 e 15.692 em 2026-10; `CNPJ_FUNDO_CLASSE` (em 2019-01 e 2022-12, `CNPJ_FUNDO`) é único em cada arquivo (uma linha por fundo ou classe por mês), e `VERSAO` registra a versão do documento.
- As colunas `NR_COTST_*` contam cotistas por tipo (pessoa física e jurídica, banco, corretora, investidor não residente, previdência, seguradora e outros) e as `PR_PL_COTST_*` dão a parcela do patrimônio líquido de cada tipo.
- Uma tabela, com 108 colunas; o maior arquivo convertido tem 24.392 linhas. Chave candidata (única no arquivo mais recente convertido): `CNPJ_FUNDO_CLASSE`.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_FUNDO_CLASSE`) | — | 2019-01 a 2022-12 |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `VERSAO` | `VERSAO` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `NR_COTST_PF_PB` | `NR_COTST_PF_PB` | inteiro | Número de clientes cotistas do tipo Pessoa Física Private Banking | quantidade | todo |
| `NR_COTST_PF_VAREJO` | `NR_COTST_PF_VAREJO` | inteiro | Número de clientes cotistas do tipo Pessoa Física Varejo | quantidade | todo |
| `NR_COTST_PJ_NAO_FINANC_PB` | `NR_COTST_PJ_NAO_FINANC_PB` | inteiro | Número de clientes cotistas do tipo Pessoa Jurídica Não-Financeira Private Banking | quantidade | todo |
| `NR_COTST_PJ_NAO_FINANC_VAREJO` | `NR_COTST_PJ_NAO_FINANC_VAREJO` | inteiro | Número de clientes cotistas do tipo Pessoa Jurídica Não-Financeira Varejo | quantidade | todo |
| `NR_COTST_BANCO` | `NR_COTST_BANCO` | inteiro | Número de clientes cotistas do tipo Banco Comercial | quantidade | todo |
| `NR_COTST_CORRETORA_DISTRIB` | `NR_COTST_CORRETORA_DISTRIB` | inteiro | Número de clientes cotistas do tipo Corretora ou Distribuidora | quantidade | todo |
| `NR_COTST_PJ_FINANC` | `NR_COTST_PJ_FINANC` | inteiro | Número de clientes cotistas do tipo Outras Pessoas Jurídicas Financeiras | quantidade | todo |
| `NR_COTST_INVNR` | `NR_COTST_INVNR` | inteiro | Número de clientes cotistas do tipo Investidores Não Residentes | quantidade | todo |
| `NR_COTST_EAPC` | `NR_COTST_EAPC` | inteiro | Número de clientes cotistas do tipo Entidade Aberta de Previdência Complementar | quantidade | todo |
| `NR_COTST_EFPC` | `NR_COTST_EFPC` | inteiro | Número de clientes cotistas do tipo Entidade Fechada de Previdência Complementar | quantidade | todo |
| `NR_COTST_RPPS` | `NR_COTST_RPPS` | inteiro | Número de clientes cotistas do tipo Regime Próprio de Previdência dos Servidores Públicos | quantidade | todo |
| `NR_COTST_SEGUR` | `NR_COTST_SEGUR` | inteiro | Número de clientes cotistas do tipo Sociedade Seguradora ou Resseguradora | quantidade | todo |
| `NR_COTST_CAPITALIZ` | `NR_COTST_CAPITALIZ` | inteiro | Número de clientes cotistas do tipo Sociedade de Capitalização e de Arrendamento Mercantil | quantidade | todo |
| `NR_COTST_FI_CLUBE` | `NR_COTST_FI_CLUBE` | inteiro | Número de clientes cotistas do tipo Fundos e Clubes de Investimento | quantidade | todo |
| `NR_COTST_DISTRIB` | `NR_COTST_DISTRIB` | inteiro | Número de clientes cotistas de Distribuidores do Fundo | quantidade | todo |
| `NR_COTST_OUTRO` | `NR_COTST_OUTRO` | inteiro | Número de clientes cotistas de outros tipos não relacionados | quantidade | todo |
| `PR_PL_COTST_PF_PB` | `PR_PL_COTST_PF_PB` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Pessoa Física Private Banking | percentual (%) | todo |
| `PR_PL_COTST_PF_VAREJO` | `PR_PL_COTST_PF_VAREJO` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Pessoa Física Varejo | percentual (%) | todo |
| `PR_PL_COTST_PJ_NAO_FINANC_PB` | `PR_PL_COTST_PJ_NAO_FINANC_PB` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Pessoa Jurídica Não-Financeira Private Banking | percentual (%) | todo |
| `PR_PL_COTST_PJ_NAO_FINANC_VAREJO` | `PR_PL_COTST_PJ_NAO_FINANC_VAREJO` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Pessoa Jurídica Não-Financeira Varejo | percentual (%) | todo |
| `PR_PL_COTST_BANCO` | `PR_PL_COTST_BANCO` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Banco Comercial | percentual (%) | todo |
| `PR_PL_COTST_CORRETORA_DISTRIB` | `PR_PL_COTST_CORRETORA_DISTRIB` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Corretora ou Distribuidora | percentual (%) | todo |
| `PR_PL_COTST_PJ_FINANC` | `PR_PL_COTST_PJ_FINANC` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Outras Pessoas Jurídicas Financeiras | percentual (%) | todo |
| `PR_PL_COTST_INVNR` | `PR_PL_COTST_INVNR` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Investidores Não Residentes | percentual (%) | todo |
| `PR_PL_COTST_EAPC` | `PR_PL_COTST_EAPC` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Entidade Aberta de Previdência Complementar | percentual (%) | todo |
| `PR_PL_COTST_EFPC` | `PR_PL_COTST_EFPC` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Entidade Fechada de Previdência Complementar | percentual (%) | todo |
| `PR_PL_COTST_RPPS` | `PR_PL_COTST_RPPS` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Regime Próprio de Previdência dos Servidores Públicos | percentual (%) | todo |
| `PR_PL_COTST_SEGUR` | `PR_PL_COTST_SEGUR` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Sociedade Seguradora ou Resseguradora | percentual (%) | todo |
| `PR_PL_COTST_CAPITALIZ` | `PR_PL_COTST_CAPITALIZ` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Sociedade de Capitalização e de Arrendamento Mercantil | percentual (%) | todo |
| `PR_PL_COTST_FI_CLUBE` | `PR_PL_COTST_FI_CLUBE` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas do tipo Fundos e Clubes de Investimento | percentual (%) | todo |
| `PR_PL_COTST_DISTRIB` | `PR_PL_COTST_DISTRIB` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas de Distribuidores do Fundo | percentual (%) | todo |
| `PR_PL_COTST_OUTRO` | `PR_PL_COTST_OUTRO` | decimal | Percentual do Patrimônio Líquido do fundo detido por clientes cotistas de outros tipos não relacionados | percentual (%) | todo |
| `VOTO_ADMIN_ASSEMB` | `VOTO_ADMIN_ASSEMB` | texto | Resumo do teor dos votos proferidos pelo administrador ou por seus representantes, nas assembleias gerais e especiais das companhias nas quais o fundo detenha participação | — | todo |
| `JUSTIF_VOTO_ADMIN_ASSEMB` | `JUSTIF_VOTO_ADMIN_ASSEMB` | texto | Justificativa teor dos votos proferidos pelo administrador ou por seus representantes, ou as razões sumárias para a sua abstenção ou não comparecimento à assembleia geral | — | todo |
| `PR_VAR_CARTEIRA` | `PR_VAR_CARTEIRA` | decimal | VAR (Valor em Risco) da carteira, calculado para 21 dias úteis e 95% de confiança  (em % do PL) | percentual (%) | todo |
| `MOD_VAR` | `MOD_VAR` | texto | Classe de modelos utilizada para o cálculo do VAR (Valor em Risco) | — | todo |
| `PRAZO_CARTEIRA_TITULO` | `PRAZO_CARTEIRA_TITULO` | decimal | Prazo médio em meses da carteira de títulos do fundo, no último dia útil do mês de referência (em meses e de acordo com a metodologia regulamentada pela SRF) | meses | todo |
| `DELIB_ASSEMB` | `DELIB_ASSEMB` | texto | Resumo das principais deliberações aprovadas em assembleia geral de cotistas | — | todo |
| `VL_CONTRATO_COMPRA_DOLAR` | `VL_CONTRATO_COMPRA_DOLAR` | decimal | Valor total dos contratos de compra de US$ liquidados no mês | moeda (o dicionário não informa a moeda; a descrição fala em US$) | todo |
| `VL_CONTRATO_VENDA_DOLAR` | `VL_CONTRATO_VENDA_DOLAR` | decimal | Valor total dos contratos de venda de US$ liquidados no mês | moeda (o dicionário não informa a moeda; a descrição fala em US$) | todo |
| `PR_VARIACAO_DIARIA_COTA` | `PR_VARIACAO_DIARIA_COTA` | decimal | Variação diária percentual esperada para o valor da cota do fundo no cenário escolhido | percentual (%) | todo |
| `FPR` | `FPR` | texto | Fator primitivo de risco (IBOVESPA, JUROS-PRE, CUPOM CAMBIAL, DOLAR, Outros) | — | todo |
| `CENARIO_FPR_IBOVESPA` | `CENARIO_FPR_IBOVESPA` | texto | Cenário utilizado (Fator primitivo de risco IBOVESPA) | — | todo |
| `CENARIO_FPR_JUROS` | `CENARIO_FPR_JUROS` | texto | Cenário utilizado (Fator primitivo de risco JUROS) | — | todo |
| `CENARIO_FPR_CUPOM` | `CENARIO_FPR_CUPOM` | texto | Cenário utilizado (Fator primitivo de risco CUPOM CAMBIAL) | — | todo |
| `CENARIO_FPR_DOLAR` | `CENARIO_FPR_DOLAR` | texto | Cenário utilizado (Fator primitivo de risco DOLAR) | — | todo |
| `CENARIO_FPR_OUTRO` | `CENARIO_FPR_OUTRO` | texto | Cenário utilizado (Fator primitivo de risco Outros) | — | todo |
| `PR_VARIACAO_DIARIA_COTA_ESTRESSE` | `PR_VARIACAO_DIARIA_COTA_ESTRESSE` | decimal | Variação diária percentual esperada para o valor da cota do fundo no pior cenário de estresse definido pelo seu administrador | percentual (%) | todo |
| `PR_VARIACAO_DIARIA_PL_TAXA_ANUAL` | `PR_VARIACAO_DIARIA_PL_TAXA_ANUAL` | decimal | Variação diária percentual esperada para o patrimônio do fundo caso ocorra uma variação negativa de 1% na taxa anual de juros | percentual (%) | todo |
| `PR_VARIACAO_DIARIA_PL_TAXA_CAMBIO` | `PR_VARIACAO_DIARIA_PL_TAXA_CAMBIO` | decimal | Variação diária percentual esperada para o patrimônio do fundo caso ocorra uma variação negativa de 1% na taxa de cambio (US$/Real) | percentual (%) | todo |
| `PR_VARIACAO_DIARIA_PL_IBOVESPA` | `PR_VARIACAO_DIARIA_PL_IBOVESPA` | decimal | Variação diária percentual esperada para o patrimônio do fundo caso ocorra uma variação negativa de 1% no preço das ações (IBOVESPA) | percentual (%) | todo |
| `FATOR_RISCO_OUTRO` | `FATOR_RISCO_OUTRO` | texto | Fator de risco dos outros tipos de fatores que não sejam juros, câmbio ou bolsa | — | todo |
| `PR_VARIACAO_DIARIA_OUTRO` | `PR_VARIACAO_DIARIA_OUTRO` | decimal | Variação diária percentual esperada para o patrimônio do fundo caso ocorra uma variação negativa de 1% no principal fator de risco a que o fundo está exposto, caso não seja juros, câmbio ou bolsa | percentual (%) | todo |
| `PR_COLATERAL_DERIV` | `PR_COLATERAL_DERIV` | decimal | Valor do Colateral depositado como garantia dos contratos derivativos de balcão mantidos pelo fundo (em % do PL) | percentual (%) | todo |
| `FATOR_RISCO_NOCIONAL` | `FATOR_RISCO_NOCIONAL` | texto | Fator de risco nocional (IBOVESPA, JUROS-PRE, CUPOM CAMBIAL, DOLAR, Outros) | — | todo |
| `VL_FATOR_RISCO_NOCIONAL_LONG_IBOVESPA` | `VL_FATOR_RISCO_NOCIONAL_LONG_IBOVESPA` | decimal | Valor do fator de risco nocional Long (Fator de risco nocional IBOVESPA) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_LONG_JUROS` | `VL_FATOR_RISCO_NOCIONAL_LONG_JUROS` | decimal | Valor do fator de risco nocional Long (Fator de risco nocional JUROS) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_LONG_CUPOM` | `VL_FATOR_RISCO_NOCIONAL_LONG_CUPOM` | decimal | Valor do fator de risco nocional Long (Fator de risco nocional CUPOM CAMBIAL) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_LONG_DOLAR` | `VL_FATOR_RISCO_NOCIONAL_LONG_DOLAR` | decimal | Valor do fator de risco nocional Long (Fator de risco nocional DOLAR) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_LONG_OUTRO` | `VL_FATOR_RISCO_NOCIONAL_LONG_OUTRO` | decimal | Valor do fator de risco nocional Long (Fator de risco nocional Outros) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_SHORT_IBOVESPA` | `VL_FATOR_RISCO_NOCIONAL_SHORT_IBOVESPA` | decimal | Valor do fator de risco nocional Short (Fator de risco nocional IBOVESPA) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_SHORT_JUROS` | `VL_FATOR_RISCO_NOCIONAL_SHORT_JUROS` | decimal | Valor do fator de risco nocional Short (Fator de risco nocional JUROS) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_SHORT_CUPOM` | `VL_FATOR_RISCO_NOCIONAL_SHORT_CUPOM` | decimal | Valor do fator de risco nocional Short (Fator de risco nocional CUPOM CAMBIAL) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_SHORT_DOLAR` | `VL_FATOR_RISCO_NOCIONAL_SHORT_DOLAR` | decimal | Valor do fator de risco nocional Short (Fator de risco nocional DOLAR) | moeda (R$) | todo |
| `VL_FATOR_RISCO_NOCIONAL_SHORT_OUTRO` | `VL_FATOR_RISCO_NOCIONAL_SHORT_OUTRO` | decimal | Valor do fator de risco nocional Short (Fator de risco nocional Outros) | moeda (R$) | todo |
| `PF_PJ_COMITENTE_1` | `PF_PJ_COMITENTE_1` | texto | Tipo de pessoa do comitente | — | todo |
| `CPF_CNPJ_COMITENTE_1` | `CPF_CNPJ_COMITENTE_1` | texto | CNPJ do comitente | — | todo |
| `COMITENTE_LIGADO_1` | `COMITENTE_LIGADO_1` | texto | Indica se o comitente é parte relacionada ao administrador ou gestor do fundo | S/N | todo |
| `PR_COMITENTE_1` | `PR_COMITENTE_1` | decimal | Valor da parte do comitente (em % do PL) | percentual (%) | todo |
| `PF_PJ_COMITENTE_2` | `PF_PJ_COMITENTE_2` | texto | Tipo de pessoa do comitente | — | todo |
| `CPF_CNPJ_COMITENTE_2` | `CPF_CNPJ_COMITENTE_2` | texto | CNPJ do comitente | — | todo |
| `COMITENTE_LIGADO_2` | `COMITENTE_LIGADO_2` | texto | Indica se o comitente é parte relacionada ao administrador ou gestor do fundo | S/N | todo |
| `PR_COMITENTE_2` | `PR_COMITENTE_2` | decimal | Valor da parte do comitente (em % do PL) | percentual (%) | todo |
| `PF_PJ_COMITENTE_3` | `PF_PJ_COMITENTE_3` | texto | Tipo de pessoa do comitente | — | todo |
| `CPF_CNPJ_COMITENTE_3` | `CPF_CNPJ_COMITENTE_3` | texto | CNPJ do comitente | — | todo |
| `COMITENTE_LIGADO_3` | `COMITENTE_LIGADO_3` | texto | Indica se o comitente é parte relacionada ao administrador ou gestor do fundo | S/N | todo |
| `PR_COMITENTE_3` | `PR_COMITENTE_3` | decimal | Valor da parte do comitente (em % do PL) | percentual (%) | todo |
| `PR_ATIVO_EMISSOR_LIGADO` | `PR_ATIVO_EMISSOR_LIGADO` | decimal | Valor total dos ativos de emissão de partes relacionadas em estoque (em % do PL) | percentual (%) | todo |
| `PF_PJ_EMISSOR_1` | `PF_PJ_EMISSOR_1` | texto | Tipo de pessoa do emissor | — | todo |
| `CPF_CNPJ_EMISSOR_1` | `CPF_CNPJ_EMISSOR_1` | texto | CNPJ do emissor | — | todo |
| `EMISSOR_LIGADO_1` | `EMISSOR_LIGADO_1` | texto | Indica se o emissor é parte relacionada ao administrador ou gestor do fundo | S/N | todo |
| `PR_EMISSOR_1` | `PR_EMISSOR_1` | decimal | Valor da parte do emissor (em % do PL) | percentual (%) | todo |
| `PF_PJ_EMISSOR_2` | `PF_PJ_EMISSOR_2` | texto | Tipo de pessoa do emissor | — | todo |
| `CPF_CNPJ_EMISSOR_2` | `CPF_CNPJ_EMISSOR_2` | texto | CNPJ do emissor | — | todo |
| `EMISSOR_LIGADO_2` | `EMISSOR_LIGADO_2` | texto | Indica se o emissor é parte relacionada ao administrador ou gestor do fundo | S/N | todo |
| `PR_EMISSOR_2` | `PR_EMISSOR_2` | decimal | Valor da parte do emissor (em % do PL) | percentual (%) | todo |
| `PF_PJ_EMISSOR_3` | `PF_PJ_EMISSOR_3` | texto | Tipo de pessoa do emissor | — | todo |
| `CPF_CNPJ_EMISSOR_3` | `CPF_CNPJ_EMISSOR_3` | texto | CNPJ do emissor | — | todo |
| `EMISSOR_LIGADO_3` | `EMISSOR_LIGADO_3` | texto | Indica se o emissor é parte relacionada ao administrador ou gestor do fundo | S/N | todo |
| `PR_EMISSOR_3` | `PR_EMISSOR_3` | decimal | Valor da parte do emissor (em % do PL) | percentual (%) | todo |
| `PR_ATIVO_CRED_PRIV` | `PR_ATIVO_CRED_PRIV` | decimal | Valor do total de ativos de crédito privado em estoque (em % do PL) | percentual (%) | todo |
| `VEDAC_TAXA_PERFM` | `VEDAC_TAXA_PERFM` | texto | Indica se é vedada no regulamento a cobrança de taxa de performance quando o valor da cota do fundo for inferior ao seu valor por ocasião da última cobrança efetuada | S/N | todo |
| `DT_COTA_TAXA_PERFM` | `DT_COTA_TAXA_PERFM` | texto | Data da cota de fundo quando da última cobrança de taxa de performance efetuada | — | todo |
| `VL_COTA_TAXA_PERFM` | `VL_COTA_TAXA_PERFM` | decimal | Valor da cota de fundo quando da última cobrança de taxa de performance efetuada | percentual (%) | todo |
| `VL_DIREITO_DISTRIB` | `VL_DIREITO_DISTRIB` | decimal | Montante distribuído diretamente aos clientes, referente a direitos a dividendos, juros sobre capital próprio ou outros rendimentos | moeda (R$) | todo |
| `NR_COTST_ENTID_PREVID_COMPL` | `NR_COTST_ENTID_PREVID_COMPL` | texto | Número de cotistas de entidade de previdência complementar | — | todo |
| `PR_COTST_ENTID_PREVID_COMPL` | `PR_COTST_ENTID_PREVID_COMPL` | texto | Percentual de Cotistas de Entidade de Previdência Complementar | — | todo |
| `PR_PATRIM_LIQ_MAIOR_COTST` | `PR_PATRIM_LIQ_MAIOR_COTST` | decimal | Percentual patrimônio líquido do maior cotista | percentual (%) | todo |
| `NR_DIA_CINQU_PERC` | `NR_DIA_CINQU_PERC` | texto | Número de dias cinquenta percentual | — | todo |
| `NR_DIA_CEM_PERC` | `NR_DIA_CEM_PERC` | texto | Número de dias cem percentual | — | todo |
| `ST_LIQDEZ` | `ST_LIQDEZ` | texto | Indica liquidez | S/N | todo |
| `PR_PATRIM_LIQ_CONVTD_CAIXA` | `PR_PATRIM_LIQ_CONVTD_CAIXA` | texto | Percentual patrimônio líquido convertido em caixa | — | todo |
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe | — | 2026-10 |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe | — | 2026-10 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fi-perfil`, particionado por `ano`, `mes`; um arquivo Parquet por arquivo CSV de origem.
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Troca de coluna de identificação em 2023-12.** Até 2023-11 o CNPJ está em `CNPJ_FUNDO`; de 2023-12 em diante, em `CNPJ_FUNDO_CLASSE`, com `TP_FUNDO_CLASSE`. Coalesça as duas colunas ao ler vários meses.
- **Colunas quase vazias.** `NR_COTST_ENTID_PREVID_COMPL`, `PR_COTST_ENTID_PREVID_COMPL`, `NR_DIA_CINQU_PERC`, `NR_DIA_CEM_PERC` e `ST_LIQDEZ` têm mais de 98% de nulos no arquivo de 2026-10; as colunas `NR_COTST_EAPC` e `NR_COTST_EFPC` (previdência aberta e fechada) existem desde 2019-01.
- **Comitentes e emissores.** `CPF_CNPJ_COMITENTE_*` e `CPF_CNPJ_EMISSOR_*` trazem CNPJ com máscara; há poucos CPF de pessoa física misturados (uma linha com 11 dígitos em cada arquivo amostrado). O fetcher e o lake preservam o que a fonte publica.

## Exemplos

Número médio de cotistas pessoa física (varejo e private) por tipo de fundo em 2026-10.

```python
import duckdb

duckdb.sql("""
    SELECT TP_FUNDO_CLASSE, count(*) AS classes, round(avg(NR_COTST_PF_VAREJO + NR_COTST_PF_PB)) AS cotistas_pf_medio
    FROM read_parquet('lake/cvm/fi-perfil/ano=2026/mes=10/*.parquet')
    GROUP BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-doc-perfil_mensal
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/DOC/PERFIL_MENSAL/
