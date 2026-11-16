---
dataset:
  id: fi-cad
  fonte: cvm
  titulo: "Fundos de Investimento: Informação Cadastral (CVM)"
  resumo: "Cadastro dos fundos de investimento em três arquivos: o cadastro dos fundos não adaptados à Resolução CVM 175 (`cad_fi`), o histórico de alterações cadastrais da ICVM 555 (`cad_fi_hist`, 20 tabelas) e o registro de fundos, classes e subclasses sob a Resolução CVM 175 (`registro_fundo_classe`, 3 tabelas)."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fi-cad
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-cad"
  periodicidade: "diária (a CVM atualiza de terça a sábado, às 8h; o portal declara atualização diária e os arquivos foram regravados em 2026-11-14)"
  cobertura: {inicio: 2026-11, fim: em-curso}
  unidade: "um fundo, uma classe ou uma subclasse de cotas (nas tabelas de cadastro); uma alteração cadastral de um fundo (nas tabelas de histórico)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "retrato do dia (cadastro vigente) e histórico de alterações da ICVM 555 (de 2004-11 a 2026-11)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [], chave: [], colunas: 122}
  unidades_de_medida:
    TAXA_PERFM: "percentual (%)"
    TAXA_ADM: "percentual (%)"
    VL_PATRIM_LIQ: "moeda (R$)"
    VL_TAXA_PERFM: "moeda (R$)"
    ID_Registro_Fundo: "código ou número de identificação (sem unidade)"
    ID_Registro_Classe: "código ou número de identificação (sem unidade)"
    Patrimonio_Liquido: "moeda (R$)"
  dados_pessoais:
    - {coluna: DIRETOR, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: Diretor, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: CPF_CNPJ_GESTOR, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_Gestor, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras:
    - {desde: 2024-10, mudanca: "o arquivo `cad_fi` passa a listar só os fundos não adaptados à Resolução CVM 175 (renomeado no portal em 2024-10-07); os adaptados ficam em `registro_fundo_classe`"}
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Fundos de Investimento: Informação Cadastral

## Resumo

Cadastro dos fundos de investimento em três arquivos: o cadastro dos fundos não adaptados à Resolução CVM 175 (`cad_fi`), o histórico de alterações cadastrais da ICVM 555 (`cad_fi_hist`, 20 tabelas) e o registro de fundos, classes e subclasses sob a Resolução CVM 175 (`registro_fundo_classe`, 3 tabelas).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fi-cad` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fi-cad |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-cad |
| Periodicidade | diária (a CVM atualiza de terça a sábado, às 8h; o portal declara atualização diária e os arquivos foram regravados em 2026-11-14) |
| Cobertura | 2026-11 a em-curso |
| Unidade (uma linha) | um fundo, uma classe ou uma subclasse de cotas (nas tabelas de cadastro); uma alteração cadastral de um fundo (nas tabelas de histórico) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: retrato do dia (cadastro vigente) e histórico de alterações da ICVM 555 (de 2004-11 a 2026-11) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 122 |
| Unidades de medida | `TAXA_PERFM`: percentual (%); `TAXA_ADM`: percentual (%); `VL_PATRIM_LIQ`: moeda (R$); `VL_TAXA_PERFM`: moeda (R$); `ID_Registro_Fundo`: código ou número de identificação (sem unidade); `ID_Registro_Classe`: código ou número de identificação (sem unidade); `Patrimonio_Liquido`: moeda (R$) |
| Dados pessoais | `DIRETOR` (nome de pessoa física (diretor, responsável ou representante)); `Diretor` (nome de pessoa física (diretor, responsável ou representante)); `CPF_CNPJ_GESTOR` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_Gestor` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | 2024-10: o arquivo `cad_fi` passa a listar só os fundos não adaptados à Resolução CVM 175 (renomeado no portal em 2024-10-07); os adaptados ficam em `registro_fundo_classe` |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fi-cad). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FI/CAD/DADOS/`.
- O catálogo do fetcher lista 3 arquivo(s): `cad_fi.csv`, `cad_fi_hist.zip`, `registro_fundo_classe.zip`.
- Em 2026-11-16 conferimos 23 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: cadastro único, sem período).
- No bruto, o arquivo fica em `fi-cad/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um fundo, uma classe ou uma subclasse de cotas (nas tabelas de cadastro); uma alteração cadastral de um fundo (nas tabelas de histórico).
- `cad_fi` tem 46.805 linhas (41.102 CNPJ distintos), das quais 46.590 com situação `CANCELADA` e só 21 `EM FUNCIONAMENTO NORMAL`: desde 2024-10-07 o portal lista nele apenas os fundos não adaptados à Resolução CVM 175, e a última data de registro (`DT_REG`) é 2024-09-24. O cadastro vigente dos fundos adaptados está em `registro_fundo` (91.141 linhas), `registro_classe` (37.147) e `registro_subclasse` (11.829).
- As tabelas `registro_*` ligam-se por `ID_Registro_Fundo` (fundo e classe) e `ID_Registro_Classe` (classe e subclasse); as tabelas `cad_fi*` ligam-se por `CNPJ_FUNDO`. Os dois grupos usam nomes de coluna e capitalização diferentes (`CNPJ_FUNDO` contra `CNPJ_Fundo`).
- As tabelas `cad_fi_hist_*` começam em 2004-11 (menor `DT_INI_SIT` de `cad_fi_hist_sit`) e vão até 2026-11-13; antes de 2022-04 o histórico tinha as tabelas `cad_fi_hist_invest_prof` e `cad_fi_hist_invest_qualif`, substituídas por `cad_fi_hist_publico_alvo`.
- Este dataset reúne 23 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `cad_fi` | 41 | 46.805 | não determinada | fundos ICVM 555 ainda não adaptados à RCVM 175: um por fundo, com 41 colunas de cadastro |
| `cad_fi_hist_admin` | 6 | 86.178 | não determinada | histórico de administrador do fundo |
| `cad_fi_hist_auditor` | 6 | 104.236 | não determinada | histórico de auditor |
| `cad_fi_hist_classe` | 5 | 62.070 | `CNPJ_FUNDO`, `DT_INI_CLASSE` | histórico de classe do fundo |
| `cad_fi_hist_condom` | 5 | 63.707 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_CONDOM` | histórico de condomínio (aberto ou fechado) |
| `cad_fi_hist_controlador` | 6 | 72.184 | não determinada | histórico de controlador do administrador/gestor |
| `cad_fi_hist_custodiante` | 6 | 73.005 | não determinada | histórico de custodiante |
| `cad_fi_hist_denom_comerc` | 5 | 81.132 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_DENOM_COMERC`, `DT_FIM_DENOM_COMERC` | histórico de denominação comercial |
| `cad_fi_hist_denom_social` | 5 | 152.988 | não determinada | histórico de denominação social |
| `cad_fi_hist_diretor_resp` | 5 | 179.413 | não determinada | histórico de diretor responsável |
| `cad_fi_hist_exclusivo` | 5 | 65.384 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_ST_EXCLUSIVO` | histórico do indicador de fundo exclusivo |
| `cad_fi_hist_exerc_social` | 4 | 508.749 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_EXERC` | histórico de data de encerramento do exercício social |
| `cad_fi_hist_fic` | 5 | 64.451 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_ST_COTAS` | histórico do indicador de fundo de cotas (FIC) |
| `cad_fi_hist_gestor` | 7 | 100.221 | não determinada | histórico de gestor |
| `cad_fi_hist_publico_alvo` | 5 | 42.985 | `CNPJ_FUNDO`, `DT_INI_PUBLICO_ALVO` | histórico de público-alvo |
| `cad_fi_hist_rentab` | 5 | 60.178 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_RENTAB` | histórico do parâmetro de rentabilidade (benchmark) |
| `cad_fi_hist_sit` | 5 | 146.376 | `CNPJ_FUNDO`, `SIT`, `DT_INI_SIT` | histórico de situação do fundo |
| `cad_fi_hist_taxa_adm` | 5 | 87.757 | `CNPJ_FUNDO`, `DT_INI_TAXA_ADM` | histórico de taxa de administração |
| `cad_fi_hist_taxa_perfm` | 5 | 43.639 | `CNPJ_FUNDO`, `DT_INI_TAXA_PERFM` | histórico de taxa de performance |
| `cad_fi_hist_trib_lprazo` | 5 | 56.545 | `CNPJ_FUNDO`, `DT_REG`, `DT_INI_ST_TRIB_LPRAZO` | histórico de tributação de longo prazo |
| `registro_classe` | 30 | 37.147 | não determinada | classes de cotas de cada fundo |
| `registro_fundo` | 21 | 91.141 | não determinada | fundos cadastrados no sistema SGF, adaptados ou não à RCVM 175 |
| `registro_subclasse` | 14 | 11.829 | `ID_Subclasse` | subclasses de cotas de cada classe |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `TP_FUNDO` | `TP_FUNDO` | texto | Tipo de fundo (só em: `cad_fi`) | — | todo |
| `CNPJ_FUNDO` | `CNPJ_FUNDO` | texto | CNPJ do fundo (só em: `cad_fi`, `cad_fi_hist_admin`, `cad_fi_hist_auditor`, `cad_fi_hist_classe` e mais 16) | — | todo |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social (só em: `cad_fi`, `cad_fi_hist_denom_social`) | — | todo |
| `DT_REG` | `DT_REG` | texto | Data de registro (só em: `cad_fi`, `cad_fi_hist_admin`, `cad_fi_hist_auditor`, `cad_fi_hist_classe` e mais 16) | — | todo |
| `DT_CONST` | `DT_CONST` | texto | Data de constituição (só em: `cad_fi`) | — | todo |
| `CD_CVM` | `CD_CVM` | texto | Código CVM (só em: `cad_fi`) | — | todo |
| `DT_CANCEL` | `DT_CANCEL` | texto | Data de cancelamento (só em: `cad_fi`) | — | todo |
| `SIT` | `SIT` | texto | Situação (só em: `cad_fi`, `cad_fi_hist_sit`) | — | todo |
| `DT_INI_SIT` | `DT_INI_SIT` | texto | Data início da situação (só em: `cad_fi`, `cad_fi_hist_sit`) | — | todo |
| `DT_INI_ATIV` | `DT_INI_ATIV` | texto | Data de início de atividade (só em: `cad_fi`) | — | todo |
| `DT_INI_EXERC` | `DT_INI_EXERC` | texto | Data início do exercício social (só em: `cad_fi`, `cad_fi_hist_exerc_social`) | — | todo |
| `DT_FIM_EXERC` | `DT_FIM_EXERC` | texto | Data fim do exercício social (só em: `cad_fi`, `cad_fi_hist_exerc_social`) | — | todo |
| `CLASSE` | `CLASSE` | texto | Classe (só em: `cad_fi`, `cad_fi_hist_classe`) | — | todo |
| `DT_INI_CLASSE` | `DT_INI_CLASSE` | texto | Data de início na classe (só em: `cad_fi`, `cad_fi_hist_classe`) | — | todo |
| `RENTAB_FUNDO` | `RENTAB_FUNDO` | texto | Forma de rentabilidade do fundo (indicador de desempenho) (só em: `cad_fi`, `cad_fi_hist_rentab`) | — | todo |
| `CONDOM` | `CONDOM` | texto | Forma de condomínio (só em: `cad_fi`, `cad_fi_hist_condom`) | Aberto/Fechado | todo |
| `FUNDO_COTAS` | `FUNDO_COTAS` | texto | Indica se é fundo de cotas (só em: `cad_fi`, `cad_fi_hist_fic`) | S/N | todo |
| `FUNDO_EXCLUSIVO` | `FUNDO_EXCLUSIVO` | texto | Indica se é fundo exclusivo (só em: `cad_fi`, `cad_fi_hist_exclusivo`) | S/N | todo |
| `TRIB_LPRAZO` | `TRIB_LPRAZO` | texto | Indica se possui tributação de longo prazo (só em: `cad_fi`, `cad_fi_hist_trib_lprazo`) | S;N;N/A | todo |
| `PUBLICO_ALVO` | `PUBLICO_ALVO` | texto | Público-alvo (só em: `cad_fi`, `cad_fi_hist_publico_alvo`) | — | todo |
| `ENTID_INVEST` | `ENTID_INVEST` | texto | Indica se o fundo é entidade de investimento (só em: `cad_fi`) | S/N | todo |
| `TAXA_PERFM` | `TAXA_PERFM` | decimal | Taxa de performance (só em: `cad_fi`) | percentual (%) | todo |
| `INF_TAXA_PERFM` | `INF_TAXA_PERFM` | texto | Informações Adicionais (Taxa de performance) (só em: `cad_fi`) | — | todo |
| `TAXA_ADM` | `TAXA_ADM` | decimal | Taxa de administração (só em: `cad_fi`, `cad_fi_hist_taxa_adm`) | percentual (%) | todo |
| `INF_TAXA_ADM` | `INF_TAXA_ADM` | texto | Informações Adicionais (Taxa de administração) (só em: `cad_fi`, `cad_fi_hist_taxa_adm`) | — | todo |
| `VL_PATRIM_LIQ` | `VL_PATRIM_LIQ` | decimal | Valor do patrimônio líquido (só em: `cad_fi`) | moeda (R$) | todo |
| `DT_PATRIM_LIQ` | `DT_PATRIM_LIQ` | texto | Data do patrimônio líquido (só em: `cad_fi`) | — | todo |
| `DIRETOR` | `DIRETOR` | texto | Nome do Diretor Responsável (só em: `cad_fi`, `cad_fi_hist_diretor_resp`) | — | todo |
| `CNPJ_ADMIN` | `CNPJ_ADMIN` | texto | CNPJ do Administrador (só em: `cad_fi`, `cad_fi_hist_admin`) | — | todo |
| `ADMIN` | `ADMIN` | texto | Nome do Administrador (só em: `cad_fi`, `cad_fi_hist_admin`) | — | todo |
| `PF_PJ_GESTOR` | `PF_PJ_GESTOR` | texto | Indica se o gestor é pessoa física ou jurídica (só em: `cad_fi`, `cad_fi_hist_gestor`) | PF/PJ | todo |
| `CPF_CNPJ_GESTOR` | `CPF_CNPJ_GESTOR` | texto | Informa o código de identificação do gestor pessoa física ou jurídica (só em: `cad_fi`, `cad_fi_hist_gestor`) | — | todo |
| `GESTOR` | `GESTOR` | texto | Nome do Gestor (só em: `cad_fi`, `cad_fi_hist_gestor`) | — | todo |
| `CNPJ_AUDITOR` | `CNPJ_AUDITOR` | texto | CNPJ do Auditor (só em: `cad_fi`, `cad_fi_hist_auditor`) | — | todo |
| `AUDITOR` | `AUDITOR` | texto | Nome do Auditor (só em: `cad_fi`, `cad_fi_hist_auditor`) | — | todo |
| `CNPJ_CUSTODIANTE` | `CNPJ_CUSTODIANTE` | texto | CNPJ do Custodiante (só em: `cad_fi`, `cad_fi_hist_custodiante`) | — | todo |
| `CUSTODIANTE` | `CUSTODIANTE` | texto | Nome do Custodiante (só em: `cad_fi`, `cad_fi_hist_custodiante`) | — | todo |
| `CNPJ_CONTROLADOR` | `CNPJ_CONTROLADOR` | texto | CNPJ do Controlador (só em: `cad_fi`, `cad_fi_hist_controlador`) | — | todo |
| `CONTROLADOR` | `CONTROLADOR` | texto | Nome do Controlador (só em: `cad_fi`, `cad_fi_hist_controlador`) | — | todo |
| `INVEST_CEMPR_EXTER` | `INVEST_CEMPR_EXTER` | texto | Indica se o fundo pode aplicar 100% dos recursos no exterior (só em: `cad_fi`) | S/N | todo |
| `CLASSE_ANBIMA` | `CLASSE_ANBIMA` | texto | Classificação de Fundos regulados ANBIMA (só em: `cad_fi`) | — | todo |
| `DT_INI_ADMIN` | `DT_INI_ADMIN` | texto | Data de início do administrador (só em: `cad_fi_hist_admin`) | — | todo |
| `DT_FIM_ADMIN` | `DT_FIM_ADMIN` | texto | Data fim do administrador (só em: `cad_fi_hist_admin`) | — | todo |
| `DT_INI_AUDITOR` | `DT_INI_AUDITOR` | texto | Data início do administrador (só em: `cad_fi_hist_auditor`) | — | todo |
| `DT_FIM_AUDITOR` | `DT_FIM_AUDITOR` | texto | Data fim do administrador (só em: `cad_fi_hist_auditor`) | — | todo |
| `DT_FIM_CLASSE` | `DT_FIM_CLASSE` | texto | Data fim da classe (só em: `cad_fi_hist_classe`) | — | todo |
| `DT_INI_CONDOM` | `DT_INI_CONDOM` | texto | Data início do condomínio (só em: `cad_fi_hist_condom`) | — | todo |
| `DT_FIM_CONDOM` | `DT_FIM_CONDOM` | texto | Data fim do condomínio (só em: `cad_fi_hist_condom`) | — | todo |
| `DT_INI_CONTROLADOR` | `DT_INI_CONTROLADOR` | texto | Data início do controlador (só em: `cad_fi_hist_controlador`) | — | todo |
| `DT_FIM_CONTROLADOR` | `DT_FIM_CONTROLADOR` | texto | Data fim do controlador (só em: `cad_fi_hist_controlador`) | — | todo |
| `DT_INI_CUSTODIANTE` | `DT_INI_CUSTODIANTE` | texto | Data início do custodiante (só em: `cad_fi_hist_custodiante`) | — | todo |
| `DT_FIM_CUSTODIANTE` | `DT_FIM_CUSTODIANTE` | texto | Data fim do custodiante (só em: `cad_fi_hist_custodiante`) | — | todo |
| `DENOM_COMERC` | `DENOM_COMERC` | texto | Denominação Comercial (só em: `cad_fi_hist_denom_comerc`) | — | todo |
| `DT_INI_DENOM_COMERC` | `DT_INI_DENOM_COMERC` | texto | Data início da denominação comercial (só em: `cad_fi_hist_denom_comerc`) | — | todo |
| `DT_FIM_DENOM_COMERC` | `DT_FIM_DENOM_COMERC` | texto | Data fim da denominação comercial (só em: `cad_fi_hist_denom_comerc`) | — | todo |
| `DT_INI_DENOM_SOCIAL` | `DT_INI_DENOM_SOCIAL` | texto | Data início da denominação social (só em: `cad_fi_hist_denom_social`) | — | todo |
| `DT_FIM_DENOM_SOCIAL` | `DT_FIM_DENOM_SOCIAL` | texto | Data fim da denominação social (só em: `cad_fi_hist_denom_social`) | — | todo |
| `DT_INI_DIRETOR` | `DT_INI_DIRETOR` | texto | Data início do diretor (só em: `cad_fi_hist_diretor_resp`) | — | todo |
| `DT_FIM_DIRETOR` | `DT_FIM_DIRETOR` | texto | Data fim do diretor (só em: `cad_fi_hist_diretor_resp`) | — | todo |
| `DT_INI_ST_EXCLUSIVO` | `DT_INI_ST_EXCLUSIVO` | texto | Data início do status exclusivo (só em: `cad_fi_hist_exclusivo`) | — | todo |
| `DT_FIM_ST_EXCLUSIVO` | `DT_FIM_ST_EXCLUSIVO` | texto | Data fim do status exclusivo (só em: `cad_fi_hist_exclusivo`) | — | todo |
| `DT_INI_ST_COTAS` | `DT_INI_ST_COTAS` | texto | Data início do status de cotas (só em: `cad_fi_hist_fic`) | — | todo |
| `DT_FIM_ST_COTAS` | `DT_FIM_ST_COTAS` | texto | Data fim do status de cotas (só em: `cad_fi_hist_fic`) | — | todo |
| `DT_INI_GESTOR` | `DT_INI_GESTOR` | texto | Data início do gestor (só em: `cad_fi_hist_gestor`) | — | todo |
| `DT_FIM_GESTOR` | `DT_FIM_GESTOR` | texto | Data fim do gestor (só em: `cad_fi_hist_gestor`) | — | todo |
| `DT_INI_PUBLICO_ALVO` | `DT_INI_PUBLICO_ALVO` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `DT_INI_PUBLICO_ALVO`) (só em: `cad_fi_hist_publico_alvo`) | — | todo |
| `DT_FIM_PUBLICO_ALVO` | `DT_FIM_PUBLICO_ALVO` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `DT_FIM_PUBLICO_ALVO`) (só em: `cad_fi_hist_publico_alvo`) | — | todo |
| `DT_INI_RENTAB` | `DT_INI_RENTAB` | texto | Data início da rentabilidade (só em: `cad_fi_hist_rentab`) | — | todo |
| `DT_FIM_RENTAB` | `DT_FIM_RENTAB` | texto | Data fim da rentabilidade (só em: `cad_fi_hist_rentab`) | — | todo |
| `DT_FIM_SIT` | `DT_FIM_SIT` | texto | Data fim da situação (só em: `cad_fi_hist_sit`) | — | todo |
| `DT_INI_TAXA_ADM` | `DT_INI_TAXA_ADM` | texto | Data início da taxa de administração (só em: `cad_fi_hist_taxa_adm`) | — | todo |
| `VL_TAXA_PERFM` | `VL_TAXA_PERFM` | decimal | valor da taxa de performance (só em: `cad_fi_hist_taxa_perfm`) | moeda (R$) | todo |
| `DS_TAXA_PERFM` | `DS_TAXA_PERFM` | texto | Descrição da taxa de performance (só em: `cad_fi_hist_taxa_perfm`) | — | todo |
| `DT_INI_TAXA_PERFM` | `DT_INI_TAXA_PERFM` | texto | Data início da taxa de performance (só em: `cad_fi_hist_taxa_perfm`) | — | todo |
| `DT_INI_ST_TRIB_LPRAZO` | `DT_INI_ST_TRIB_LPRAZO` | texto | Data início do status de tributação de longo prazo (só em: `cad_fi_hist_trib_lprazo`) | — | todo |
| `DT_FIM_ST_TRIB_LPRAZO` | `DT_FIM_ST_TRIB_LPRAZO` | texto | Data fim do status de tributação de longo prazo (só em: `cad_fi_hist_trib_lprazo`) | — | todo |
| `ID_Registro_Fundo` | `ID_Registro_Fundo` | inteiro | Sem descrição no dicionário da CVM (só em: `registro_classe`, `registro_fundo`) | código ou número de identificação (sem unidade) | todo |
| `ID_Registro_Classe` | `ID_Registro_Classe` | inteiro | Identificador de Registro da Classe (só em: `registro_classe`, `registro_subclasse`) | código ou número de identificação (sem unidade) | todo |
| `CNPJ_Classe` | `CNPJ_Classe` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_Classe`) (só em: `registro_classe`) | — | todo |
| `Codigo_CVM` | `Codigo_CVM` | texto | Código CVM (só em: `registro_classe`, `registro_fundo`, `registro_subclasse`) | — | todo |
| `Data_Registro` | `Data_Registro` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Data_Registro`) (só em: `registro_classe`, `registro_fundo`) | — | todo |
| `Data_Constituicao` | `Data_Constituicao` | texto | Data da constituição (só em: `registro_classe`, `registro_fundo`, `registro_subclasse`) | — | todo |
| `Data_Inicio` | `Data_Inicio` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Data_Inicio`) (só em: `registro_classe`, `registro_subclasse`) | — | todo |
| `Tipo_Classe` | `Tipo_Classe` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Tipo_Classe`) (só em: `registro_classe`) | — | todo |
| `Denominacao_Social` | `Denominacao_Social` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Denominacao_Social`) (só em: `registro_classe`, `registro_fundo`, `registro_subclasse`) | — | todo |
| `Situacao` | `Situacao` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Situacao`) (só em: `registro_classe`, `registro_fundo`, `registro_subclasse`) | — | todo |
| `Data_Inicio_Situacao` | `Data_Inicio_Situacao` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Data_Inicio_Situacao`) (só em: `registro_classe`, `registro_fundo`, `registro_subclasse`) | — | todo |
| `Classificacao` | `Classificacao` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Classificacao`) (só em: `registro_classe`) | — | todo |
| `Indicador_Desempenho` | `Indicador_Desempenho` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Indicador_Desempenho`) (só em: `registro_classe`) | — | todo |
| `Classe_Cotas` | `Classe_Cotas` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Classe_Cotas`) (só em: `registro_classe`) | — | todo |
| `Classificacao_Anbima` | `Classificacao_Anbima` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Classificacao_Anbima`) (só em: `registro_classe`) | — | todo |
| `Tributacao_Longo_Prazo` | `Tributacao_Longo_Prazo` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Tributacao_Longo_Prazo`) (só em: `registro_classe`) | — | todo |
| `Entidade_Investimento` | `Entidade_Investimento` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Entidade_Investimento`) (só em: `registro_classe`) | — | todo |
| `Permitido_Aplicacao_CemPorCento_Exterior` | `Permitido_Aplicacao_CemPorCento_Exterior` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Permitido_Aplicacao_CemPorCento_Exterior`) (só em: `registro_classe`) | — | todo |
| `Classe_ESG` | `Classe_ESG` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Classe_ESG`) (só em: `registro_classe`) | — | todo |
| `Forma_Condominio` | `Forma_Condominio` | texto | Forma de Condomínio (só em: `registro_classe`, `registro_subclasse`) | Aberto/Fechado | todo |
| `Exclusivo` | `Exclusivo` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Exclusivo`) (só em: `registro_classe`, `registro_subclasse`) | — | todo |
| `Publico_Alvo` | `Publico_Alvo` | texto | Público-alvo (só em: `registro_classe`, `registro_subclasse`) | — | todo |
| `Patrimonio_Liquido` | `Patrimonio_Liquido` | decimal | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Patrimonio_Liquido`) (só em: `registro_classe`, `registro_fundo`) | moeda (R$) | todo |
| `Data_Patrimonio_Liquido` | `Data_Patrimonio_Liquido` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Data_Patrimonio_Liquido`) (só em: `registro_classe`, `registro_fundo`) | — | todo |
| `CNPJ_Auditor` | `CNPJ_Auditor` | texto | CNPJ do Auditor (só em: `registro_classe`) | — | todo |
| `Auditor` | `Auditor` | texto | Nome do Auditor (só em: `registro_classe`) | — | todo |
| `CNPJ_Custodiante` | `CNPJ_Custodiante` | texto | CNPJ do Custodiante (só em: `registro_classe`) | — | todo |
| `Custodiante` | `Custodiante` | texto | Nome do Custodiante (só em: `registro_classe`) | — | todo |
| `CNPJ_Controlador` | `CNPJ_Controlador` | texto | CNPJ do Controlador (só em: `registro_classe`) | — | todo |
| `Controlador` | `Controlador` | texto | Nome do Controlador (só em: `registro_classe`) | — | todo |
| `CNPJ_Fundo` | `CNPJ_Fundo` | texto | CNPJ do fundo (só em: `registro_fundo`) | — | todo |
| `Tipo_Fundo` | `Tipo_Fundo` | texto | Sem descrição no dicionário da CVM (só em: `registro_fundo`) | — | todo |
| `Data_Cancelamento` | `Data_Cancelamento` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Data_Cancelamento`) (só em: `registro_fundo`) | — | todo |
| `Data_Adaptacao_RCVM175` | `Data_Adaptacao_RCVM175` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Data_Adaptacao_RCVM175`) (só em: `registro_fundo`) | — | todo |
| `Data_Inicio_Exercicio_Social` | `Data_Inicio_Exercicio_Social` | texto | Data de início do Exercício Social (só em: `registro_fundo`) | — | todo |
| `Data_Fim_Exercicio_Social` | `Data_Fim_Exercicio_Social` | texto | Data fim do Exercício Social (só em: `registro_fundo`) | — | todo |
| `Diretor` | `Diretor` | texto | Nome do Diretor Responsável (só em: `registro_fundo`) | — | todo |
| `CNPJ_Administrador` | `CNPJ_Administrador` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `CNPJ_Administrador`) (só em: `registro_fundo`) | — | todo |
| `Administrador` | `Administrador` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Administrador`) (só em: `registro_fundo`) | — | todo |
| `Tipo_Pessoa_Gestor` | `Tipo_Pessoa_Gestor` | texto | (nome da coluna nos arquivos anteriores à adaptação à Resolução CVM 175; depois, `Tipo_Pessoa_Gestor`) (só em: `registro_fundo`) | — | todo |
| `CPF_CNPJ_Gestor` | `CPF_CNPJ_Gestor` | texto | Informa o código de identificação do gestor pessoa física ou jurídica (só em: `registro_fundo`) | — | todo |
| `Gestor` | `Gestor` | texto | Nome do Gestor (só em: `registro_fundo`) | — | todo |
| `ID_Subclasse` | `ID_Subclasse` | texto | Identificador da subclasse (só em: `registro_subclasse`) | — | todo |
| `Previdenciario` | `Previdenciario` | texto | Indica se é subclasse previdenciária (só em: `registro_subclasse`) | S/N | todo |
| `Exclusivo_INR` | `Exclusivo_INR` | texto | Indica se é subclasse destinada exclusivamente a investidores não residentes (só em: `registro_subclasse`) | S/N | todo |
| `Exclusivo_Previdencia_Complementar` | `Exclusivo_Previdencia_Complementar` | texto | Indica se é subclasse vinculada exclusivamente a planos de previdência complementar ou a seguros de vida com cláusula de cobertura por sobrevivência (só em: `registro_subclasse`) | S/N | todo |

## No lake

- Dataset `cvm/fi-cad`, sem partição; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Dois arquivos de cadastro.** Para a lista completa de fundos hoje, use `registro_fundo`; `cad_fi` cobre só os fundos ainda não adaptados à RCVM 175 e deixou de receber os demais em 2024-10. Para o histórico anterior à RCVM 175, use as tabelas `cad_fi_hist_*`.
- **CNPJ com e sem máscara.** `cad_fi` e `cad_fi_hist_*` trazem o CNPJ com máscara (`00.000.000/0000-00`); as tabelas `registro_*` trazem só os 14 dígitos (`CNPJ_Fundo`, `CNPJ_Classe`, `CNPJ_Administrador`, `CPF_CNPJ_Gestor`). Normalize antes de juntar.
- **Situações com maiúsculas diferentes.** `cad_fi` e o histórico escrevem `EM FUNCIONAMENTO NORMAL` e `CANCELADA`; `registro_fundo` escreve `Em Funcionamento Normal` e `Cancelado`. As tabelas de histórico de situação têm um valor a mais (`EM LIQUIDAÇÃO ORDINÁRIA`, 1 linha).
- **Dados pessoais.** `DIRETOR`/`Diretor` trazem o nome do diretor responsável, e `CPF_CNPJ_GESTOR`/`CPF_CNPJ_Gestor` o CNPJ do gestor ou, para gestor pessoa física, o CPF (226 linhas de `registro_fundo` têm 11 dígitos). O fetcher e o lake preservam o que a fonte publica.
- **Linhas repetidas.** No arquivo mais recente convertido há linhas inteiramente repetidas em: `cad_fi_hist_admin` (12), `cad_fi_hist_auditor` (35), `cad_fi_hist_controlador` (16), `cad_fi_hist_custodiante` (26), `cad_fi_hist_denom_social` (567), `cad_fi_hist_diretor_resp` (24) e mais 3. Remova as duplicatas antes de contar ou somar.

## Exemplos

Fundos por situação no registro vigente (Resolução CVM 175).

```python
import duckdb

duckdb.sql("""
    SELECT Situacao, Tipo_Fundo, count(*) AS fundos
    FROM read_parquet('lake/cvm/fi-cad/registro_fundo_classe__registro_fundo.parquet')
    GROUP BY ALL
    ORDER BY fundos DESC
    LIMIT 10
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fi-cad
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FI/CAD/
