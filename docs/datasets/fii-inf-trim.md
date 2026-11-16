---
dataset:
  id: fii-inf-trim
  fonte: cvm
  titulo: "FII: Documentos: Informe Trimestral Estruturado (CVM)"
  resumo: "Informe trimestral estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, ativos, imóveis, terrenos, aquisições e alienações, rentabilidade e resultado contábil e financeiro, em 16 tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fii-doc-inf_trimestral
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_trimestral"
  periodicidade: "anual (um arquivo por ano, com um informe por trimestre); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2016, fim: em-curso}
  unidade: "o informe trimestral de um FII em um trimestre e versão (nas tabelas gerais); um item de ativo, imóvel, terreno, aquisição ou alienação do informe (nas demais)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "trimestral (`Data_Referencia` costuma ser o fim do trimestre), em arquivos anuais"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 221}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    Area: "área (unidade não informada no dicionário da CVM)"
    Numero_Unidades: "quantidade"
    Percentual_Imovel_Total_Investido: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Imovel_PL: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Terreno_Total_Investido: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Terreno_PL: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Emissao: "código ou número de identificação (sem unidade)"
    Serie: "código ou número de identificação (sem unidade)"
    Quantidade: "quantidade"
    Valor: "moeda (R$)"
    Percentual_Garantido_Relativo: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_Ate_3Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_Ate_3Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_3a6Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_3a6Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_6a9Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_6a9Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_9a12Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_9a12Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_12a15Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_12a15Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_15a18Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_15a18Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_18a21Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_18a21Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_21a24Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_21a24Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_24a27Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_24a27Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_27a30Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_27a30Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_30a33Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_30a33Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_33a36Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_33a36Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_Acima_36Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_Acima_36Meses: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Valor_Total_Faixa_Indeterminado: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vencimento_Receita_FII_Faixa_Indeterminado: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Valor_Total_IGPM: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Receita_FII_IGPM: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Valor_Total_INPC: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Receita_FII_INPC: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Valor_Total_IPCA: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Receita_FII_IPCA: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Valor_Total_INCC: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Indexador_Receita_FII_INCC: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Ativo_Liquidez_Valor_Disponibilidades: "moeda (R$)"
    Ativo_Liquidez_Valor_Titulos_Publicos: "moeda (R$)"
    Ativo_Liquidez_Valor_Titulos_Privados: "moeda (R$)"
    Ativo_Liquidez_Valor_Fundos_Renda_Fixa: "moeda (R$)"
    Quantidade_Cotas_Emitidas: "quantidade"
    Percentual_Vacancia: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Inadimplencia: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Receitas_FII: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Locado: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Vendido: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Conclusao_Obras_Realizado: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Conclusao_Obras_Previsto: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Custo_Construcao_Realizado: "moeda (R$)"
    Custo_Construcao_Previsto: "moeda (R$)"
    Percentual_Receita_Imovel: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Rentabilidade_Efetiva_Mes: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Rentabilidade_Auferida_Ausencia_Garantia: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Receita_Venda_Estoque_Contabil: "moeda (R$)"
    Receita_Venda_Estoque_Financeiro: "moeda (R$)"
    Custo_Estoque_Contabil: "moeda (R$)"
    Custo_Estoque_Financeiro: "moeda (R$)"
    Ajuste_Realizacao_Estoque_Contabil: "moeda (R$)"
    Ajuste_Realizacao_Estoque_Financeiro: "moeda (R$)"
    Outras_Receitas_Despesas_Estoque_Contabil: "moeda (R$)"
    Outras_Receitas_Despesas_Estoque_Financeiro: "moeda (R$)"
    Resultado_Liquido_Estoque_Contabil: "moeda (R$)"
    Resultado_Liquido_Estoque_Financeiro: "moeda (R$)"
    Receita_Aluguel_Investimento_Contabil: "moeda (R$)"
    Receita_Aluguel_Investimento_Financeiro: "moeda (R$)"
    Despesa_Manutencao_Investimento_Contabil: "moeda (R$)"
    Despesa_Manutencao_Investimento_Financeiro: "moeda (R$)"
    Receita_Venda_Investimento_Contabil: "moeda (R$)"
    Receita_Venda_Investimento_Financeiro: "moeda (R$)"
    Custo_Investimento_Contabil: "moeda (R$)"
    Custo_Investimento_Financeiro: "moeda (R$)"
    Ajuste_Justo_Investimento_Contabil: "moeda (R$)"
    Ajuste_Justo_Investimento_Financeiro: "moeda (R$)"
    Outras_Receitas_Despesas_Investimento_Contabil: "moeda (R$)"
    Outras_Receitas_Despesas_Investimento_Financeiro: "moeda (R$)"
    Resultado_Liquido_Renda_Contabil: "moeda (R$)"
    Resultado_Liquido_Renda_Investimento_Financeiro: "moeda (R$)"
    Receita_Juros_TVM_Contabil: "moeda (R$)"
    Receita_Juros_TVM_Financeiro: "moeda (R$)"
    Ajuste_Justo_TVM_Contabil: "moeda (R$)"
    Ajuste_Justo_TVM_Financeiro: "moeda (R$)"
    Resultado_Venda_TVM_Contabil: "moeda (R$)"
    Resultado_Venda_TVM_Financeiro: "moeda (R$)"
    Outras_Receitas_Despesas_TVM_Contabil: "moeda (R$)"
    Outras_Receitas_Despesas_TVM_Financeiro: "moeda (R$)"
    Resultado_Liquido_TVM_Contabil: "moeda (R$)"
    Resultado_Liquido_TVM_Financeiro: "moeda (R$)"
    Resultado_Liquido_Total_Contabil: "moeda (R$)"
    Resultado_Liquido_Total_Financeiro: "moeda (R$)"
    Receita_Juros_Aplicacao_Contabil: "moeda (R$)"
    Receita_Juros_Aplicacao_Financeiro: "moeda (R$)"
    Ajuste_Justo_Aplicacao_Contabil: "moeda (R$)"
    Ajuste_Justo_Aplicacao_Financeiro: "moeda (R$)"
    Resultado_Venda_Aplicacao_Contabil: "moeda (R$)"
    Resultado_Venda_Aplicacao_Financeiro: "moeda (R$)"
    Outras_Receitas_Despesas_Aplicacao_Contabil: "moeda (R$)"
    Outras_Receitas_Despesas_Aplicacao_Financeiro: "moeda (R$)"
    Resultado_Liquido_Recurso_Liquidez_Contabil: "moeda (R$)"
    Resultado_Liquido_Recurso_Liquidez_Financeiro: "moeda (R$)"
    Resultado_Liquido_Derivativos_Contabil: "moeda (R$)"
    Resultado_Liquido_Derivativos_Financeiro: "moeda (R$)"
    Taxa_Administracao_Contabil: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Taxa_Administracao_Financeiro: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Taxa_Desempenho_Contabil: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Taxa_Desempenho_Financeiro: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Despesa_Consultoria_Especializada_Contabil: "moeda (R$)"
    Despesa_Consultoria_Especializada_Financeiro: "moeda (R$)"
    Despesa_Empresa_Especializada_Contabil: "moeda (R$)"
    Despesa_Empresa_Especializada_Financeiro: "moeda (R$)"
    Despesa_Formador_Mercado_Contabil: "moeda (R$)"
    Despesa_Formador_Mercado_Financeiro: "moeda (R$)"
    Despesa_Custodia_Contabil: "moeda (R$)"
    Despesa_Custodia_Financeiro: "moeda (R$)"
    Despesa_Auditoria_Independente_Contabil: "moeda (R$)"
    Despesa_Auditoria_Independente_Financeiro: "moeda (R$)"
    Despesa_Representantes_Cotistas_Contabil: "moeda (R$)"
    Despesa_Representantes_Cotistas_Financeiro: "moeda (R$)"
    Taxa_Imposto_Contribuicao_Contabil: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Taxa_Imposto_Contribuicao_Financeiro: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Despesa_Comissoes_Emolumentos_Contabil: "moeda (R$)"
    Despesa_Comissoes_Emolumentos_Financeiro: "moeda (R$)"
    Despesa_Honorarios_Defesas_Contabil: "moeda (R$)"
    Despesa_Honorarios_Defesas_Financeiro: "moeda (R$)"
    Despesa_Contratos_Seguros_Contabil: "moeda (R$)"
    Despesa_Contratos_Seguros_Financeiro: "moeda (R$)"
    Despesa_Avaliacoes_Contabil: "moeda (R$)"
    Despesa_Avaliacoes_Financeiro: "moeda (R$)"
    Taxa_Ingresso_Saida_Cotista_Contabil: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Taxa_Ingresso_Saida_Cotista_Financeiro: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Despesa_Registro_Cartorio_Contabil: "moeda (R$)"
    Despesa_Registro_Cartorio_Financeiro: "moeda (R$)"
    Outras_Receitas_Depesas_Contabil: "moeda (R$)"
    Outras_Receitas_Depesas_Financeiro: "moeda (R$)"
    Total_Receitas_Despesas_Contabil: "moeda (R$)"
    Total_Receitas_Despesas_Financeiro: "moeda (R$)"
    Resultado_Trimestral_Liquido_Contabil: "moeda (R$)"
    Resultado_Trimestral_Liquido_Financeiro: "moeda (R$)"
    Resultado_Financeiro_Liquido_Acumulado: "moeda (R$)"
    Resultado_Financeiro_Liquido_Acumulado_95: "moeda (R$)"
    Lucro_Contabil: "moeda (R$)"
    Rendimentos_Declarados: "moeda (R$)"
    Rendimentos_Pagos_Antecipadamente: "moeda (R$)"
    Rendimento_Liquido_Pagar: "moeda (R$)"
    Percentual_Resultado_Financeiro_Liquido_Declarado: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
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

# FII: Documentos: Informe Trimestral Estruturado

## Resumo

Informe trimestral estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, ativos, imóveis, terrenos, aquisições e alienações, rentabilidade e resultado contábil e financeiro, em 16 tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fii-inf-trim` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fii-doc-inf_trimestral |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_trimestral |
| Periodicidade | anual (um arquivo por ano, com um informe por trimestre); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2016 a em-curso |
| Unidade (uma linha) | o informe trimestral de um FII em um trimestre e versão (nas tabelas gerais); um item de ativo, imóvel, terreno, aquisição ou alienação do informe (nas demais) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: trimestral (`Data_Referencia` costuma ser o fim do trimestre), em arquivos anuais |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 221 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `Area`: área (unidade não informada no dicionário da CVM); `Numero_Unidades`: quantidade; `Percentual_Imovel_Total_Investido`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Imovel_PL`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Terreno_Total_Investido`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Terreno_PL`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Emissao`: código ou número de identificação (sem unidade); `Serie`: código ou número de identificação (sem unidade); `Quantidade`: quantidade; `Valor`: moeda (R$); `Percentual_Garantido_Relativo`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_Ate_3Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_Ate_3Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_3a6Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_3a6Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_6a9Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_6a9Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_9a12Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_9a12Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_12a15Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_12a15Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_15a18Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_15a18Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_18a21Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_18a21Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_21a24Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_21a24Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_24a27Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_24a27Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_27a30Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_27a30Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_30a33Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_30a33Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_33a36Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_33a36Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_Acima_36Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_Acima_36Meses`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Valor_Total_Faixa_Indeterminado`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vencimento_Receita_FII_Faixa_Indeterminado`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Valor_Total_IGPM`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Receita_FII_IGPM`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Valor_Total_INPC`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Receita_FII_INPC`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Valor_Total_IPCA`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Receita_FII_IPCA`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Valor_Total_INCC`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Indexador_Receita_FII_INCC`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Ativo_Liquidez_Valor_Disponibilidades`: moeda (R$); `Ativo_Liquidez_Valor_Titulos_Publicos`: moeda (R$); `Ativo_Liquidez_Valor_Titulos_Privados`: moeda (R$); `Ativo_Liquidez_Valor_Fundos_Renda_Fixa`: moeda (R$); `Quantidade_Cotas_Emitidas`: quantidade; `Percentual_Vacancia`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Inadimplencia`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Receitas_FII`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Locado`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Vendido`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Conclusao_Obras_Realizado`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Conclusao_Obras_Previsto`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Custo_Construcao_Realizado`: moeda (R$); `Custo_Construcao_Previsto`: moeda (R$); `Percentual_Receita_Imovel`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Rentabilidade_Efetiva_Mes`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Rentabilidade_Auferida_Ausencia_Garantia`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Receita_Venda_Estoque_Contabil`: moeda (R$); `Receita_Venda_Estoque_Financeiro`: moeda (R$); `Custo_Estoque_Contabil`: moeda (R$); `Custo_Estoque_Financeiro`: moeda (R$); `Ajuste_Realizacao_Estoque_Contabil`: moeda (R$); `Ajuste_Realizacao_Estoque_Financeiro`: moeda (R$); `Outras_Receitas_Despesas_Estoque_Contabil`: moeda (R$); `Outras_Receitas_Despesas_Estoque_Financeiro`: moeda (R$); `Resultado_Liquido_Estoque_Contabil`: moeda (R$); `Resultado_Liquido_Estoque_Financeiro`: moeda (R$); `Receita_Aluguel_Investimento_Contabil`: moeda (R$); `Receita_Aluguel_Investimento_Financeiro`: moeda (R$); `Despesa_Manutencao_Investimento_Contabil`: moeda (R$); `Despesa_Manutencao_Investimento_Financeiro`: moeda (R$); `Receita_Venda_Investimento_Contabil`: moeda (R$); `Receita_Venda_Investimento_Financeiro`: moeda (R$); `Custo_Investimento_Contabil`: moeda (R$); `Custo_Investimento_Financeiro`: moeda (R$); `Ajuste_Justo_Investimento_Contabil`: moeda (R$); `Ajuste_Justo_Investimento_Financeiro`: moeda (R$); `Outras_Receitas_Despesas_Investimento_Contabil`: moeda (R$); `Outras_Receitas_Despesas_Investimento_Financeiro`: moeda (R$); `Resultado_Liquido_Renda_Contabil`: moeda (R$); `Resultado_Liquido_Renda_Investimento_Financeiro`: moeda (R$); `Receita_Juros_TVM_Contabil`: moeda (R$); `Receita_Juros_TVM_Financeiro`: moeda (R$); `Ajuste_Justo_TVM_Contabil`: moeda (R$); `Ajuste_Justo_TVM_Financeiro`: moeda (R$); `Resultado_Venda_TVM_Contabil`: moeda (R$); `Resultado_Venda_TVM_Financeiro`: moeda (R$); `Outras_Receitas_Despesas_TVM_Contabil`: moeda (R$); `Outras_Receitas_Despesas_TVM_Financeiro`: moeda (R$); `Resultado_Liquido_TVM_Contabil`: moeda (R$); `Resultado_Liquido_TVM_Financeiro`: moeda (R$); `Resultado_Liquido_Total_Contabil`: moeda (R$); `Resultado_Liquido_Total_Financeiro`: moeda (R$); `Receita_Juros_Aplicacao_Contabil`: moeda (R$); `Receita_Juros_Aplicacao_Financeiro`: moeda (R$); `Ajuste_Justo_Aplicacao_Contabil`: moeda (R$); `Ajuste_Justo_Aplicacao_Financeiro`: moeda (R$); `Resultado_Venda_Aplicacao_Contabil`: moeda (R$); `Resultado_Venda_Aplicacao_Financeiro`: moeda (R$); `Outras_Receitas_Despesas_Aplicacao_Contabil`: moeda (R$); `Outras_Receitas_Despesas_Aplicacao_Financeiro`: moeda (R$); `Resultado_Liquido_Recurso_Liquidez_Contabil`: moeda (R$); `Resultado_Liquido_Recurso_Liquidez_Financeiro`: moeda (R$); `Resultado_Liquido_Derivativos_Contabil`: moeda (R$); `Resultado_Liquido_Derivativos_Financeiro`: moeda (R$); `Taxa_Administracao_Contabil`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Taxa_Administracao_Financeiro`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Taxa_Desempenho_Contabil`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Taxa_Desempenho_Financeiro`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Despesa_Consultoria_Especializada_Contabil`: moeda (R$); `Despesa_Consultoria_Especializada_Financeiro`: moeda (R$); `Despesa_Empresa_Especializada_Contabil`: moeda (R$); `Despesa_Empresa_Especializada_Financeiro`: moeda (R$); `Despesa_Formador_Mercado_Contabil`: moeda (R$); `Despesa_Formador_Mercado_Financeiro`: moeda (R$); `Despesa_Custodia_Contabil`: moeda (R$); `Despesa_Custodia_Financeiro`: moeda (R$); `Despesa_Auditoria_Independente_Contabil`: moeda (R$); `Despesa_Auditoria_Independente_Financeiro`: moeda (R$); `Despesa_Representantes_Cotistas_Contabil`: moeda (R$); `Despesa_Representantes_Cotistas_Financeiro`: moeda (R$); `Taxa_Imposto_Contribuicao_Contabil`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Taxa_Imposto_Contribuicao_Financeiro`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Despesa_Comissoes_Emolumentos_Contabil`: moeda (R$); `Despesa_Comissoes_Emolumentos_Financeiro`: moeda (R$); `Despesa_Honorarios_Defesas_Contabil`: moeda (R$); `Despesa_Honorarios_Defesas_Financeiro`: moeda (R$); `Despesa_Contratos_Seguros_Contabil`: moeda (R$); `Despesa_Contratos_Seguros_Financeiro`: moeda (R$); `Despesa_Avaliacoes_Contabil`: moeda (R$); `Despesa_Avaliacoes_Financeiro`: moeda (R$); `Taxa_Ingresso_Saida_Cotista_Contabil`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Taxa_Ingresso_Saida_Cotista_Financeiro`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Despesa_Registro_Cartorio_Contabil`: moeda (R$); `Despesa_Registro_Cartorio_Financeiro`: moeda (R$); `Outras_Receitas_Depesas_Contabil`: moeda (R$); `Outras_Receitas_Depesas_Financeiro`: moeda (R$); `Total_Receitas_Despesas_Contabil`: moeda (R$); `Total_Receitas_Despesas_Financeiro`: moeda (R$); `Resultado_Trimestral_Liquido_Contabil`: moeda (R$); `Resultado_Trimestral_Liquido_Financeiro`: moeda (R$); `Resultado_Financeiro_Liquido_Acumulado`: moeda (R$); `Resultado_Financeiro_Liquido_Acumulado_95`: moeda (R$); `Lucro_Contabil`: moeda (R$); `Rendimentos_Declarados`: moeda (R$); `Rendimentos_Pagos_Antecipadamente`: moeda (R$); `Rendimento_Liquido_Pagar`: moeda (R$); `Percentual_Resultado_Financeiro_Liquido_Declarado`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) |
| Dados pessoais | `Logradouro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Complemento` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Bairro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Email` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fii-doc-inf_trimestral). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FII/DOC/INF_TRIMESTRAL/DADOS/`.
- O catálogo do fetcher lista 11 arquivo(s): de `inf_trimestral_fii_2016.zip` a `inf_trimestral_fii_2026.zip`.
- Em 2026-11-16 conferimos 48 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2016, 2021, 2026).
- No bruto, o arquivo fica em `fii-inf-trim/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe trimestral de um FII em um trimestre e versão (nas tabelas gerais); um item de ativo, imóvel, terreno, aquisição ou alienação do informe (nas demais).
- Particionado por `ano`; o catálogo cobre 2016 a 2026, e conferimos as amostras 2016, 2021, 2026.
- O arquivo de 2026 tem 3.885 informes em `inf_trimestral_fii_geral` (1.417 fundos, `Data_Referencia` de 2026-01-31 a 2026-09-30); os de 2021 e 2016 têm 2.566 e 293. `Versao` vai de 1 a 4 em 2026 (3.709 informes na versão 1).
- Este dataset reúne 16 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `inf_trimestral_fii_alienacao_imovel` | 12 | 1.362 | não determinada | alienações de imóveis no trimestre |
| `inf_trimestral_fii_alienacao_terreno` | 10 | 24 | não determinada | alienações de terrenos no trimestre |
| `inf_trimestral_fii_aquisicao_imovel` | 11 | 1.676 | não determinada | aquisições de imóveis no trimestre |
| `inf_trimestral_fii_aquisicao_terreno` | 9 | 302 | não determinada | aquisições de terrenos no trimestre |
| `inf_trimestral_fii_ativo` | 14 | 38.325 | não determinada | ativos financeiros detidos pelo fundo |
| `inf_trimestral_fii_ativo_garantia_rentabilidade` | 8 | 62 | não determinada | ativos com garantia de rentabilidade (garantidor e percentual garantido) |
| `inf_trimestral_fii_complemento` | 49 | 3.885 | `CNPJ_Fundo_Classe`, `Data_Referencia` | informações complementares (políticas, prazos de vencimento e outras) |
| `inf_trimestral_fii_direito` | 7 | 257 | não determinada | direitos detidos (nome do ativo, valor e principais características) |
| `inf_trimestral_fii_geral` | 41 | 3.885 | `CNPJ_Fundo_Classe`, `Data_Encerramento_Trimestre` | dados gerais do fundo e do administrador |
| `inf_trimestral_fii_imovel` | 20 | 18.212 | não determinada | imóveis da carteira, com endereço e características |
| `inf_trimestral_fii_imovel_desempenho` | 8 | 474 | não determinada | desempenho dos imóveis (justificativa de custo superior ao previsto) |
| `inf_trimestral_fii_imovel_renda_acabado_contrato` | 6 | 6.242 | não determinada | características contratuais dos imóveis para renda acabados |
| `inf_trimestral_fii_imovel_renda_acabado_inquilino` | 8 | 27.560 | não determinada | inquilinos dos imóveis para renda acabados (setor e percentual da receita) |
| `inf_trimestral_fii_rentabilidade_efetiva` | 7 | 360 | não determinada | rentabilidade efetiva mensal |
| `inf_trimestral_fii_resultado_contabil_financeiro` | 96 | 3.885 | `CNPJ_Fundo_Classe`, `Data_Referencia` | resultado contábil e financeiro do trimestre (96 colunas) |
| `inf_trimestral_fii_terreno` | 9 | 1.531 | não determinada | terrenos da carteira |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Fundo` | `CNPJ_Fundo` | texto | CNPJ do fundo/classe (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_Fundo_Classe`) | — | 2016 |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Nome_Imovel` | `Nome_Imovel` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome imovel (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_aquisicao_imovel`, `inf_trimestral_fii_imovel`, `inf_trimestral_fii_imovel_renda_acabado_inquilino`) | — | todo |
| `Endereco` | `Endereco` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_alienacao_terreno`, `inf_trimestral_fii_aquisicao_imovel`, `inf_trimestral_fii_aquisicao_terreno` e mais 2) | — | todo |
| `Data_Alienacao` | `Data_Alienacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data alienacao (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_alienacao_terreno`) | — | todo |
| `Area` | `Area` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: area (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_alienacao_terreno`, `inf_trimestral_fii_aquisicao_imovel`, `inf_trimestral_fii_aquisicao_terreno` e mais 2) | área (unidade não informada no dicionário da CVM) | todo |
| `Numero_Unidades` | `Numero_Unidades` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero unidades (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_aquisicao_imovel`, `inf_trimestral_fii_imovel`) | quantidade | todo |
| `Outras_Caracteristicas_Relevantes` | `Outras_Caracteristicas_Relevantes` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outras caracteristicas relevantes (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_alienacao_terreno`, `inf_trimestral_fii_aquisicao_imovel`, `inf_trimestral_fii_aquisicao_terreno` e mais 2) | — | todo |
| `Percentual_Imovel_Total_Investido` | `Percentual_Imovel_Total_Investido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual imovel total investido (só em: `inf_trimestral_fii_alienacao_imovel`, `inf_trimestral_fii_aquisicao_imovel`, `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Imovel_PL` | `Percentual_Imovel_PL` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual imovel pl (só em: `inf_trimestral_fii_alienacao_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Terreno_Total_Investido` | `Percentual_Terreno_Total_Investido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual terreno total investido (só em: `inf_trimestral_fii_alienacao_terreno`, `inf_trimestral_fii_aquisicao_terreno`, `inf_trimestral_fii_terreno`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Terreno_PL` | `Percentual_Terreno_PL` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual terreno pl (só em: `inf_trimestral_fii_alienacao_terreno`, `inf_trimestral_fii_aquisicao_terreno`, `inf_trimestral_fii_terreno`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Categoria` | `Categoria` | texto | Categoria (só em: `inf_trimestral_fii_aquisicao_imovel`) | — | todo |
| `Tipo` | `Tipo` | texto | Tipo (só em: `inf_trimestral_fii_ativo`) | — | todo |
| `Emissor` | `Emissor` | texto | Nome do Emissor (só em: `inf_trimestral_fii_ativo`) | — | todo |
| `CNPJ_Emissor` | `CNPJ_Emissor` | texto | CNPJ do emissor (só em: `inf_trimestral_fii_ativo`) | — | todo |
| `Emissao` | `Emissao` | inteiro / texto | Número da Emissão (só em: `inf_trimestral_fii_ativo`) | código ou número de identificação (sem unidade) | todo |
| `Serie` | `Serie` | inteiro / texto | Número da Série (só em: `inf_trimestral_fii_ativo`) | código ou número de identificação (sem unidade) | todo |
| `Codigo_Acao` | `Codigo_Acao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo acao (só em: `inf_trimestral_fii_ativo`) | — | todo |
| `Nome_Ativo` | `Nome_Ativo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome ativo (só em: `inf_trimestral_fii_ativo`, `inf_trimestral_fii_ativo_garantia_rentabilidade`, `inf_trimestral_fii_direito`) | — | todo |
| `Data_Vencimento` | `Data_Vencimento` | texto | Data de Vencimento (só em: `inf_trimestral_fii_ativo`) | — | todo |
| `Quantidade` | `Quantidade` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade (só em: `inf_trimestral_fii_ativo`) | quantidade | todo |
| `Valor` | `Valor` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor (só em: `inf_trimestral_fii_ativo`, `inf_trimestral_fii_direito`) | moeda (R$) | todo |
| `Percentual_Garantido_Relativo` | `Percentual_Garantido_Relativo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual garantido relativo (só em: `inf_trimestral_fii_ativo_garantia_rentabilidade`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Garantidor` | `Garantidor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: garantidor (só em: `inf_trimestral_fii_ativo_garantia_rentabilidade`) | — | todo |
| `Principais_Caracteristicas_Garantia` | `Principais_Caracteristicas_Garantia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: principais caracteristicas garantia (só em: `inf_trimestral_fii_ativo_garantia_rentabilidade`) | — | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_Ate_3Meses` | `Percentual_Vencimento_Valor_Total_Faixa_Ate_3Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa ate 3meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_Ate_3Meses` | `Percentual_Vencimento_Receita_FII_Faixa_Ate_3Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa ate 3meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_3a6Meses` | `Percentual_Vencimento_Valor_Total_Faixa_3a6Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 3a6meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_3a6Meses` | `Percentual_Vencimento_Receita_FII_Faixa_3a6Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 3a6meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_6a9Meses` | `Percentual_Vencimento_Valor_Total_Faixa_6a9Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 6a9meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_6a9Meses` | `Percentual_Vencimento_Receita_FII_Faixa_6a9Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 6a9meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_9a12Meses` | `Percentual_Vencimento_Valor_Total_Faixa_9a12Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 9a12meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_9a12Meses` | `Percentual_Vencimento_Receita_FII_Faixa_9a12Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 9a12meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_12a15Meses` | `Percentual_Vencimento_Valor_Total_Faixa_12a15Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 12a15meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_12a15Meses` | `Percentual_Vencimento_Receita_FII_Faixa_12a15Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 12a15meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_15a18Meses` | `Percentual_Vencimento_Valor_Total_Faixa_15a18Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 15a18meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_15a18Meses` | `Percentual_Vencimento_Receita_FII_Faixa_15a18Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 15a18meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_18a21Meses` | `Percentual_Vencimento_Valor_Total_Faixa_18a21Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 18a21meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_18a21Meses` | `Percentual_Vencimento_Receita_FII_Faixa_18a21Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 18a21meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_21a24Meses` | `Percentual_Vencimento_Valor_Total_Faixa_21a24Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 21a24meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_21a24Meses` | `Percentual_Vencimento_Receita_FII_Faixa_21a24Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 21a24meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_24a27Meses` | `Percentual_Vencimento_Valor_Total_Faixa_24a27Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 24a27meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_24a27Meses` | `Percentual_Vencimento_Receita_FII_Faixa_24a27Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 24a27meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_27a30Meses` | `Percentual_Vencimento_Valor_Total_Faixa_27a30Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 27a30meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_27a30Meses` | `Percentual_Vencimento_Receita_FII_Faixa_27a30Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 27a30meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_30a33Meses` | `Percentual_Vencimento_Valor_Total_Faixa_30a33Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 30a33meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_30a33Meses` | `Percentual_Vencimento_Receita_FII_Faixa_30a33Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 30a33meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_33a36Meses` | `Percentual_Vencimento_Valor_Total_Faixa_33a36Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa 33a36meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_33a36Meses` | `Percentual_Vencimento_Receita_FII_Faixa_33a36Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa 33a36meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_Acima_36Meses` | `Percentual_Vencimento_Valor_Total_Faixa_Acima_36Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa acima 36meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_Acima_36Meses` | `Percentual_Vencimento_Receita_FII_Faixa_Acima_36Meses` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa acima 36meses (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Valor_Total_Faixa_Indeterminado` | `Percentual_Vencimento_Valor_Total_Faixa_Indeterminado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento valor total faixa indeterminado (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vencimento_Receita_FII_Faixa_Indeterminado` | `Percentual_Vencimento_Receita_FII_Faixa_Indeterminado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vencimento receita fii faixa indeterminado (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Valor_Total_IGPM` | `Percentual_Indexador_Valor_Total_IGPM` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador valor total igpm (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Receita_FII_IGPM` | `Percentual_Indexador_Receita_FII_IGPM` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador receita fii igpm (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Valor_Total_INPC` | `Percentual_Indexador_Valor_Total_INPC` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador valor total inpc (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Receita_FII_INPC` | `Percentual_Indexador_Receita_FII_INPC` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador receita fii inpc (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Valor_Total_IPCA` | `Percentual_Indexador_Valor_Total_IPCA` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador valor total ipca (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Receita_FII_IPCA` | `Percentual_Indexador_Receita_FII_IPCA` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador receita fii ipca (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Valor_Total_INCC` | `Percentual_Indexador_Valor_Total_INCC` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador valor total incc (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Indexador_Receita_FII_INCC` | `Percentual_Indexador_Receita_FII_INCC` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual indexador receita fii incc (só em: `inf_trimestral_fii_complemento`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Caracteristicas_Contratuais` | `Caracteristicas_Contratuais` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: caracteristicas contratuais (só em: `inf_trimestral_fii_complemento`, `inf_trimestral_fii_imovel_renda_acabado_contrato`) | — | todo |
| `Politica_Contratacao_Seguro_Imovel_Renda_Acabado` | `Politica_Contratacao_Seguro_Imovel_Renda_Acabado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica contratacao seguro imovel renda acabado (só em: `inf_trimestral_fii_complemento`) | — | todo |
| `Politica_Contratacao_Seguro_Imovel_Renda_Construcao` | `Politica_Contratacao_Seguro_Imovel_Renda_Construcao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica contratacao seguro imovel renda construcao (só em: `inf_trimestral_fii_complemento`) | — | todo |
| `Politica_Contratacao_Seguro_Imovel_Venda_Acabado` | `Politica_Contratacao_Seguro_Imovel_Venda_Acabado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica contratacao seguro imovel venda acabado (só em: `inf_trimestral_fii_complemento`) | — | todo |
| `Politica_Contratacao_Seguro_Imovel_Venda_Construcao` | `Politica_Contratacao_Seguro_Imovel_Venda_Construcao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: politica contratacao seguro imovel venda construcao (só em: `inf_trimestral_fii_complemento`) | — | todo |
| `Ativo_Liquidez_Valor_Disponibilidades` | `Ativo_Liquidez_Valor_Disponibilidades` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo liquidez valor disponibilidades (só em: `inf_trimestral_fii_complemento`) | moeda (R$) | todo |
| `Ativo_Liquidez_Valor_Titulos_Publicos` | `Ativo_Liquidez_Valor_Titulos_Publicos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo liquidez valor titulos publicos (só em: `inf_trimestral_fii_complemento`) | moeda (R$) | todo |
| `Ativo_Liquidez_Valor_Titulos_Privados` | `Ativo_Liquidez_Valor_Titulos_Privados` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo liquidez valor titulos privados (só em: `inf_trimestral_fii_complemento`) | moeda (R$) | todo |
| `Ativo_Liquidez_Valor_Fundos_Renda_Fixa` | `Ativo_Liquidez_Valor_Fundos_Renda_Fixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo liquidez valor fundos renda fixa (só em: `inf_trimestral_fii_complemento`) | moeda (R$) | todo |
| `Principais_Caracteristicas` | `Principais_Caracteristicas` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: principais caracteristicas (só em: `inf_trimestral_fii_direito`) | — | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Nome_Fundo` | `Nome_Fundo` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Nome_Fundo_Classe`) (só em: `inf_trimestral_fii_geral`) | — | 2016 |
| `Data_Funcionamento` | `Data_Funcionamento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data funcionamento (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Publico_Alvo` | `Publico_Alvo` | texto | Público-alvo (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Codigo_ISIN` | `Codigo_ISIN` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo isin (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Quantidade_Cotas_Emitidas` | `Quantidade_Cotas_Emitidas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade cotas emitidas (só em: `inf_trimestral_fii_geral`) | quantidade | todo |
| `Fundo_Exclusivo` | `Fundo_Exclusivo` | texto | Indica se é fundo exclusivo (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Fundo_Nao_Listado_Exclusivo` | `Fundo_Nao_Listado_Exclusivo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: fundo nao listado exclusivo (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Cotistas_Vinculo_Familiar` | `Cotistas_Vinculo_Familiar` | texto | Indica se os cotistas possuem vínculo familiar ou societário familiar (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Mandato` | `Mandato` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mandato (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Segmento_Atuacao` | `Segmento_Atuacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: segmento atuacao (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Tipo_Gestao` | `Tipo_Gestao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo gestao (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Prazo_Duracao` | `Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: prazo duracao (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Data_Prazo_Duracao` | `Data_Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data prazo duracao (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Encerramento_Exercicio_Social` | `Encerramento_Exercicio_Social` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: encerramento exercicio social (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Mercado_Negociacao_Bolsa` | `Mercado_Negociacao_Bolsa` | texto | Indica se o mercado de negociação das cotas é Bolsa (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Mercado_Negociacao_MBO` | `Mercado_Negociacao_MBO` | texto | Indica se o mercado de negociação das cotas é MBO (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Mercado_Negociacao_MB` | `Mercado_Negociacao_MB` | texto | Indica se o mercado de negociação das cotas é MB (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Entidade_Administradora_BVMF` | `Entidade_Administradora_BVMF` | texto | Indica se a entidade administradora de mercado organizado é BVMF (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Entidade_Administradora_CETIP` | `Entidade_Administradora_CETIP` | texto | Indica se a entidade administradora de mercado organizado é CETIP (só em: `inf_trimestral_fii_geral`) | S/N | todo |
| `Nome_Administrador` | `Nome_Administrador` | texto | Nome do administrador (só em: `inf_trimestral_fii_geral`) | — | todo |
| `CNPJ_Administrador` | `CNPJ_Administrador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj administrador (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Logradouro` | `Logradouro` | texto | Logradouro (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Numero` | `Numero` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: numero (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Complemento` | `Complemento` | texto | Complemento (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Bairro` | `Bairro` | texto | Bairro (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Cidade` | `Cidade` | texto | Cidade (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Estado` | `Estado` | texto | Estado (só em: `inf_trimestral_fii_geral`) | — | todo |
| `CEP` | `CEP` | texto | CEP (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Telefone1` | `Telefone1` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone1 (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Telefone2` | `Telefone2` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone2 (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Telefone3` | `Telefone3` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: telefone3 (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Site` | `Site` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: site (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Email` | `Email` | texto | Endereço de e-mail (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Data_Encerramento_Trimestre` | `Data_Encerramento_Trimestre` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data encerramento trimestre (só em: `inf_trimestral_fii_geral`) | — | todo |
| `Classe` | `Classe` | texto | Classe (só em: `inf_trimestral_fii_imovel`, `inf_trimestral_fii_imovel_desempenho`) | — | todo |
| `Percentual_Vacancia` | `Percentual_Vacancia` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vacancia (só em: `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Inadimplencia` | `Percentual_Inadimplencia` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual inadimplencia (só em: `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Receitas_FII` | `Percentual_Receitas_FII` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual receitas fii (só em: `inf_trimestral_fii_imovel`, `inf_trimestral_fii_imovel_renda_acabado_inquilino`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Locado` | `Percentual_Locado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual locado (só em: `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Vendido` | `Percentual_Vendido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual vendido (só em: `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Conclusao_Obras_Realizado` | `Percentual_Conclusao_Obras_Realizado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual conclusao obras realizado (só em: `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Conclusao_Obras_Previsto` | `Percentual_Conclusao_Obras_Previsto` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual conclusao obras previsto (só em: `inf_trimestral_fii_imovel`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Custo_Construcao_Realizado` | `Custo_Construcao_Realizado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: custo construcao realizado (só em: `inf_trimestral_fii_imovel`) | moeda (R$) | todo |
| `Custo_Construcao_Previsto` | `Custo_Construcao_Previsto` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: custo construcao previsto (só em: `inf_trimestral_fii_imovel`) | moeda (R$) | todo |
| `Nome_Endereco_Imovel` | `Nome_Endereco_Imovel` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome endereco imovel (só em: `inf_trimestral_fii_imovel_desempenho`, `inf_trimestral_fii_imovel_renda_acabado_contrato`) | — | todo |
| `Justificativa_Evolucao_Inferior_Previsto` | `Justificativa_Evolucao_Inferior_Previsto` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: justificativa evolucao inferior previsto (só em: `inf_trimestral_fii_imovel_desempenho`) | — | todo |
| `Justificativa_Custo_Superior_Previsto` | `Justificativa_Custo_Superior_Previsto` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: justificativa custo superior previsto (só em: `inf_trimestral_fii_imovel_desempenho`) | — | todo |
| `Setor_Atuacao` | `Setor_Atuacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: setor atuacao (só em: `inf_trimestral_fii_imovel_renda_acabado_inquilino`) | — | todo |
| `Percentual_Receita_Imovel` | `Percentual_Receita_Imovel` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual receita imovel (só em: `inf_trimestral_fii_imovel_renda_acabado_inquilino`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Mes_Referencia` | `Mes_Referencia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mes referencia (só em: `inf_trimestral_fii_rentabilidade_efetiva`) | — | todo |
| `Percentual_Rentabilidade_Efetiva_Mes` | `Percentual_Rentabilidade_Efetiva_Mes` | decimal | Percentual de Rentabilidade Efetiva Mensal (só em: `inf_trimestral_fii_rentabilidade_efetiva`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Rentabilidade_Auferida_Ausencia_Garantia` | `Percentual_Rentabilidade_Auferida_Ausencia_Garantia` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual rentabilidade auferida ausencia garantia (só em: `inf_trimestral_fii_rentabilidade_efetiva`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Receita_Venda_Estoque_Contabil` | `Receita_Venda_Estoque_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita venda estoque contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Venda_Estoque_Financeiro` | `Receita_Venda_Estoque_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita venda estoque financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Custo_Estoque_Contabil` | `Custo_Estoque_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: custo estoque contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Custo_Estoque_Financeiro` | `Custo_Estoque_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: custo estoque financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Realizacao_Estoque_Contabil` | `Ajuste_Realizacao_Estoque_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste realizacao estoque contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Realizacao_Estoque_Financeiro` | `Ajuste_Realizacao_Estoque_Financeiro` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste realizacao estoque financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_Estoque_Contabil` | `Outras_Receitas_Despesas_Estoque_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas estoque contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_Estoque_Financeiro` | `Outras_Receitas_Despesas_Estoque_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas estoque financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Estoque_Contabil` | `Resultado_Liquido_Estoque_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido estoque contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Estoque_Financeiro` | `Resultado_Liquido_Estoque_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido estoque financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Aluguel_Investimento_Contabil` | `Receita_Aluguel_Investimento_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita aluguel investimento contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Aluguel_Investimento_Financeiro` | `Receita_Aluguel_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita aluguel investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Manutencao_Investimento_Contabil` | `Despesa_Manutencao_Investimento_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa manutencao investimento contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Manutencao_Investimento_Financeiro` | `Despesa_Manutencao_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa manutencao investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Venda_Investimento_Contabil` | `Receita_Venda_Investimento_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita venda investimento contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Venda_Investimento_Financeiro` | `Receita_Venda_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita venda investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Custo_Investimento_Contabil` | `Custo_Investimento_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: custo investimento contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Custo_Investimento_Financeiro` | `Custo_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: custo investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Justo_Investimento_Contabil` | `Ajuste_Justo_Investimento_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste justo investimento contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Justo_Investimento_Financeiro` | `Ajuste_Justo_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste justo investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_Investimento_Contabil` | `Outras_Receitas_Despesas_Investimento_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas investimento contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_Investimento_Financeiro` | `Outras_Receitas_Despesas_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Renda_Contabil` | `Resultado_Liquido_Renda_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido renda contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Renda_Investimento_Financeiro` | `Resultado_Liquido_Renda_Investimento_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido renda investimento financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Juros_TVM_Contabil` | `Receita_Juros_TVM_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita juros tvm contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Juros_TVM_Financeiro` | `Receita_Juros_TVM_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita juros tvm financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Justo_TVM_Contabil` | `Ajuste_Justo_TVM_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste justo tvm contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Justo_TVM_Financeiro` | `Ajuste_Justo_TVM_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste justo tvm financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Venda_TVM_Contabil` | `Resultado_Venda_TVM_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado venda tvm contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Venda_TVM_Financeiro` | `Resultado_Venda_TVM_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado venda tvm financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_TVM_Contabil` | `Outras_Receitas_Despesas_TVM_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas tvm contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_TVM_Financeiro` | `Outras_Receitas_Despesas_TVM_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas tvm financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_TVM_Contabil` | `Resultado_Liquido_TVM_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido tvm contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_TVM_Financeiro` | `Resultado_Liquido_TVM_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido tvm financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Total_Contabil` | `Resultado_Liquido_Total_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido total contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Total_Financeiro` | `Resultado_Liquido_Total_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido total financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Juros_Aplicacao_Contabil` | `Receita_Juros_Aplicacao_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita juros aplicacao contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Receita_Juros_Aplicacao_Financeiro` | `Receita_Juros_Aplicacao_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: receita juros aplicacao financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Justo_Aplicacao_Contabil` | `Ajuste_Justo_Aplicacao_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste justo aplicacao contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Ajuste_Justo_Aplicacao_Financeiro` | `Ajuste_Justo_Aplicacao_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ajuste justo aplicacao financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Venda_Aplicacao_Contabil` | `Resultado_Venda_Aplicacao_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado venda aplicacao contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Venda_Aplicacao_Financeiro` | `Resultado_Venda_Aplicacao_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado venda aplicacao financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_Aplicacao_Contabil` | `Outras_Receitas_Despesas_Aplicacao_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas aplicacao contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Despesas_Aplicacao_Financeiro` | `Outras_Receitas_Despesas_Aplicacao_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas despesas aplicacao financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Recurso_Liquidez_Contabil` | `Resultado_Liquido_Recurso_Liquidez_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido recurso liquidez contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Recurso_Liquidez_Financeiro` | `Resultado_Liquido_Recurso_Liquidez_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido recurso liquidez financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Derivativos_Contabil` | `Resultado_Liquido_Derivativos_Contabil` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido derivativos contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Liquido_Derivativos_Financeiro` | `Resultado_Liquido_Derivativos_Financeiro` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado liquido derivativos financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Taxa_Administracao_Contabil` | `Taxa_Administracao_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa administracao contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Taxa_Administracao_Financeiro` | `Taxa_Administracao_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa administracao financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Taxa_Desempenho_Contabil` | `Taxa_Desempenho_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa desempenho contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Taxa_Desempenho_Financeiro` | `Taxa_Desempenho_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa desempenho financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Despesa_Consultoria_Especializada_Contabil` | `Despesa_Consultoria_Especializada_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa consultoria especializada contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Consultoria_Especializada_Financeiro` | `Despesa_Consultoria_Especializada_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa consultoria especializada financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Empresa_Especializada_Contabil` | `Despesa_Empresa_Especializada_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa empresa especializada contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Empresa_Especializada_Financeiro` | `Despesa_Empresa_Especializada_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa empresa especializada financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Formador_Mercado_Contabil` | `Despesa_Formador_Mercado_Contabil` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa formador mercado contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Formador_Mercado_Financeiro` | `Despesa_Formador_Mercado_Financeiro` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa formador mercado financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Custodia_Contabil` | `Despesa_Custodia_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa custodia contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Custodia_Financeiro` | `Despesa_Custodia_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa custodia financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Auditoria_Independente_Contabil` | `Despesa_Auditoria_Independente_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa auditoria independente contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Auditoria_Independente_Financeiro` | `Despesa_Auditoria_Independente_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa auditoria independente financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Representantes_Cotistas_Contabil` | `Despesa_Representantes_Cotistas_Contabil` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa representantes cotistas contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Representantes_Cotistas_Financeiro` | `Despesa_Representantes_Cotistas_Financeiro` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa representantes cotistas financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Taxa_Imposto_Contribuicao_Contabil` | `Taxa_Imposto_Contribuicao_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa imposto contribuicao contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Taxa_Imposto_Contribuicao_Financeiro` | `Taxa_Imposto_Contribuicao_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa imposto contribuicao financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Despesa_Comissoes_Emolumentos_Contabil` | `Despesa_Comissoes_Emolumentos_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa comissoes emolumentos contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Comissoes_Emolumentos_Financeiro` | `Despesa_Comissoes_Emolumentos_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa comissoes emolumentos financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Honorarios_Defesas_Contabil` | `Despesa_Honorarios_Defesas_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa honorarios defesas contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Honorarios_Defesas_Financeiro` | `Despesa_Honorarios_Defesas_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa honorarios defesas financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Contratos_Seguros_Contabil` | `Despesa_Contratos_Seguros_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa contratos seguros contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Contratos_Seguros_Financeiro` | `Despesa_Contratos_Seguros_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa contratos seguros financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Avaliacoes_Contabil` | `Despesa_Avaliacoes_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa avaliacoes contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Avaliacoes_Financeiro` | `Despesa_Avaliacoes_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa avaliacoes financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Taxa_Ingresso_Saida_Cotista_Contabil` | `Taxa_Ingresso_Saida_Cotista_Contabil` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa ingresso saida cotista contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Taxa_Ingresso_Saida_Cotista_Financeiro` | `Taxa_Ingresso_Saida_Cotista_Financeiro` | decimal / inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa ingresso saida cotista financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Despesa_Registro_Cartorio_Contabil` | `Despesa_Registro_Cartorio_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa registro cartorio contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Despesa_Registro_Cartorio_Financeiro` | `Despesa_Registro_Cartorio_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: despesa registro cartorio financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Depesas_Contabil` | `Outras_Receitas_Depesas_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas depesas contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Outras_Receitas_Depesas_Financeiro` | `Outras_Receitas_Depesas_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outras receitas depesas financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Total_Receitas_Despesas_Contabil` | `Total_Receitas_Despesas_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total receitas despesas contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Total_Receitas_Despesas_Financeiro` | `Total_Receitas_Despesas_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total receitas despesas financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Trimestral_Liquido_Contabil` | `Resultado_Trimestral_Liquido_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado trimestral liquido contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Trimestral_Liquido_Financeiro` | `Resultado_Trimestral_Liquido_Financeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado trimestral liquido financeiro (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Financeiro_Liquido_Acumulado` | `Resultado_Financeiro_Liquido_Acumulado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado financeiro liquido acumulado (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Resultado_Financeiro_Liquido_Acumulado_95` | `Resultado_Financeiro_Liquido_Acumulado_95` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: resultado financeiro liquido acumulado 95 (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Parcela_Rendimento_Retido` | `Parcela_Rendimento_Retido` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: parcela rendimento retido (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | — | todo |
| `Lucro_Contabil` | `Lucro_Contabil` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: lucro contabil (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Rendimentos_Declarados` | `Rendimentos_Declarados` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimentos declarados (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Rendimentos_Pagos_Antecipadamente` | `Rendimentos_Pagos_Antecipadamente` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimentos pagos antecipadamente (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Rendimento_Liquido_Pagar` | `Rendimento_Liquido_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimento liquido pagar (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | moeda (R$) | todo |
| `Percentual_Resultado_Financeiro_Liquido_Declarado` | `Percentual_Resultado_Financeiro_Liquido_Declarado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual resultado financeiro liquido declarado (só em: `inf_trimestral_fii_resultado_contabil_financeiro`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `CNPJ_Fundo_Classe` | `CNPJ_Fundo_Classe` | texto | CNPJ do fundo/classe | — | 2021 a 2026 |
| `Tipo_Fundo_Classe` | `Tipo_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo fundo classe (só em: `inf_trimestral_fii_geral`) | — | 2021 a 2026 |
| `Nome_Fundo_Classe` | `Nome_Fundo_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome fundo classe (só em: `inf_trimestral_fii_geral`) | — | 2021 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fii-inf-trim`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Várias versões por fundo e trimestre.** O arquivo traz cada reapresentação (`Versao`); para a posição vigente, escolha a maior `Versao` de cada `CNPJ_Fundo_Classe` e `Data_Referencia`.
- **Datas de referência fora do fim do trimestre.** Em `inf_trimestral_fii_geral` (arquivo de 2026), 14 das 3.885 linhas têm `Data_Referencia` diferente do último dia do trimestre (2026-01-31, 2026-03-30 e 2026-06-20); a tabela traz também `Data_Encerramento_Trimestre`, com valores como 2026-03-01 e 2026-06-03. Confira as duas datas antes de agrupar por trimestre.
- **Tabelas de itens repetem linhas.** As tabelas de imóveis, inquilinos e contratos têm linhas inteiramente repetidas (587 em `inf_trimestral_fii_imovel_renda_acabado_inquilino` e 210 em `..._contrato` no arquivo de 2026); remova duplicatas antes de contar.
- **CNPJ do administrador só com dígitos; `CNPJ_Emissor` misto.** `CNPJ_Administrador` não tem máscara; `CNPJ_Emissor` mistura CNPJ com e sem máscara.
- **Texto com espaços nas pontas.** `Emissor`, `CNPJ_Emissor`, `Nome_Ativo`, `Nome_Imovel` e `Endereco` têm espaços no início ou no fim de alguns valores; aplique `trim`.
- **Tipo inferido varia entre arquivos.** 11 coluna(s) (`Emissao`, `Serie`, `Ajuste_Realizacao_Estoque_Financeiro`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.
- **Linhas repetidas.** No arquivo mais recente convertido há linhas inteiramente repetidas em: `inf_trimestral_fii_alienacao_imovel` (40), `inf_trimestral_fii_aquisicao_imovel` (13), `inf_trimestral_fii_imovel_renda_acabado_contrato` (210), `inf_trimestral_fii_imovel_renda_acabado_inquilino` (587). Remova as duplicatas antes de contar ou somar.

## Exemplos

Informes trimestrais por data de referência, só a última versão de cada fundo.

```python
import duckdb

duckdb.sql("""
    SELECT Data_Referencia, count(DISTINCT CNPJ_Fundo_Classe) AS fundos
    FROM read_parquet('lake/cvm/fii-inf-trim/ano=2026/*__inf_trimestral_fii_geral_2026.parquet')
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fii-doc-inf_trimestral
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FII/DOC/INF_TRIMESTRAL/
