---
dataset:
  id: securit-cri
  fonte: cvm
  titulo: "Securitizadoras: Documentos: Demonstrações Financeiras e Informe Mensal de CRI (CVM)"
  resumo: "Securitização de Certificados de Recebíveis Imobiliários (CRI): as demonstrações financeiras anuais dos certificados (`dfin_cri`) e o informe mensal de cada CRI (`inf_mensal_cri`), em doze tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cri
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cri"
  periodicidade: "anual (um arquivo por ano, com um informe por mês); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2018, fim: em-curso}
  unidade: "uma demonstração financeira entregue (em `dfin_cri`) ou o informe mensal de um certificado em uma competência e versão (nas tabelas `inf_mensal_cri_*`)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (informe, `Data_Referencia` no primeiro dia do mês) e anual (demonstrações financeiras), em arquivos anuais"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 263}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    Ativo: "moeda (R$)"
    Ativo_Circulante: "moeda (R$)"
    Ativo_Circulante_Disponibilidades: "moeda (R$)"
    Ativo_Circulante_Aplicacoes: "moeda (R$)"
    Ativo_Circulante_Creditos: "moeda (R$)"
    Ativo_Circulante_Outros: "moeda (R$)"
    Ativo_Nao_Circulante: "moeda (R$)"
    Ativo_Nao_Circulante_Aplicacoes: "moeda (R$)"
    Ativo_Nao_Circulante_Creditos: "moeda (R$)"
    Ativo_Nao_Circulante_Outros: "moeda (R$)"
    Creditos: "moeda (R$)"
    Creditos_A_Vencer_Sem_Parcelas_Atraso: "moeda (R$)"
    Creditos_A_Vencer_Com_Parcelas_Atraso: "moeda (R$)"
    Creditos_Vencidos: "moeda (R$)"
    Reducao_Valor_Recuperacao: "moeda (R$)"
    Caixa_Equivalentes: "moeda (R$)"
    Caixa_Titulos_Publicos_Federais: "moeda (R$)"
    Caixa_Cotas_Fundos: "moeda (R$)"
    Caixa_Operacoes_Compromissadas: "moeda (R$)"
    Caixa_Outros: "moeda (R$)"
    Ativo_Derivativos: "moeda (R$)"
    Ativo_Contratos_Termo: "moeda (R$)"
    Ativo_Futuros: "moeda (R$)"
    Ativo_Opcoes: "moeda (R$)"
    Ativo_Swap: "moeda (R$)"
    Outros_Ativos: "moeda (R$)"
    Passivo: "moeda (R$)"
    Passivo_Circulante: "moeda (R$)"
    Passivo_Circulante_Valores_Mobiliarios: "moeda (R$)"
    Passivo_Circulante_Outros: "moeda (R$)"
    Passivo_Nao_Circulante: "moeda (R$)"
    Passivo_Nao_Circulante_Valores_Mobiliarios: "moeda (R$)"
    Passivo_Nao_Circulante_Outros: "moeda (R$)"
    Passivo_Derivativos: "moeda (R$)"
    Passivo_Contratos_Termo: "moeda (R$)"
    Passivo_Futuros: "moeda (R$)"
    Passivo_Opcoes: "moeda (R$)"
    Passivo_Swap: "moeda (R$)"
    Valor_Atualizado_Emissao: "moeda (R$)"
    Reducao_Valor_Emissao: "moeda (R$)"
    Outros_Passivos: "moeda (R$)"
    Companhia_Securitizadora_Emissora: "moeda (R$)"
    Total_Recebimentos: "moeda (R$)"
    Pagamentos_Despesas_Comissoes: "moeda (R$)"
    Senior_Pagamentos: "moeda (R$)"
    Senior_Amortizacao_Principal: "moeda (R$)"
    Senior_Juros: "moeda (R$)"
    Subordinada_Pagamentos: "moeda (R$)"
    Subordinada_Amortizacao_Principal: "moeda (R$)"
    Subordinada_Juros: "moeda (R$)"
    Outros_Pagamentos_Recebimentos: "moeda (R$)"
    Suficiencia_Insuficiencia_Caixa: "moeda (R$)"
    Premio_Subordinacao: "moeda (R$)"
    Valor_Securitizadora: "moeda (R$)"
    Valor_Fundo_Despesa: "moeda (R$)"
    Valor_Fundo_Reforco: "moeda (R$)"
    Outros_Valores: "moeda (R$)"
    Valor_Pagamentos_Contratuais: "moeda (R$)"
    Valor_Pagamentos_Contratuais_Senior: "moeda (R$)"
    Valor_Pagamentos_Contratuais_Subordinada: "moeda (R$)"
    Creditos_Vinculados: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_Ate30Dias: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_31a60Dias: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_61a90Dias: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_91a120Dias: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_121a150Dias: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_151a180Dias: "moeda (R$)"
    Creditos_Vinculados_Prazo_Vencimento_Acima180Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_Ate30Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_31a60Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_61a90Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_91a120Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_121a150Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_151a180Dias: "moeda (R$)"
    Creditos_Vinculados_Inadimplentes_Acima180Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos: "moeda (R$)"
    Creditos_Vinculados_Pagos_Ate30Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos_31a60Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos_61a90Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos_91a120Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos_121a150Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos_151a180Dias: "moeda (R$)"
    Creditos_Vinculados_Pagos_Acima180Dias: "moeda (R$)"
    Valor: "moeda (R$)"
    Numero_Serie: "código ou número de identificação (sem unidade)"
    Quantidade: "quantidade"
    Total_Integralizado: "moeda (R$)"
    Quantidade_Certificados: "quantidade"
    Valor_Certificados: "moeda (R$)"
    Rendimentos: "moeda (R$)"
    Amortizacoes: "moeda (R$)"
    Rentabilidade: "percentual (%)"
    Nivel_Subordinacao: "moeda (R$)"
    Indice_Subordinacao_Minimo: "índice (sem unidade)"
    Indice_Subordinacao_Data_Base: "índice (sem unidade)"
    Parcelas_Atraso: "quantidade (parcelas)"
    Creditos_Natureza_Economica: "moeda (R$)"
    Creditos_Incorporacao_Imobiliaria: "moeda (R$)"
    Creditos_Alugueis: "moeda (R$)"
    Creditos_Aquisicao_Imoveis: "moeda (R$)"
    Creditos_Loteamento: "moeda (R$)"
    Creditos_Multipropriedade: "moeda (R$)"
    Creditos_Home_Equity: "moeda (R$)"
    Creditos_Outros: "moeda (R$)"
    A_Vencer: "moeda (R$)"
    A_Vencer_Ate30Dias: "moeda (R$)"
    A_Vencer_31a60Dias: "moeda (R$)"
    A_Vencer_61a90Dias: "moeda (R$)"
    A_Vencer_91a120Dias: "moeda (R$)"
    A_Vencer_121a150Dias: "moeda (R$)"
    A_Vencer_151a180Dias: "moeda (R$)"
    A_Vencer_181a360Dias: "moeda (R$)"
    A_Vencer_Acima361Dias: "moeda (R$)"
    Nao_Pagos: "moeda (R$)"
    Nao_Pagos_Ate30Dias: "moeda (R$)"
    Nao_Pagos_31a60Dias: "moeda (R$)"
    Nao_Pagos_61a90Dias: "moeda (R$)"
    Nao_Pagos_91a120Dias: "moeda (R$)"
    Nao_Pagos_121a150Dias: "moeda (R$)"
    Nao_Pagos_151a180Dias: "moeda (R$)"
    Nao_Pagos_181a360Dias: "moeda (R$)"
    Nao_Pagos_Acima361Dias: "moeda (R$)"
    Pre_Pagamentos: "moeda (R$)"
    Pre_Pagamento_Lastro: "moeda (R$)"
    Dividas_Emissor_Securitizadora: "moeda (R$)"
    Percentual_Risco_Cedentes: "percentual (%)"
    Percentual_Outras_Garantias: "percentual (%)"
    Percentual_Garantias_Exceto_Coobrigacao: "percentual (%)"
    Relacao_Total_Emissao: "moeda (R$)"
    Maior_Devedor: "moeda (R$)"
    Cinco_Maiores_Devedores: "moeda (R$)"
    Dez_Maiores_Devedores: "moeda (R$)"
    Vinte_Maiores_Devedores: "moeda (R$)"
    Maior_Cedente: "moeda (R$)"
    Cinco_Maiores_Cedentes: "moeda (R$)"
    Dez_Maiores_Cedentes: "moeda (R$)"
    Vinte_Maiores_Cedentes: "moeda (R$)"
    Mercado_Termo_Juros: "moeda (R$)"
    Mercado_Termo_Commodities: "moeda (R$)"
    Mercado_Termo_Cambio: "moeda (R$)"
    Mercado_Termo_Outros: "moeda (R$)"
    Futuros_Juros: "moeda (R$)"
    Futuros_Commodities: "moeda (R$)"
    Futuros_Cambio: "moeda (R$)"
    Futuros_Outros: "moeda (R$)"
    Opcoes_Juros: "moeda (R$)"
    Opcoes_Commodities: "moeda (R$)"
    Opcoes_Cambio: "moeda (R$)"
    Opcoes_Outros: "moeda (R$)"
    Swap_Juros: "moeda (R$)"
    Swap_Commodities: "moeda (R$)"
    Swap_Cambio: "moeda (R$)"
    Swap_Outros: "moeda (R$)"
    Pagamento_Despesas: "moeda (R$)"
    Pagamento_Despesas_Ate30Dias: "moeda (R$)"
    Pagamento_Despesas_31a60Dias: "moeda (R$)"
    Pagamento_Despesas_61a90Dias: "moeda (R$)"
    Pagamento_Despesas_91a120Dias: "moeda (R$)"
    Pagamento_Despesas_121a150Dias: "moeda (R$)"
    Pagamento_Despesas_151a180Dias: "moeda (R$)"
    Pagamento_Despesas_181a360Dias: "moeda (R$)"
    Pagamento_Despesas_Acima361Dias: "moeda (R$)"
    Pagamento_Investidores: "moeda (R$)"
    Pagamento_Investidores_Ate30Dias: "moeda (R$)"
    Pagamento_Investidores_31a60Dias: "moeda (R$)"
    Pagamento_Investidores_61a90Dias: "moeda (R$)"
    Pagamento_Investidores_91a120Dias: "moeda (R$)"
    Pagamento_Investidores_121a150Dias: "moeda (R$)"
    Pagamento_Investidores_151a180Dias: "moeda (R$)"
    Pagamento_Investidores_181a360Dias: "moeda (R$)"
    Pagamento_Investidores_Acima361Dias: "moeda (R$)"
    Recebimentos_Creditos: "moeda (R$)"
    Pagamentos_Despesas: "moeda (R$)"
    Pagamentos_Classe_Senior: "moeda (R$)"
    Pagamentos_Classe_Senior_Amortizacao_Principal: "moeda (R$)"
    Pagamentos_Classe_Senior_Juros: "moeda (R$)"
    Pagamentos_Classe_Subordinada_Mezanino: "moeda (R$)"
    Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal: "moeda (R$)"
    Pagamentos_Classe_Subordinada_Mezanino_Juros: "moeda (R$)"
    Pagamentos_Classe_Subordinada_Junior: "moeda (R$)"
    Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal: "moeda (R$)"
    Pagamentos_Classe_Subordinada_Junior_Juros: "moeda (R$)"
    Recebimentos_Alienacao_Caixa: "moeda (R$)"
    Aquisicao_Caixa: "moeda (R$)"
    Aquisicao_Novos_Creditos: "moeda (R$)"
    Outros_Recebimentos: "moeda (R$)"
    Outros_Pagamentos: "moeda (R$)"
    Variacao_Liquida_Caixa: "moeda (R$)"
    Numero_Emissao: "código ou número de identificação (sem unidade)"
    Quantidade_Series: "quantidade"
    Valor_Aquisicao_Credito: "moeda (R$)"
    Anos_Duration_Carteira: "anos"
    Meses_Duration_Carteira: "meses"
    Retentor_Risco: "moeda (R$)"
    Patrimonio_Liquido_Emissao: "moeda (R$)"
    Percentual: "percentual (%)"
  dados_pessoais:
    - {coluna: CNPJ, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Nome, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Securitizadoras: Documentos: Demonstrações Financeiras e Informe Mensal de CRI

## Resumo

Securitização de Certificados de Recebíveis Imobiliários (CRI): as demonstrações financeiras anuais dos certificados (`dfin_cri`) e o informe mensal de cada CRI (`inf_mensal_cri`), em doze tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/securit-cri` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/securit-doc-dfin_cri |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cri |
| Periodicidade | anual (um arquivo por ano, com um informe por mês); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2018 a em-curso |
| Unidade (uma linha) | uma demonstração financeira entregue (em `dfin_cri`) ou o informe mensal de um certificado em uma competência e versão (nas tabelas `inf_mensal_cri_*`) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (informe, `Data_Referencia` no primeiro dia do mês) e anual (demonstrações financeiras), em arquivos anuais |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 263 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `Ativo`: moeda (R$); `Ativo_Circulante`: moeda (R$); `Ativo_Circulante_Disponibilidades`: moeda (R$); `Ativo_Circulante_Aplicacoes`: moeda (R$); `Ativo_Circulante_Creditos`: moeda (R$); `Ativo_Circulante_Outros`: moeda (R$); `Ativo_Nao_Circulante`: moeda (R$); `Ativo_Nao_Circulante_Aplicacoes`: moeda (R$); `Ativo_Nao_Circulante_Creditos`: moeda (R$); `Ativo_Nao_Circulante_Outros`: moeda (R$); `Creditos`: moeda (R$); `Creditos_A_Vencer_Sem_Parcelas_Atraso`: moeda (R$); `Creditos_A_Vencer_Com_Parcelas_Atraso`: moeda (R$); `Creditos_Vencidos`: moeda (R$); `Reducao_Valor_Recuperacao`: moeda (R$); `Caixa_Equivalentes`: moeda (R$); `Caixa_Titulos_Publicos_Federais`: moeda (R$); `Caixa_Cotas_Fundos`: moeda (R$); `Caixa_Operacoes_Compromissadas`: moeda (R$); `Caixa_Outros`: moeda (R$); `Ativo_Derivativos`: moeda (R$); `Ativo_Contratos_Termo`: moeda (R$); `Ativo_Futuros`: moeda (R$); `Ativo_Opcoes`: moeda (R$); `Ativo_Swap`: moeda (R$); `Outros_Ativos`: moeda (R$); `Passivo`: moeda (R$); `Passivo_Circulante`: moeda (R$); `Passivo_Circulante_Valores_Mobiliarios`: moeda (R$); `Passivo_Circulante_Outros`: moeda (R$); `Passivo_Nao_Circulante`: moeda (R$); `Passivo_Nao_Circulante_Valores_Mobiliarios`: moeda (R$); `Passivo_Nao_Circulante_Outros`: moeda (R$); `Passivo_Derivativos`: moeda (R$); `Passivo_Contratos_Termo`: moeda (R$); `Passivo_Futuros`: moeda (R$); `Passivo_Opcoes`: moeda (R$); `Passivo_Swap`: moeda (R$); `Valor_Atualizado_Emissao`: moeda (R$); `Reducao_Valor_Emissao`: moeda (R$); `Outros_Passivos`: moeda (R$); `Companhia_Securitizadora_Emissora`: moeda (R$); `Total_Recebimentos`: moeda (R$); `Pagamentos_Despesas_Comissoes`: moeda (R$); `Senior_Pagamentos`: moeda (R$); `Senior_Amortizacao_Principal`: moeda (R$); `Senior_Juros`: moeda (R$); `Subordinada_Pagamentos`: moeda (R$); `Subordinada_Amortizacao_Principal`: moeda (R$); `Subordinada_Juros`: moeda (R$); `Outros_Pagamentos_Recebimentos`: moeda (R$); `Suficiencia_Insuficiencia_Caixa`: moeda (R$); `Premio_Subordinacao`: moeda (R$); `Valor_Securitizadora`: moeda (R$); `Valor_Fundo_Despesa`: moeda (R$); `Valor_Fundo_Reforco`: moeda (R$); `Outros_Valores`: moeda (R$); `Valor_Pagamentos_Contratuais`: moeda (R$); `Valor_Pagamentos_Contratuais_Senior`: moeda (R$); `Valor_Pagamentos_Contratuais_Subordinada`: moeda (R$); `Creditos_Vinculados`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_Ate30Dias`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_31a60Dias`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_61a90Dias`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_91a120Dias`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_121a150Dias`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_151a180Dias`: moeda (R$); `Creditos_Vinculados_Prazo_Vencimento_Acima180Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes`: moeda (R$); `Creditos_Vinculados_Inadimplentes_Ate30Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes_31a60Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes_61a90Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes_91a120Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes_121a150Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes_151a180Dias`: moeda (R$); `Creditos_Vinculados_Inadimplentes_Acima180Dias`: moeda (R$); `Creditos_Vinculados_Pagos`: moeda (R$); `Creditos_Vinculados_Pagos_Ate30Dias`: moeda (R$); `Creditos_Vinculados_Pagos_31a60Dias`: moeda (R$); `Creditos_Vinculados_Pagos_61a90Dias`: moeda (R$); `Creditos_Vinculados_Pagos_91a120Dias`: moeda (R$); `Creditos_Vinculados_Pagos_121a150Dias`: moeda (R$); `Creditos_Vinculados_Pagos_151a180Dias`: moeda (R$); `Creditos_Vinculados_Pagos_Acima180Dias`: moeda (R$); `Valor`: moeda (R$); `Numero_Serie`: código ou número de identificação (sem unidade); `Quantidade`: quantidade; `Total_Integralizado`: moeda (R$); `Quantidade_Certificados`: quantidade; `Valor_Certificados`: moeda (R$); `Rendimentos`: moeda (R$); `Amortizacoes`: moeda (R$); `Rentabilidade`: percentual (%); `Nivel_Subordinacao`: moeda (R$); `Indice_Subordinacao_Minimo`: índice (sem unidade); `Indice_Subordinacao_Data_Base`: índice (sem unidade); `Parcelas_Atraso`: quantidade (parcelas); `Creditos_Natureza_Economica`: moeda (R$); `Creditos_Incorporacao_Imobiliaria`: moeda (R$); `Creditos_Alugueis`: moeda (R$); `Creditos_Aquisicao_Imoveis`: moeda (R$); `Creditos_Loteamento`: moeda (R$); `Creditos_Multipropriedade`: moeda (R$); `Creditos_Home_Equity`: moeda (R$); `Creditos_Outros`: moeda (R$); `A_Vencer`: moeda (R$); `A_Vencer_Ate30Dias`: moeda (R$); `A_Vencer_31a60Dias`: moeda (R$); `A_Vencer_61a90Dias`: moeda (R$); `A_Vencer_91a120Dias`: moeda (R$); `A_Vencer_121a150Dias`: moeda (R$); `A_Vencer_151a180Dias`: moeda (R$); `A_Vencer_181a360Dias`: moeda (R$); `A_Vencer_Acima361Dias`: moeda (R$); `Nao_Pagos`: moeda (R$); `Nao_Pagos_Ate30Dias`: moeda (R$); `Nao_Pagos_31a60Dias`: moeda (R$); `Nao_Pagos_61a90Dias`: moeda (R$); `Nao_Pagos_91a120Dias`: moeda (R$); `Nao_Pagos_121a150Dias`: moeda (R$); `Nao_Pagos_151a180Dias`: moeda (R$); `Nao_Pagos_181a360Dias`: moeda (R$); `Nao_Pagos_Acima361Dias`: moeda (R$); `Pre_Pagamentos`: moeda (R$); `Pre_Pagamento_Lastro`: moeda (R$); `Dividas_Emissor_Securitizadora`: moeda (R$); `Percentual_Risco_Cedentes`: percentual (%); `Percentual_Outras_Garantias`: percentual (%); `Percentual_Garantias_Exceto_Coobrigacao`: percentual (%); `Relacao_Total_Emissao`: moeda (R$); `Maior_Devedor`: moeda (R$); `Cinco_Maiores_Devedores`: moeda (R$); `Dez_Maiores_Devedores`: moeda (R$); `Vinte_Maiores_Devedores`: moeda (R$); `Maior_Cedente`: moeda (R$); `Cinco_Maiores_Cedentes`: moeda (R$); `Dez_Maiores_Cedentes`: moeda (R$); `Vinte_Maiores_Cedentes`: moeda (R$); `Mercado_Termo_Juros`: moeda (R$); `Mercado_Termo_Commodities`: moeda (R$); `Mercado_Termo_Cambio`: moeda (R$); `Mercado_Termo_Outros`: moeda (R$); `Futuros_Juros`: moeda (R$); `Futuros_Commodities`: moeda (R$); `Futuros_Cambio`: moeda (R$); `Futuros_Outros`: moeda (R$); `Opcoes_Juros`: moeda (R$); `Opcoes_Commodities`: moeda (R$); `Opcoes_Cambio`: moeda (R$); `Opcoes_Outros`: moeda (R$); `Swap_Juros`: moeda (R$); `Swap_Commodities`: moeda (R$); `Swap_Cambio`: moeda (R$); `Swap_Outros`: moeda (R$); `Pagamento_Despesas`: moeda (R$); `Pagamento_Despesas_Ate30Dias`: moeda (R$); `Pagamento_Despesas_31a60Dias`: moeda (R$); `Pagamento_Despesas_61a90Dias`: moeda (R$); `Pagamento_Despesas_91a120Dias`: moeda (R$); `Pagamento_Despesas_121a150Dias`: moeda (R$); `Pagamento_Despesas_151a180Dias`: moeda (R$); `Pagamento_Despesas_181a360Dias`: moeda (R$); `Pagamento_Despesas_Acima361Dias`: moeda (R$); `Pagamento_Investidores`: moeda (R$); `Pagamento_Investidores_Ate30Dias`: moeda (R$); `Pagamento_Investidores_31a60Dias`: moeda (R$); `Pagamento_Investidores_61a90Dias`: moeda (R$); `Pagamento_Investidores_91a120Dias`: moeda (R$); `Pagamento_Investidores_121a150Dias`: moeda (R$); `Pagamento_Investidores_151a180Dias`: moeda (R$); `Pagamento_Investidores_181a360Dias`: moeda (R$); `Pagamento_Investidores_Acima361Dias`: moeda (R$); `Recebimentos_Creditos`: moeda (R$); `Pagamentos_Despesas`: moeda (R$); `Pagamentos_Classe_Senior`: moeda (R$); `Pagamentos_Classe_Senior_Amortizacao_Principal`: moeda (R$); `Pagamentos_Classe_Senior_Juros`: moeda (R$); `Pagamentos_Classe_Subordinada_Mezanino`: moeda (R$); `Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal`: moeda (R$); `Pagamentos_Classe_Subordinada_Mezanino_Juros`: moeda (R$); `Pagamentos_Classe_Subordinada_Junior`: moeda (R$); `Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal`: moeda (R$); `Pagamentos_Classe_Subordinada_Junior_Juros`: moeda (R$); `Recebimentos_Alienacao_Caixa`: moeda (R$); `Aquisicao_Caixa`: moeda (R$); `Aquisicao_Novos_Creditos`: moeda (R$); `Outros_Recebimentos`: moeda (R$); `Outros_Pagamentos`: moeda (R$); `Variacao_Liquida_Caixa`: moeda (R$); `Numero_Emissao`: código ou número de identificação (sem unidade); `Quantidade_Series`: quantidade; `Valor_Aquisicao_Credito`: moeda (R$); `Anos_Duration_Carteira`: anos; `Meses_Duration_Carteira`: meses; `Retentor_Risco`: moeda (R$); `Patrimonio_Liquido_Emissao`: moeda (R$); `Percentual`: percentual (%) |
| Dados pessoais | `CNPJ` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Nome` (nome de pessoa física (diretor, responsável ou representante)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/securit-doc-dfin_cri, https://dados.cvm.gov.br/dataset/securit-doc-inf_mensal_cri). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/SECURIT/DOC/DFIN_CRI/DADOS/`, `https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRI/DADOS/`.
- O catálogo do fetcher lista 17 arquivo(s), em 2 séries: `dfin_cri` (de `dfin_cri_2018.csv` a `dfin_cri_2026.csv`); `inf_mensal_cri` (de `inf_mensal_cri_2019.zip` a `inf_mensal_cri_2026.zip`).
- Em 2026-11-16 conferimos 22 arquivos Parquet convertidos de 5 arquivo(s) de origem (amostra: 2018, 2019, 2026).
- No bruto, o arquivo fica em `securit-cri/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma demonstração financeira entregue (em `dfin_cri`) ou o informe mensal de um certificado em uma competência e versão (nas tabelas `inf_mensal_cri_*`).
- Particionado por `ano`; o catálogo cobre 2018 a 2026, e conferimos as amostras 2018, 2019, 2026.
- O informe mensal de 2026 tem 21.350 linhas em `inf_mensal_cri_geral` (2.668 certificados, competências 2026-01 a 2026-10) e o de 2019 tem 3.897 (2019-09 a 2019-12): a série mensal começa em 2019-09. `Versao` vai de 1 a 4 em 2026 (18.298 linhas na versão 1, 2.614 na 2, 432 na 3 e 6 na 4).
- `dfin_cri` tem 1.244 demonstrações em 2026, 592 em 2019 e 22 em 2018 (`Data_Referencia` de 2018-12-31 em diante).
- O conjunto de tabelas mudou ao longo do tempo: `inf_mensal_cri_carteira_modificacao` e `inf_mensal_cri_responsavel` só existem no arquivo de 2019 da amostra, e `inf_mensal_cri_cedente_devedor`, só no de 2026.
- Este dataset reúne 12 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `dfin_cri` | 9 | 1.244 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | o índice das demonstrações financeiras: emissora, certificado, data, versão, parecer do auditor e link do documento |
| `inf_mensal_cri_ativo_passivo` | 65 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | ativo e passivo da emissão (65 colunas) |
| `inf_mensal_cri_carteira` | 29 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | créditos vinculados por faixa de prazo de vencimento |
| `inf_mensal_cri_carteira_modificacao` | 7 | 8.468 | não determinada | eventos de modificação da carteira, com justificativa (só nos arquivos antigos, como o de 2019) |
| `inf_mensal_cri_cedente_devedor` | 7 | 33.250 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Tipo`, `CNPJ` | cedentes e devedores, com o percentual de cada um (só nos arquivos recentes, como o de 2026) |
| `inf_mensal_cri_classe` | 28 | 42.782 | não determinada | classes e séries do certificado |
| `inf_mensal_cri_creditos` | 51 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | créditos por natureza econômica e por tipo (incorporação, aluguéis e outros) |
| `inf_mensal_cri_derivativos` | 20 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | operações com derivativos |
| `inf_mensal_cri_desembolso` | 22 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | pagamentos previstos por faixa de prazo |
| `inf_mensal_cri_fluxo_caixa` | 21 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | recebimentos e pagamentos do mês, por classe |
| `inf_mensal_cri_geral` | 44 | 21.350 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | dados gerais da emissão e do certificado (44 colunas) |
| `inf_mensal_cri_responsavel` | 6 | 4.152 | não determinada | responsáveis pelo informe, com nome e cargo (só nos arquivos antigos, como o de 2019) |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Emissora` | `CNPJ_Emissora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj emissora | — | todo |
| `Nome_Emissora` | `Nome_Emissora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome emissora (só em: `dfin_cri`) | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `dfin_cri`, `inf_mensal_cri_geral`) | — | todo |
| `Nome_Certificado` | `Nome_Certificado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome certificado (só em: `dfin_cri`) | — | todo |
| `Codigo_Identificacao_Certificado` | `Codigo_Identificacao_Certificado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo identificacao certificado | — | todo |
| `Link_Download` | `Link_Download` | texto | Endereço para download do documento (só em: `dfin_cri`) | — | todo |
| `Parecer_Auditor` | `Parecer_Auditor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: parecer auditor (só em: `dfin_cri`) | — | todo |
| `Ativo` | `Ativo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Circulante` | `Ativo_Circulante` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo circulante (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Circulante_Disponibilidades` | `Ativo_Circulante_Disponibilidades` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo circulante disponibilidades (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Circulante_Aplicacoes` | `Ativo_Circulante_Aplicacoes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo circulante aplicacoes (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Circulante_Creditos` | `Ativo_Circulante_Creditos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo circulante creditos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Circulante_Outros` | `Ativo_Circulante_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo circulante outros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Nao_Circulante` | `Ativo_Nao_Circulante` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo nao circulante (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Nao_Circulante_Aplicacoes` | `Ativo_Nao_Circulante_Aplicacoes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo nao circulante aplicacoes (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Nao_Circulante_Creditos` | `Ativo_Nao_Circulante_Creditos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo nao circulante creditos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Nao_Circulante_Outros` | `Ativo_Nao_Circulante_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo nao circulante outros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Creditos` | `Creditos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_A_Vencer_Sem_Parcelas_Atraso` | `Creditos_A_Vencer_Sem_Parcelas_Atraso` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos a vencer sem parcelas atraso (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_A_Vencer_Com_Parcelas_Atraso` | `Creditos_A_Vencer_Com_Parcelas_Atraso` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos a vencer com parcelas atraso (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_Vencidos` | `Creditos_Vencidos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vencidos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Reducao_Valor_Recuperacao` | `Reducao_Valor_Recuperacao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: reducao valor recuperacao (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Equivalentes` | `Caixa_Equivalentes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa equivalentes (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Titulos_Publicos_Federais` | `Caixa_Titulos_Publicos_Federais` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa titulos publicos federais (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Cotas_Fundos` | `Caixa_Cotas_Fundos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa cotas fundos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Operacoes_Compromissadas` | `Caixa_Operacoes_Compromissadas` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa operacoes compromissadas (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Outros` | `Caixa_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa outros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Derivativos` | `Ativo_Derivativos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo derivativos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Contratos_Termo` | `Ativo_Contratos_Termo` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo contratos termo (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Futuros` | `Ativo_Futuros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo futuros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Opcoes` | `Ativo_Opcoes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo opcoes (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Swap` | `Ativo_Swap` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo swap (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Ativos` | `Outros_Ativos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outros ativos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo` | `Passivo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Circulante` | `Passivo_Circulante` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo circulante (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Circulante_Valores_Mobiliarios` | `Passivo_Circulante_Valores_Mobiliarios` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo circulante valores mobiliarios (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Circulante_Outros` | `Passivo_Circulante_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo circulante outros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Nao_Circulante` | `Passivo_Nao_Circulante` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo nao circulante (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Nao_Circulante_Valores_Mobiliarios` | `Passivo_Nao_Circulante_Valores_Mobiliarios` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo nao circulante valores mobiliarios (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Nao_Circulante_Outros` | `Passivo_Nao_Circulante_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo nao circulante outros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Derivativos` | `Passivo_Derivativos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo derivativos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Contratos_Termo` | `Passivo_Contratos_Termo` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo contratos termo (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Futuros` | `Passivo_Futuros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo futuros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Opcoes` | `Passivo_Opcoes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo opcoes (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Swap` | `Passivo_Swap` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo swap (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Atualizado_Emissao` | `Valor_Atualizado_Emissao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor atualizado emissao (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Reducao_Valor_Emissao` | `Reducao_Valor_Emissao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: reducao valor emissao (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Passivos` | `Outros_Passivos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outros passivos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Companhia_Securitizadora_Emissora` | `Companhia_Securitizadora_Emissora` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: companhia securitizadora emissora (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Total_Recebimentos` | `Total_Recebimentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: total recebimentos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Pagamentos_Despesas_Comissoes` | `Pagamentos_Despesas_Comissoes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos despesas comissoes (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Senior_Pagamentos` | `Senior_Pagamentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: senior pagamentos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Senior_Amortizacao_Principal` | `Senior_Amortizacao_Principal` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: senior amortizacao principal (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Senior_Juros` | `Senior_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: senior juros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Subordinada_Pagamentos` | `Subordinada_Pagamentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: subordinada pagamentos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Subordinada_Amortizacao_Principal` | `Subordinada_Amortizacao_Principal` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: subordinada amortizacao principal (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Subordinada_Juros` | `Subordinada_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: subordinada juros (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Pagamentos_Recebimentos` | `Outros_Pagamentos_Recebimentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outros pagamentos recebimentos (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Suficiencia_Insuficiencia_Caixa` | `Suficiencia_Insuficiencia_Caixa` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: suficiencia insuficiencia caixa (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Premio_Subordinacao` | `Premio_Subordinacao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: premio subordinacao (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Securitizadora` | `Valor_Securitizadora` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor securitizadora (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Fundo_Despesa` | `Valor_Fundo_Despesa` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor fundo despesa (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Fundo_Reforco` | `Valor_Fundo_Reforco` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor fundo reforco (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Valores` | `Outros_Valores` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outros valores (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Descricao_Outros_Valores` | `Descricao_Outros_Valores` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: descricao outros valores (só em: `inf_mensal_cri_ativo_passivo`) | — | todo |
| `Valor_Pagamentos_Contratuais` | `Valor_Pagamentos_Contratuais` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor pagamentos contratuais (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Pagamentos_Contratuais_Senior` | `Valor_Pagamentos_Contratuais_Senior` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor pagamentos contratuais senior (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Pagamentos_Contratuais_Subordinada` | `Valor_Pagamentos_Contratuais_Subordinada` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor pagamentos contratuais subordinada (só em: `inf_mensal_cri_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_Vinculados` | `Creditos_Vinculados` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_Ate30Dias` | `Creditos_Vinculados_Prazo_Vencimento_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento ate30dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_31a60Dias` | `Creditos_Vinculados_Prazo_Vencimento_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento 31a60dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_61a90Dias` | `Creditos_Vinculados_Prazo_Vencimento_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento 61a90dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_91a120Dias` | `Creditos_Vinculados_Prazo_Vencimento_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento 91a120dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_121a150Dias` | `Creditos_Vinculados_Prazo_Vencimento_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento 121a150dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_151a180Dias` | `Creditos_Vinculados_Prazo_Vencimento_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento 151a180dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Prazo_Vencimento_Acima180Dias` | `Creditos_Vinculados_Prazo_Vencimento_Acima180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados prazo vencimento acima180dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes` | `Creditos_Vinculados_Inadimplentes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_Ate30Dias` | `Creditos_Vinculados_Inadimplentes_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes ate30dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_31a60Dias` | `Creditos_Vinculados_Inadimplentes_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes 31a60dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_61a90Dias` | `Creditos_Vinculados_Inadimplentes_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes 61a90dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_91a120Dias` | `Creditos_Vinculados_Inadimplentes_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes 91a120dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_121a150Dias` | `Creditos_Vinculados_Inadimplentes_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes 121a150dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_151a180Dias` | `Creditos_Vinculados_Inadimplentes_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes 151a180dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Inadimplentes_Acima180Dias` | `Creditos_Vinculados_Inadimplentes_Acima180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados inadimplentes acima180dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos` | `Creditos_Vinculados_Pagos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_Ate30Dias` | `Creditos_Vinculados_Pagos_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos ate30dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_31a60Dias` | `Creditos_Vinculados_Pagos_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos 31a60dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_61a90Dias` | `Creditos_Vinculados_Pagos_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos 61a90dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_91a120Dias` | `Creditos_Vinculados_Pagos_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos 91a120dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_121a150Dias` | `Creditos_Vinculados_Pagos_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos 121a150dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_151a180Dias` | `Creditos_Vinculados_Pagos_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos 151a180dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Vinculados_Pagos_Acima180Dias` | `Creditos_Vinculados_Pagos_Acima180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vinculados pagos acima180dias (só em: `inf_mensal_cri_carteira`) | moeda (R$) | todo |
| `Creditos_Processo_Liquidacao` | `Creditos_Processo_Liquidacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos processo liquidacao (só em: `inf_mensal_cri_carteira`) | — | todo |
| `Evento` | `Evento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: evento (só em: `inf_mensal_cri_carteira_modificacao`) | — | todo |
| `Valor` | `Valor` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor (só em: `inf_mensal_cri_carteira_modificacao`, `inf_mensal_cri_classe`) | moeda (R$) | todo |
| `Justificativa` | `Justificativa` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: justificativa (só em: `inf_mensal_cri_carteira_modificacao`) | — | todo |
| `Classe` | `Classe` | texto | Classe (só em: `inf_mensal_cri_classe`) | — | todo |
| `Numero_Serie` | `Numero_Serie` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero serie (só em: `inf_mensal_cri_classe`) | código ou número de identificação (sem unidade) | todo |
| `Tipo_Oferta` | `Tipo_Oferta` | texto | Tipo da Oferta: se primária, secundária ou mista (só em: `inf_mensal_cri_classe`) | — | todo |
| `Codigo_CETIP` | `Codigo_CETIP` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo cetip (só em: `inf_mensal_cri_classe`) | — | todo |
| `Codigo_ISIN` | `Codigo_ISIN` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo isin (só em: `inf_mensal_cri_classe`) | — | todo |
| `Quantidade` | `Quantidade` | inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade (só em: `inf_mensal_cri_classe`) | quantidade | todo |
| `Data_Vencimento` | `Data_Vencimento` | texto | Data de Vencimento (só em: `inf_mensal_cri_classe`) | — | todo |
| `Taxas_Indexadores` | `Taxas_Indexadores` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: taxas indexadores (só em: `inf_mensal_cri_classe`) | — | todo |
| `Situacao` | `Situacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: situacao (só em: `inf_mensal_cri_classe`) | — | todo |
| `Total_Integralizado` | `Total_Integralizado` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: total integralizado (só em: `inf_mensal_cri_classe`) | moeda (R$) | todo |
| `Taxa_Juros` | `Taxa_Juros` | texto | Taxa de juros (só em: `inf_mensal_cri_classe`) | — | todo |
| `Pagamento_Periodicidade` | `Pagamento_Periodicidade` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento periodicidade (só em: `inf_mensal_cri_classe`) | — | todo |
| `Pagamento_Mes_Base` | `Pagamento_Mes_Base` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento mes base (só em: `inf_mensal_cri_classe`) | — | todo |
| `Quantidade_Certificados` | `Quantidade_Certificados` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade certificados (só em: `inf_mensal_cri_classe`) | quantidade | todo |
| `Valor_Certificados` | `Valor_Certificados` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor certificados (só em: `inf_mensal_cri_classe`) | moeda (R$) | todo |
| `Rendimentos` | `Rendimentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimentos (só em: `inf_mensal_cri_classe`) | moeda (R$) | todo |
| `Amortizacoes` | `Amortizacoes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: amortizacoes (só em: `inf_mensal_cri_classe`) | moeda (R$) | todo |
| `Rentabilidade` | `Rentabilidade` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: rentabilidade (só em: `inf_mensal_cri_classe`) | percentual (%) | todo |
| `Classificacao_Risco_Atual` | `Classificacao_Risco_Atual` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: classificacao risco atual (só em: `inf_mensal_cri_classe`) | — | todo |
| `Nivel_Subordinacao` | `Nivel_Subordinacao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nivel subordinacao (só em: `inf_mensal_cri_classe`) | moeda (R$) | todo |
| `Periodicidade_Amortizacao` | `Periodicidade_Amortizacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: periodicidade amortizacao (só em: `inf_mensal_cri_classe`) | — | todo |
| `Indice_Subordinacao_Minimo` | `Indice_Subordinacao_Minimo` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: indice subordinacao minimo (só em: `inf_mensal_cri_classe`) | índice (sem unidade) | todo |
| `Indice_Subordinacao_Data_Base` | `Indice_Subordinacao_Data_Base` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: indice subordinacao data base (só em: `inf_mensal_cri_classe`) | índice (sem unidade) | todo |
| `Parcelas_Atraso` | `Parcelas_Atraso` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: parcelas atraso (só em: `inf_mensal_cri_creditos`) | quantidade (parcelas) | todo |
| `Concentracao` | `Concentracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: concentracao (só em: `inf_mensal_cri_creditos`) | — | todo |
| `Creditos_Natureza_Economica` | `Creditos_Natureza_Economica` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos natureza economica (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Incorporacao_Imobiliaria` | `Creditos_Incorporacao_Imobiliaria` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos incorporacao imobiliaria (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Alugueis` | `Creditos_Alugueis` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos alugueis (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Aquisicao_Imoveis` | `Creditos_Aquisicao_Imoveis` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos aquisicao imoveis (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Loteamento` | `Creditos_Loteamento` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos loteamento (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Multipropriedade` | `Creditos_Multipropriedade` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos multipropriedade (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Home_Equity` | `Creditos_Home_Equity` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos home equity (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Creditos_Outros` | `Creditos_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos outros (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer` | `A_Vencer` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_Ate30Dias` | `A_Vencer_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer ate30dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_31a60Dias` | `A_Vencer_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 31a60dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_61a90Dias` | `A_Vencer_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 61a90dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_91a120Dias` | `A_Vencer_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 91a120dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_121a150Dias` | `A_Vencer_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 121a150dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_151a180Dias` | `A_Vencer_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 151a180dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_181a360Dias` | `A_Vencer_181a360Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 181a360dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `A_Vencer_Acima361Dias` | `A_Vencer_Acima361Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer acima361dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos` | `Nao_Pagos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_Ate30Dias` | `Nao_Pagos_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos ate30dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_31a60Dias` | `Nao_Pagos_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 31a60dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_61a90Dias` | `Nao_Pagos_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 61a90dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_91a120Dias` | `Nao_Pagos_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 91a120dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_121a150Dias` | `Nao_Pagos_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 121a150dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_151a180Dias` | `Nao_Pagos_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 151a180dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_181a360Dias` | `Nao_Pagos_181a360Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 181a360dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Nao_Pagos_Acima361Dias` | `Nao_Pagos_Acima361Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos acima361dias (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Pre_Pagamentos` | `Pre_Pagamentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pre pagamentos (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Pre_Pagamento_Lastro` | `Pre_Pagamento_Lastro` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pre pagamento lastro (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Pre_Pagamento_Impacto` | `Pre_Pagamento_Impacto` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pre pagamento impacto (só em: `inf_mensal_cri_creditos`) | — | todo |
| `Dividas_Emissor_Securitizadora` | `Dividas_Emissor_Securitizadora` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: dividas emissor securitizadora (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Percentual_Risco_Cedentes` | `Percentual_Risco_Cedentes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual risco cedentes (só em: `inf_mensal_cri_creditos`) | percentual (%) | todo |
| `Percentual_Outras_Garantias` | `Percentual_Outras_Garantias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual outras garantias (só em: `inf_mensal_cri_creditos`) | percentual (%) | todo |
| `Percentual_Garantias_Exceto_Coobrigacao` | `Percentual_Garantias_Exceto_Coobrigacao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual garantias exceto coobrigacao (só em: `inf_mensal_cri_creditos`) | percentual (%) | todo |
| `Periodicidade_Avaliacao_Garantias` | `Periodicidade_Avaliacao_Garantias` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: periodicidade avaliacao garantias (só em: `inf_mensal_cri_creditos`) | — | todo |
| `Duration_Carteira` | `Duration_Carteira` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: duration carteira (só em: `inf_mensal_cri_creditos`) | — | todo |
| `Relacao_Total_Emissao` | `Relacao_Total_Emissao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: relacao total emissao (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Outras_Consideracoes` | `Outras_Consideracoes` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outras consideracoes (só em: `inf_mensal_cri_creditos`) | — | todo |
| `Maior_Devedor` | `Maior_Devedor` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: maior devedor (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Cinco_Maiores_Devedores` | `Cinco_Maiores_Devedores` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cinco maiores devedores (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Dez_Maiores_Devedores` | `Dez_Maiores_Devedores` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: dez maiores devedores (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Vinte_Maiores_Devedores` | `Vinte_Maiores_Devedores` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: vinte maiores devedores (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Maior_Cedente` | `Maior_Cedente` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: maior cedente (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Cinco_Maiores_Cedentes` | `Cinco_Maiores_Cedentes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cinco maiores cedentes (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Dez_Maiores_Cedentes` | `Dez_Maiores_Cedentes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: dez maiores cedentes (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Vinte_Maiores_Cedentes` | `Vinte_Maiores_Cedentes` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: vinte maiores cedentes (só em: `inf_mensal_cri_creditos`) | moeda (R$) | todo |
| `Mercado_Termo_Juros` | `Mercado_Termo_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo juros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Mercado_Termo_Commodities` | `Mercado_Termo_Commodities` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo commodities (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Mercado_Termo_Cambio` | `Mercado_Termo_Cambio` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo cambio (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Mercado_Termo_Outros` | `Mercado_Termo_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo outros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Futuros_Juros` | `Futuros_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros juros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Futuros_Commodities` | `Futuros_Commodities` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros commodities (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Futuros_Cambio` | `Futuros_Cambio` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros cambio (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Futuros_Outros` | `Futuros_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros outros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Opcoes_Juros` | `Opcoes_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes juros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Opcoes_Commodities` | `Opcoes_Commodities` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes commodities (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Opcoes_Cambio` | `Opcoes_Cambio` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes cambio (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Opcoes_Outros` | `Opcoes_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes outros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Swap_Juros` | `Swap_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: swap juros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Swap_Commodities` | `Swap_Commodities` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: swap commodities (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Swap_Cambio` | `Swap_Cambio` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: swap cambio (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Swap_Outros` | `Swap_Outros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: swap outros (só em: `inf_mensal_cri_derivativos`) | moeda (R$) | todo |
| `Pagamento_Despesas` | `Pagamento_Despesas` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_Ate30Dias` | `Pagamento_Despesas_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas ate30dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_31a60Dias` | `Pagamento_Despesas_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 31a60dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_61a90Dias` | `Pagamento_Despesas_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 61a90dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_91a120Dias` | `Pagamento_Despesas_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 91a120dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_121a150Dias` | `Pagamento_Despesas_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 121a150dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_151a180Dias` | `Pagamento_Despesas_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 151a180dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_181a360Dias` | `Pagamento_Despesas_181a360Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 181a360dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_Acima361Dias` | `Pagamento_Despesas_Acima361Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas acima361dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores` | `Pagamento_Investidores` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_Ate30Dias` | `Pagamento_Investidores_Ate30Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores ate30dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_31a60Dias` | `Pagamento_Investidores_31a60Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 31a60dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_61a90Dias` | `Pagamento_Investidores_61a90Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 61a90dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_91a120Dias` | `Pagamento_Investidores_91a120Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 91a120dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_121a150Dias` | `Pagamento_Investidores_121a150Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 121a150dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_151a180Dias` | `Pagamento_Investidores_151a180Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 151a180dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_181a360Dias` | `Pagamento_Investidores_181a360Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 181a360dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_Acima361Dias` | `Pagamento_Investidores_Acima361Dias` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores acima361dias (só em: `inf_mensal_cri_desembolso`) | moeda (R$) | todo |
| `Recebimentos_Creditos` | `Recebimentos_Creditos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: recebimentos creditos (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Despesas` | `Pagamentos_Despesas` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos despesas (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Senior` | `Pagamentos_Classe_Senior` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe senior (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Senior_Amortizacao_Principal` | `Pagamentos_Classe_Senior_Amortizacao_Principal` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe senior amortizacao principal (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Senior_Juros` | `Pagamentos_Classe_Senior_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe senior juros (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Mezanino` | `Pagamentos_Classe_Subordinada_Mezanino` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada mezanino (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal` | `Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada mezanino amortizacao principal (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Mezanino_Juros` | `Pagamentos_Classe_Subordinada_Mezanino_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada mezanino juros (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Junior` | `Pagamentos_Classe_Subordinada_Junior` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada junior (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal` | `Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada junior amortizacao principal (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Junior_Juros` | `Pagamentos_Classe_Subordinada_Junior_Juros` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada junior juros (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Recebimentos_Alienacao_Caixa` | `Recebimentos_Alienacao_Caixa` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: recebimentos alienacao caixa (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Aquisicao_Caixa` | `Aquisicao_Caixa` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: aquisicao caixa (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Aquisicao_Novos_Creditos` | `Aquisicao_Novos_Creditos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: aquisicao novos creditos (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Outros_Recebimentos` | `Outros_Recebimentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outros recebimentos (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Outros_Pagamentos` | `Outros_Pagamentos` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outros pagamentos (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Variacao_Liquida_Caixa` | `Variacao_Liquida_Caixa` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: variacao liquida caixa (só em: `inf_mensal_cri_fluxo_caixa`) | moeda (R$) | todo |
| `Numero_Emissao` | `Numero_Emissao` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero emissao (só em: `inf_mensal_cri_geral`) | código ou número de identificação (sem unidade) | todo |
| `Nome_Emissao` | `Nome_Emissao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome emissao (só em: `inf_mensal_cri_geral`) | — | todo |
| `Quantidade_Series` | `Quantidade_Series` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade series (só em: `inf_mensal_cri_geral`) | quantidade | todo |
| `Data_Emissao` | `Data_Emissao` | texto | Data de Emissão (só em: `inf_mensal_cri_geral`) | — | todo |
| `Companhia_Emissora` | `Companhia_Emissora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: companhia emissora (só em: `inf_mensal_cri_geral`) | — | todo |
| `Instituicao_Regime_Fiduciario` | `Instituicao_Regime_Fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: instituicao regime fiduciario (só em: `inf_mensal_cri_geral`) | — | todo |
| `Agente_Fiduciario` | `Agente_Fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: agente fiduciario (só em: `inf_mensal_cri_geral`) | — | todo |
| `CNPJ_Agente_Fiduciario` | `CNPJ_Agente_Fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj agente fiduciario (só em: `inf_mensal_cri_geral`) | — | todo |
| `Custodiante` | `Custodiante` | texto | Nome do Custodiante (só em: `inf_mensal_cri_geral`) | — | todo |
| `CNPJ_Custodiante` | `CNPJ_Custodiante` | texto | CNPJ do Custodiante (só em: `inf_mensal_cri_geral`) | — | todo |
| `Segmento_Creditos_Vinculados` | `Segmento_Creditos_Vinculados` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: segmento creditos vinculados (só em: `inf_mensal_cri_geral`) | — | todo |
| `Valor_Aquisicao_Credito` | `Valor_Aquisicao_Credito` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: valor aquisicao credito (só em: `inf_mensal_cri_geral`) | moeda (R$) | todo |
| `Taxas_Medias_Indexadores_Creditos_Vinculados` | `Taxas_Medias_Indexadores_Creditos_Vinculados` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: taxas medias indexadores creditos vinculados (só em: `inf_mensal_cri_geral`) | — | todo |
| `Anos_Duration_Carteira` | `Anos_Duration_Carteira` | inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: anos duration carteira (só em: `inf_mensal_cri_geral`) | anos | todo |
| `Meses_Duration_Carteira` | `Meses_Duration_Carteira` | inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: meses duration carteira (só em: `inf_mensal_cri_geral`) | meses | todo |
| `Forma_Calculo_Duration` | `Forma_Calculo_Duration` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: forma calculo duration (só em: `inf_mensal_cri_geral`) | — | todo |
| `Tipos_Garantias_Coobrigacao_Securitizadora` | `Tipos_Garantias_Coobrigacao_Securitizadora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipos garantias coobrigacao securitizadora (só em: `inf_mensal_cri_geral`) | — | todo |
| `Tipos_Garantias_Coobrigacao_Terceiros` | `Tipos_Garantias_Coobrigacao_Terceiros` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipos garantias coobrigacao terceiros (só em: `inf_mensal_cri_geral`) | — | todo |
| `Indice_LTV` | `Indice_LTV` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: indice ltv (só em: `inf_mensal_cri_geral`) | — | todo |
| `Data_LTV` | `Data_LTV` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data ltv (só em: `inf_mensal_cri_geral`) | — | todo |
| `Tipo_Lastro` | `Tipo_Lastro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo lastro (só em: `inf_mensal_cri_geral`) | — | todo |
| `Detalhamento_Lastro` | `Detalhamento_Lastro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: detalhamento lastro (só em: `inf_mensal_cri_geral`) | — | todo |
| `Sobrecolateralizacao` | `Sobrecolateralizacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: sobrecolateralizacao (só em: `inf_mensal_cri_geral`) | — | todo |
| `Outras_Caracteristicas_Emissao` | `Outras_Caracteristicas_Emissao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outras caracteristicas emissao (só em: `inf_mensal_cri_geral`) | — | todo |
| `Tipo_Retencao_Risco` | `Tipo_Retencao_Risco` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo retencao risco (só em: `inf_mensal_cri_geral`) | — | todo |
| `Retentor_Risco` | `Retentor_Risco` | inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: retentor risco (só em: `inf_mensal_cri_geral`) | moeda (R$) | todo |
| `Agencia_Classificadora` | `Agencia_Classificadora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: agencia classificadora (só em: `inf_mensal_cri_geral`) | — | todo |
| `CNPJ_Agencia_Classificadora` | `CNPJ_Agencia_Classificadora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj agencia classificadora (só em: `inf_mensal_cri_geral`) | — | todo |
| `Data_Ultima_Classificacao` | `Data_Ultima_Classificacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data ultima classificacao (só em: `inf_mensal_cri_geral`) | — | todo |
| `Recomposicao_Indice` | `Recomposicao_Indice` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: recomposicao indice (só em: `inf_mensal_cri_geral`) | — | todo |
| `Impacto_Eventos_Pre_Pagamento` | `Impacto_Eventos_Pre_Pagamento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: impacto eventos pre pagamento (só em: `inf_mensal_cri_geral`) | — | todo |
| `Analise_Impacto_Eventos_Pre_Pagamento` | `Analise_Impacto_Eventos_Pre_Pagamento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: analise impacto eventos pre pagamento (só em: `inf_mensal_cri_geral`) | — | todo |
| `Analise_Impacto_Outros_Eventos` | `Analise_Impacto_Outros_Eventos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: analise impacto outros eventos (só em: `inf_mensal_cri_geral`) | — | todo |
| `Analise_Impacto_Demais_Fatos` | `Analise_Impacto_Demais_Fatos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: analise impacto demais fatos (só em: `inf_mensal_cri_geral`) | — | todo |
| `Patrimonio_Liquido_Emissao` | `Patrimonio_Liquido_Emissao` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: patrimonio liquido emissao (só em: `inf_mensal_cri_geral`) | moeda (R$) | todo |
| `Desempenho_Emissao` | `Desempenho_Emissao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: desempenho emissao (só em: `inf_mensal_cri_geral`) | — | todo |
| `Contingencias_Principais_Fatos` | `Contingencias_Principais_Fatos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: contingencias principais fatos (só em: `inf_mensal_cri_geral`) | — | todo |
| `Contingencias_Valores_Envolvidos` | `Contingencias_Valores_Envolvidos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: contingencias valores envolvidos (só em: `inf_mensal_cri_geral`) | — | todo |
| `Outras_Contigencias_Relevantes` | `Outras_Contigencias_Relevantes` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outras contigencias relevantes (só em: `inf_mensal_cri_geral`) | — | todo |
| `Nome` | `Nome` | texto | Nome da Pessoa Física (só em: `inf_mensal_cri_responsavel`) | — | todo |
| `Cargo` | `Cargo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cargo (só em: `inf_mensal_cri_responsavel`) | — | todo |
| `Tipo` | `Tipo` | texto | Tipo (só em: `inf_mensal_cri_cedente_devedor`) | — | todo |
| `CNPJ` | `CNPJ` | texto | Cadastro Nacional de Pessoas Jurídicas (só em: `inf_mensal_cri_cedente_devedor`) | — | todo |
| `Percentual` | `Percentual` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual (só em: `inf_mensal_cri_cedente_devedor`) | percentual (%) | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/securit-cri`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Várias versões por certificado e competência.** O arquivo traz cada reapresentação (`Versao`); para a posição vigente, escolha a maior `Versao` de cada `Codigo_Identificacao_Certificado` e `Data_Referencia`. A chave com `Versao` é única na maioria das tabelas.
- **`CNPJ` de cedentes e devedores não é só CNPJ.** Em `inf_mensal_cri_cedente_devedor` (arquivo de 2026), de 33.250 linhas, 12.922 têm 14 dígitos, 14 têm 15, 10.011 têm 1 dígito (valor de preenchimento) e 912 vêm sem dígitos; a máscara é inconsistente. Valide o tamanho antes de tratar como CNPJ.
- **Muitas colunas quase vazias e de tipo instável.** 34 colunas de `inf_mensal_cri_ativo_passivo` e 25 de `inf_mensal_cri_carteira` têm mais de 98% de nulos no arquivo de 2026; os tipos mudam entre arquivos (veja o item de tipos abaixo).
- **Competência como primeiro dia do mês.** `Data_Referencia` vem como `AAAA-MM-01` nos informes mensais.
- **Tipo inferido varia entre arquivos.** 191 coluna(s) (`Ativo_Circulante`, `Ativo_Circulante_Disponibilidades`, `Ativo_Circulante_Aplicacoes`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.
- **Linhas repetidas.** No arquivo mais recente convertido há linhas inteiramente repetidas em: `inf_mensal_cri_classe` (136). Remova as duplicatas antes de contar ou somar.

## Exemplos

Certificados distintos informados por mês em 2026.

```python
import duckdb

duckdb.sql("""
    SELECT Data_Referencia, count(DISTINCT Codigo_Identificacao_Certificado) AS certificados
    FROM read_parquet('lake/cvm/securit-cri/ano=2026/*__inf_mensal_cri_geral_2026.parquet')
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cri
- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-inf_mensal_cri
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/SECURIT/DOC/DFIN_CRI/
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRI/
