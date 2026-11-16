---
dataset:
  id: cia-fca
  fonte: cvm
  titulo: "Cias Abertas: Documentos: Formulário Cadastral (FCA) - Conjunto de dad (CVM)"
  resumo: "Formulário Cadastral (FCA) das companhias abertas: dados gerais, endereços, auditor, escriturador, valores mobiliários, canais de divulgação e outros dados cadastrais, em tabelas separadas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fca
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fca"
  periodicidade: "anual (um arquivo por ano; a CVM atualiza todos os dias)"
  cobertura: {inicio: 2010, fim: em-curso}
  unidade: "um documento FCA entregue, ou um item cadastral dentro dele (conforme a tabela)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (ano de entrega)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 87}
  unidades_de_medida:
    VERSAO: "código ou número de identificação (sem unidade)"
    ID_DOC: "código ou número de identificação (sem unidade)"
    Dia_Encerramento_Exercicio_Social: "ver a descrição"
    Mes_Encerramento_Exercicio_Social: "código ou número de identificação (sem unidade)"
  dados_pessoais:
    - {coluna: CPF_CNPJ_Auditor, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_Responsavel_Tecnico, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Logradouro, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Complemento, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDI_Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDD_Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Email, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_Responsavel, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.0.0
---

# Cias Abertas: Documentos: Formulário Cadastral (FCA) - Conjunto de dad

## Resumo

Formulário Cadastral (FCA) das companhias abertas: dados gerais, endereços, auditor, escriturador, valores mobiliários, canais de divulgação e outros dados cadastrais, em tabelas separadas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/cia-fca` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/cia_aberta-doc-fca |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fca |
| Periodicidade | anual (um arquivo por ano; a CVM atualiza todos os dias) |
| Cobertura | 2010 a em-curso |
| Unidade (uma linha) | um documento FCA entregue, ou um item cadastral dentro dele (conforme a tabela) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (ano de entrega) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 87 |
| Unidades de medida | `VERSAO`: código ou número de identificação (sem unidade); `ID_DOC`: código ou número de identificação (sem unidade); `Dia_Encerramento_Exercicio_Social`: ver a descrição; `Mes_Encerramento_Exercicio_Social`: código ou número de identificação (sem unidade) |
| Dados pessoais | `CPF_CNPJ_Auditor` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_Responsavel_Tecnico` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Logradouro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Complemento` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDI_Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDD_Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Email` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_Responsavel` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.0.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/cia_aberta-doc-fca). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FCA/DADOS/`.
- O catálogo do fetcher lista 17 arquivo(s): de `fca_cia_aberta_2010.zip` a `fca_cia_aberta_2026.zip`. Em 2026-11-15 conferimos 60 arquivos Parquet convertidos de 6 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `cia-fca/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um documento FCA entregue, ou um item cadastral dentro dele (conforme a tabela).
- Particionado por `ano`; anos convertidos: 2010 a 2026.
- Este dataset reúne 10 tabelas (um CSV por tabela em cada ZIP), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<zip>__<csv>.parquet`:

| Tabela (nome do CSV sem o ano) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no maior arquivo) |
|---|---|---|---|
| `fca_cia_aberta` | 9 | 1.993 | `ID_DOC` |
| `fca_cia_aberta_auditor` | 15 | 1.069 | não determinada |
| `fca_cia_aberta_canal_divulgacao` | 7 | 1.520 | não determinada |
| `fca_cia_aberta_departamento_acionistas` | 23 | 721 | não determinada |
| `fca_cia_aberta_dri` | 26 | 1.012 | não determinada |
| `fca_cia_aberta_endereco` | 21 | 1.543 | não determinada |
| `fca_cia_aberta_escriturador` | 24 | 552 | `CNPJ_Companhia`, `CNPJ_Escriturador` |
| `fca_cia_aberta_geral` | 26 | 766 | `ID_Documento` |
| `fca_cia_aberta_pais_estrangeiro_negociacao` | 7 | 111 | não determinada |
| `fca_cia_aberta_valor_mobiliario` | 18 | 1.010 | não determinada |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima). Os arquivos de uma mesma competência ligam-se por identificador do documento ou do fundo (veja as colunas de cada tabela).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_CIA` | `CNPJ_CIA` | texto | CNPJ da companhia (só em: `fca_cia_aberta`) | — | todo |
| `DT_REFER` | `DT_REFER` | texto | Data de referência do documento (só em: `fca_cia_aberta`) | — | todo |
| `VERSAO` | `VERSAO` | inteiro | Versão do documento (só em: `fca_cia_aberta`) | código ou número de identificação (sem unidade) | todo |
| `DENOM_CIA` | `DENOM_CIA` | texto | Nome empresarial da companhia (só em: `fca_cia_aberta`) | — | todo |
| `CD_CVM` | `CD_CVM` | texto | Código CVM (só em: `fca_cia_aberta`) | — | todo |
| `CATEG_DOC` | `CATEG_DOC` | texto | Categoria do documento (só em: `fca_cia_aberta`) | — | todo |
| `ID_DOC` | `ID_DOC` | inteiro | Identificador do documento (só em: `fca_cia_aberta`) | código ou número de identificação (sem unidade) | todo |
| `DT_RECEB` | `DT_RECEB` | texto | Data da recebimento do documento (só em: `fca_cia_aberta`) | — | todo |
| `LINK_DOC` | `LINK_DOC` | texto | Endereço para download do documento (só em: `fca_cia_aberta`) | — | todo |
| `CNPJ_Companhia` | `CNPJ_Companhia` | texto | CNPJ da companhia (só em: `fca_cia_aberta_auditor`, `fca_cia_aberta_canal_divulgacao`, `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri` e mais 5) | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento (só em: `fca_cia_aberta_auditor`, `fca_cia_aberta_canal_divulgacao`, `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri` e mais 5) | — | todo |
| `Versao` | `Versao` | inteiro / texto | Versão do documento (só em: `fca_cia_aberta_auditor`, `fca_cia_aberta_canal_divulgacao`, `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri` e mais 5) | — | todo |
| `ID_Documento` | `ID_Documento` | inteiro / texto | Identificador do documento (só em: `fca_cia_aberta_auditor`, `fca_cia_aberta_canal_divulgacao`, `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri` e mais 5) | — | todo |
| `Nome_Empresarial` | `Nome_Empresarial` | texto | Nome da empresa (só em: `fca_cia_aberta_auditor`, `fca_cia_aberta_canal_divulgacao`, `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri` e mais 5) | — | todo |
| `Auditor` | `Auditor` | texto | Nome do Auditor (só em: `fca_cia_aberta_auditor`) | — | todo |
| `CPF_CNPJ_Auditor` | `CPF_CNPJ_Auditor` | texto | CPF/CNPJ do auditor (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Codigo_CVM_Auditor` | `Codigo_CVM_Auditor` | texto | Código CVM do auditor (só em: `fca_cia_aberta_auditor`) | Númerico | todo |
| `Origem_Auditor` | `Origem_Auditor` | texto | Nacionalidade do auditor (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Data_Inicio_Atuacao_Auditor` | `Data_Inicio_Atuacao_Auditor` | texto | Data de início de atuação do auditor (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Data_Fim_Atuacao_Auditor` | `Data_Fim_Atuacao_Auditor` | texto | Data fim de atuação do auditor (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Responsavel_Tecnico` | `Responsavel_Tecnico` | texto | Responsável técnico (só em: `fca_cia_aberta_auditor`) | — | todo |
| `CPF_Responsavel_Tecnico` | `CPF_Responsavel_Tecnico` | texto | CPF do responsável técnico (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Data_Inicio_Atuacao_Responsavel_Tecnico` | `Data_Inicio_Atuacao_Responsavel_Tecnico` | texto | Data de início de atuação do responsável técnico (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Data_Fim_Atuacao_Responsavel_Tecnico` | `Data_Fim_Atuacao_Responsavel_Tecnico` | texto | Data fim de atuação do responsável técnico (só em: `fca_cia_aberta_auditor`) | — | todo |
| `Canal_Divulgacao` | `Canal_Divulgacao` | texto | Canal de Divulgação (só em: `fca_cia_aberta_canal_divulgacao`) | — | todo |
| `Sigla_UF` | `Sigla_UF` | texto | Sigla da Unidade da Federação (só em: `fca_cia_aberta_canal_divulgacao`, `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco` e mais 1) | — | todo |
| `Contato` | `Contato` | texto | Contato (só em: `fca_cia_aberta_departamento_acionistas`) | — | todo |
| `Data_Inicio_Contato` | `Data_Inicio_Contato` | texto | Data de início do contato (só em: `fca_cia_aberta_departamento_acionistas`) | — | todo |
| `Data_Fim_Contato` | `Data_Fim_Contato` | texto | Data fim do contato (só em: `fca_cia_aberta_departamento_acionistas`) | — | todo |
| `Tipo_Endereco` | `Tipo_Endereco` | texto | Tipo de endereço (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Logradouro` | `Logradouro` | texto | Logradouro (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Complemento` | `Complemento` | texto | Complemento (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Bairro` | `Bairro` | texto | Bairro (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Cidade` | `Cidade` | texto | Cidade (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Pais` | `Pais` | texto | País (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador` e mais 1) | — | todo |
| `CEP` | `CEP` | inteiro / texto | CEP (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `DDI_Telefone` | `DDI_Telefone` | texto | Código de DDI (Telefone) (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `DDD_Telefone` | `DDD_Telefone` | inteiro / texto | Código de DDD (Telefone) (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Telefone` | `Telefone` | inteiro / texto | Telefone (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `DDI_Fax` | `DDI_Fax` | texto | DDI fax (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `DDD_Fax` | `DDD_Fax` | inteiro / texto | Código de DDD (FAX) (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Fax` | `Fax` | inteiro / texto | FAX (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Email` | `Email` | texto | Endereço de e-mail (só em: `fca_cia_aberta_departamento_acionistas`, `fca_cia_aberta_dri`, `fca_cia_aberta_endereco`, `fca_cia_aberta_escriturador`) | — | todo |
| `Tipo_Responsavel` | `Tipo_Responsavel` | texto | Tipo de responsável (só em: `fca_cia_aberta_dri`) | — | todo |
| `Responsavel` | `Responsavel` | texto | Responsável (só em: `fca_cia_aberta_dri`) | — | todo |
| `CPF_Responsavel` | `CPF_Responsavel` | texto | CPF do responsável (só em: `fca_cia_aberta_dri`) | — | todo |
| `UF` | `UF` | texto | Unidade da Federação (só em: `fca_cia_aberta_dri`) | — | todo |
| `Data_Inicio_Atuacao` | `Data_Inicio_Atuacao` | texto | Data de início de atuação (só em: `fca_cia_aberta_dri`, `fca_cia_aberta_escriturador`) | — | todo |
| `Data_Fim_Atuacao` | `Data_Fim_Atuacao` | texto | Data fim de atuação (só em: `fca_cia_aberta_dri`, `fca_cia_aberta_escriturador`) | — | todo |
| `Caixa_Postal` | `Caixa_Postal` | texto | Caixa Postal (só em: `fca_cia_aberta_endereco`) | — | todo |
| `Escriturador` | `Escriturador` | texto | Escriturador (só em: `fca_cia_aberta_escriturador`) | — | todo |
| `CNPJ_Escriturador` | `CNPJ_Escriturador` | texto | CNPJ do Escriturador (só em: `fca_cia_aberta_escriturador`) | — | todo |
| `Data_Nome_Empresarial` | `Data_Nome_Empresarial` | texto | Data do nome empresarial (só em: `fca_cia_aberta_geral`) | — | todo |
| `Nome_Empresarial_Anterior` | `Nome_Empresarial_Anterior` | texto | Nome anterior da empresa (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Constituicao` | `Data_Constituicao` | texto | Data da constituição (só em: `fca_cia_aberta_geral`) | — | todo |
| `Codigo_CVM` | `Codigo_CVM` | texto | Código CVM (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Registro_CVM` | `Data_Registro_CVM` | texto | Data de registro na CVM (só em: `fca_cia_aberta_geral`) | — | todo |
| `Categoria_Registro_CVM` | `Categoria_Registro_CVM` | texto | Categoria do registro na CVM (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Categoria_Registro_CVM` | `Data_Categoria_Registro_CVM` | texto | Data da categoria do registro na CVM (só em: `fca_cia_aberta_geral`) | — | todo |
| `Situacao_Registro_CVM` | `Situacao_Registro_CVM` | texto | Situação do registro na CVM (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Situacao_Registro_CVM` | `Data_Situacao_Registro_CVM` | texto | Data da situação do registro na CVM (só em: `fca_cia_aberta_geral`) | — | todo |
| `Pais_Origem` | `Pais_Origem` | texto | País de origem (só em: `fca_cia_aberta_geral`) | — | todo |
| `Pais_Custodia_Valores_Mobiliarios` | `Pais_Custodia_Valores_Mobiliarios` | texto | Pais de custódia dos valores mobiliários (só em: `fca_cia_aberta_geral`) | — | todo |
| `Setor_Atividade` | `Setor_Atividade` | texto | Setor de Atividade (só em: `fca_cia_aberta_geral`) | — | todo |
| `Descricao_Atividade` | `Descricao_Atividade` | texto | Descrição da atividade (só em: `fca_cia_aberta_geral`) | — | todo |
| `Situacao_Emissor` | `Situacao_Emissor` | texto | Situação do emissor (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Situacao_Emissor` | `Data_Situacao_Emissor` | texto | Data da situação do emissor (só em: `fca_cia_aberta_geral`) | — | todo |
| `Especie_Controle_Acionario` | `Especie_Controle_Acionario` | texto | Espécie de controle acionário (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Especie_Controle_Acionario` | `Data_Especie_Controle_Acionario` | texto | Data da espécie do controle acionário (só em: `fca_cia_aberta_geral`) | — | todo |
| `Dia_Encerramento_Exercicio_Social` | `Dia_Encerramento_Exercicio_Social` | inteiro | Dia de encerramento do exercício social (só em: `fca_cia_aberta_geral`) | ver a descrição | todo |
| `Mes_Encerramento_Exercicio_Social` | `Mes_Encerramento_Exercicio_Social` | inteiro | Mês de encerramento do exercício social (só em: `fca_cia_aberta_geral`) | código ou número de identificação (sem unidade) | todo |
| `Data_Alteracao_Exercicio_Social` | `Data_Alteracao_Exercicio_Social` | texto | Data de alteração do exercício social (só em: `fca_cia_aberta_geral`) | — | todo |
| `Pagina_Web` | `Pagina_Web` | texto | Página Web (só em: `fca_cia_aberta_geral`) | — | todo |
| `Data_Admissao_Negociacao` | `Data_Admissao_Negociacao` | texto | Data de admissão para negociação (só em: `fca_cia_aberta_pais_estrangeiro_negociacao`) | — | todo |
| `Valor_Mobiliario` | `Valor_Mobiliario` | texto | Valor mobiliário (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Sigla_Classe_Acao_Preferencial` | `Sigla_Classe_Acao_Preferencial` | texto | Sigla da classe de ação preferencial (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Classe_Acao_Preferencial` | `Classe_Acao_Preferencial` | texto | Classe de ação preferencial (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Codigo_Negociacao` | `Codigo_Negociacao` | texto | Código de negociação (ticker) (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Composicao_BDR_Unit` | `Composicao_BDR_Unit` | texto | Composição de BDR Unit (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Mercado` | `Mercado` | texto | Nome do Mercado (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Sigla_Entidade_Administradora` | `Sigla_Entidade_Administradora` | texto | Sigla da entidade administradora (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Entidade_Administradora` | `Entidade_Administradora` | texto | Entidade administradora (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Data_Inicio_Negociacao` | `Data_Inicio_Negociacao` | texto | Data de início da negociação (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Data_Fim_Negociacao` | `Data_Fim_Negociacao` | texto | Data fim da negociação (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Segmento` | `Segmento` | texto | Segmento (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Data_Inicio_Listagem` | `Data_Inicio_Listagem` | texto | Data de início de listagem (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `Data_Fim_Listagem` | `Data_Fim_Listagem` | texto | Data fim de listagem (só em: `fca_cia_aberta_valor_mobiliario`) | — | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/cia-fca`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- O FCA é reentregue com frequência: o mesmo `CNPJ_Companhia` pode ter várias versões no mesmo ano (`Versao`); use a maior para o retrato mais recente.
- **Dados de contato e identificação.** Há colunas de endereço, telefone, e-mail ou CPF (`CPF_CNPJ_Auditor`, ...); parte pode ser de pessoa física. O fetcher e o lake preservam o que a fonte publica.
- **Tipo inferido varia entre arquivos.** 7 coluna(s) (`Versao`, ...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Linhas por ano nos arquivos convertidos.

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(*) AS linhas
    FROM read_parquet('lake/cvm/cia-fca/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fca
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FCA/
