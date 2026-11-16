---
dataset:
  id: ofertas
  fonte: cvm
  titulo: "Ofertas Públicas de Distribuição (CVM)"
  resumo: "Ofertas públicas de distribuição de valores mobiliários registradas ou dispensadas de registro na CVM (ICVM 400, RCVM 160, ICVM 476 encerradas), em duas tabelas: `oferta_distribuicao` e `oferta_resolucao_160` (ofertas em rito automático desde 2023)."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/oferta-distrib
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/oferta-distrib"
  periodicidade: "diária (o portal declara atualização diária; o arquivo foi regravado em 2026-11-14, mas estava sem conteúdo)"
  cobertura: {inicio: 2000, fim: em-curso}
  unidade: "uma oferta pública de distribuição de valores mobiliários"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "por oferta (sem periodicidade fixa); o arquivo é um retrato completo reenviado todo dia"}
  formato_bruto: "ZIP com dois CSV (`oferta_distribuicao.csv` e `oferta_resolucao_160.csv`, ponto e vírgula) no espelho público da CVM"
  lake: {estado: so-bruto, particoes: [], chave: [], colunas: null}
  dados_pessoais:
    - {coluna: Nome_Ofertante, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: Nome_Vendedor, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
  eras:
    - {desde: 2022-05, mudanca: "entram `Modalidade_Oferta`, `Data_Inicio_Oferta`, `Tipo_Societario_Emissor`, `Tipo_Fundo_Investimento`, `Ultimo_Comunicado` e `Data_Comunicado`; `Modalidade_Registro_Oferta` e `Modalidade_Dispensa_Oferta` viram `Modalidade_Registro` e `Modalidade_Dispensa_Registro` (segundo o portal)"}
    - {desde: 2023-10, mudanca: "as ofertas em rito automático (Resolução CVM 160, requeridas desde 2023-01) passam a ser publicadas no segundo CSV, `oferta_resolucao_160` (segundo o portal, desde 2023-10-27)"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Ofertas Públicas de Distribuição

## Resumo

Ofertas públicas de distribuição de valores mobiliários registradas ou dispensadas de registro na CVM (ICVM 400, RCVM 160, ICVM 476 encerradas), em duas tabelas: `oferta_distribuicao` e `oferta_resolucao_160` (ofertas em rito automático desde 2023).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/ofertas` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/oferta-distrib |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/oferta-distrib |
| Periodicidade | diária (o portal declara atualização diária; o arquivo foi regravado em 2026-11-14, mas estava sem conteúdo) |
| Cobertura | 2000 a em-curso |
| Unidade (uma linha) | uma oferta pública de distribuição de valores mobiliários |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: por oferta (sem periodicidade fixa); o arquivo é um retrato completo reenviado todo dia |
| Formato bruto | ZIP com dois CSV (`oferta_distribuicao.csv` e `oferta_resolucao_160.csv`, ponto e vírgula) no espelho público da CVM |
| Estado no lake | so-bruto |
| Partições | — |
| Chave | — |
| Colunas | — |
| Unidades de medida | — |
| Dados pessoais | `Nome_Ofertante` (nome de pessoa física (diretor, responsável ou representante)); `Nome_Vendedor` (nome de pessoa física (diretor, responsável ou representante)) |
| Eras | 2022-05: entram `Modalidade_Oferta`, `Data_Inicio_Oferta`, `Tipo_Societario_Emissor`, `Tipo_Fundo_Investimento`, `Ultimo_Comunicado` e `Data_Comunicado`; `Modalidade_Registro_Oferta` e `Modalidade_Dispensa_Oferta` viram `Modalidade_Registro` e `Modalidade_Dispensa_Registro` (segundo o portal); 2023-10: as ofertas em rito automático (Resolução CVM 160, requeridas desde 2023-01) passam a ser publicadas no segundo CSV, `oferta_resolucao_160` (segundo o portal, desde 2023-10-27) |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/oferta-distrib). O arquivo fica no espelho público `https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/`.
- O catálogo do fetcher lista 1 arquivo: `oferta_distribuicao.zip`. **Em 2026-11-16 esse ZIP tinha 22 bytes e nenhum arquivo dentro** (só o registro de fim de arquivo; `Last-Modified` de 2026-11-14); por isso não há Parquet convertido nem esquema de referência, e as descrições abaixo vêm só do dicionário de dados.
- No bruto, o arquivo fica em `ofertas/oferta_distribuicao@AAAAMMDD.zip`; o carimbo é a data da coleta.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`, um por tabela) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele e **não foram conferidas contra os cabeçalhos dos arquivos**, porque o arquivo estava vazio.

## Conteúdo

- Unidade de análise: uma oferta pública de distribuição de valores mobiliários.
- Sem partição: um único arquivo reenviado todo dia, com todas as ofertas.
- Segundo o portal, `oferta_distribuicao.csv` traz as ofertas registradas ou dispensadas de registro (ICVM 400 ou RCVM 160 em rito ordinário), as de registro automático (ICVM 555) e as de esforços restritos (ICVM 476) encerradas desde 2022-01-01; `oferta_resolucao_160.csv` traz as ofertas primárias ou secundárias requeridas em rito automático (Resolução CVM 160) desde 2023-01-02.
- O início da cobertura (2000) vem da descrição do catálogo do fetcher; não foi conferido na fonte.

| Tabela | Colunas no dicionário |
|---|---|
| `oferta_distribuicao` | 76 |
| `oferta_resolucao_160` | 71 |

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM, sem conferência contra dados (o arquivo de origem estava vazio). O tipo é o do dicionário (`varchar`, `numeric`, `bigint` ou `date`). Os nomes de coluna são os do dicionário, sem normalização.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Atualizacao_Monetaria` | `Atualizacao_Monetaria` | texto | Atualização Monetária (só em: `oferta_distribuicao`) | — | todo |
| `Classe_Ativo` | `Classe_Ativo` | texto | Classe do ativo (valor mobiliário) objeto da oferta (só em: `oferta_distribuicao`) | — | todo |
| `CNPJ_Emissor` | `CNPJ_Emissor` | texto | CNPJ do emissor | — | todo |
| `CNPJ_Lider` | `CNPJ_Lider` | texto | CNPJ do Líder | — | todo |
| `CNPJ_Ofertante` | `CNPJ_Ofertante` | texto | CNPJ do Ofertante (só em: `oferta_distribuicao`) | — | todo |
| `Data_Abertura_Processo` | `Data_Abertura_Processo` | texto (data AAAA-MM-DD) | Data de Abertura do Processo Administrativo (só em: `oferta_distribuicao`) | — | todo |
| `Data_Dispensa_Oferta` | `Data_Dispensa_Oferta` | texto (data AAAA-MM-DD) | Data em que foi concedido o pedido de dispensa de registro da oferta (só em: `oferta_distribuicao`) | — | todo |
| `Data_Emissao` | `Data_Emissao` | texto (data AAAA-MM-DD) | Data de Emissão (só em: `oferta_distribuicao`) | — | todo |
| `Data_Encerramento_Oferta` | `Data_Encerramento_Oferta` | texto (data AAAA-MM-DD) | Data em que a oferta foi encerrada (só em: `oferta_distribuicao`) | — | todo |
| `Data_Protocolo` | `Data_Protocolo` | texto (data AAAA-MM-DD) | Data de Protocolo (só em: `oferta_distribuicao`) | — | todo |
| `Data_Registro_Oferta` | `Data_Registro_Oferta` | texto (data AAAA-MM-DD) | Data em que foi concedido o pedido de registro da oferta (só em: `oferta_distribuicao`) | — | todo |
| `Data_Vencimento` | `Data_Vencimento` | texto (data AAAA-MM-DD) | Data de Vencimento (só em: `oferta_distribuicao`) | — | todo |
| `Emissao` | `Emissao` | texto | Número da Emissão | — | todo |
| `Especie_Ativo` | `Especie_Ativo` | texto | Espécie do ativo (valor mobiliário) objeto da oferta (só em: `oferta_distribuicao`) | — | todo |
| `Forma_Ativo` | `Forma_Ativo` | texto | Forma do ativo (valor mobiliário) objeto da oferta (só em: `oferta_distribuicao`) | — | todo |
| `Juros` | `Juros` | texto | Juros (só em: `oferta_distribuicao`) | — | todo |
| `Nome_Emissor` | `Nome_Emissor` | texto | Nome do Emissor | — | todo |
| `Nome_Lider` | `Nome_Lider` | texto | Nome do Líder | — | todo |
| `Nome_Ofertante` | `Nome_Ofertante` | texto | Nome do Ofertante (só em: `oferta_distribuicao`) | — | todo |
| `Nome_Vendedor` | `Nome_Vendedor` | texto | Nome do Vendedor (só em: `oferta_distribuicao`) | — | todo |
| `Numero_Processo` | `Numero_Processo` | texto | Número do Processo Administrativo | — | todo |
| `Numero_Registro_Oferta` | `Numero_Registro_Oferta` | texto | Número de Registro da Oferta (só em: `oferta_distribuicao`) | — | todo |
| `Oferta_Incentivo_Fiscal` | `Oferta_Incentivo_Fiscal` | texto | Indica se a oferta é elegível ao incentivo previsto na Lei nº 12.431/11 (só em: `oferta_distribuicao`) | S/N | todo |
| `Oferta_Inicial` | `Oferta_Inicial` | texto | Indica se é uma oferta inicial (IPO) (só em: `oferta_distribuicao`) | S/N | todo |
| `Oferta_Regime_Fiduciario` | `Oferta_Regime_Fiduciario` | texto | Indica se os créditos que lastream a emissão dos ativos (valores mobiliários) objeto da oferta contam com regime fiduciário (só em: `oferta_distribuicao`) | S/N | todo |
| `Preco_Unitario` | `Preco_Unitario` | decimal | Preço Unitário (só em: `oferta_distribuicao`) | moeda (R$) | todo |
| `Projeto_Audiovisual` | `Projeto_Audiovisual` | texto | Projeto Audiovisual (só em: `oferta_distribuicao`) | — | todo |
| `Quantidade_No_Lote_Suplementar` | `Quantidade_No_Lote_Suplementar` | decimal | Quantidade no Lote Suplementar (só em: `oferta_distribuicao`) | quantidade | todo |
| `Quantidade_Sem_Lote_Suplementar` | `Quantidade_Sem_Lote_Suplementar` | decimal | Quantidade sem Lote Suplementar (só em: `oferta_distribuicao`) | quantidade | todo |
| `Quantidade_Total` | `Quantidade_Total` | decimal | Quantidade Total (só em: `oferta_distribuicao`) | quantidade | todo |
| `Rito_Oferta` | `Rito_Oferta` | texto | Rito seguido para a realização da oferta (só em: `oferta_distribuicao`) | — | todo |
| `Serie` | `Serie` | texto | Número da Série (só em: `oferta_distribuicao`) | — | todo |
| `Tipo_Ativo` | `Tipo_Ativo` | texto | Tipo de Ativo (Valor Mobiliário) (só em: `oferta_distribuicao`) | — | todo |
| `Tipo_Componente_Oferta_Mista` | `Tipo_Componente_Oferta_Mista` | texto | Tipo do componente de uma oferta mista (só em: `oferta_distribuicao`) | — | todo |
| `Tipo_Oferta` | `Tipo_Oferta` | texto | Tipo da Oferta: se primária, secundária ou mista | — | todo |
| `Valor_Total` | `Valor_Total` | decimal | Valor Total (só em: `oferta_distribuicao`) | moeda (R$) | todo |
| `Nr_Fundos_Investimento` | `Nr_Fundos_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr fundos investimento (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Investidor_Estrangeiro` | `Qtd_Investidor_Estrangeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd investidor estrangeiro (só em: `oferta_distribuicao`) | quantidade | todo |
| `Data_Inicio_Oferta` | `Data_Inicio_Oferta` | texto (data AAAA-MM-DD) | Sem descrição no dicionário da CVM; pelo nome da coluna: data inicio oferta (só em: `oferta_distribuicao`) | — | todo |
| `Nr_Pessoa_Fisica` | `Nr_Pessoa_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr pessoa fisica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Cli_Investidor_Estrangeiro` | `Qtd_Cli_Investidor_Estrangeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd cli investidor estrangeiro (só em: `oferta_distribuicao`) | quantidade | todo |
| `QtD_Cli_Demais_Pessoa_Juridica` | `QtD_Cli_Demais_Pessoa_Juridica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd cli demais pessoa juridica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Instit_Financ_Emissora_Partic_Consorcio` | `Qtd_Instit_Financ_Emissora_Partic_Consorcio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd instit financ emissora partic consorcio (só em: `oferta_distribuicao`) | quantidade | todo |
| `Modalidade_Oferta` | `Modalidade_Oferta` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: modalidade oferta (só em: `oferta_distribuicao`) | — | todo |
| `Nr_Outros` | `Nr_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr outros (só em: `oferta_distribuicao`) | quantidade | todo |
| `Tipo_Fundo_Investimento` | `Tipo_Fundo_Investimento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo fundo investimento (só em: `oferta_distribuicao`) | — | todo |
| `Qtd_Demais_Pessoa_Juridica` | `Qtd_Demais_Pessoa_Juridica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd demais pessoa juridica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Pessoa_Fisica` | `Qtd_Pessoa_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd pessoa fisica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Ultimo_Comunicado` | `Ultimo_Comunicado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ultimo comunicado (só em: `oferta_distribuicao`) | — | todo |
| `Qtd_Cli_Pessoa_Juridica_Ligada_Adm` | `Qtd_Cli_Pessoa_Juridica_Ligada_Adm` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd cli pessoa juridica ligada adm (só em: `oferta_distribuicao`) | quantidade | todo |
| `Modalidade_Registro` | `Modalidade_Registro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: modalidade registro (só em: `oferta_distribuicao`) | — | todo |
| `Qdt_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_Parti` | `Qdt_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_Parti` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qdt soc adm emp prop demais pess jurid emiss parti (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Investidor_Estrangeiro` | `Nr_Investidor_Estrangeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr investidor estrangeiro (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_Partic` | `Nr_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_Partic` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr soc adm emp prop demais pess jurid emiss partic (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Entidade_Previdencia_Privada` | `Nr_Entidade_Previdencia_Privada` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr entidade previdencia privada (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Demais_Instit_Financ` | `Qtd_Demais_Instit_Financ` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd demais instit financ (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Demais_Pessoa_Juridica_Emissora_Partic_Consorc` | `Qtd_Demais_Pessoa_Juridica_Emissora_Partic_Consorc` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd demais pessoa juridica emissora partic consorc (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Demais_Pessoa_Juridica_Emissora_Partic_Consorci` | `Nr_Demais_Pessoa_Juridica_Emissora_Partic_Consorci` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr demais pessoa juridica emissora partic consorci (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Outros` | `Qtd_Outros` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd outros (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Entidade_Previdencia_Privada` | `Qtd_Entidade_Previdencia_Privada` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd entidade previdencia privada (só em: `oferta_distribuicao`) | quantidade | todo |
| `Tipo_Societario_Emissor` | `Tipo_Societario_Emissor` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo societario emissor (só em: `oferta_distribuicao`) | — | todo |
| `Modalidade_Dispensa_Registro` | `Modalidade_Dispensa_Registro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: modalidade dispensa registro (só em: `oferta_distribuicao`) | — | todo |
| `Data_Comunicado` | `Data_Comunicado` | texto (data AAAA-MM-DD) | Sem descrição no dicionário da CVM; pelo nome da coluna: data comunicado (só em: `oferta_distribuicao`) | — | todo |
| `Nr_Demais_Pessoa_Juridica` | `Nr_Demais_Pessoa_Juridica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr demais pessoa juridica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Instit_Financ_Emissora_Partic_Consorcio` | `Nr_Instit_Financ_Emissora_Partic_Consorcio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr instit financ emissora partic consorcio (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Instit_Intermed_Partic_Consorcio_Distrib` | `Nr_Instit_Intermed_Partic_Consorcio_Distrib` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr instit intermed partic consorcio distrib (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Clube_Investimento` | `Qtd_Clube_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd clube investimento (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Instit_Intermed_Partic_Consorcio_Distrib` | `Qtd_Instit_Intermed_Partic_Consorcio_Distrib` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd instit intermed partic consorcio distrib (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Clube_Investimento` | `Nr_Clube_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr clube investimento (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Cli_Pessoa_Juridica` | `Qtd_Cli_Pessoa_Juridica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd cli pessoa juridica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Demais_Instit_Financ` | `Nr_Demais_Instit_Financ` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr demais instit financ (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Fundos_Investimento` | `Qtd_Fundos_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd fundos investimento (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Cli_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_P` | `Qtd_Cli_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_P` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd cli soc adm emp prop demais pess jurid emiss p (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Cli_Pessoa_Fisica` | `Qtd_Cli_Pessoa_Fisica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd cli pessoa fisica (só em: `oferta_distribuicao`) | quantidade | todo |
| `Nr_Companhia_Seguradora` | `Nr_Companhia_Seguradora` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: nr companhia seguradora (só em: `oferta_distribuicao`) | quantidade | todo |
| `Qtd_Companhia_Seguradora` | `Qtd_Companhia_Seguradora` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtd companhia seguradora (só em: `oferta_distribuicao`) | quantidade | todo |
| `Custodiante` | `Custodiante` | texto | Nome do Custodiante (só em: `oferta_resolucao_160`) | — | todo |
| `Escriturador` | `Escriturador` | texto | Escriturador (só em: `oferta_resolucao_160`) | — | todo |
| `Gestor` | `Gestor` | texto | Nome do Gestor (só em: `oferta_resolucao_160`) | — | todo |
| `Oferta_inicial` | `Oferta_inicial` | texto | Indica se é uma oferta inicial (IPO) (só em: `oferta_resolucao_160`) | S/N | todo |
| `Publico_alvo` | `Publico_alvo` | texto | Público-alvo (só em: `oferta_resolucao_160`) | — | todo |
| `Valor_Mobiliario` | `Valor_Mobiliario` | texto | Valor mobiliário (só em: `oferta_resolucao_160`) | — | todo |
| `Qtde_VM_Instit_Intermed_Partic_Consorcio_Distrib` | `Qtde_VM_Instit_Intermed_Partic_Consorcio_Distrib` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm instit intermed partic consorcio distrib (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Num_Invest_Entidade_Previdencia_Privada` | `Num_Invest_Entidade_Previdencia_Privada` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest entidade previdencia privada (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Data_deliberacao_aprovou_oferta` | `Data_deliberacao_aprovou_oferta` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: data deliberacao aprovou oferta (só em: `oferta_resolucao_160`) | — | todo |
| `Rito_Requerimento` | `Rito_Requerimento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: rito requerimento (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Investidor_Estrangeiro` | `Num_Invest_Investidor_Estrangeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest investidor estrangeiro (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Identificacao_devedores_coobrigados` | `Identificacao_devedores_coobrigados` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: identificacao devedores coobrigados (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Demais_Pessoa_Juridica` | `Num_Invest_Demais_Pessoa_Juridica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest demais pessoa juridica (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Tipo_lastro` | `Tipo_lastro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo lastro (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Demais_Pessoa_Juridica_Emissora_Partic_` | `Num_Invest_Demais_Pessoa_Juridica_Emissora_Partic_` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest demais pessoa juridica emissora partic  (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Entidade_Previdencia_Privada` | `Qtde_VM_Entidade_Previdencia_Privada` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm entidade previdencia privada (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Pessoa_Natural` | `Qtde_VM_Pessoa_Natural` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm pessoa natural (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Endereco_emissor_rede_mundial_computadores` | `Endereco_emissor_rede_mundial_computadores` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: endereco emissor rede mundial computadores (só em: `oferta_resolucao_160`) | — | todo |
| `Destinacao_recursos` | `Destinacao_recursos` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: destinacao recursos (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Clube_Investimento` | `Num_Invest_Clube_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest clube investimento (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Num_Invest_Instit_Financ_Emissora_Partic_Consorcio` | `Num_Invest_Instit_Financ_Emissora_Partic_Consorcio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest instit financ emissora partic consorcio (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Fundos_Investimento` | `Qtde_VM_Fundos_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm fundos investimento (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Demais_Instit_Financ` | `Qtde_VM_Demais_Instit_Financ` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm demais instit financ (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Bookbuilding` | `Bookbuilding` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: bookbuilding (só em: `oferta_resolucao_160`) | — | todo |
| `Qtde_VM_Clube_Investimento` | `Qtde_VM_Clube_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm clube investimento (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Demais_Pessoa_Juridica_Emissora_Partic_Con` | `Qtde_VM_Demais_Pessoa_Juridica_Emissora_Partic_Con` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm demais pessoa juridica emissora partic con (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Data_Encerramento` | `Data_Encerramento` | texto (data AAAA-MM-DD) | Sem descrição no dicionário da CVM; pelo nome da coluna: data encerramento (só em: `oferta_resolucao_160`) | — | todo |
| `Regime_fiduciario` | `Regime_fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: regime fiduciario (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Instit_Intermed_Partic_Consorcio_Distri` | `Num_Invest_Instit_Intermed_Partic_Consorcio_Distri` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest instit intermed partic consorcio distri (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Titulo_incentivado` | `Titulo_incentivado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: titulo incentivado (só em: `oferta_resolucao_160`) | — | todo |
| `Tipo_requerimento` | `Tipo_requerimento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo requerimento (só em: `oferta_resolucao_160`) | — | todo |
| `Possibilidade_revolvencia` | `Possibilidade_revolvencia` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: possibilidade revolvencia (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Fundos_Investimento` | `Num_Invest_Fundos_Investimento` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest fundos investimento (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Status_Requerimento` | `Status_Requerimento` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: status requerimento (só em: `oferta_resolucao_160`) | — | todo |
| `Agente_fiduciario` | `Agente_fiduciario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: agente fiduciario (só em: `oferta_resolucao_160`) | — | todo |
| `Descricao_garantias` | `Descricao_garantias` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: descricao garantias (só em: `oferta_resolucao_160`) | — | todo |
| `Data_Registro` | `Data_Registro` | texto (data AAAA-MM-DD) | Sem descrição no dicionário da CVM; pelo nome da coluna: data registro (só em: `oferta_resolucao_160`) | — | todo |
| `Descricao_lastro` | `Descricao_lastro` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: descricao lastro (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Pessoa_Natural` | `Num_Invest_Pessoa_Natural` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest pessoa natural (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Valor_Total_Registrado` | `Valor_Total_Registrado` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor total registrado (só em: `oferta_resolucao_160`) | moeda (R$) | todo |
| `Avaliador_Risco` | `Avaliador_Risco` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: avaliador risco (só em: `oferta_resolucao_160`) | — | todo |
| `Qtde_VM_Instit_Financ_Emissora_Partic_Consorcio` | `Qtde_VM_Instit_Financ_Emissora_Partic_Consorcio` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm instit financ emissora partic consorcio (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Num_Invest_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emis` | `Num_Invest_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emis` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest soc adm emp prop demais pess jurid emis (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Administrador` | `Administrador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: administrador (só em: `oferta_resolucao_160`) | — | todo |
| `Reabertura_serie` | `Reabertura_serie` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: reabertura serie (só em: `oferta_resolucao_160`) | — | todo |
| `Ativos_alvo` | `Ativos_alvo` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: ativos alvo (só em: `oferta_resolucao_160`) | — | todo |
| `Qtde_Total_Registrada` | `Qtde_Total_Registrada` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde total registrada (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Numero_Requerimento` | `Numero_Requerimento` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: numero requerimento (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Processo_SEI` | `Processo_SEI` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: processo sei (só em: `oferta_resolucao_160`) | — | todo |
| `Qtde_VM_Demais_Pessoa_Juridica` | `Qtde_VM_Demais_Pessoa_Juridica` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm demais pessoa juridica (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qdte_VM_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_P` | `Qdte_VM_Soc_Adm_Emp_Prop_Demais_Pess_Jurid_Emiss_P` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qdte vm soc adm emp prop demais pess jurid emiss p (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Investidor_Estrangeiro` | `Qtde_VM_Investidor_Estrangeiro` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm investidor estrangeiro (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Oferta_vasos_comunicantes` | `Oferta_vasos_comunicantes` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: oferta vasos comunicantes (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Demais_Instit_Financ` | `Num_Invest_Demais_Instit_Financ` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest demais instit financ (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Qtde_VM_Companhia_Seguradora` | `Qtde_VM_Companhia_Seguradora` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: qtde vm companhia seguradora (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Data_requerimento` | `Data_requerimento` | texto (data AAAA-MM-DD) | Sem descrição no dicionário da CVM; pelo nome da coluna: data requerimento (só em: `oferta_resolucao_160`) | — | todo |
| `Mercado_negociacao` | `Mercado_negociacao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: mercado negociacao (só em: `oferta_resolucao_160`) | — | todo |
| `FIDC_nao_padronizado` | `FIDC_nao_padronizado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: fidc nao padronizado (só em: `oferta_resolucao_160`) | — | todo |
| `Titulo_padronizado` | `Titulo_padronizado` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: titulo padronizado (só em: `oferta_resolucao_160`) | — | todo |
| `Regime_distribuicao` | `Regime_distribuicao` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: regime distribuicao (só em: `oferta_resolucao_160`) | — | todo |
| `Grupo_Coordenador` | `Grupo_Coordenador` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: grupo coordenador (só em: `oferta_resolucao_160`) | — | todo |
| `Tipo_societario` | `Tipo_societario` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: tipo societario (só em: `oferta_resolucao_160`) | — | todo |
| `Num_Invest_Companhia_Seguradora` | `Num_Invest_Companhia_Seguradora` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: num invest companhia seguradora (só em: `oferta_resolucao_160`) | quantidade | todo |
| `Titulo_classificado_como_sustentavel` | `Titulo_classificado_como_sustentavel` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: titulo classificado como sustentavel (só em: `oferta_resolucao_160`) | — | todo |

## No lake

- **Sem conversão para o lake.** O conversor (`cvm-fetcher convert`) falha com o ZIP vazio e registra `oferta_distribuicao@AAAAMMDD.zip: Archive produced no files`; nenhum Parquet é gravado e o dataset `cvm/ofertas` fica vazio. Por isso o estado é `so-bruto` e não há `ofertas.schema.json`.
- Com o ZIP preenchido, o conversor gravaria um Parquet por CSV (`oferta_distribuicao__oferta_distribuicao.parquet` e `oferta_distribuicao__oferta_resolucao_160.parquet`), sem partição, lendo o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1) e inferindo os tipos.

## Cuidados de uso

- **Arquivo de origem vazio.** Em 2026-11-16 o ZIP não tinha nenhum arquivo (22 bytes; `Last-Modified` 2026-11-14). Confira o tamanho do bruto antes de converter; um bruto de 22 bytes é o ZIP vazio. Reproduza com `curl -sI https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/oferta_distribuicao.zip | grep -i content-length`.
- **A CVM reenvia o arquivo todo dia.** Quando voltar a ter conteúdo, reconverta e gere o esquema (`quantilica docs schema`) para promover o dataset a `convertido`; as descrições abaixo precisam ser conferidas contra os cabeçalhos.
- **Duas tabelas com colunas diferentes.** `oferta_resolucao_160` (71 colunas) usa outros nomes (`Data_Registro`, `Valor_Total_Registrado`, `Qtde_Total_Registrada`) que `oferta_distribuicao` (76 colunas: `Data_Registro_Oferta`, `Valor_Total`, `Quantidade_Total`), e só 7 colunas têm o mesmo nome nas duas.
- **Dados pessoais.** `Nome_Ofertante` e `Nome_Vendedor` podem ser de pessoa física. O fetcher e o lake preservam o que a fonte publica.

## Exemplos

Conferir se o ZIP bruto tem arquivos antes de converter.

```python
import zipfile

with zipfile.ZipFile("ofertas/oferta_distribuicao@20261116.zip") as z:
    print(z.namelist())  # [] quando o arquivo da CVM está vazio
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/oferta-distrib
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/
