---
dataset:
  id: fii-inf-anual
  fonte: cvm
  titulo: "FII: Documentos: Informe Anual Estruturado (CVM)"
  resumo: "Informe anual estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, administração, prestadores de serviço, diretores, representantes de cotistas, distribuição de cotistas, ativos e processos, em 13 tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fii-doc-inf_anual
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_anual"
  periodicidade: "anual (um arquivo por ano); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2016, fim: em-curso}
  unidade: "o informe anual de um FII (nas tabelas gerais); um item do informe (diretor, representante, ativo, prestador, processo) nas demais"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (arquivo por ano de referência)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 177}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    Valor_Envolvido: "moeda (R$)"
    Valor: "moeda (R$)"
    Percentual_Valorizacao_Desvalorizacao: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Valor_Pago_Ano_Referencia: "moeda (R$)"
    Percentual_Patrimonio_Contabil: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Patrimonio_Valor_Mercado: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    CPF: "código ou número de identificação (sem unidade)"
    Quantidade_Cotas_FII_Detidas: "quantidade"
    Quantidade_Cotas_FII_Compradas: "quantidade"
    Quantidade_Cotas_FII_Vendidas: "quantidade"
    Numero_Cotistas_Faixa_Ate_5: "quantidade"
    Numero_Cotas_Detidas_Faixa_Ate_5: "quantidade"
    Percentual_Cotas_Detidas_Faixa_Ate_5: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_Ate_5: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_Ate_5: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_5a10: "quantidade"
    Numero_Cotas_Detidas_Faixa_5a10: "quantidade"
    Percentual_Cotas_Detidas_Faixa_5a10: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_5a10: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_5a10: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_10a15: "quantidade"
    Numero_Cotas_Detidas_Faixa_10a15: "quantidade"
    Percentual_Cotas_Detidas_Faixa_10a15: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_10a15: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_10a15: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_15a20: "quantidade"
    Numero_Cotas_Detidas_Faixa_15a20: "quantidade"
    Percentual_Cotas_Detidas_Faixa_15a20: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_15a20: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_15a20: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_20a30: "quantidade"
    Numero_Cotas_Detidas_Faixa_20a30: "quantidade"
    Percentual_Cotas_Detidas_Faixa_20a30: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_20a30: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_20a30: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_30a40: "quantidade"
    Numero_Cotas_Detidas_Faixa_30a40: "quantidade"
    Percentual_Cotas_Detidas_Faixa_30a40: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_30a40: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_30a40: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_40a50: "quantidade"
    Numero_Cotas_Detidas_Faixa_40a50: "quantidade"
    Percentual_Cotas_Detidas_Faixa_40a50: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_40a50: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_40a50: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Cotistas_Faixa_Acima_50: "quantidade"
    Numero_Cotas_Detidas_Faixa_Acima_50: "quantidade"
    Percentual_Cotas_Detidas_Faixa_Acima_50: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PF_Faixa_Acima_50: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Detido_PJ_Faixa_Acima_50: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Quantidade_Cotas_Emitidas: "quantidade"
    Valor_Causa: "moeda (R$)"
  dados_pessoais:
    - {coluna: Nome_Diretor_Responsavel, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: Nome_Diretor_Representante, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: Nome_Representante, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: Endereco_Gestor, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Gestor, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Custodiante, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Custodiante, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Auditor_Independente, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Auditor_Independente, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Formador_Mercado, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Formador_Mercado, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Distribuidor_Cotas, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Distribuidor_Cotas, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Consultor_Especializado, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Consultor_Especializado, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Empresa_Locacao, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone_Empresa_Locacao, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Fisico_Documentos_Assembleia_Geral, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco_Eletronico_Documentos_Assembleia_Geral, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Email, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Logradouro, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Complemento, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Bairro, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone1, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone2, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone3, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Endereco, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# FII: Documentos: Informe Anual Estruturado

## Resumo

Informe anual estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, administração, prestadores de serviço, diretores, representantes de cotistas, distribuição de cotistas, ativos e processos, em 13 tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fii-inf-anual` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fii-doc-inf_anual |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_anual |
| Periodicidade | anual (um arquivo por ano); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2016 a em-curso |
| Unidade (uma linha) | o informe anual de um FII (nas tabelas gerais); um item do informe (diretor, representante, ativo, prestador, processo) nas demais |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (arquivo por ano de referência) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 177 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `Valor_Envolvido`: moeda (R$); `Valor`: moeda (R$); `Percentual_Valorizacao_Desvalorizacao`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Valor_Pago_Ano_Referencia`: moeda (R$); `Percentual_Patrimonio_Contabil`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Patrimonio_Valor_Mercado`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `CPF`: código ou número de identificação (sem unidade); `Quantidade_Cotas_FII_Detidas`: quantidade; `Quantidade_Cotas_FII_Compradas`: quantidade; `Quantidade_Cotas_FII_Vendidas`: quantidade; `Numero_Cotistas_Faixa_Ate_5`: quantidade; `Numero_Cotas_Detidas_Faixa_Ate_5`: quantidade; `Percentual_Cotas_Detidas_Faixa_Ate_5`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_Ate_5`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_Ate_5`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_5a10`: quantidade; `Numero_Cotas_Detidas_Faixa_5a10`: quantidade; `Percentual_Cotas_Detidas_Faixa_5a10`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_5a10`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_5a10`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_10a15`: quantidade; `Numero_Cotas_Detidas_Faixa_10a15`: quantidade; `Percentual_Cotas_Detidas_Faixa_10a15`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_10a15`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_10a15`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_15a20`: quantidade; `Numero_Cotas_Detidas_Faixa_15a20`: quantidade; `Percentual_Cotas_Detidas_Faixa_15a20`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_15a20`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_15a20`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_20a30`: quantidade; `Numero_Cotas_Detidas_Faixa_20a30`: quantidade; `Percentual_Cotas_Detidas_Faixa_20a30`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_20a30`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_20a30`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_30a40`: quantidade; `Numero_Cotas_Detidas_Faixa_30a40`: quantidade; `Percentual_Cotas_Detidas_Faixa_30a40`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_30a40`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_30a40`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_40a50`: quantidade; `Numero_Cotas_Detidas_Faixa_40a50`: quantidade; `Percentual_Cotas_Detidas_Faixa_40a50`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_40a50`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_40a50`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Cotistas_Faixa_Acima_50`: quantidade; `Numero_Cotas_Detidas_Faixa_Acima_50`: quantidade; `Percentual_Cotas_Detidas_Faixa_Acima_50`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PF_Faixa_Acima_50`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Detido_PJ_Faixa_Acima_50`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Quantidade_Cotas_Emitidas`: quantidade; `Valor_Causa`: moeda (R$) |
| Dados pessoais | `Nome_Diretor_Responsavel` (nome de pessoa física (diretor, responsável ou representante)); `Nome_Diretor_Representante` (nome de pessoa física (diretor, responsável ou representante)); `Nome_Representante` (nome de pessoa física (diretor, responsável ou representante)); `Endereco_Gestor` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Gestor` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Custodiante` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Custodiante` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Auditor_Independente` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Auditor_Independente` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Formador_Mercado` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Formador_Mercado` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Distribuidor_Cotas` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Distribuidor_Cotas` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Consultor_Especializado` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Consultor_Especializado` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Empresa_Locacao` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone_Empresa_Locacao` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Fisico_Documentos_Assembleia_Geral` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco_Eletronico_Documentos_Assembleia_Geral` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Email` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Logradouro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Complemento` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Bairro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Endereco` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fii-doc-inf_anual). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FII/DOC/INF_ANUAL/DADOS/`.
- O catálogo do fetcher lista 11 arquivo(s): de `inf_anual_fii_2016.zip` a `inf_anual_fii_2026.zip`.
- Em 2026-11-16 conferimos 36 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2016, 2021, 2026).
- No bruto, o arquivo fica em `fii-inf-anual/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe anual de um FII (nas tabelas gerais); um item do informe (diretor, representante, ativo, prestador, processo) nas demais.
- Particionado por `ano`; o catálogo cobre 2016 a 2026, e conferimos as amostras 2016, 2021, 2026.
- O arquivo de 2026 tem 416 informes em `inf_anual_fii_geral` (um por fundo, `CNPJ_Fundo_Classe` único), o de 2021 tem 660 e o de 2016 tem 260; as tabelas `ativo_*`, `processo*` e `experiencia_profissional` têm várias linhas por fundo (26.835 em `ativo_transacao`, no arquivo de 2026).
- Este dataset reúne 13 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `inf_anual_fii_ativo_adquirido` | 8 | 4.908 | não determinada | ativos adquiridos |
| `inf_anual_fii_ativo_transacao` | 10 | 26.835 | não determinada | transações com ativos |
| `inf_anual_fii_ativo_valor_contabil` | 8 | 8.722 | não determinada | valor contábil dos ativos |
| `inf_anual_fii_complemento` | 53 | 660 | `CNPJ_Fundo_Classe` | gestor, custodiante, auditor, formador de mercado e demais prestadores, com CNPJ, endereço e telefone (53 colunas) |
| `inf_anual_fii_diretor_responsavel` | 16 | 660 | `CNPJ_Fundo_Classe` | diretor responsável (nome, CPF, e-mail e cotas detidas) |
| `inf_anual_fii_distribuicao_cotistas` | 44 | 660 | `CNPJ_Fundo_Classe` | distribuição de cotistas por faixa de cotas e por tipo de cotista |
| `inf_anual_fii_experiencia_profissional` | 10 | 1.202 | `CNPJ_Fundo_Classe`, `Periodo` | experiência profissional do diretor |
| `inf_anual_fii_geral` | 39 | 660 | `CNPJ_Fundo_Classe` | dados gerais do fundo e do administrador |
| `inf_anual_fii_prestador_servico` | 8 | 86 | `CNPJ_Fundo_Classe` | prestadores de serviço |
| `inf_anual_fii_processo` | 13 | 558 | não determinada | processos judiciais e administrativos |
| `inf_anual_fii_processo_semelhante` | 7 | 178 | não determinada | processos semelhantes |
| `inf_anual_fii_representante_cotista` | 21 | 25 | `CNPJ_Fundo_Classe`, `CPF` | representante de cotistas (nome, CPF, e-mail) |
| `inf_anual_fii_representante_cotista_fundo` | 8 | 30 | não determinada | fundos em que o representante atua |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Fundo` | `CNPJ_Fundo` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_Fundo_Classe`) | — | 2016 |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Nome_Ativo` | `Nome_Ativo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome ativo (só em: `inf_anual_fii_ativo_adquirido`, `inf_anual_fii_ativo_valor_contabil`) | — | todo |
| `Objetivos` | `Objetivos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: objetivos (só em: `inf_anual_fii_ativo_adquirido`) | — | todo |
| `Montante_Investido` | `Montante_Investido` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: montante investido (só em: `inf_anual_fii_ativo_adquirido`) | — | todo |
| `Origem_Recursos` | `Origem_Recursos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: origem recursos (só em: `inf_anual_fii_ativo_adquirido`) | — | todo |
| `Ativo_Negociado` | `Ativo_Negociado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo negociado (só em: `inf_anual_fii_ativo_transacao`) | — | todo |
| `Natureza_Transacao` | `Natureza_Transacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: natureza transacao (só em: `inf_anual_fii_ativo_transacao`) | — | todo |
| `Data_Transacao` | `Data_Transacao` | texto | Data da transação (só em: `inf_anual_fii_ativo_transacao`) | — | todo |
| `Valor_Envolvido` | `Valor_Envolvido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor envolvido (só em: `inf_anual_fii_ativo_transacao`) | moeda (R$) | todo |
| `Data_Assembleia` | `Data_Assembleia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data assembleia (só em: `inf_anual_fii_ativo_transacao`) | — | todo |
| `Contraparte` | `Contraparte` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: contraparte (só em: `inf_anual_fii_ativo_transacao`) | — | todo |
| `Valor` | `Valor` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor (só em: `inf_anual_fii_ativo_valor_contabil`) | moeda (R$) | todo |
| `Valor_Justo` | `Valor_Justo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor justo (só em: `inf_anual_fii_ativo_valor_contabil`) | — | todo |
| `Percentual_Valorizacao_Desvalorizacao` | `Percentual_Valorizacao_Desvalorizacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual valorizacao desvalorizacao (só em: `inf_anual_fii_ativo_valor_contabil`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Nome_Gestor` | `Nome_Gestor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome gestor (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Gestor` | `CNPJ_Gestor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj gestor (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Gestor` | `Endereco_Gestor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco gestor (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Gestor` | `Telefone_Gestor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone gestor (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Custodiante` | `Nome_Custodiante` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome custodiante (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Custodiante` | `CNPJ_Custodiante` | texto | CNPJ do Custodiante (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Custodiante` | `Endereco_Custodiante` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco custodiante (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Custodiante` | `Telefone_Custodiante` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone custodiante (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Auditor_Independente` | `Nome_Auditor_Independente` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome auditor independente (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Auditor_Independente` | `CNPJ_Auditor_Independente` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj auditor independente (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Auditor_Independente` | `Endereco_Auditor_Independente` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco auditor independente (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Auditor_Independente` | `Telefone_Auditor_Independente` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone auditor independente (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Formador_Mercado` | `Nome_Formador_Mercado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome formador mercado (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Formador_Mercado` | `CNPJ_Formador_Mercado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj formador mercado (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Formador_Mercado` | `Endereco_Formador_Mercado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco formador mercado (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Formador_Mercado` | `Telefone_Formador_Mercado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone formador mercado (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Distribuidor_Cotas` | `Nome_Distribuidor_Cotas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome distribuidor cotas (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Distribuidor_Cotas` | `CNPJ_Distribuidor_Cotas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj distribuidor cotas (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Distribuidor_Cotas` | `Endereco_Distribuidor_Cotas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco distribuidor cotas (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Distribuidor_Cotas` | `Telefone_Distribuidor_Cotas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone distribuidor cotas (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Consultor_Especializado` | `Nome_Consultor_Especializado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome consultor especializado (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Consultor_Especializado` | `CNPJ_Consultor_Especializado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj consultor especializado (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Consultor_Especializado` | `Endereco_Consultor_Especializado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco consultor especializado (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Consultor_Especializado` | `Telefone_Consultor_Especializado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone consultor especializado (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Empresa_Locacao` | `Nome_Empresa_Locacao` | texto | Nome da Empresa Especializada para administrar as locações (só em: `inf_anual_fii_complemento`) | — | todo |
| `CNPJ_Empresa_Locacao` | `CNPJ_Empresa_Locacao` | texto | CNPJ da Empresa Especializada para administrar as locações (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Empresa_Locacao` | `Endereco_Empresa_Locacao` | texto | Endereço da Empresa Especializada para administrar as locações (só em: `inf_anual_fii_complemento`) | — | todo |
| `Telefone_Empresa_Locacao` | `Telefone_Empresa_Locacao` | texto | Telefone da Empresa Especializada para administrar as locações (só em: `inf_anual_fii_complemento`) | — | todo |
| `Programa_Investimentos_Exercicio_Seguinte` | `Programa_Investimentos_Exercicio_Seguinte` | texto | Programa de investimentos para os exercícios seguintes (só em: `inf_anual_fii_complemento`) | — | todo |
| `Resultado_Exercicio_Findo` | `Resultado_Exercicio_Findo` | texto | Análise do administrador sobre o resultado do fundo no exercício findo (só em: `inf_anual_fii_complemento`) | — | todo |
| `Conjuntura_Economica_Periodo_Findo` | `Conjuntura_Economica_Periodo_Findo` | texto | Análise do administrador sobre a conjuntura econômica do segmento do mercado imobiliário de atuação relativo ao período findo (só em: `inf_anual_fii_complemento`) | — | todo |
| `Perspectiva_Periodo_Seguinte` | `Perspectiva_Periodo_Seguinte` | texto | Análise do administrador sobre a perspectiva para o período seguinte com base na composição da carteira (só em: `inf_anual_fii_complemento`) | — | todo |
| `Criterios_Avaliacao` | `Criterios_Avaliacao` | texto | Critérios utilizados na avaliação dos ativos imobiliários do FII (só em: `inf_anual_fii_complemento`) | — | todo |
| `Analise_Impacto_Perda_Processos_Sigilosos` | `Analise_Impacto_Perda_Processos_Sigilosos` | texto | Análise dos impactos em caso de perda e valores envolvidos relacionados aos processos judiciais sigilosos relevantes (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Fisico_Documentos_Assembleia_Geral` | `Endereco_Fisico_Documentos_Assembleia_Geral` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco fisico documentos assembleia geral (só em: `inf_anual_fii_complemento`) | — | todo |
| `Endereco_Eletronico_Documentos_Assembleia_Geral` | `Endereco_Eletronico_Documentos_Assembleia_Geral` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco eletronico documentos assembleia geral (só em: `inf_anual_fii_complemento`) | — | todo |
| `Meio_Comunicacao_Cotistas` | `Meio_Comunicacao_Cotistas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: meio comunicacao cotistas (só em: `inf_anual_fii_complemento`) | — | todo |
| `Regras_Participacao_Cotistas_Assembleia_Geral` | `Regras_Participacao_Cotistas_Assembleia_Geral` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: regras participacao cotistas assembleia geral (só em: `inf_anual_fii_complemento`) | — | todo |
| `Pratica_Assembleia_Meio_Eletronico` | `Pratica_Assembleia_Meio_Eletronico` | texto | Práticas para a realização de assembleia por meio eletrônico (só em: `inf_anual_fii_complemento`) | — | todo |
| `Politica_Remuneracao` | `Politica_Remuneracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica remuneracao (só em: `inf_anual_fii_complemento`) | — | todo |
| `Valor_Pago_Ano_Referencia` | `Valor_Pago_Ano_Referencia` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: valor pago ano referencia (só em: `inf_anual_fii_complemento`, `inf_anual_fii_representante_cotista`) | moeda (R$) | todo |
| `Percentual_Patrimonio_Contabil` | `Percentual_Patrimonio_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual patrimonio contabil (só em: `inf_anual_fii_complemento`, `inf_anual_fii_representante_cotista`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Patrimonio_Valor_Mercado` | `Percentual_Patrimonio_Valor_Mercado` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual patrimonio valor mercado (só em: `inf_anual_fii_complemento`, `inf_anual_fii_representante_cotista`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Politica_Divulgacao_Fato_Relevante` | `Politica_Divulgacao_Fato_Relevante` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica divulgacao fato relevante (só em: `inf_anual_fii_complemento`) | — | todo |
| `Politica_Negociacao_Cotas` | `Politica_Negociacao_Cotas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica negociacao cotas (só em: `inf_anual_fii_complemento`) | — | todo |
| `Politica_Exercicio_Direito_Voto` | `Politica_Exercicio_Direito_Voto` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica exercicio direito voto (só em: `inf_anual_fii_complemento`) | — | todo |
| `Responsaveis_Politica_Divulgacao` | `Responsaveis_Politica_Divulgacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: responsaveis politica divulgacao (só em: `inf_anual_fii_complemento`) | — | todo |
| `Regras_Prazos_Chamada_Capital` | `Regras_Prazos_Chamada_Capital` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: regras prazos chamada capital (só em: `inf_anual_fii_complemento`) | — | todo |
| `Link_Download_Anexo` | `Link_Download_Anexo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: link download anexo (só em: `inf_anual_fii_complemento`) | — | todo |
| `Nome_Diretor_Responsavel` | `Nome_Diretor_Responsavel` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome diretor responsavel (só em: `inf_anual_fii_diretor_responsavel`) | — | todo |
| `Idade` | `Idade` | texto | Idade (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | — | todo |
| `CPF` | `CPF` | inteiro / texto | Cadastro de Pessoas Físicas (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | código ou número de identificação (sem unidade) | todo |
| `Profissao` | `Profissao` | texto | Profissão (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | — | todo |
| `Email` | `Email` | texto | Endereço de e-mail (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_geral`, `inf_anual_fii_representante_cotista`) | — | todo |
| `Formacao_Academica` | `Formacao_Academica` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: formacao academica (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | — | todo |
| `Quantidade_Cotas_FII_Detidas` | `Quantidade_Cotas_FII_Detidas` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade cotas fii detidas (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | quantidade | todo |
| `Quantidade_Cotas_FII_Compradas` | `Quantidade_Cotas_FII_Compradas` | inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade cotas fii compradas (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | quantidade | todo |
| `Quantidade_Cotas_FII_Vendidas` | `Quantidade_Cotas_FII_Vendidas` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade cotas fii vendidas (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | quantidade | todo |
| `Data_Inicio` | `Data_Inicio` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data inicio (só em: `inf_anual_fii_diretor_responsavel`) | — | todo |
| `Condenacao_Criminal` | `Condenacao_Criminal` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: condenacao criminal (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | — | todo |
| `Condenacao_Processo_CVM` | `Condenacao_Processo_CVM` | texto | Condenação em processo administrativo da CVM (só em: `inf_anual_fii_diretor_responsavel`, `inf_anual_fii_representante_cotista`) | — | todo |
| `Numero_Cotistas_Faixa_Ate_5` | `Numero_Cotistas_Faixa_Ate_5` | decimal / inteiro | Número de cotistas (Faixa de distribuição: até 5% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_Ate_5` | `Numero_Cotas_Detidas_Faixa_Ate_5` | decimal | Número de cotas detidas (Faixa de distribuição: até 5% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_Ate_5` | `Percentual_Cotas_Detidas_Faixa_Ate_5` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: até 5% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_Ate_5` | `Percentual_Detido_PF_Faixa_Ate_5` | decimal | Percentual detido por PF (Faixa de distribuição: até 5% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_Ate_5` | `Percentual_Detido_PJ_Faixa_Ate_5` | decimal | Percentual detido por PJ (Faixa de distribuição: até 5% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_5a10` | `Numero_Cotistas_Faixa_5a10` | inteiro | Número de cotistas (Faixa de distribuição: acima de 5% até 10% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_5a10` | `Numero_Cotas_Detidas_Faixa_5a10` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 5% até 10% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_5a10` | `Percentual_Cotas_Detidas_Faixa_5a10` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 5% até 10% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_5a10` | `Percentual_Detido_PF_Faixa_5a10` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 5% até 10% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_5a10` | `Percentual_Detido_PJ_Faixa_5a10` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 5% até 10% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_10a15` | `Numero_Cotistas_Faixa_10a15` | inteiro | Número de cotistas (Faixa de distribuição: acima de 10% até 15% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_10a15` | `Numero_Cotas_Detidas_Faixa_10a15` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 10% até 15% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_10a15` | `Percentual_Cotas_Detidas_Faixa_10a15` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 10% até 15% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_10a15` | `Percentual_Detido_PF_Faixa_10a15` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 10% até 15% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_10a15` | `Percentual_Detido_PJ_Faixa_10a15` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 10% até 15% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_15a20` | `Numero_Cotistas_Faixa_15a20` | inteiro | Número de cotistas (Faixa de distribuição: acima de 15% até 20% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_15a20` | `Numero_Cotas_Detidas_Faixa_15a20` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 15% até 20% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_15a20` | `Percentual_Cotas_Detidas_Faixa_15a20` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 15% até 20% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_15a20` | `Percentual_Detido_PF_Faixa_15a20` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 15% até 20% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_15a20` | `Percentual_Detido_PJ_Faixa_15a20` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 15% até 20% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_20a30` | `Numero_Cotistas_Faixa_20a30` | inteiro | Número de cotistas (Faixa de distribuição: acima de 20% até 30% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_20a30` | `Numero_Cotas_Detidas_Faixa_20a30` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 20% até 30% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_20a30` | `Percentual_Cotas_Detidas_Faixa_20a30` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 20% até 30% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_20a30` | `Percentual_Detido_PF_Faixa_20a30` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 20% até 30% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_20a30` | `Percentual_Detido_PJ_Faixa_20a30` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 20% até 30% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_30a40` | `Numero_Cotistas_Faixa_30a40` | inteiro | Número de cotistas (Faixa de distribuição: acima de 30% até 40% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_30a40` | `Numero_Cotas_Detidas_Faixa_30a40` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 30% até 40% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_30a40` | `Percentual_Cotas_Detidas_Faixa_30a40` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 30% até 40% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_30a40` | `Percentual_Detido_PF_Faixa_30a40` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 30% até 40% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_30a40` | `Percentual_Detido_PJ_Faixa_30a40` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 30% até 40% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_40a50` | `Numero_Cotistas_Faixa_40a50` | inteiro | Número de cotistas (Faixa de distribuição: acima de 40% até 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_40a50` | `Numero_Cotas_Detidas_Faixa_40a50` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 40% até 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_40a50` | `Percentual_Cotas_Detidas_Faixa_40a50` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 40% até 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_40a50` | `Percentual_Detido_PF_Faixa_40a50` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 40% até 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_40a50` | `Percentual_Detido_PJ_Faixa_40a50` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 40% até 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Numero_Cotistas_Faixa_Acima_50` | `Numero_Cotistas_Faixa_Acima_50` | inteiro | Número de cotistas (Faixa de distribuição: acima de 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Numero_Cotas_Detidas_Faixa_Acima_50` | `Numero_Cotas_Detidas_Faixa_Acima_50` | decimal | Número de cotas detidas (Faixa de distribuição: acima de 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | quantidade | todo |
| `Percentual_Cotas_Detidas_Faixa_Acima_50` | `Percentual_Cotas_Detidas_Faixa_Acima_50` | decimal | Percentual de cotas detido em relação ao total emitido (Faixa de distribuição: acima de 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PF_Faixa_Acima_50` | `Percentual_Detido_PF_Faixa_Acima_50` | decimal | Percentual detido por PF (Faixa de distribuição: acima de 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Detido_PJ_Faixa_Acima_50` | `Percentual_Detido_PJ_Faixa_Acima_50` | decimal | Percentual detido por PJ (Faixa de distribuição: acima de 50% das cotas) (só em: `inf_anual_fii_distribuicao_cotistas`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Nome_Diretor_Representante` | `Nome_Diretor_Representante` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome diretor representante (só em: `inf_anual_fii_experiencia_profissional`) | — | todo |
| `Funcao` | `Funcao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: funcao (só em: `inf_anual_fii_experiencia_profissional`) | — | todo |
| `Nome_Empresa` | `Nome_Empresa` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome empresa (só em: `inf_anual_fii_experiencia_profissional`) | — | todo |
| `Periodo` | `Periodo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: periodo (só em: `inf_anual_fii_experiencia_profissional`) | — | todo |
| `Cargo_Funcao` | `Cargo_Funcao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cargo funcao (só em: `inf_anual_fii_experiencia_profissional`) | — | todo |
| `Atividade_Principal` | `Atividade_Principal` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: atividade principal (só em: `inf_anual_fii_experiencia_profissional`) | — | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `inf_anual_fii_geral`) | — | todo |
| `Nome_Fundo` | `Nome_Fundo` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Nome_Fundo_Classe`) (só em: `inf_anual_fii_geral`, `inf_anual_fii_representante_cotista_fundo`) | — | 2016 a 2021 |
| `Data_Funcionamento` | `Data_Funcionamento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data funcionamento (só em: `inf_anual_fii_geral`) | — | todo |
| `Publico_Alvo` | `Publico_Alvo` | texto | Público-alvo (só em: `inf_anual_fii_geral`) | — | todo |
| `Codigo_ISIN` | `Codigo_ISIN` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo isin (só em: `inf_anual_fii_geral`) | — | todo |
| `Quantidade_Cotas_Emitidas` | `Quantidade_Cotas_Emitidas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade cotas emitidas (só em: `inf_anual_fii_geral`) | quantidade | todo |
| `Fundo_Exclusivo` | `Fundo_Exclusivo` | texto | Indica se é fundo exclusivo (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Cotistas_Vinculo_Familiar` | `Cotistas_Vinculo_Familiar` | texto | Indica se os cotistas possuem vínculo familiar ou societário familiar (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Mandato` | `Mandato` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mandato (só em: `inf_anual_fii_geral`) | — | todo |
| `Segmento_Atuacao` | `Segmento_Atuacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: segmento atuacao (só em: `inf_anual_fii_geral`) | — | todo |
| `Tipo_Gestao` | `Tipo_Gestao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo gestao (só em: `inf_anual_fii_geral`) | — | todo |
| `Prazo_Duracao` | `Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: prazo duracao (só em: `inf_anual_fii_geral`) | — | todo |
| `Data_Prazo_Duracao` | `Data_Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data prazo duracao (só em: `inf_anual_fii_geral`) | — | todo |
| `Encerramento_Exercicio_Social` | `Encerramento_Exercicio_Social` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: encerramento exercicio social (só em: `inf_anual_fii_geral`) | — | todo |
| `Mercado_Negociacao_Bolsa` | `Mercado_Negociacao_Bolsa` | texto | Indica se o mercado de negociação das cotas é Bolsa (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Mercado_Negociacao_MBO` | `Mercado_Negociacao_MBO` | texto | Indica se o mercado de negociação das cotas é MBO (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Mercado_Negociacao_MB` | `Mercado_Negociacao_MB` | texto | Indica se o mercado de negociação das cotas é MB (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Entidade_Administradora_BVMF` | `Entidade_Administradora_BVMF` | texto | Indica se a entidade administradora de mercado organizado é BVMF (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Entidade_Administradora_CETIP` | `Entidade_Administradora_CETIP` | texto | Indica se a entidade administradora de mercado organizado é CETIP (só em: `inf_anual_fii_geral`) | S/N | todo |
| `Nome_Administrador` | `Nome_Administrador` | texto | Nome do administrador (só em: `inf_anual_fii_geral`) | — | todo |
| `CNPJ_Administrador` | `CNPJ_Administrador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj administrador (só em: `inf_anual_fii_geral`) | — | todo |
| `Logradouro` | `Logradouro` | texto | Logradouro (só em: `inf_anual_fii_geral`) | — | todo |
| `Numero` | `Numero` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: numero (só em: `inf_anual_fii_geral`) | — | todo |
| `Complemento` | `Complemento` | texto | Complemento (só em: `inf_anual_fii_geral`) | — | todo |
| `Bairro` | `Bairro` | texto | Bairro (só em: `inf_anual_fii_geral`) | — | todo |
| `Cidade` | `Cidade` | texto | Cidade (só em: `inf_anual_fii_geral`) | — | todo |
| `Estado` | `Estado` | texto | Estado (só em: `inf_anual_fii_geral`) | — | todo |
| `CEP` | `CEP` | texto | CEP (só em: `inf_anual_fii_geral`) | — | todo |
| `Telefone1` | `Telefone1` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone1 (só em: `inf_anual_fii_geral`) | — | todo |
| `Telefone2` | `Telefone2` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone2 (só em: `inf_anual_fii_geral`) | — | todo |
| `Telefone3` | `Telefone3` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone3 (só em: `inf_anual_fii_geral`) | — | todo |
| `Site` | `Site` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: site (só em: `inf_anual_fii_geral`) | — | todo |
| `Nome_Prestador` | `Nome_Prestador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome prestador (só em: `inf_anual_fii_prestador_servico`) | — | todo |
| `CNPJ_Prestador` | `CNPJ_Prestador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj prestador (só em: `inf_anual_fii_prestador_servico`) | — | todo |
| `Endereco` | `Endereco` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco (só em: `inf_anual_fii_prestador_servico`) | — | todo |
| `Telefone` | `Telefone` | texto | Telefone (só em: `inf_anual_fii_prestador_servico`) | — | todo |
| `Numero_Processo` | `Numero_Processo` | texto | Número do Processo Administrativo (só em: `inf_anual_fii_processo`, `inf_anual_fii_processo_semelhante`) | — | todo |
| `Juizo` | `Juizo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: juizo (só em: `inf_anual_fii_processo`) | — | todo |
| `Instancia` | `Instancia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: instancia (só em: `inf_anual_fii_processo`) | — | todo |
| `Data_Instauracao` | `Data_Instauracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data instauracao (só em: `inf_anual_fii_processo`) | — | todo |
| `Valor_Causa` | `Valor_Causa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor causa (só em: `inf_anual_fii_processo`) | moeda (R$) | todo |
| `Partes_Processo` | `Partes_Processo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: partes processo (só em: `inf_anual_fii_processo`) | — | todo |
| `Chance_Perda` | `Chance_Perda` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: chance perda (só em: `inf_anual_fii_processo`) | — | todo |
| `Principais_Fatos` | `Principais_Fatos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: principais fatos (só em: `inf_anual_fii_processo`) | — | todo |
| `Analise_Impacto_Perda` | `Analise_Impacto_Perda` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: analise impacto perda (só em: `inf_anual_fii_processo`) | — | todo |
| `Valores` | `Valores` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valores (só em: `inf_anual_fii_processo_semelhante`) | — | todo |
| `Causa_Contingencia` | `Causa_Contingencia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: causa contingencia (só em: `inf_anual_fii_processo_semelhante`) | — | todo |
| `Nome_Representante` | `Nome_Representante` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome representante (só em: `inf_anual_fii_representante_cotista`, `inf_anual_fii_representante_cotista_fundo`) | — | todo |
| `Forma_Remuneracao` | `Forma_Remuneracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: forma remuneracao (só em: `inf_anual_fii_representante_cotista`) | — | todo |
| `Data_Eleicao` | `Data_Eleicao` | texto | Data da eleição (só em: `inf_anual_fii_representante_cotista`, `inf_anual_fii_representante_cotista_fundo`) | — | todo |
| `Termino_Mandato` | `Termino_Mandato` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: termino mandato (só em: `inf_anual_fii_representante_cotista`, `inf_anual_fii_representante_cotista_fundo`) | — | todo |
| `CNPJ_Fundo_Classe` | `CNPJ_Fundo_Classe` | texto | CNPJ do fundo/classe | — | 2021 a 2026 |
| `Tipo_Fundo_Classe` | `Tipo_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo fundo classe (só em: `inf_anual_fii_geral`) | — | 2021 a 2026 |
| `Nome_Fundo_Classe` | `Nome_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome fundo classe (só em: `inf_anual_fii_geral`) | — | 2021 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fii-inf-anual`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **CPF em formatos diferentes.** `CPF` em `inf_anual_fii_diretor_responsavel` (arquivo de 2026) vem com máscara em 249 valores, só com 11 dígitos em 130, com 10 dígitos em 24 e com 9 em 4 (zeros à esquerda perdidos na origem), além de poucos outros formatos; em `inf_anual_fii_representante_cotista` o tipo varia entre inteiro e texto conforme o arquivo. Normalize (`regexp_replace(CPF::VARCHAR, '\D', '', 'g')` e `lpad(..., 11, '0')`) antes de usar.
- **CNPJ de prestadores misto.** `CNPJ_Gestor`, `CNPJ_Custodiante`, `CNPJ_Auditor_Independente` e `CNPJ_Administrador` misturam valores com e sem máscara (por exemplo, 22% com máscara e 63% só com dígitos em `CNPJ_Gestor`); normalize antes de juntar.
- **Tabelas de ativos com linhas repetidas.** `inf_anual_fii_ativo_transacao` (158), `ativo_valor_contabil` (32) e `ativo_adquirido` (6) têm linhas inteiramente repetidas no arquivo de 2026; remova duplicatas antes de somar.
- **Dados pessoais.** Há nome, CPF, e-mail e telefone de diretores e representantes de cotistas, e endereço e telefone de prestadores. O fetcher e o lake preservam o que a fonte publica.
- **Tipo inferido varia entre arquivos.** 7 coluna(s) (`Valor_Pago_Ano_Referencia`, `Percentual_Patrimonio_Valor_Mercado`, `CPF`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.
- **Linhas repetidas.** No arquivo mais recente convertido há linhas inteiramente repetidas em: `inf_anual_fii_ativo_adquirido` (6), `inf_anual_fii_ativo_transacao` (158), `inf_anual_fii_ativo_valor_contabil` (32). Remova as duplicatas antes de contar ou somar.
- **CEP, DDD, telefone e CPF viram número.** O conversor infere o tipo de cada CSV e lê `CPF` como inteiro, o que descarta zeros à esquerda; reconstrua o texto com `lpad` quando precisar do código.

## Exemplos

Fundos com informe anual por ano de arquivo (a coluna do CNPJ mudou de nome entre arquivos).

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(DISTINCT coalesce(CNPJ_Fundo_Classe, CNPJ_Fundo)) AS fundos
    FROM read_parquet('lake/cvm/fii-inf-anual/**/*__inf_anual_fii_geral_*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_anual
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FII/DOC/INF_ANUAL/
