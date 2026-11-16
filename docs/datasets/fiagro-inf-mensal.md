---
dataset:
  id: fiagro-inf-mensal
  fonte: cvm
  titulo: "FIAGRO: Documentos: Informe Mensal (CVM)"
  resumo: "Informe mensal dos Fundos de Investimento nas Cadeias Produtivas Agroindustriais (FIAGRO): dados gerais, cotistas, ativos, passivos, rentabilidade e demais itens do informe, por classe (133 colunas), e as subclasses de cotas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fiagro-doc-inf_mensal
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fiagro-doc-inf_mensal"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização semanal para os últimos doze meses"
  cobertura: {inicio: 2025-05, fim: em-curso}
  unidade: "o informe mensal de uma classe de cotas de FIAGRO (tabela principal) ou de uma subclasse (tabela `inf_mensal_fiagro_subclasse`)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (competência, `Data_Referencia`)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [], colunas: 136}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    Numero_Cotistas: "quantidade"
    Numero_Cotistas_Pessoa_Natural: "quantidade"
    Numero_Cotistas_Pessoa_Juridica_Nao_Financeira: "quantidade"
    Numero_Cotistas_Pessoa_Juridica_Financeira: "quantidade"
    Numero_Cotistas_Investidor_Nao_Residente: "quantidade"
    Numero_Cotistas_Entidade_Previdencia_Complementar_Exceto_RPPS: "quantidade"
    Numero_Cotistas_Entidade_RPPS: "quantidade"
    Numero_Cotistas_Sociedade_Seguradora_Resseguradora: "quantidade"
    Numero_Cotistas_Fundos_Investimento: "quantidade"
    Numero_Cotistas_Distribuidos_Conta_Ordem: "quantidade"
    Numero_Cotistas_Outros_Tipos: "quantidade"
    Valor_Ativo: "moeda (R$)"
    Patrimonio_Liquido: "moeda (R$)"
    Cotas_Emitidas: "quantidade (cotas)"
    Valor_Patrimonial_Cotas: "moeda (R$)"
    Percentual_Despesas_Taxa_Administracao: "percentual (%)"
    Percentual_Despesas_Taxa_Gestao: "percentual (%)"
    Percentual_Despesas_Taxa_Distribuicao: "percentual (%)"
    Rentabilidade_Efetiva_Mes: "percentual (%)"
    Rentabilidade_Patrimonial_Mes: "percentual (%)"
    Dividend_Yield_Mes: "percentual (%)"
    Percentual_Amortizacao_Cotas_Mes: "percentual (%)"
    Total_Necessidades_Liquidez: "moeda (R$)"
    Fundos_Renda_Fixa: "moeda (R$)"
    Titulos_Renda_Fixa: "moeda (R$)"
    Total_Investido: "moeda (R$)"
    Imoveis_Rurais: "moeda (R$)"
    Participacoes_Societarias: "moeda (R$)"
    Ativos_Financeiros_Lato_Sensu: "moeda (R$)"
    Ativos_Financeiros: "moeda (R$)"
    Ativos_Financeiros_Emissao_IF: "moeda (R$)"
    LCA: "moeda (R$)"
    LCI: "moeda (R$)"
    Outros_Ativos_Emissao_IF: "moeda (R$)"
    Outros_Ativos_Financeiros: "moeda (R$)"
    Valores_Mobiliarios: "moeda (R$)"
    Titulos_Participacoes_Societarias: "moeda (R$)"
    Acoes_Certificados_Deposito: "moeda (R$)"
    Outros_Titulos_Participacao: "moeda (R$)"
    Titulos_Divida_Corporativa: "moeda (R$)"
    Debentures: "moeda (R$)"
    Debentures_Conversiveis: "moeda (R$)"
    Debentures_Nao_Conversiveis: "moeda (R$)"
    Notas_Comerciais: "moeda (R$)"
    Notas_Comerciais_Curto_Prazo: "moeda (R$)"
    Notas_Comerciais_Longo_Prazo: "moeda (R$)"
    Outros_Titulos_Divida_Corporativa: "moeda (R$)"
    Valor_Titulos_Credito: "moeda (R$)"
    CPR: "moeda (R$)"
    CPR_Financeira: "moeda (R$)"
    CPR_Fisica: "moeda (R$)"
    CDCA: "moeda (R$)"
    CDA_WA: "moeda (R$)"
    Outros_Titulos_Credito_Agronegocio: "moeda (R$)"
    Titulos_Credito_Liquidacao_Financeira: "moeda (R$)"
    Devedor_Pessoa_Juridica_Liquidacao_Financeira: "moeda (R$)"
    Devedor_Pessoa_Natural_Liquidacao_Financeira: "moeda (R$)"
    Titulos_Credito_Liquidacao_Fisica: "moeda (R$)"
    Devedor_Pessoa_Juridica_Liquidacao_Fisica: "moeda (R$)"
    Devedor_Pessoa_Natural_Liquidacao_Fisica: "moeda (R$)"
    Demais_Direitos_Creditorios: "moeda (R$)"
    Direitos_Creditorios_Agronegocio: "moeda (R$)"
    Direitos_Creditorios_Imoveis_Rurais: "moeda (R$)"
    Titulos_Securitizacao: "moeda (R$)"
    CRA: "moeda (R$)"
    CRI: "moeda (R$)"
    Outros_Titulos_Securitizacao: "moeda (R$)"
    Cotas_Fundos_Investimento: "moeda (R$)"
    FIF: "moeda (R$)"
    FIDC: "moeda (R$)"
    FII: "moeda (R$)"
    FIP: "moeda (R$)"
    FIIM: "moeda (R$)"
    FIAGRO: "moeda (R$)"
    Creditos_Carbono_Agronegocio: "moeda (R$)"
    Creditos_Descarbonizacao: "moeda (R$)"
    Valores_Receber: "moeda (R$)"
    Total_Ativos_Prazo_Vencimento: "moeda (R$)"
    A_Vencer: "moeda (R$)"
    A_Vencer_Ate30Dias: "moeda (R$)"
    A_Vencer_31a60Dias: "moeda (R$)"
    A_Vencer_61a90Dias: "moeda (R$)"
    A_Vencer_91a120Dias: "moeda (R$)"
    A_Vencer_121a180Dias: "moeda (R$)"
    A_Vencer_181a360Dias: "moeda (R$)"
    A_Vencer_361a720Dias: "moeda (R$)"
    A_Vencer_721a1080Dias: "moeda (R$)"
    A_Vencer_Acima1080_Dias: "moeda (R$)"
    Vencidos: "moeda (R$)"
    Vencidos_Ate30Dias: "moeda (R$)"
    Vencidos_31a60Dias: "moeda (R$)"
    Vencidos_61a90Dias: "moeda (R$)"
    Vencidos_91a120Dias: "moeda (R$)"
    Vencidos_121a180Dias: "moeda (R$)"
    Vencidos_181a360Dias: "moeda (R$)"
    Vencidos_361a720Dias: "moeda (R$)"
    Vencidos_721a1080Dias: "moeda (R$)"
    Vencidos_Acima1080Dias: "moeda (R$)"
    Rendimentos_Distribuir: "moeda (R$)"
    Taxa_Administracao_Pagar: "moeda (R$)"
    Taxa_Gestao_Pagar: "moeda (R$)"
    Taxa_Performance_Pagar: "moeda (R$)"
    Taxa_Distribuicao_Pagar: "moeda (R$)"
    Obrigacoes_Aquisicao_Ativos: "moeda (R$)"
    Adiantamento_Venda_Ativos: "moeda (R$)"
    Adiantamento_Valores_Receber: "moeda (R$)"
    Instrumentos_Financeiros_Derivativos: "moeda (R$)"
    Provisoes_Contigencias: "moeda (R$)"
    Outros_Valores_Pagar: "moeda (R$)"
    Total_Passivo: "moeda (R$)"
    Numero_Cotas: "quantidade"
    Valor_Patrimonial_Cota: "moeda (R$)"
  dados_pessoais:
    - {coluna: Email_Administrador, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# FIAGRO: Documentos: Informe Mensal

## Resumo

Informe mensal dos Fundos de Investimento nas Cadeias Produtivas Agroindustriais (FIAGRO): dados gerais, cotistas, ativos, passivos, rentabilidade e demais itens do informe, por classe (133 colunas), e as subclasses de cotas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fiagro-inf-mensal` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fiagro-doc-inf_mensal |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fiagro-doc-inf_mensal |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização semanal para os últimos doze meses |
| Cobertura | 2025-05 a em-curso |
| Unidade (uma linha) | o informe mensal de uma classe de cotas de FIAGRO (tabela principal) ou de uma subclasse (tabela `inf_mensal_fiagro_subclasse`) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (competência, `Data_Referencia`) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 136 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `Numero_Cotistas`: quantidade; `Numero_Cotistas_Pessoa_Natural`: quantidade; `Numero_Cotistas_Pessoa_Juridica_Nao_Financeira`: quantidade; `Numero_Cotistas_Pessoa_Juridica_Financeira`: quantidade; `Numero_Cotistas_Investidor_Nao_Residente`: quantidade; `Numero_Cotistas_Entidade_Previdencia_Complementar_Exceto_RPPS`: quantidade; `Numero_Cotistas_Entidade_RPPS`: quantidade; `Numero_Cotistas_Sociedade_Seguradora_Resseguradora`: quantidade; `Numero_Cotistas_Fundos_Investimento`: quantidade; `Numero_Cotistas_Distribuidos_Conta_Ordem`: quantidade; `Numero_Cotistas_Outros_Tipos`: quantidade; `Valor_Ativo`: moeda (R$); `Patrimonio_Liquido`: moeda (R$); `Cotas_Emitidas`: quantidade (cotas); `Valor_Patrimonial_Cotas`: moeda (R$); `Percentual_Despesas_Taxa_Administracao`: percentual (%); `Percentual_Despesas_Taxa_Gestao`: percentual (%); `Percentual_Despesas_Taxa_Distribuicao`: percentual (%); `Rentabilidade_Efetiva_Mes`: percentual (%); `Rentabilidade_Patrimonial_Mes`: percentual (%); `Dividend_Yield_Mes`: percentual (%); `Percentual_Amortizacao_Cotas_Mes`: percentual (%); `Total_Necessidades_Liquidez`: moeda (R$); `Fundos_Renda_Fixa`: moeda (R$); `Titulos_Renda_Fixa`: moeda (R$); `Total_Investido`: moeda (R$); `Imoveis_Rurais`: moeda (R$); `Participacoes_Societarias`: moeda (R$); `Ativos_Financeiros_Lato_Sensu`: moeda (R$); `Ativos_Financeiros`: moeda (R$); `Ativos_Financeiros_Emissao_IF`: moeda (R$); `LCA`: moeda (R$); `LCI`: moeda (R$); `Outros_Ativos_Emissao_IF`: moeda (R$); `Outros_Ativos_Financeiros`: moeda (R$); `Valores_Mobiliarios`: moeda (R$); `Titulos_Participacoes_Societarias`: moeda (R$); `Acoes_Certificados_Deposito`: moeda (R$); `Outros_Titulos_Participacao`: moeda (R$); `Titulos_Divida_Corporativa`: moeda (R$); `Debentures`: moeda (R$); `Debentures_Conversiveis`: moeda (R$); `Debentures_Nao_Conversiveis`: moeda (R$); `Notas_Comerciais`: moeda (R$); `Notas_Comerciais_Curto_Prazo`: moeda (R$); `Notas_Comerciais_Longo_Prazo`: moeda (R$); `Outros_Titulos_Divida_Corporativa`: moeda (R$); `Valor_Titulos_Credito`: moeda (R$); `CPR`: moeda (R$); `CPR_Financeira`: moeda (R$); `CPR_Fisica`: moeda (R$); `CDCA`: moeda (R$); `CDA_WA`: moeda (R$); `Outros_Titulos_Credito_Agronegocio`: moeda (R$); `Titulos_Credito_Liquidacao_Financeira`: moeda (R$); `Devedor_Pessoa_Juridica_Liquidacao_Financeira`: moeda (R$); `Devedor_Pessoa_Natural_Liquidacao_Financeira`: moeda (R$); `Titulos_Credito_Liquidacao_Fisica`: moeda (R$); `Devedor_Pessoa_Juridica_Liquidacao_Fisica`: moeda (R$); `Devedor_Pessoa_Natural_Liquidacao_Fisica`: moeda (R$); `Demais_Direitos_Creditorios`: moeda (R$); `Direitos_Creditorios_Agronegocio`: moeda (R$); `Direitos_Creditorios_Imoveis_Rurais`: moeda (R$); `Titulos_Securitizacao`: moeda (R$); `CRA`: moeda (R$); `CRI`: moeda (R$); `Outros_Titulos_Securitizacao`: moeda (R$); `Cotas_Fundos_Investimento`: moeda (R$); `FIF`: moeda (R$); `FIDC`: moeda (R$); `FII`: moeda (R$); `FIP`: moeda (R$); `FIIM`: moeda (R$); `FIAGRO`: moeda (R$); `Creditos_Carbono_Agronegocio`: moeda (R$); `Creditos_Descarbonizacao`: moeda (R$); `Valores_Receber`: moeda (R$); `Total_Ativos_Prazo_Vencimento`: moeda (R$); `A_Vencer`: moeda (R$); `A_Vencer_Ate30Dias`: moeda (R$); `A_Vencer_31a60Dias`: moeda (R$); `A_Vencer_61a90Dias`: moeda (R$); `A_Vencer_91a120Dias`: moeda (R$); `A_Vencer_121a180Dias`: moeda (R$); `A_Vencer_181a360Dias`: moeda (R$); `A_Vencer_361a720Dias`: moeda (R$); `A_Vencer_721a1080Dias`: moeda (R$); `A_Vencer_Acima1080_Dias`: moeda (R$); `Vencidos`: moeda (R$); `Vencidos_Ate30Dias`: moeda (R$); `Vencidos_31a60Dias`: moeda (R$); `Vencidos_61a90Dias`: moeda (R$); `Vencidos_91a120Dias`: moeda (R$); `Vencidos_121a180Dias`: moeda (R$); `Vencidos_181a360Dias`: moeda (R$); `Vencidos_361a720Dias`: moeda (R$); `Vencidos_721a1080Dias`: moeda (R$); `Vencidos_Acima1080Dias`: moeda (R$); `Rendimentos_Distribuir`: moeda (R$); `Taxa_Administracao_Pagar`: moeda (R$); `Taxa_Gestao_Pagar`: moeda (R$); `Taxa_Performance_Pagar`: moeda (R$); `Taxa_Distribuicao_Pagar`: moeda (R$); `Obrigacoes_Aquisicao_Ativos`: moeda (R$); `Adiantamento_Venda_Ativos`: moeda (R$); `Adiantamento_Valores_Receber`: moeda (R$); `Instrumentos_Financeiros_Derivativos`: moeda (R$); `Provisoes_Contigencias`: moeda (R$); `Outros_Valores_Pagar`: moeda (R$); `Total_Passivo`: moeda (R$); `Numero_Cotas`: quantidade; `Valor_Patrimonial_Cota`: moeda (R$) |
| Dados pessoais | `Email_Administrador` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fiagro-doc-inf_mensal). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FIAGRO/DOC/INF_MENSAL/DADOS/`.
- O catálogo do fetcher lista 19 arquivo(s): de `inf_mensal_fiagro_202505.zip` a `inf_mensal_fiagro_202611.zip`.
- Em 2026-11-16 conferimos 6 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2025-05, 2026-02, 2026-10).
- No bruto, o arquivo fica em `fiagro-inf-mensal/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe mensal de uma classe de cotas de FIAGRO (tabela principal) ou de uma subclasse (tabela `inf_mensal_fiagro_subclasse`).
- Particionado por `ano` e `mes`; o catálogo cobre 2025-05 a 2026-11, e conferimos as amostras 2025-05, 2026-02, 2026-10.
- Os FIAGRO entraram no informe mensal em 2025-05: o arquivo de 2025-05 tem 3 classes, o de 2026-02 tem 226 e o de 2026-10 tem 317 linhas para 315 CNPJ (mais 721 linhas de subclasses). `Versao` numera as reapresentações.
- Este dataset reúne 2 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `inf_mensal_fiagro` | 133 | 317 | `CNPJ_Classe`, `Data_Registro` | o informe por classe: dados gerais, cotistas por tipo, ativos, passivos, liquidez e rentabilidade |
| `inf_mensal_fiagro_subclasse` | 6 | 721 | não determinada | o valor patrimonial da cota por subclasse, com o nome da classe e da subclasse |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Classe` | `CNPJ_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj classe | — | todo |
| `Nome_Classe` | `Nome_Classe` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome classe | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `inf_mensal_fiagro`) | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento (só em: `inf_mensal_fiagro`) | código ou número de identificação (sem unidade) | todo |
| `Classe_Unica` | `Classe_Unica` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: classe unica (só em: `inf_mensal_fiagro`) | — | todo |
| `CNPJ_Administrador` | `CNPJ_Administrador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj administrador (só em: `inf_mensal_fiagro`) | — | todo |
| `Nome_Administrador` | `Nome_Administrador` | texto | Nome do administrador (só em: `inf_mensal_fiagro`) | — | todo |
| `Data_Registro` | `Data_Registro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data registro (só em: `inf_mensal_fiagro`) | — | todo |
| `Publico_Alvo` | `Publico_Alvo` | texto | Público-alvo (só em: `inf_mensal_fiagro`) | — | todo |
| `Codigo_ISIN` | `Codigo_ISIN` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: codigo isin (só em: `inf_mensal_fiagro`) | — | todo |
| `Cotistas_Vinculo_Familiar` | `Cotistas_Vinculo_Familiar` | texto | Indica se os cotistas possuem vínculo familiar ou societário familiar (só em: `inf_mensal_fiagro`) | S/N | todo |
| `Regra_Anexo` | `Regra_Anexo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: regra anexo (só em: `inf_mensal_fiagro`) | — | todo |
| `Classificacao_Autorregulada` | `Classificacao_Autorregulada` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: classificacao autorregulada (só em: `inf_mensal_fiagro`) | — | todo |
| `Prazo_Duracao` | `Prazo_Duracao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: prazo duracao (só em: `inf_mensal_fiagro`) | — | todo |
| `Encerramento_Exercicio_Social` | `Encerramento_Exercicio_Social` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: encerramento exercicio social (só em: `inf_mensal_fiagro`) | — | todo |
| `Mercado_Negociacao` | `Mercado_Negociacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado negociacao (só em: `inf_mensal_fiagro`) | — | todo |
| `Entidade_Administradora` | `Entidade_Administradora` | texto | Entidade administradora (só em: `inf_mensal_fiagro`) | — | todo |
| `Email_Administrador` | `Email_Administrador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: email administrador (só em: `inf_mensal_fiagro`) | — | todo |
| `Servico_Atendimento_Cotista` | `Servico_Atendimento_Cotista` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: servico atendimento cotista (só em: `inf_mensal_fiagro`) | — | todo |
| `Site` | `Site` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: site (só em: `inf_mensal_fiagro`) | — | todo |
| `Nome_Gestor` | `Nome_Gestor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome gestor (só em: `inf_mensal_fiagro`) | — | todo |
| `CNPJ_Gestor` | `CNPJ_Gestor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj gestor (só em: `inf_mensal_fiagro`) | — | todo |
| `Numero_Cotistas` | `Numero_Cotistas` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Pessoa_Natural` | `Numero_Cotistas_Pessoa_Natural` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas pessoa natural (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Pessoa_Juridica_Nao_Financeira` | `Numero_Cotistas_Pessoa_Juridica_Nao_Financeira` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas pessoa juridica nao financeira (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Pessoa_Juridica_Financeira` | `Numero_Cotistas_Pessoa_Juridica_Financeira` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas pessoa juridica financeira (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Investidor_Nao_Residente` | `Numero_Cotistas_Investidor_Nao_Residente` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas investidor nao residente (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Entidade_Previdencia_Complementar_Exceto_RPPS` | `Numero_Cotistas_Entidade_Previdencia_Complementar_Exceto_RPPS` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas entidade previdencia complementar exceto rpps (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Entidade_RPPS` | `Numero_Cotistas_Entidade_RPPS` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas entidade rpps (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Sociedade_Seguradora_Resseguradora` | `Numero_Cotistas_Sociedade_Seguradora_Resseguradora` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas sociedade seguradora resseguradora (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Fundos_Investimento` | `Numero_Cotistas_Fundos_Investimento` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas fundos investimento (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Distribuidos_Conta_Ordem` | `Numero_Cotistas_Distribuidos_Conta_Ordem` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas distribuidos conta ordem (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Numero_Cotistas_Outros_Tipos` | `Numero_Cotistas_Outros_Tipos` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotistas outros tipos (só em: `inf_mensal_fiagro`) | quantidade | todo |
| `Valor_Ativo` | `Valor_Ativo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor ativo (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Patrimonio_Liquido` | `Patrimonio_Liquido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: patrimonio liquido (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Cotas_Emitidas` | `Cotas_Emitidas` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: cotas emitidas (só em: `inf_mensal_fiagro`) | quantidade (cotas) | todo |
| `Valor_Patrimonial_Cotas` | `Valor_Patrimonial_Cotas` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor patrimonial cotas (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Percentual_Despesas_Taxa_Administracao` | `Percentual_Despesas_Taxa_Administracao` | decimal | Percentual de despesas com a taxa de administração em relação ao patrimônio líquido do mês (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Percentual_Despesas_Taxa_Gestao` | `Percentual_Despesas_Taxa_Gestao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual despesas taxa gestao (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Percentual_Despesas_Taxa_Distribuicao` | `Percentual_Despesas_Taxa_Distribuicao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: percentual despesas taxa distribuicao (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Rentabilidade_Efetiva_Mes` | `Rentabilidade_Efetiva_Mes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rentabilidade efetiva mes (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Rentabilidade_Patrimonial_Mes` | `Rentabilidade_Patrimonial_Mes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rentabilidade patrimonial mes (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Dividend_Yield_Mes` | `Dividend_Yield_Mes` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: dividend yield mes (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Percentual_Amortizacao_Cotas_Mes` | `Percentual_Amortizacao_Cotas_Mes` | decimal | Percentual de amortizações de cotas do Mês de Referência (só em: `inf_mensal_fiagro`) | percentual (%) | todo |
| `Total_Necessidades_Liquidez` | `Total_Necessidades_Liquidez` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total necessidades liquidez (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Fundos_Renda_Fixa` | `Fundos_Renda_Fixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: fundos renda fixa (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Titulos_Renda_Fixa` | `Titulos_Renda_Fixa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos renda fixa (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Total_Investido` | `Total_Investido` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total investido (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Imoveis_Rurais` | `Imoveis_Rurais` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: imoveis rurais (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Participacoes_Societarias` | `Participacoes_Societarias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: participacoes societarias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Ativos_Financeiros_Lato_Sensu` | `Ativos_Financeiros_Lato_Sensu` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativos financeiros lato sensu (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Ativos_Financeiros` | `Ativos_Financeiros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativos financeiros (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Ativos_Financeiros_Emissao_IF` | `Ativos_Financeiros_Emissao_IF` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: ativos financeiros emissao if (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `LCA` | `LCA` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: lca (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `LCI` | `LCI` | decimal | Letras de Crédito Imobiliário (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Ativos_Emissao_IF` | `Outros_Ativos_Emissao_IF` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros ativos emissao if (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Ativos_Financeiros` | `Outros_Ativos_Financeiros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros ativos financeiros (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Valores_Mobiliarios` | `Valores_Mobiliarios` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valores mobiliarios (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Titulos_Participacoes_Societarias` | `Titulos_Participacoes_Societarias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos participacoes societarias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Acoes_Certificados_Deposito` | `Acoes_Certificados_Deposito` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: acoes certificados deposito (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Titulos_Participacao` | `Outros_Titulos_Participacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros titulos participacao (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Titulos_Divida_Corporativa` | `Titulos_Divida_Corporativa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos divida corporativa (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Debentures` | `Debentures` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: debentures (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Debentures_Conversiveis` | `Debentures_Conversiveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: debentures conversiveis (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Debentures_Nao_Conversiveis` | `Debentures_Nao_Conversiveis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: debentures nao conversiveis (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Notas_Comerciais` | `Notas_Comerciais` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: notas comerciais (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Notas_Comerciais_Curto_Prazo` | `Notas_Comerciais_Curto_Prazo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: notas comerciais curto prazo (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Notas_Comerciais_Longo_Prazo` | `Notas_Comerciais_Longo_Prazo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: notas comerciais longo prazo (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Titulos_Divida_Corporativa` | `Outros_Titulos_Divida_Corporativa` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros titulos divida corporativa (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Valor_Titulos_Credito` | `Valor_Titulos_Credito` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor titulos credito (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CPR` | `CPR` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cpr (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CPR_Financeira` | `CPR_Financeira` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cpr financeira (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CPR_Fisica` | `CPR_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cpr fisica (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CDCA` | `CDCA` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cdca (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CDA_WA` | `CDA_WA` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cda wa (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Titulos_Credito_Agronegocio` | `Outros_Titulos_Credito_Agronegocio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros titulos credito agronegocio (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Titulos_Credito_Liquidacao_Financeira` | `Titulos_Credito_Liquidacao_Financeira` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos credito liquidacao financeira (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Devedor_Pessoa_Juridica_Liquidacao_Financeira` | `Devedor_Pessoa_Juridica_Liquidacao_Financeira` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: devedor pessoa juridica liquidacao financeira (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Devedor_Pessoa_Natural_Liquidacao_Financeira` | `Devedor_Pessoa_Natural_Liquidacao_Financeira` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: devedor pessoa natural liquidacao financeira (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Titulos_Credito_Liquidacao_Fisica` | `Titulos_Credito_Liquidacao_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos credito liquidacao fisica (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Devedor_Pessoa_Juridica_Liquidacao_Fisica` | `Devedor_Pessoa_Juridica_Liquidacao_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: devedor pessoa juridica liquidacao fisica (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Devedor_Pessoa_Natural_Liquidacao_Fisica` | `Devedor_Pessoa_Natural_Liquidacao_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: devedor pessoa natural liquidacao fisica (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Demais_Direitos_Creditorios` | `Demais_Direitos_Creditorios` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: demais direitos creditorios (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Direitos_Creditorios_Agronegocio` | `Direitos_Creditorios_Agronegocio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios agronegocio (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Direitos_Creditorios_Imoveis_Rurais` | `Direitos_Creditorios_Imoveis_Rurais` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: direitos creditorios imoveis rurais (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Titulos_Securitizacao` | `Titulos_Securitizacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: titulos securitizacao (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CRA` | `CRA` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cra (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `CRI` | `CRI` | decimal | Certificado de Recebíveis Imobiliários (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Titulos_Securitizacao` | `Outros_Titulos_Securitizacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros titulos securitizacao (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Cotas_Fundos_Investimento` | `Cotas_Fundos_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: cotas fundos investimento (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `FIF` | `FIF` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: fif (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `FIDC` | `FIDC` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: fidc (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `FII` | `FII` | decimal | Fundo de Investimento Imobiliário (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `FIP` | `FIP` | decimal | Fundo de Investimento em Participações (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `FIIM` | `FIIM` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: fiim (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `FIAGRO` | `FIAGRO` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: fiagro (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Creditos_Carbono_Agronegocio` | `Creditos_Carbono_Agronegocio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos carbono agronegocio (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Creditos_Descarbonizacao` | `Creditos_Descarbonizacao` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: creditos descarbonizacao (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Valores_Receber` | `Valores_Receber` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valores receber (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Total_Ativos_Prazo_Vencimento` | `Total_Ativos_Prazo_Vencimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total ativos prazo vencimento (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer` | `A_Vencer` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_Ate30Dias` | `A_Vencer_Ate30Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer ate30dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_31a60Dias` | `A_Vencer_31a60Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 31a60dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_61a90Dias` | `A_Vencer_61a90Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 61a90dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_91a120Dias` | `A_Vencer_91a120Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 91a120dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_121a180Dias` | `A_Vencer_121a180Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 121a180dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_181a360Dias` | `A_Vencer_181a360Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 181a360dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_361a720Dias` | `A_Vencer_361a720Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 361a720dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_721a1080Dias` | `A_Vencer_721a1080Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer 721a1080dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `A_Vencer_Acima1080_Dias` | `A_Vencer_Acima1080_Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: a vencer acima1080 dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos` | `Vencidos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_Ate30Dias` | `Vencidos_Ate30Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos ate30dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_31a60Dias` | `Vencidos_31a60Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 31a60dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_61a90Dias` | `Vencidos_61a90Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 61a90dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_91a120Dias` | `Vencidos_91a120Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 91a120dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_121a180Dias` | `Vencidos_121a180Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 121a180dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_181a360Dias` | `Vencidos_181a360Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 181a360dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_361a720Dias` | `Vencidos_361a720Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 361a720dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_721a1080Dias` | `Vencidos_721a1080Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos 721a1080dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Vencidos_Acima1080Dias` | `Vencidos_Acima1080Dias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: vencidos acima1080dias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Rendimentos_Distribuir` | `Rendimentos_Distribuir` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: rendimentos distribuir (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Taxa_Administracao_Pagar` | `Taxa_Administracao_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa administracao pagar (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Taxa_Gestao_Pagar` | `Taxa_Gestao_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa gestao pagar (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Taxa_Performance_Pagar` | `Taxa_Performance_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa performance pagar (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Taxa_Distribuicao_Pagar` | `Taxa_Distribuicao_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: taxa distribuicao pagar (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Obrigacoes_Aquisicao_Ativos` | `Obrigacoes_Aquisicao_Ativos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: obrigacoes aquisicao ativos (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Adiantamento_Venda_Ativos` | `Adiantamento_Venda_Ativos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: adiantamento venda ativos (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Adiantamento_Valores_Receber` | `Adiantamento_Valores_Receber` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: adiantamento valores receber (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Instrumentos_Financeiros_Derivativos` | `Instrumentos_Financeiros_Derivativos` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: instrumentos financeiros derivativos (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Provisoes_Contigencias` | `Provisoes_Contigencias` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: provisoes contigencias (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Outros_Valores_Pagar` | `Outros_Valores_Pagar` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: outros valores pagar (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Total_Passivo` | `Total_Passivo` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: total passivo (só em: `inf_mensal_fiagro`) | moeda (R$) | todo |
| `Nome_Subclasse` | `Nome_Subclasse` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: nome subclasse (só em: `inf_mensal_fiagro_subclasse`) | — | todo |
| `Numero_Cotas` | `Numero_Cotas` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero cotas (só em: `inf_mensal_fiagro_subclasse`) | quantidade | todo |
| `Valor_Patrimonial_Cota` | `Valor_Patrimonial_Cota` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor patrimonial cota (só em: `inf_mensal_fiagro_subclasse`) | moeda (R$) | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fiagro-inf-mensal`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **CNPJ só com dígitos.** `CNPJ_Classe`, `CNPJ_Administrador` e `CNPJ_Gestor` vêm sem máscara, ao contrário dos informes de fundos e balancetes (`00.000.000/0000-00`); normalize antes de juntar.
- **Reapresentações.** Uma classe pode ter mais de uma linha na mesma competência (`Versao`, `Data_Entrega`); escolha a maior `Versao` antes de somar.
- **Texto com espaços nas pontas.** `Nome_Gestor` traz espaços no início ou no fim de alguns valores; aplique `trim` antes de agrupar.
- **Competência como data do primeiro dia do mês.** `Data_Referencia` vem como `AAAA-MM-01` (por exemplo, 2026-10-01 no arquivo de 2026-10), não como o último dia do mês.

## Exemplos

Classes de FIAGRO informadas por mês, só a última versão de cada classe e competência.

```python
import duckdb

duckdb.sql("""
    SELECT ano, mes, count(DISTINCT CNPJ_Classe) AS classes
    FROM read_parquet('lake/cvm/fiagro-inf-mensal/**/inf_mensal_fiagro_20*__inf_mensal_fiagro_20*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fiagro-doc-inf_mensal
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FIAGRO/DOC/INF_MENSAL/
