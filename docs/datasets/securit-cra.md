---
dataset:
  id: securit-cra
  fonte: cvm
  titulo: "Securitizadoras: Documentos: Demonstrações Financeiras e Informe Mensal de CRA (CVM)"
  resumo: "Securitização de Certificados de Recebíveis do Agronegócio (CRA): as demonstrações financeiras anuais dos certificados (`dfin_cra`) e o informe mensal de cada CRA (`inf_mensal_cra`), em nove tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cra
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cra"
  periodicidade: "anual (um arquivo por ano, com um informe por mês); o portal declara atualização semanal para os últimos cinco anos"
  cobertura: {inicio: 2019, fim: em-curso}
  unidade: "uma demonstração financeira entregue (em `dfin_cra`) ou o informe mensal de um certificado em uma competência e versão (nas tabelas `inf_mensal_cra_*`)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (informe, `Data_Referencia` no primeiro dia do mês) e anual (demonstrações financeiras), em arquivos anuais"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 187}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    Ativo: "moeda (R$)"
    Direitos_Creditorios: "moeda (R$)"
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
    Passivo_Derivativos: "moeda (R$)"
    Passivo_Contratos_Termo: "moeda (R$)"
    Passivo_Futuros: "moeda (R$)"
    Passivo_Opcoes: "moeda (R$)"
    Passivo_Swap: "moeda (R$)"
    Valor_Atualizado_Emissao: "moeda (R$)"
    Reducao_Valor_Emissao: "moeda (R$)"
    Outros_Passivos: "moeda (R$)"
    Companhia_Securitizadora_Emissora: "moeda (R$)"
    Percentual: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Numero_Serie: "código ou número de identificação (sem unidade)"
    Valor_Total_Integralizado: "moeda (R$)"
    Quantidade_Certificados: "quantidade"
    Valor_Certificados: "moeda (R$)"
    Rendimentos: "moeda (R$)"
    Amortizacoes: "moeda (R$)"
    Rentabilidade: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Indice_Subordinacao_Minimo: "índice (sem unidade)"
    Indice_Subordinacao_Data_Base: "índice (sem unidade)"
    Mercado_Termo_Juros: "moeda (R$)"
    Mercado_Termo_Commodities_Agricolas: "moeda (R$)"
    Mercado_Termo_Cambio: "moeda (R$)"
    Mercado_Termo_Outros: "moeda (R$)"
    Futuros_Juros: "moeda (R$)"
    Futuros_Commodities_Agricolas: "moeda (R$)"
    Futuros_Cambio: "moeda (R$)"
    Futuros_Outros: "moeda (R$)"
    Opcoes_Juros: "moeda (R$)"
    Opcoes_Commodities_Agricolas: "moeda (R$)"
    Opcoes_Cambio: "moeda (R$)"
    Opcoes_Outros: "moeda (R$)"
    Swap_Juros: "moeda (R$)"
    Swap_Commodities_Agricolas: "moeda (R$)"
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
    Parcelas_Atraso: "quantidade (parcelas)"
    Direitos_Creditorios_Receber: "moeda (R$)"
    Direitos_Creditorios_Receber_Producao: "moeda (R$)"
    Direitos_Creditorios_Receber_Comercializacao: "moeda (R$)"
    Direitos_Creditorios_Receber_Beneficiamento: "moeda (R$)"
    Direitos_Creditorios_Receber_Industrializacao: "moeda (R$)"
    Direitos_Creditorios_Receber_Producao_Insumos: "moeda (R$)"
    Direitos_Creditorios_Receber_Comercializacao_Insumos: "moeda (R$)"
    Direitos_Creditorios_Receber_Beneficiamento_Insumos: "moeda (R$)"
    Direitos_Creditorios_Receber_Industrializacao_Insumos: "moeda (R$)"
    Direitos_Creditorios_Receber_Producao_Maquinas: "moeda (R$)"
    Direitos_Creditorios_Receber_Comercializacao_Maquinas: "moeda (R$)"
    Direitos_Creditorios_Receber_Beneficiamento_Maquinas: "moeda (R$)"
    Direitos_Creditorios_Receber_Industrializacao_Maquinas: "moeda (R$)"
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
    Percentual_Coobrigacao_Cedentes: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Outras_Garantias: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Percentual_Garantias_Exceto_Coobrigacao: "percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras)"
    Relacao_Total_Emissao: "moeda (R$)"
    Maior_Devedor: "moeda (R$)"
    Cinco_Maiores_Devedores: "moeda (R$)"
    Dez_Maiores_Devedores: "moeda (R$)"
    Vinte_Maiores_Devedores: "moeda (R$)"
    Maior_Cedente: "moeda (R$)"
    Cinco_Maiores_Cedentes: "moeda (R$)"
    Dez_Maiores_Cedentes: "moeda (R$)"
    Vinte_Maiores_Cedentes: "moeda (R$)"
    Recebimentos_Direitos_Creditorios: "moeda (R$)"
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
    Aquisicao_Novos_Direitos_Creditorios: "moeda (R$)"
    Outros_Recebimentos: "moeda (R$)"
    Outros_Pagamentos: "moeda (R$)"
    Variacao_Liquida_Caixa: "moeda (R$)"
    Numero_Emissao: "código ou número de identificação (sem unidade)"
    Quantidade_Series: "quantidade"
    Retentor_Risco: "moeda (R$)"
    Patrimonio_Liquido_Emissao: "moeda (R$)"
  dados_pessoais:
    - {coluna: CNPJ, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Securitizadoras: Documentos: Demonstrações Financeiras e Informe Mensal de CRA

## Resumo

Securitização de Certificados de Recebíveis do Agronegócio (CRA): as demonstrações financeiras anuais dos certificados (`dfin_cra`) e o informe mensal de cada CRA (`inf_mensal_cra`), em nove tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/securit-cra` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/securit-doc-dfin_cra |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cra |
| Periodicidade | anual (um arquivo por ano, com um informe por mês); o portal declara atualização semanal para os últimos cinco anos |
| Cobertura | 2019 a em-curso |
| Unidade (uma linha) | uma demonstração financeira entregue (em `dfin_cra`) ou o informe mensal de um certificado em uma competência e versão (nas tabelas `inf_mensal_cra_*`) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (informe, `Data_Referencia` no primeiro dia do mês) e anual (demonstrações financeiras), em arquivos anuais |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 187 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `Ativo`: moeda (R$); `Direitos_Creditorios`: moeda (R$); `Creditos_A_Vencer_Sem_Parcelas_Atraso`: moeda (R$); `Creditos_A_Vencer_Com_Parcelas_Atraso`: moeda (R$); `Creditos_Vencidos`: moeda (R$); `Reducao_Valor_Recuperacao`: moeda (R$); `Caixa_Equivalentes`: moeda (R$); `Caixa_Titulos_Publicos_Federais`: moeda (R$); `Caixa_Cotas_Fundos`: moeda (R$); `Caixa_Operacoes_Compromissadas`: moeda (R$); `Caixa_Outros`: moeda (R$); `Ativo_Derivativos`: moeda (R$); `Ativo_Contratos_Termo`: moeda (R$); `Ativo_Futuros`: moeda (R$); `Ativo_Opcoes`: moeda (R$); `Ativo_Swap`: moeda (R$); `Outros_Ativos`: moeda (R$); `Passivo`: moeda (R$); `Passivo_Derivativos`: moeda (R$); `Passivo_Contratos_Termo`: moeda (R$); `Passivo_Futuros`: moeda (R$); `Passivo_Opcoes`: moeda (R$); `Passivo_Swap`: moeda (R$); `Valor_Atualizado_Emissao`: moeda (R$); `Reducao_Valor_Emissao`: moeda (R$); `Outros_Passivos`: moeda (R$); `Companhia_Securitizadora_Emissora`: moeda (R$); `Percentual`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Numero_Serie`: código ou número de identificação (sem unidade); `Valor_Total_Integralizado`: moeda (R$); `Quantidade_Certificados`: quantidade; `Valor_Certificados`: moeda (R$); `Rendimentos`: moeda (R$); `Amortizacoes`: moeda (R$); `Rentabilidade`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Indice_Subordinacao_Minimo`: índice (sem unidade); `Indice_Subordinacao_Data_Base`: índice (sem unidade); `Mercado_Termo_Juros`: moeda (R$); `Mercado_Termo_Commodities_Agricolas`: moeda (R$); `Mercado_Termo_Cambio`: moeda (R$); `Mercado_Termo_Outros`: moeda (R$); `Futuros_Juros`: moeda (R$); `Futuros_Commodities_Agricolas`: moeda (R$); `Futuros_Cambio`: moeda (R$); `Futuros_Outros`: moeda (R$); `Opcoes_Juros`: moeda (R$); `Opcoes_Commodities_Agricolas`: moeda (R$); `Opcoes_Cambio`: moeda (R$); `Opcoes_Outros`: moeda (R$); `Swap_Juros`: moeda (R$); `Swap_Commodities_Agricolas`: moeda (R$); `Swap_Cambio`: moeda (R$); `Swap_Outros`: moeda (R$); `Pagamento_Despesas`: moeda (R$); `Pagamento_Despesas_Ate30Dias`: moeda (R$); `Pagamento_Despesas_31a60Dias`: moeda (R$); `Pagamento_Despesas_61a90Dias`: moeda (R$); `Pagamento_Despesas_91a120Dias`: moeda (R$); `Pagamento_Despesas_121a150Dias`: moeda (R$); `Pagamento_Despesas_151a180Dias`: moeda (R$); `Pagamento_Despesas_181a360Dias`: moeda (R$); `Pagamento_Despesas_Acima361Dias`: moeda (R$); `Pagamento_Investidores`: moeda (R$); `Pagamento_Investidores_Ate30Dias`: moeda (R$); `Pagamento_Investidores_31a60Dias`: moeda (R$); `Pagamento_Investidores_61a90Dias`: moeda (R$); `Pagamento_Investidores_91a120Dias`: moeda (R$); `Pagamento_Investidores_121a150Dias`: moeda (R$); `Pagamento_Investidores_151a180Dias`: moeda (R$); `Pagamento_Investidores_181a360Dias`: moeda (R$); `Pagamento_Investidores_Acima361Dias`: moeda (R$); `Parcelas_Atraso`: quantidade (parcelas); `Direitos_Creditorios_Receber`: moeda (R$); `Direitos_Creditorios_Receber_Producao`: moeda (R$); `Direitos_Creditorios_Receber_Comercializacao`: moeda (R$); `Direitos_Creditorios_Receber_Beneficiamento`: moeda (R$); `Direitos_Creditorios_Receber_Industrializacao`: moeda (R$); `Direitos_Creditorios_Receber_Producao_Insumos`: moeda (R$); `Direitos_Creditorios_Receber_Comercializacao_Insumos`: moeda (R$); `Direitos_Creditorios_Receber_Beneficiamento_Insumos`: moeda (R$); `Direitos_Creditorios_Receber_Industrializacao_Insumos`: moeda (R$); `Direitos_Creditorios_Receber_Producao_Maquinas`: moeda (R$); `Direitos_Creditorios_Receber_Comercializacao_Maquinas`: moeda (R$); `Direitos_Creditorios_Receber_Beneficiamento_Maquinas`: moeda (R$); `Direitos_Creditorios_Receber_Industrializacao_Maquinas`: moeda (R$); `A_Vencer`: moeda (R$); `A_Vencer_Ate30Dias`: moeda (R$); `A_Vencer_31a60Dias`: moeda (R$); `A_Vencer_61a90Dias`: moeda (R$); `A_Vencer_91a120Dias`: moeda (R$); `A_Vencer_121a150Dias`: moeda (R$); `A_Vencer_151a180Dias`: moeda (R$); `A_Vencer_181a360Dias`: moeda (R$); `A_Vencer_Acima361Dias`: moeda (R$); `Nao_Pagos`: moeda (R$); `Nao_Pagos_Ate30Dias`: moeda (R$); `Nao_Pagos_31a60Dias`: moeda (R$); `Nao_Pagos_61a90Dias`: moeda (R$); `Nao_Pagos_91a120Dias`: moeda (R$); `Nao_Pagos_121a150Dias`: moeda (R$); `Nao_Pagos_151a180Dias`: moeda (R$); `Nao_Pagos_181a360Dias`: moeda (R$); `Nao_Pagos_Acima361Dias`: moeda (R$); `Pre_Pagamentos`: moeda (R$); `Pre_Pagamento_Lastro`: moeda (R$); `Dividas_Emissor_Securitizadora`: moeda (R$); `Percentual_Coobrigacao_Cedentes`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Outras_Garantias`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Percentual_Garantias_Exceto_Coobrigacao`: percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras); `Relacao_Total_Emissao`: moeda (R$); `Maior_Devedor`: moeda (R$); `Cinco_Maiores_Devedores`: moeda (R$); `Dez_Maiores_Devedores`: moeda (R$); `Vinte_Maiores_Devedores`: moeda (R$); `Maior_Cedente`: moeda (R$); `Cinco_Maiores_Cedentes`: moeda (R$); `Dez_Maiores_Cedentes`: moeda (R$); `Vinte_Maiores_Cedentes`: moeda (R$); `Recebimentos_Direitos_Creditorios`: moeda (R$); `Pagamentos_Despesas`: moeda (R$); `Pagamentos_Classe_Senior`: moeda (R$); `Pagamentos_Classe_Senior_Amortizacao_Principal`: moeda (R$); `Pagamentos_Classe_Senior_Juros`: moeda (R$); `Pagamentos_Classe_Subordinada_Mezanino`: moeda (R$); `Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal`: moeda (R$); `Pagamentos_Classe_Subordinada_Mezanino_Juros`: moeda (R$); `Pagamentos_Classe_Subordinada_Junior`: moeda (R$); `Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal`: moeda (R$); `Pagamentos_Classe_Subordinada_Junior_Juros`: moeda (R$); `Recebimentos_Alienacao_Caixa`: moeda (R$); `Aquisicao_Caixa`: moeda (R$); `Aquisicao_Novos_Direitos_Creditorios`: moeda (R$); `Outros_Recebimentos`: moeda (R$); `Outros_Pagamentos`: moeda (R$); `Variacao_Liquida_Caixa`: moeda (R$); `Numero_Emissao`: código ou número de identificação (sem unidade); `Quantidade_Series`: quantidade; `Retentor_Risco`: moeda (R$); `Patrimonio_Liquido_Emissao`: moeda (R$) |
| Dados pessoais | `CNPJ` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/securit-doc-dfin_cra, https://dados.cvm.gov.br/dataset/securit-doc-inf_mensal_cra). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/SECURIT/DOC/DFIN_CRA/DADOS/`, `https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRA/DADOS/`.
- O catálogo do fetcher lista 16 arquivo(s), em 2 séries: `dfin_cra` (de `dfin_cra_2019.csv` a `dfin_cra_2026.csv`); `inf_mensal_cra` (de `inf_mensal_cra_2019.zip` a `inf_mensal_cra_2026.zip`).
- Em 2026-11-16 conferimos 18 arquivos Parquet convertidos de 4 arquivo(s) de origem (amostra: 2019, 2026).
- No bruto, o arquivo fica em `securit-cra/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma demonstração financeira entregue (em `dfin_cra`) ou o informe mensal de um certificado em uma competência e versão (nas tabelas `inf_mensal_cra_*`).
- Particionado por `ano`; o catálogo cobre 2019 a 2026, e conferimos as amostras 2019, 2026.
- O informe mensal de 2026 tem 5.942 linhas em `inf_mensal_cra_geral` (754 certificados, competências 2026-01 a 2026-09) e o de 2019 tem 580 (2019-09 a 2019-12): a série mensal começa em 2019-09. `Versao` vai de 1 a 4 em 2026 (4.856 linhas na versão 1 e 1.055 na 2).
- `dfin_cra` tem 384 demonstrações em 2026 e 137 em 2019; `Codigo_Identificacao_Certificado`, `Data_Referencia` e `Versao` identificam cada demonstração.
- Este dataset reúne 9 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `dfin_cra` | 9 | 384 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | o índice das demonstrações financeiras: emissora, certificado, data, versão, parecer do auditor e link do documento |
| `inf_mensal_cra_ativo_passivo` | 31 | 5.942 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | ativo e passivo da emissão |
| `inf_mensal_cra_cedente_devedor` | 7 | 10.933 | não determinada | cedentes e devedores dos direitos creditórios, com o percentual de cada um |
| `inf_mensal_cra_classe` | 23 | 10.858 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Codigo_CETIP`, `Quantidade_Certificados` | classes e séries do certificado, com quantidade, valor e taxas |
| `inf_mensal_cra_derivativos` | 20 | 5.942 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | operações com derivativos |
| `inf_mensal_cra_desembolso` | 22 | 5.942 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | pagamentos previstos por faixa de prazo |
| `inf_mensal_cra_direitos_creditorios` | 56 | 5.942 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | os direitos creditórios vinculados, por tipo e faixa de vencimento |
| `inf_mensal_cra_fluxo_caixa` | 21 | 5.942 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | recebimentos e pagamentos do mês, por classe |
| `inf_mensal_cra_geral` | 31 | 5.942 | `Codigo_Identificacao_Certificado`, `Data_Referencia`, `Versao` | dados gerais da emissão e do certificado (emissora, agente fiduciário, custodiante, séries) |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Emissora` | `CNPJ_Emissora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj emissora | — | todo |
| `Nome_Emissora` | `Nome_Emissora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome emissora (só em: `dfin_cra`) | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `dfin_cra`, `inf_mensal_cra_geral`) | — | todo |
| `Nome_Certificado` | `Nome_Certificado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome certificado (só em: `dfin_cra`) | — | todo |
| `Codigo_Identificacao_Certificado` | `Codigo_Identificacao_Certificado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo identificacao certificado | — | todo |
| `Link_Download` | `Link_Download` | texto | Endereço para download do documento (só em: `dfin_cra`) | — | todo |
| `Parecer_Auditor` | `Parecer_Auditor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: parecer auditor (só em: `dfin_cra`) | — | todo |
| `Ativo` | `Ativo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Direitos_Creditorios` | `Direitos_Creditorios` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_A_Vencer_Sem_Parcelas_Atraso` | `Creditos_A_Vencer_Sem_Parcelas_Atraso` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos a vencer sem parcelas atraso (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_A_Vencer_Com_Parcelas_Atraso` | `Creditos_A_Vencer_Com_Parcelas_Atraso` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos a vencer com parcelas atraso (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Creditos_Vencidos` | `Creditos_Vencidos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos vencidos (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Reducao_Valor_Recuperacao` | `Reducao_Valor_Recuperacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: reducao valor recuperacao (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Equivalentes` | `Caixa_Equivalentes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa equivalentes (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Titulos_Publicos_Federais` | `Caixa_Titulos_Publicos_Federais` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa titulos publicos federais (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Cotas_Fundos` | `Caixa_Cotas_Fundos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa cotas fundos (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Operacoes_Compromissadas` | `Caixa_Operacoes_Compromissadas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa operacoes compromissadas (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Caixa_Outros` | `Caixa_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: caixa outros (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Derivativos` | `Ativo_Derivativos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo derivativos (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Contratos_Termo` | `Ativo_Contratos_Termo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo contratos termo (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Futuros` | `Ativo_Futuros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo futuros (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Opcoes` | `Ativo_Opcoes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo opcoes (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Ativo_Swap` | `Ativo_Swap` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativo swap (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Ativos` | `Outros_Ativos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros ativos (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Passivo` | `Passivo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Derivativos` | `Passivo_Derivativos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo derivativos (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Contratos_Termo` | `Passivo_Contratos_Termo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo contratos termo (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Futuros` | `Passivo_Futuros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo futuros (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Opcoes` | `Passivo_Opcoes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo opcoes (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Passivo_Swap` | `Passivo_Swap` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: passivo swap (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Valor_Atualizado_Emissao` | `Valor_Atualizado_Emissao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor atualizado emissao (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Reducao_Valor_Emissao` | `Reducao_Valor_Emissao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: reducao valor emissao (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Outros_Passivos` | `Outros_Passivos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros passivos (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Companhia_Securitizadora_Emissora` | `Companhia_Securitizadora_Emissora` | decimal / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: companhia securitizadora emissora (só em: `inf_mensal_cra_ativo_passivo`) | moeda (R$) | todo |
| `Tipo` | `Tipo` | texto | Tipo (só em: `inf_mensal_cra_cedente_devedor`) | — | todo |
| `CNPJ` | `CNPJ` | texto | Cadastro Nacional de Pessoas Jurídicas (só em: `inf_mensal_cra_cedente_devedor`) | — | todo |
| `Percentual` | `Percentual` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual (só em: `inf_mensal_cra_cedente_devedor`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Classe` | `Classe` | texto | Classe (só em: `inf_mensal_cra_classe`) | — | todo |
| `Numero_Serie` | `Numero_Serie` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero serie (só em: `inf_mensal_cra_classe`) | código ou número de identificação (sem unidade) | todo |
| `Tipo_Oferta` | `Tipo_Oferta` | texto | Tipo da Oferta: se primária, secundária ou mista (só em: `inf_mensal_cra_classe`) | — | todo |
| `Codigo_CETIP` | `Codigo_CETIP` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo cetip (só em: `inf_mensal_cra_classe`) | — | todo |
| `Codigo_ISIN` | `Codigo_ISIN` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo isin (só em: `inf_mensal_cra_classe`) | — | todo |
| `Data_Vencimento` | `Data_Vencimento` | texto | Data de Vencimento (só em: `inf_mensal_cra_classe`) | — | todo |
| `Situacao` | `Situacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: situacao (só em: `inf_mensal_cra_classe`) | — | todo |
| `Valor_Total_Integralizado` | `Valor_Total_Integralizado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor total integralizado (só em: `inf_mensal_cra_classe`) | moeda (R$) | todo |
| `Taxa_Juros` | `Taxa_Juros` | texto | Taxa de juros (só em: `inf_mensal_cra_classe`) | — | todo |
| `Pagamento_Periodicidade` | `Pagamento_Periodicidade` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento periodicidade (só em: `inf_mensal_cra_classe`) | — | todo |
| `Pagamento_Mes_Base` | `Pagamento_Mes_Base` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento mes base (só em: `inf_mensal_cra_classe`) | — | todo |
| `Quantidade_Certificados` | `Quantidade_Certificados` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade certificados (só em: `inf_mensal_cra_classe`) | quantidade | todo |
| `Valor_Certificados` | `Valor_Certificados` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor certificados (só em: `inf_mensal_cra_classe`) | moeda (R$) | todo |
| `Rendimentos` | `Rendimentos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimentos (só em: `inf_mensal_cra_classe`) | moeda (R$) | todo |
| `Amortizacoes` | `Amortizacoes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: amortizacoes (só em: `inf_mensal_cra_classe`) | moeda (R$) | todo |
| `Rentabilidade` | `Rentabilidade` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rentabilidade (só em: `inf_mensal_cra_classe`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Classificacao_Risco_Atual` | `Classificacao_Risco_Atual` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: classificacao risco atual (só em: `inf_mensal_cra_classe`) | — | todo |
| `Indice_Subordinacao_Minimo` | `Indice_Subordinacao_Minimo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: indice subordinacao minimo (só em: `inf_mensal_cra_classe`) | índice (sem unidade) | todo |
| `Indice_Subordinacao_Data_Base` | `Indice_Subordinacao_Data_Base` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: indice subordinacao data base (só em: `inf_mensal_cra_classe`) | índice (sem unidade) | todo |
| `Mercado_Termo_Juros` | `Mercado_Termo_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo juros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Mercado_Termo_Commodities_Agricolas` | `Mercado_Termo_Commodities_Agricolas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo commodities agricolas (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Mercado_Termo_Cambio` | `Mercado_Termo_Cambio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo cambio (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Mercado_Termo_Outros` | `Mercado_Termo_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado termo outros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Futuros_Juros` | `Futuros_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros juros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Futuros_Commodities_Agricolas` | `Futuros_Commodities_Agricolas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros commodities agricolas (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Futuros_Cambio` | `Futuros_Cambio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros cambio (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Futuros_Outros` | `Futuros_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: futuros outros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Opcoes_Juros` | `Opcoes_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes juros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Opcoes_Commodities_Agricolas` | `Opcoes_Commodities_Agricolas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes commodities agricolas (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Opcoes_Cambio` | `Opcoes_Cambio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes cambio (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Opcoes_Outros` | `Opcoes_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: opcoes outros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Swap_Juros` | `Swap_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: swap juros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Swap_Commodities_Agricolas` | `Swap_Commodities_Agricolas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: swap commodities agricolas (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Swap_Cambio` | `Swap_Cambio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: swap cambio (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Swap_Outros` | `Swap_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: swap outros (só em: `inf_mensal_cra_derivativos`) | moeda (R$) | todo |
| `Pagamento_Despesas` | `Pagamento_Despesas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_Ate30Dias` | `Pagamento_Despesas_Ate30Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas ate30dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_31a60Dias` | `Pagamento_Despesas_31a60Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 31a60dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_61a90Dias` | `Pagamento_Despesas_61a90Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 61a90dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_91a120Dias` | `Pagamento_Despesas_91a120Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 91a120dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_121a150Dias` | `Pagamento_Despesas_121a150Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 121a150dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_151a180Dias` | `Pagamento_Despesas_151a180Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 151a180dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_181a360Dias` | `Pagamento_Despesas_181a360Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas 181a360dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Despesas_Acima361Dias` | `Pagamento_Despesas_Acima361Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento despesas acima361dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores` | `Pagamento_Investidores` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_Ate30Dias` | `Pagamento_Investidores_Ate30Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores ate30dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_31a60Dias` | `Pagamento_Investidores_31a60Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 31a60dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_61a90Dias` | `Pagamento_Investidores_61a90Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 61a90dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_91a120Dias` | `Pagamento_Investidores_91a120Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 91a120dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_121a150Dias` | `Pagamento_Investidores_121a150Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 121a150dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_151a180Dias` | `Pagamento_Investidores_151a180Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 151a180dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_181a360Dias` | `Pagamento_Investidores_181a360Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores 181a360dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Pagamento_Investidores_Acima361Dias` | `Pagamento_Investidores_Acima361Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamento investidores acima361dias (só em: `inf_mensal_cra_desembolso`) | moeda (R$) | todo |
| `Parcelas_Atraso` | `Parcelas_Atraso` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: parcelas atraso (só em: `inf_mensal_cra_direitos_creditorios`) | quantidade (parcelas) | todo |
| `Direitos_Creditorios_Receber` | `Direitos_Creditorios_Receber` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Producao` | `Direitos_Creditorios_Receber_Producao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber producao (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Comercializacao` | `Direitos_Creditorios_Receber_Comercializacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber comercializacao (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Beneficiamento` | `Direitos_Creditorios_Receber_Beneficiamento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber beneficiamento (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Industrializacao` | `Direitos_Creditorios_Receber_Industrializacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber industrializacao (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Producao_Insumos` | `Direitos_Creditorios_Receber_Producao_Insumos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber producao insumos (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Comercializacao_Insumos` | `Direitos_Creditorios_Receber_Comercializacao_Insumos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber comercializacao insumos (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Beneficiamento_Insumos` | `Direitos_Creditorios_Receber_Beneficiamento_Insumos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber beneficiamento insumos (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Industrializacao_Insumos` | `Direitos_Creditorios_Receber_Industrializacao_Insumos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber industrializacao insumos (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Producao_Maquinas` | `Direitos_Creditorios_Receber_Producao_Maquinas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber producao maquinas (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Comercializacao_Maquinas` | `Direitos_Creditorios_Receber_Comercializacao_Maquinas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber comercializacao maquinas (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Beneficiamento_Maquinas` | `Direitos_Creditorios_Receber_Beneficiamento_Maquinas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber beneficiamento maquinas (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Direitos_Creditorios_Receber_Industrializacao_Maquinas` | `Direitos_Creditorios_Receber_Industrializacao_Maquinas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios receber industrializacao maquinas (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Concentracao` | `Concentracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: concentracao (só em: `inf_mensal_cra_direitos_creditorios`) | — | todo |
| `A_Vencer` | `A_Vencer` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_Ate30Dias` | `A_Vencer_Ate30Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer ate30dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_31a60Dias` | `A_Vencer_31a60Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 31a60dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_61a90Dias` | `A_Vencer_61a90Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 61a90dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_91a120Dias` | `A_Vencer_91a120Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 91a120dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_121a150Dias` | `A_Vencer_121a150Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 121a150dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_151a180Dias` | `A_Vencer_151a180Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 151a180dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_181a360Dias` | `A_Vencer_181a360Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 181a360dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `A_Vencer_Acima361Dias` | `A_Vencer_Acima361Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer acima361dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos` | `Nao_Pagos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_Ate30Dias` | `Nao_Pagos_Ate30Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos ate30dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_31a60Dias` | `Nao_Pagos_31a60Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 31a60dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_61a90Dias` | `Nao_Pagos_61a90Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 61a90dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_91a120Dias` | `Nao_Pagos_91a120Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 91a120dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_121a150Dias` | `Nao_Pagos_121a150Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 121a150dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_151a180Dias` | `Nao_Pagos_151a180Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 151a180dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_181a360Dias` | `Nao_Pagos_181a360Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos 181a360dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Nao_Pagos_Acima361Dias` | `Nao_Pagos_Acima361Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nao pagos acima361dias (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Pre_Pagamentos` | `Pre_Pagamentos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pre pagamentos (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Pre_Pagamento_Lastro` | `Pre_Pagamento_Lastro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pre pagamento lastro (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Pre_Pagamento_Impacto` | `Pre_Pagamento_Impacto` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: pre pagamento impacto (só em: `inf_mensal_cra_direitos_creditorios`) | — | todo |
| `Dividas_Emissor_Securitizadora` | `Dividas_Emissor_Securitizadora` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: dividas emissor securitizadora (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Percentual_Coobrigacao_Cedentes` | `Percentual_Coobrigacao_Cedentes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual coobrigacao cedentes (só em: `inf_mensal_cra_direitos_creditorios`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Outras_Garantias` | `Percentual_Outras_Garantias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual outras garantias (só em: `inf_mensal_cra_direitos_creditorios`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Percentual_Garantias_Exceto_Coobrigacao` | `Percentual_Garantias_Exceto_Coobrigacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual garantias exceto coobrigacao (só em: `inf_mensal_cra_direitos_creditorios`) | percentual (a escala não consta do dicionário: fração de 0 a 1 em parte das colunas e pontos percentuais em outras) | todo |
| `Periodicidade_Avaliacao_Garantias` | `Periodicidade_Avaliacao_Garantias` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: periodicidade avaliacao garantias (só em: `inf_mensal_cra_direitos_creditorios`) | — | todo |
| `Duration_Carteira` | `Duration_Carteira` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: duration carteira (só em: `inf_mensal_cra_direitos_creditorios`) | — | todo |
| `Relacao_Total_Emissao` | `Relacao_Total_Emissao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: relacao total emissao (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Outras_Consideracoes` | `Outras_Consideracoes` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outras consideracoes (só em: `inf_mensal_cra_direitos_creditorios`) | — | todo |
| `Maior_Devedor` | `Maior_Devedor` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: maior devedor (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Cinco_Maiores_Devedores` | `Cinco_Maiores_Devedores` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cinco maiores devedores (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Dez_Maiores_Devedores` | `Dez_Maiores_Devedores` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: dez maiores devedores (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Vinte_Maiores_Devedores` | `Vinte_Maiores_Devedores` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vinte maiores devedores (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Maior_Cedente` | `Maior_Cedente` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: maior cedente (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Cinco_Maiores_Cedentes` | `Cinco_Maiores_Cedentes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cinco maiores cedentes (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Dez_Maiores_Cedentes` | `Dez_Maiores_Cedentes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: dez maiores cedentes (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Vinte_Maiores_Cedentes` | `Vinte_Maiores_Cedentes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vinte maiores cedentes (só em: `inf_mensal_cra_direitos_creditorios`) | moeda (R$) | todo |
| `Recebimentos_Direitos_Creditorios` | `Recebimentos_Direitos_Creditorios` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: recebimentos direitos creditorios (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Despesas` | `Pagamentos_Despesas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos despesas (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Senior` | `Pagamentos_Classe_Senior` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe senior (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Senior_Amortizacao_Principal` | `Pagamentos_Classe_Senior_Amortizacao_Principal` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe senior amortizacao principal (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Senior_Juros` | `Pagamentos_Classe_Senior_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe senior juros (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Mezanino` | `Pagamentos_Classe_Subordinada_Mezanino` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada mezanino (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal` | `Pagamentos_Classe_Subordinada_Mezanino_Amortizacao_Principal` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada mezanino amortizacao principal (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Mezanino_Juros` | `Pagamentos_Classe_Subordinada_Mezanino_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada mezanino juros (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Junior` | `Pagamentos_Classe_Subordinada_Junior` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada junior (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal` | `Pagamentos_Classe_Subordinada_Junior_Amortizacao_Principal` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada junior amortizacao principal (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Pagamentos_Classe_Subordinada_Junior_Juros` | `Pagamentos_Classe_Subordinada_Junior_Juros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: pagamentos classe subordinada junior juros (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Recebimentos_Alienacao_Caixa` | `Recebimentos_Alienacao_Caixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: recebimentos alienacao caixa (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Aquisicao_Caixa` | `Aquisicao_Caixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: aquisicao caixa (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Aquisicao_Novos_Direitos_Creditorios` | `Aquisicao_Novos_Direitos_Creditorios` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: aquisicao novos direitos creditorios (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Outros_Recebimentos` | `Outros_Recebimentos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros recebimentos (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Outros_Pagamentos` | `Outros_Pagamentos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros pagamentos (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Variacao_Liquida_Caixa` | `Variacao_Liquida_Caixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: variacao liquida caixa (só em: `inf_mensal_cra_fluxo_caixa`) | moeda (R$) | todo |
| `Companhia_Emissora` | `Companhia_Emissora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: companhia emissora (só em: `inf_mensal_cra_geral`) | — | todo |
| `Agente_Fiduciario` | `Agente_Fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: agente fiduciario (só em: `inf_mensal_cra_geral`) | — | todo |
| `CNPJ_Agente_Fiduciario` | `CNPJ_Agente_Fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj agente fiduciario (só em: `inf_mensal_cra_geral`) | — | todo |
| `Custodiante` | `Custodiante` | texto | Nome do Custodiante (só em: `inf_mensal_cra_geral`) | — | todo |
| `CNPJ_Custodiante` | `CNPJ_Custodiante` | texto | CNPJ do Custodiante (só em: `inf_mensal_cra_geral`) | — | todo |
| `Instituicao_Regime_Fiduciario` | `Instituicao_Regime_Fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: instituicao regime fiduciario (só em: `inf_mensal_cra_geral`) | — | todo |
| `Revolvencia` | `Revolvencia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: revolvencia (só em: `inf_mensal_cra_geral`) | — | todo |
| `Numero_Emissao` | `Numero_Emissao` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero emissao (só em: `inf_mensal_cra_geral`) | código ou número de identificação (sem unidade) | todo |
| `Nome_Emissao` | `Nome_Emissao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome emissao (só em: `inf_mensal_cra_geral`) | — | todo |
| `Quantidade_Series` | `Quantidade_Series` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: quantidade series (só em: `inf_mensal_cra_geral`) | quantidade | todo |
| `Data_Emissao` | `Data_Emissao` | texto | Data de Emissão (só em: `inf_mensal_cra_geral`) | — | todo |
| `Tipo_Lastro` | `Tipo_Lastro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo lastro (só em: `inf_mensal_cra_geral`) | — | todo |
| `Detalhamento_Lastro` | `Detalhamento_Lastro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: detalhamento lastro (só em: `inf_mensal_cra_geral`) | — | todo |
| `Sobrecolateralizacao` | `Sobrecolateralizacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: sobrecolateralizacao (só em: `inf_mensal_cra_geral`) | — | todo |
| `Outras_Caracteristicas_Emissao` | `Outras_Caracteristicas_Emissao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: outras caracteristicas emissao (só em: `inf_mensal_cra_geral`) | — | todo |
| `Cadeia_Producao` | `Cadeia_Producao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cadeia producao (só em: `inf_mensal_cra_geral`) | — | todo |
| `Tipo_Segmento` | `Tipo_Segmento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo segmento (só em: `inf_mensal_cra_geral`) | — | todo |
| `Especificacao_Tipo_Segmento` | `Especificacao_Tipo_Segmento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: especificacao tipo segmento (só em: `inf_mensal_cra_geral`) | — | todo |
| `Tipo_Retencao_Risco` | `Tipo_Retencao_Risco` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo retencao risco (só em: `inf_mensal_cra_geral`) | — | todo |
| `Retentor_Risco` | `Retentor_Risco` | inteiro / texto | Sem descrição no dicionário da CVM; pelo nome da coluna: retentor risco (só em: `inf_mensal_cra_geral`) | moeda (R$) | todo |
| `Agencia_Classificadora` | `Agencia_Classificadora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: agencia classificadora (só em: `inf_mensal_cra_geral`) | — | todo |
| `CNPJ_Agencia_Classificadora` | `CNPJ_Agencia_Classificadora` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj agencia classificadora (só em: `inf_mensal_cra_geral`) | — | todo |
| `Data_Ultima_Classificacao` | `Data_Ultima_Classificacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data ultima classificacao (só em: `inf_mensal_cra_geral`) | — | todo |
| `Recomposicao_Indice` | `Recomposicao_Indice` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: recomposicao indice (só em: `inf_mensal_cra_geral`) | — | todo |
| `Patrimonio_Liquido_Emissao` | `Patrimonio_Liquido_Emissao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: patrimonio liquido emissao (só em: `inf_mensal_cra_geral`) | moeda (R$) | todo |
| `Desempenho_Emissao` | `Desempenho_Emissao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: desempenho emissao (só em: `inf_mensal_cra_geral`) | — | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/securit-cra`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Várias versões por certificado e competência.** O arquivo traz cada reapresentação (`Versao`); para a posição vigente, escolha a maior `Versao` de cada `Codigo_Identificacao_Certificado` e `Data_Referencia`. A chave com `Versao` é única na maioria das tabelas.
- **`CNPJ` de cedentes e devedores não é só CNPJ.** Em `inf_mensal_cra_cedente_devedor` (arquivo de 2026), de 10.933 linhas, 5.948 têm 14 dígitos, 275 têm 11 (CPF), 1.106 têm 1 dígito (valor de preenchimento) e 99 vêm vazias; a coluna traz espaços nas pontas em alguns valores. Valide o tamanho antes de tratar como CNPJ.
- **`CNPJ_Emissora` com máscara.** Nas demais colunas de CNPJ (`CNPJ_Agente_Fiduciario`, `CNPJ_Custodiante`) o formato varia; normalize antes de juntar.
- **Competência como primeiro dia do mês.** `Data_Referencia` vem como `AAAA-MM-01` nos informes mensais.
- **Tipo inferido varia entre arquivos.** 2 coluna(s) (`Companhia_Securitizadora_Emissora`, `Retentor_Risco`) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Certificados distintos informados por mês em 2026.

```python
import duckdb

duckdb.sql("""
    SELECT Data_Referencia, count(DISTINCT Codigo_Identificacao_Certificado) AS certificados
    FROM read_parquet('lake/cvm/securit-cra/ano=2026/*__inf_mensal_cra_geral_2026.parquet')
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-dfin_cra
- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/securit-doc-inf_mensal_cra
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/SECURIT/DOC/DFIN_CRA/
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/SECURIT/DOC/INF_MENSAL_CRA/
