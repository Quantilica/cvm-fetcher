---
dataset:
  id: fii-inf-mensal
  fonte: cvm
  titulo: "FII: Documentos: Informe Mensal Estruturado (CVM)"
  resumo: "Informe mensal estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, cotistas e ativos e passivos por fundo e competência, em três tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fii-doc-inf_mensal
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_mensal"
  periodicidade: "anual (um arquivo por ano, com um informe por mês); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2016, fim: em-curso}
  unidade: "o informe mensal de um FII em uma competência e versão"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (competência, `Data_Referencia`), em arquivos anuais"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 115}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    Total_Necessidades_Liquidez: "moeda (R$)"
    Disponibilidades: "moeda (R$)"
    Titulos_Publicos: "moeda (R$)"
    Titulos_Privados: "moeda (R$)"
    Fundos_Renda_Fixa: "moeda (R$)"
    Total_Investido: "moeda (R$)"
    Direitos_Bens_Imoveis: "moeda (R$)"
    Terrenos: "moeda (R$)"
    Imoveis_Renda_Acabados: "moeda (R$)"
    Imoveis_Renda_Construcao: "moeda (R$)"
    Imoveis_Venda_Acabados: "moeda (R$)"
    Imoveis_Venda_Construcao: "moeda (R$)"
    Outros_Direitos_Reais: "moeda (R$)"
    Acoes: "moeda (R$)"
    Debentures: "moeda (R$)"
    Bonus_Subscricao: "moeda (R$)"
    Certificados_Deposito_Valores_Mobiliarios: "moeda (R$)"
    Cedulas_Debentures: "moeda (R$)"
    Fundo_Acoes: "moeda (R$)"
    FIP: "moeda (R$)"
    FII: "moeda (R$)"
    FDIC: "moeda (R$)"
    Outras_Cotas_FI: "moeda (R$)"
    Notas_Promissorias: "moeda (R$)"
    Acoes_Sociedades_Atividades_FII: "moeda (R$)"
    Cotas_Sociedades_Atividades_FII: "moeda (R$)"
    CEPAC: "moeda (R$)"
    CRI: "moeda (R$)"
    Letras_Hipotecarias: "moeda (R$)"
    LCI: "moeda (R$)"
    LIG: "moeda (R$)"
    Outros_Valores_Mobliarios: "moeda (R$)"
    Valores_Receber: "moeda (R$)"
    Contas_Receber_Aluguel: "moeda (R$)"
    Contas_Receber_Venda_Imoveis: "moeda (R$)"
    Outros_Valores_Receber: "moeda (R$)"
    Rendimentos_Distribuir: "moeda (R$)"
    Taxa_Administracao_Pagar: "moeda (R$)"
    Taxa_Performance_Pagar: "moeda (R$)"
    Obrigacoes_Aquisicao_Imoveis: "moeda (R$)"
    Adiantamento_Venda_Imoveis: "moeda (R$)"
    Adiantamento_Alugueis: "moeda (R$)"
    Obrigacoes_Securitizacao_Recebiveis: "moeda (R$)"
    Instrumentos_Financeiros_Derivativos: "moeda (R$)"
    Provisoes_Contigencias: "moeda (R$)"
    Outros_Valores_Pagar: "moeda (R$)"
    Total_Passivo: "moeda (R$)"
    Total_Numero_Cotistas: "quantidade"
    Numero_Cotistas_Pessoa_Fisica: "quantidade"
    Numero_Cotistas_Pessoa_Juridica_Nao_Financeira: "quantidade"
    Numero_Cotistas_Banco_Comercial: "quantidade"
    Numero_Cotistas_Corretora_Distribuidora: "quantidade"
    Numero_Cotistas_Outras_Pessoas_Juridicas_Financeira: "quantidade"
    Numero_Cotistas_Investidores_Nao_Residentes: "quantidade"
    Numero_Cotistas_Entidade_Aberta_Previdencia_Complementar: "quantidade"
    Numero_Cotistas_Entidade_Fechada_Previdência_Complementar: "quantidade"
    Numero_Cotistas_Regime_Proprio_Previdencia_Servidores_Publicos: "quantidade"
    Numero_Cotistas_Sociedade_Seguradora_Resseguradora: "quantidade"
    Numero_Cotistas_Sociedade_Capitalizacao_Arrendamento_Mercantil: "quantidade"
    Numero_Cotistas_FII: "quantidade"
    Numero_Cotistas_Outros_Fundos: "quantidade"
    Numero_Cotistas_Distribuidores_Fundo: "quantidade"
    Numero_Cotistas_Outros_Tipos: "quantidade"
    Valor_Ativo: "moeda (R$)"
    Patrimonio_Liquido: "moeda (R$)"
    Cotas_Emitidas: "quantidade (cotas)"
    Valor_Patrimonial_Cotas: "moeda (R$)"
    Percentual_Despesas_Taxa_Administracao: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Despesas_Agente_Custodiante: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Rentabilidade_Efetiva_Mes: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Rentabilidade_Patrimonial_Mes: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Dividend_Yield_Mes: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Amortizacao_Cotas_Mes: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Quantidade_Cotas_Emitidas: "quantidade"
    CRI_CRA: "moeda (R$)"
    LCI_LCA: "moeda (R$)"
  dados_pessoais:
    - {coluna: Logradouro, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Complemento, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Bairro, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone1, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone2, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone3, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Email, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# FII: Documentos: Informe Mensal Estruturado

## Resumo

Informe mensal estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, cotistas e ativos e passivos por fundo e competência, em três tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fii-inf-mensal` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fii-doc-inf_mensal |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_mensal |
| Periodicidade | anual (um arquivo por ano, com um informe por mês); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2016 a em-curso |
| Unidade (uma linha) | o informe mensal de um FII em uma competência e versão |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (competência, `Data_Referencia`), em arquivos anuais |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 115 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `Total_Necessidades_Liquidez`: moeda (R$); `Disponibilidades`: moeda (R$); `Titulos_Publicos`: moeda (R$); `Titulos_Privados`: moeda (R$); `Fundos_Renda_Fixa`: moeda (R$); `Total_Investido`: moeda (R$); `Direitos_Bens_Imoveis`: moeda (R$); `Terrenos`: moeda (R$); `Imoveis_Renda_Acabados`: moeda (R$); `Imoveis_Renda_Construcao`: moeda (R$); `Imoveis_Venda_Acabados`: moeda (R$); `Imoveis_Venda_Construcao`: moeda (R$); `Outros_Direitos_Reais`: moeda (R$); `Acoes`: moeda (R$); `Debentures`: moeda (R$); `Bonus_Subscricao`: moeda (R$); `Certificados_Deposito_Valores_Mobiliarios`: moeda (R$); `Cedulas_Debentures`: moeda (R$); `Fundo_Acoes`: moeda (R$); `FIP`: moeda (R$); `FII`: moeda (R$); `FDIC`: moeda (R$); `Outras_Cotas_FI`: moeda (R$); `Notas_Promissorias`: moeda (R$); `Acoes_Sociedades_Atividades_FII`: moeda (R$); `Cotas_Sociedades_Atividades_FII`: moeda (R$); `CEPAC`: moeda (R$); `CRI`: moeda (R$); `Letras_Hipotecarias`: moeda (R$); `LCI`: moeda (R$); `LIG`: moeda (R$); `Outros_Valores_Mobliarios`: moeda (R$); `Valores_Receber`: moeda (R$); `Contas_Receber_Aluguel`: moeda (R$); `Contas_Receber_Venda_Imoveis`: moeda (R$); `Outros_Valores_Receber`: moeda (R$); `Rendimentos_Distribuir`: moeda (R$); `Taxa_Administracao_Pagar`: moeda (R$); `Taxa_Performance_Pagar`: moeda (R$); `Obrigacoes_Aquisicao_Imoveis`: moeda (R$); `Adiantamento_Venda_Imoveis`: moeda (R$); `Adiantamento_Alugueis`: moeda (R$); `Obrigacoes_Securitizacao_Recebiveis`: moeda (R$); `Instrumentos_Financeiros_Derivativos`: moeda (R$); `Provisoes_Contigencias`: moeda (R$); `Outros_Valores_Pagar`: moeda (R$); `Total_Passivo`: moeda (R$); `Total_Numero_Cotistas`: quantidade; `Numero_Cotistas_Pessoa_Fisica`: quantidade; `Numero_Cotistas_Pessoa_Juridica_Nao_Financeira`: quantidade; `Numero_Cotistas_Banco_Comercial`: quantidade; `Numero_Cotistas_Corretora_Distribuidora`: quantidade; `Numero_Cotistas_Outras_Pessoas_Juridicas_Financeira`: quantidade; `Numero_Cotistas_Investidores_Nao_Residentes`: quantidade; `Numero_Cotistas_Entidade_Aberta_Previdencia_Complementar`: quantidade; `Numero_Cotistas_Entidade_Fechada_Previdência_Complementar`: quantidade; `Numero_Cotistas_Regime_Proprio_Previdencia_Servidores_Publicos`: quantidade; `Numero_Cotistas_Sociedade_Seguradora_Resseguradora`: quantidade; `Numero_Cotistas_Sociedade_Capitalizacao_Arrendamento_Mercantil`: quantidade; `Numero_Cotistas_FII`: quantidade; `Numero_Cotistas_Outros_Fundos`: quantidade; `Numero_Cotistas_Distribuidores_Fundo`: quantidade; `Numero_Cotistas_Outros_Tipos`: quantidade; `Valor_Ativo`: moeda (R$); `Patrimonio_Liquido`: moeda (R$); `Cotas_Emitidas`: quantidade (cotas); `Valor_Patrimonial_Cotas`: moeda (R$); `Percentual_Despesas_Taxa_Administracao`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Despesas_Agente_Custodiante`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Rentabilidade_Efetiva_Mes`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Rentabilidade_Patrimonial_Mes`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Dividend_Yield_Mes`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Amortizacao_Cotas_Mes`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Quantidade_Cotas_Emitidas`: quantidade; `CRI_CRA`: moeda (R$); `LCI_LCA`: moeda (R$) |
| Dados pessoais | `Logradouro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Complemento` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Bairro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Email` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fii-doc-inf_mensal). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/`.
- O catálogo do fetcher lista 11 arquivo(s): de `inf_mensal_fii_2016.zip` a `inf_mensal_fii_2026.zip`.
- Em 2026-11-16 conferimos 9 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2016, 2021, 2026).
- No bruto, o arquivo fica em `fii-inf-mensal/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe mensal de um FII em uma competência e versão.
- Particionado por `ano`; o catálogo cobre 2016 a 2026, e conferimos as amostras 2016, 2021, 2026.
- O arquivo de 2026 tem 13.103 linhas em cada tabela, 1.446 fundos e competências de 2026-01 a 2026-10 (`Data_Referencia` de 2026-01-01 a 2026-10-01). Os arquivos de 2016 e 2021 têm 368 e 7.568 linhas.
- Este dataset reúne 3 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `inf_mensal_fii_ativo_passivo` | 53 | 13.103 | não determinada | ativos e passivos do fundo (disponibilidades, títulos, cotas de fundos, imóveis e obrigações) |
| `inf_mensal_fii_complemento` | 31 | 13.103 | não determinada | cotistas por tipo e demais informações complementares |
| `inf_mensal_fii_geral` | 39 | 13.103 | não determinada | dados gerais do fundo e do administrador, por competência |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Fundo` | `CNPJ_Fundo` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_Fundo_Classe`) | — | 2016 |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Total_Necessidades_Liquidez` | `Total_Necessidades_Liquidez` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total necessidades liquidez (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Disponibilidades` | `Disponibilidades` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: disponibilidades (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Titulos_Publicos` | `Titulos_Publicos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos publicos (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Titulos_Privados` | `Titulos_Privados` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos privados (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Fundos_Renda_Fixa` | `Fundos_Renda_Fixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: fundos renda fixa (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Total_Investido` | `Total_Investido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total investido (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Direitos_Bens_Imoveis` | `Direitos_Bens_Imoveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos bens imoveis (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Terrenos` | `Terrenos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: terrenos (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Imoveis_Renda_Acabados` | `Imoveis_Renda_Acabados` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: imoveis renda acabados (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Imoveis_Renda_Construcao` | `Imoveis_Renda_Construcao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: imoveis renda construcao (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Imoveis_Venda_Acabados` | `Imoveis_Venda_Acabados` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: imoveis venda acabados (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Imoveis_Venda_Construcao` | `Imoveis_Venda_Construcao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: imoveis venda construcao (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Direitos_Reais` | `Outros_Direitos_Reais` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros direitos reais (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Acoes` | `Acoes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: acoes (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Debentures` | `Debentures` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: debentures (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Bonus_Subscricao` | `Bonus_Subscricao` | decimal / inteiro | Bônus de Subscrição, seus cupons, direitos, recibos de subscrição e certificados de desdobramentos (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Certificados_Deposito_Valores_Mobiliarios` | `Certificados_Deposito_Valores_Mobiliarios` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: certificados deposito valores mobiliarios (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Cedulas_Debentures` | `Cedulas_Debentures` | decimal / inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cedulas debentures (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Fundo_Acoes` | `Fundo_Acoes` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: fundo acoes (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `FIP` | `FIP` | decimal | Fundo de Investimento em Participações (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `FII` | `FII` | decimal | Fundo de Investimento Imobiliário (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `FDIC` | `FDIC` | decimal | Fundo de Investimento em Direitos Creditórios (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Outras_Cotas_FI` | `Outras_Cotas_FI` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras cotas fi (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Notas_Promissorias` | `Notas_Promissorias` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: notas promissorias (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Acoes_Sociedades_Atividades_FII` | `Acoes_Sociedades_Atividades_FII` | decimal | Ações de Sociedades cujo único propósito se enquadra entre as atividades permitidas aos FII (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Cotas_Sociedades_Atividades_FII` | `Cotas_Sociedades_Atividades_FII` | decimal | Cotas de Sociedades que se enquadre entre as atividades permitidas aos FII (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `CEPAC` | `CEPAC` | decimal | Certificados de Potencial Adicional de Construção (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `CRI` | `CRI` | decimal / texto | Certificado de Recebíveis Imobiliários (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Letras_Hipotecarias` | `Letras_Hipotecarias` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: letras hipotecarias (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `LCI` | `LCI` | decimal / texto | Letras de Crédito Imobiliário (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `LIG` | `LIG` | inteiro | Letra Imobiliária Garantida (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Valores_Mobliarios` | `Outros_Valores_Mobliarios` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros valores mobliarios (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Valores_Receber` | `Valores_Receber` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valores receber (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Contas_Receber_Aluguel` | `Contas_Receber_Aluguel` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: contas receber aluguel (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Contas_Receber_Venda_Imoveis` | `Contas_Receber_Venda_Imoveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: contas receber venda imoveis (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Valores_Receber` | `Outros_Valores_Receber` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros valores receber (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Rendimentos_Distribuir` | `Rendimentos_Distribuir` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimentos distribuir (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Taxa_Administracao_Pagar` | `Taxa_Administracao_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa administracao pagar (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Taxa_Performance_Pagar` | `Taxa_Performance_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa performance pagar (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Obrigacoes_Aquisicao_Imoveis` | `Obrigacoes_Aquisicao_Imoveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: obrigacoes aquisicao imoveis (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Adiantamento_Venda_Imoveis` | `Adiantamento_Venda_Imoveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: adiantamento venda imoveis (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Adiantamento_Alugueis` | `Adiantamento_Alugueis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: adiantamento alugueis (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Obrigacoes_Securitizacao_Recebiveis` | `Obrigacoes_Securitizacao_Recebiveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: obrigacoes securitizacao recebiveis (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Instrumentos_Financeiros_Derivativos` | `Instrumentos_Financeiros_Derivativos` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: instrumentos financeiros derivativos (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Provisoes_Contigencias` | `Provisoes_Contigencias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: provisoes contigencias (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Valores_Pagar` | `Outros_Valores_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros valores pagar (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Total_Passivo` | `Total_Passivo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total passivo (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | todo |
| `Data_Informacao_Numero_Cotistas` | `Data_Informacao_Numero_Cotistas` | texto | Data da Informação sobre detalhamento do número de cotistas (só em: `inf_mensal_fii_complemento`) | — | todo |
| `Total_Numero_Cotistas` | `Total_Numero_Cotistas` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: total numero cotistas (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Pessoa_Fisica` | `Numero_Cotistas_Pessoa_Fisica` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas pessoa fisica (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Pessoa_Juridica_Nao_Financeira` | `Numero_Cotistas_Pessoa_Juridica_Nao_Financeira` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas pessoa juridica nao financeira (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Banco_Comercial` | `Numero_Cotistas_Banco_Comercial` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas banco comercial (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Corretora_Distribuidora` | `Numero_Cotistas_Corretora_Distribuidora` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas corretora distribuidora (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Outras_Pessoas_Juridicas_Financeira` | `Numero_Cotistas_Outras_Pessoas_Juridicas_Financeira` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas outras pessoas juridicas financeira (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Investidores_Nao_Residentes` | `Numero_Cotistas_Investidores_Nao_Residentes` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas investidores nao residentes (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Entidade_Aberta_Previdencia_Complementar` | `Numero_Cotistas_Entidade_Aberta_Previdencia_Complementar` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas entidade aberta previdencia complementar (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Entidade_Fechada_Previdência_Complementar` | `Numero_Cotistas_Entidade_Fechada_Previdência_Complementar` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas entidade fechada previdência complementar (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Regime_Proprio_Previdencia_Servidores_Publicos` | `Numero_Cotistas_Regime_Proprio_Previdencia_Servidores_Publicos` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas regime proprio previdencia servidores publicos (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Sociedade_Seguradora_Resseguradora` | `Numero_Cotistas_Sociedade_Seguradora_Resseguradora` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas sociedade seguradora resseguradora (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Sociedade_Capitalizacao_Arrendamento_Mercantil` | `Numero_Cotistas_Sociedade_Capitalizacao_Arrendamento_Mercantil` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas sociedade capitalizacao arrendamento mercantil (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_FII` | `Numero_Cotistas_FII` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas fii (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Outros_Fundos` | `Numero_Cotistas_Outros_Fundos` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas outros fundos (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Distribuidores_Fundo` | `Numero_Cotistas_Distribuidores_Fundo` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas distribuidores fundo (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Numero_Cotistas_Outros_Tipos` | `Numero_Cotistas_Outros_Tipos` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas outros tipos (só em: `inf_mensal_fii_complemento`) | quantidade | todo |
| `Valor_Ativo` | `Valor_Ativo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor ativo (só em: `inf_mensal_fii_complemento`) | moeda (R$) | todo |
| `Patrimonio_Liquido` | `Patrimonio_Liquido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: patrimonio liquido (só em: `inf_mensal_fii_complemento`) | moeda (R$) | todo |
| `Cotas_Emitidas` | `Cotas_Emitidas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cotas emitidas (só em: `inf_mensal_fii_complemento`) | quantidade (cotas) | todo |
| `Valor_Patrimonial_Cotas` | `Valor_Patrimonial_Cotas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor patrimonial cotas (só em: `inf_mensal_fii_complemento`) | moeda (R$) | todo |
| `Percentual_Despesas_Taxa_Administracao` | `Percentual_Despesas_Taxa_Administracao` | decimal | Percentual de despesas com a taxa de administração em relação ao patrimônio líquido do mês (só em: `inf_mensal_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Despesas_Agente_Custodiante` | `Percentual_Despesas_Agente_Custodiante` | decimal | Percentual de despesas com o agente custodiante em relação ao patrimônio líquido do mês (só em: `inf_mensal_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Rentabilidade_Efetiva_Mes` | `Percentual_Rentabilidade_Efetiva_Mes` | decimal | Percentual de Rentabilidade Efetiva Mensal (só em: `inf_mensal_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Rentabilidade_Patrimonial_Mes` | `Percentual_Rentabilidade_Patrimonial_Mes` | decimal | Percentual de Rentabilidade Patrimonial do Mês de Referência (só em: `inf_mensal_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Dividend_Yield_Mes` | `Percentual_Dividend_Yield_Mes` | decimal | Percentual de Dividend Yield do Mês de Referência (só em: `inf_mensal_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Amortizacao_Cotas_Mes` | `Percentual_Amortizacao_Cotas_Mes` | decimal | Percentual de amortizações de cotas do Mês de Referência (só em: `inf_mensal_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `inf_mensal_fii_geral`) | — | todo |
| `Nome_Fundo` | `Nome_Fundo` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Nome_Fundo_Classe`) (só em: `inf_mensal_fii_geral`) | — | 2016 |
| `Data_Funcionamento` | `Data_Funcionamento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data funcionamento (só em: `inf_mensal_fii_geral`) | — | todo |
| `Publico_Alvo` | `Publico_Alvo` | texto | Público-alvo (só em: `inf_mensal_fii_geral`) | — | todo |
| `Codigo_ISIN` | `Codigo_ISIN` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo isin (só em: `inf_mensal_fii_geral`) | — | todo |
| `Quantidade_Cotas_Emitidas` | `Quantidade_Cotas_Emitidas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade cotas emitidas (só em: `inf_mensal_fii_geral`) | quantidade | todo |
| `Fundo_Exclusivo` | `Fundo_Exclusivo` | texto | Indica se é fundo exclusivo (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Cotistas_Vinculo_Familiar` | `Cotistas_Vinculo_Familiar` | texto | Indica se os cotistas possuem vínculo familiar ou societário familiar (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Mandato` | `Mandato` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mandato (só em: `inf_mensal_fii_geral`) | — | todo |
| `Segmento_Atuacao` | `Segmento_Atuacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: segmento atuacao (só em: `inf_mensal_fii_geral`) | — | todo |
| `Tipo_Gestao` | `Tipo_Gestao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo gestao (só em: `inf_mensal_fii_geral`) | — | todo |
| `Prazo_Duracao` | `Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: prazo duracao (só em: `inf_mensal_fii_geral`) | — | todo |
| `Data_Prazo_Duracao` | `Data_Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data prazo duracao (só em: `inf_mensal_fii_geral`) | — | todo |
| `Encerramento_Exercicio_Social` | `Encerramento_Exercicio_Social` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: encerramento exercicio social (só em: `inf_mensal_fii_geral`) | — | todo |
| `Mercado_Negociacao_Bolsa` | `Mercado_Negociacao_Bolsa` | texto | Indica se o mercado de negociação das cotas é Bolsa (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Mercado_Negociacao_MBO` | `Mercado_Negociacao_MBO` | texto | Indica se o mercado de negociação das cotas é MBO (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Mercado_Negociacao_MB` | `Mercado_Negociacao_MB` | texto | Indica se o mercado de negociação das cotas é MB (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Entidade_Administradora_BVMF` | `Entidade_Administradora_BVMF` | texto | Indica se a entidade administradora de mercado organizado é BVMF (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Entidade_Administradora_CETIP` | `Entidade_Administradora_CETIP` | texto | Indica se a entidade administradora de mercado organizado é CETIP (só em: `inf_mensal_fii_geral`) | S/N | todo |
| `Nome_Administrador` | `Nome_Administrador` | texto | Nome do administrador (só em: `inf_mensal_fii_geral`) | — | todo |
| `CNPJ_Administrador` | `CNPJ_Administrador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj administrador (só em: `inf_mensal_fii_geral`) | — | todo |
| `Logradouro` | `Logradouro` | texto | Logradouro (só em: `inf_mensal_fii_geral`) | — | todo |
| `Numero` | `Numero` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: numero (só em: `inf_mensal_fii_geral`) | — | todo |
| `Complemento` | `Complemento` | texto | Complemento (só em: `inf_mensal_fii_geral`) | — | todo |
| `Bairro` | `Bairro` | texto | Bairro (só em: `inf_mensal_fii_geral`) | — | todo |
| `Cidade` | `Cidade` | texto | Cidade (só em: `inf_mensal_fii_geral`) | — | todo |
| `Estado` | `Estado` | texto | Estado (só em: `inf_mensal_fii_geral`) | — | todo |
| `CEP` | `CEP` | texto | CEP (só em: `inf_mensal_fii_geral`) | — | todo |
| `Telefone1` | `Telefone1` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone1 (só em: `inf_mensal_fii_geral`) | — | todo |
| `Telefone2` | `Telefone2` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone2 (só em: `inf_mensal_fii_geral`) | — | todo |
| `Telefone3` | `Telefone3` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone3 (só em: `inf_mensal_fii_geral`) | — | todo |
| `Site` | `Site` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: site (só em: `inf_mensal_fii_geral`) | — | todo |
| `Email` | `Email` | texto | Endereço de e-mail (só em: `inf_mensal_fii_geral`) | — | todo |
| `CNPJ_Fundo_Classe` | `CNPJ_Fundo_Classe` | texto | CNPJ do fundo/classe | — | 2021 a 2026 |
| `CRI_CRA` | `CRI_CRA` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cri cra (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | 2021 a 2026 |
| `LCI_LCA` | `LCI_LCA` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: lci lca (só em: `inf_mensal_fii_ativo_passivo`) | moeda (R$) | 2021 a 2026 |
| `Tipo_Fundo_Classe` | `Tipo_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo fundo classe (só em: `inf_mensal_fii_geral`) | — | 2021 a 2026 |
| `Nome_Fundo_Classe` | `Nome_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome fundo classe (só em: `inf_mensal_fii_geral`) | — | 2021 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fii-inf-mensal`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Várias versões por fundo e competência.** O arquivo traz cada reapresentação: em 2026, `Versao` vai de 1 a 6 em `inf_mensal_fii_geral` (12.251 linhas na versão 1 e 797 na 2). Para a posição vigente, escolha a maior `Versao` de cada `CNPJ_Fundo_Classe` e `Data_Referencia`.
- **Competência como primeiro dia do mês.** `Data_Referencia` vem como `AAAA-MM-01` (a competência de outubro é 2026-10-01), não como o último dia do mês.
- **CNPJ do administrador só com dígitos.** `CNPJ_Administrador` não traz máscara, enquanto `CNPJ_Fundo_Classe` traz; normalize antes de juntar.
- **Mudança de layout entre arquivos.** O arquivo de 2016 (não regravado) traz `CNPJ_Fundo` em vez de `CNPJ_Fundo_Classe`; `inf_mensal_fii_ativo_passivo` tem 50 colunas em 2016 e 52 em 2021 e 2026, e `inf_mensal_fii_geral` passa de 36 para 37. Coalesça as colunas ao ler vários anos.
- **Tipo inferido varia entre arquivos.** 11 coluna(s) (`Debentures`, `Bonus_Subscricao`, `Certificados_Deposito_Valores_Mobiliarios`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.
- **Linhas repetidas.** No arquivo mais recente convertido há linhas inteiramente repetidas em: `inf_mensal_fii_ativo_passivo` (2), `inf_mensal_fii_complemento` (2). Remova as duplicatas antes de contar ou somar.

## Exemplos

Fundos distintos informados por competência, com a última versão de cada uma.

```python
import duckdb

duckdb.sql("""
    SELECT Data_Referencia, count(DISTINCT CNPJ_Fundo_Classe) AS fundos
    FROM read_parquet('lake/cvm/fii-inf-mensal/ano=2026/*__inf_mensal_fii_geral_2026.parquet')
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_mensal
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/
