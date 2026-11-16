---
dataset:
  id: intermed-cad
  fonte: cvm
  titulo: "Participantes Intermediários: Informação Cadastral (CVM)"
  resumo: "Cadastro dos participantes intermediários registrados na CVM (bancos, corretoras, distribuidoras, cooperativas de crédito, custodiantes, escrituradores e outros), em duas tabelas: o cadastro do participante e os responsáveis indicados por cada um."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/intermed-cad
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/intermed-cad"
  periodicidade: "diária (o portal declara atualização diária; o arquivo foi regravado em 2026-11-14)"
  cobertura: {inicio: 2026-11, fim: em-curso}
  unidade: "um participante intermediário (na tabela de cadastro) ou um responsável de um participante (na tabela de responsáveis)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "retrato do dia (cadastro vigente, sem histórico)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), no espelho público da CVM"
  lake: {estado: convertido, particoes: [], chave: [], colunas: 32}
  unidades_de_medida:
    VL_PATRIM_LIQ: "moeda (R$)"
    CEP: "código ou número de identificação (sem unidade)"
    DDD_TEL: "código ou número de identificação (sem unidade)"
    TEL: "código ou número de identificação (sem unidade)"
    DDD_FAX: "código ou número de identificação (sem unidade)"
    FAX: "código ou número de identificação (sem unidade)"
  dados_pessoais:
    - {coluna: LOGRADOURO, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: COMPL, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: BAIRRO, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDD_TEL, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TEL, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDD_FAX, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: FAX, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: EMAIL, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: RESP, categoria: "nome de pessoa física (diretor, responsável ou representante)"}
    - {coluna: EMAIL_RESP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# Participantes Intermediários: Informação Cadastral

## Resumo

Cadastro dos participantes intermediários registrados na CVM (bancos, corretoras, distribuidoras, cooperativas de crédito, custodiantes, escrituradores e outros), em duas tabelas: o cadastro do participante e os responsáveis indicados por cada um.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/intermed-cad` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/intermed-cad |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/intermed-cad |
| Periodicidade | diária (o portal declara atualização diária; o arquivo foi regravado em 2026-11-14) |
| Cobertura | 2026-11 a em-curso |
| Unidade (uma linha) | um participante intermediário (na tabela de cadastro) ou um responsável de um participante (na tabela de responsáveis) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: retrato do dia (cadastro vigente, sem histórico) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), no espelho público da CVM |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 32 |
| Unidades de medida | `VL_PATRIM_LIQ`: moeda (R$); `CEP`: código ou número de identificação (sem unidade); `DDD_TEL`: código ou número de identificação (sem unidade); `TEL`: código ou número de identificação (sem unidade); `DDD_FAX`: código ou número de identificação (sem unidade); `FAX`: código ou número de identificação (sem unidade) |
| Dados pessoais | `LOGRADOURO` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `COMPL` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `BAIRRO` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDD_TEL` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TEL` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDD_FAX` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `FAX` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `EMAIL` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `RESP` (nome de pessoa física (diretor, responsável ou representante)); `EMAIL_RESP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/intermed-cad). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/INTERMED/CAD/DADOS/`.
- O catálogo do fetcher lista 1 arquivo(s): `cad_intermed.zip`.
- Em 2026-11-16 conferimos 2 arquivos Parquet convertidos de 1 arquivo(s) de origem (amostra: cadastro único, sem período).
- No bruto, o arquivo fica em `intermed-cad/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um participante intermediário (na tabela de cadastro) ou um responsável de um participante (na tabela de responsáveis).
- O cadastro traz 2.354 participantes no arquivo convertido: 1.846 com situação `CANCELADA`, 507 `EM FUNCIONAMENTO NORMAL` e 1 em `LIQUIDAÇÃO EXTRAJUDICIAL`. O tipo de participante (`TP_PARTIC`) tem 12 valores, entre eles distribuidoras (690), cooperativas de crédito (481), corretoras (375) e custodiantes de valores mobiliários (297).
- Este dataset reúne 2 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `cad_intermed` | 28 | 2.354 | `CNPJ`, `DT_INI_SIT`, `CD_CVM` | o cadastro de cada participante, com situação, endereço e patrimônio líquido |
| `cad_intermed_resp` | 8 | 5.581 | não determinada | os responsáveis indicados por participante (diretores e contatos), um por linha |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `TP_PARTIC` | `TP_PARTIC` | texto | Tipo de participante | — | todo |
| `CNPJ` | `CNPJ` | texto | Cadastro Nacional de Pessoas Jurídicas | — | todo |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DENOM_COMERC` | `DENOM_COMERC` | texto | Denominação Comercial (só em: `cad_intermed`) | — | todo |
| `DT_REG` | `DT_REG` | texto | Data de registro | — | todo |
| `DT_CANCEL` | `DT_CANCEL` | texto | Data de cancelamento (só em: `cad_intermed`) | — | todo |
| `MOTIVO_CANCEL` | `MOTIVO_CANCEL` | texto | Motivo de cancelamento (só em: `cad_intermed`) | — | todo |
| `SIT` | `SIT` | texto | Situação (só em: `cad_intermed`) | — | todo |
| `DT_INI_SIT` | `DT_INI_SIT` | texto | Data início da situação (só em: `cad_intermed`) | — | todo |
| `CD_CVM` | `CD_CVM` | texto | Código CVM (só em: `cad_intermed`) | — | todo |
| `SETOR_ATIV` | `SETOR_ATIV` | texto | Setor de atividade (só em: `cad_intermed`) | — | todo |
| `CONTROLE_ACIONARIO` | `CONTROLE_ACIONARIO` | texto | Controle Acionário (só em: `cad_intermed`) | — | todo |
| `VL_PATRIM_LIQ` | `VL_PATRIM_LIQ` | decimal | Valor do patrimônio líquido (só em: `cad_intermed`) | moeda (R$) | todo |
| `DT_PATRIM_LIQ` | `DT_PATRIM_LIQ` | texto | Data do patrimônio líquido (só em: `cad_intermed`) | — | todo |
| `TP_ENDER` | `TP_ENDER` | texto | Tipo de endereço (só em: `cad_intermed`) | — | todo |
| `LOGRADOURO` | `LOGRADOURO` | texto | Logradouro (só em: `cad_intermed`) | — | todo |
| `COMPL` | `COMPL` | texto | Complemento de endereço (só em: `cad_intermed`) | — | todo |
| `BAIRRO` | `BAIRRO` | texto | Bairro (só em: `cad_intermed`) | — | todo |
| `MUN` | `MUN` | texto | Nome do município (só em: `cad_intermed`) | — | todo |
| `UF` | `UF` | texto | Unidade da Federação (só em: `cad_intermed`) | — | todo |
| `PAIS` | `PAIS` | texto | País (só em: `cad_intermed`) | — | todo |
| `CEP` | `CEP` | inteiro | CEP (só em: `cad_intermed`) | código ou número de identificação (sem unidade) | todo |
| `DDD_TEL` | `DDD_TEL` | inteiro | Código de DDD (Telefone) (só em: `cad_intermed`) | código ou número de identificação (sem unidade) | todo |
| `TEL` | `TEL` | inteiro | Telefone (só em: `cad_intermed`) | código ou número de identificação (sem unidade) | todo |
| `DDD_FAX` | `DDD_FAX` | inteiro | Código de DDD (FAX) (só em: `cad_intermed`) | código ou número de identificação (sem unidade) | todo |
| `FAX` | `FAX` | inteiro | FAX (só em: `cad_intermed`) | código ou número de identificação (sem unidade) | todo |
| `EMAIL` | `EMAIL` | texto | Endereço de e-mail (só em: `cad_intermed`) | — | todo |
| `SITE_WEB` | `SITE_WEB` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: site web (só em: `cad_intermed`) | — | todo |
| `TP_RESP` | `TP_RESP` | texto | Tipo de responsável (só em: `cad_intermed_resp`) | — | todo |
| `RESP` | `RESP` | texto | Nome do Responsável (só em: `cad_intermed_resp`) | — | todo |
| `DT_INI_RESP` | `DT_INI_RESP` | texto | Data início de atuação do responsável (só em: `cad_intermed_resp`) | — | todo |
| `EMAIL_RESP` | `EMAIL_RESP` | texto | Endereço de e-mail do responsável (só em: `cad_intermed_resp`) | — | todo |

## No lake

- Dataset `cvm/intermed-cad`, sem partição; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Cadastro com cancelados.** A maior parte das linhas é de participantes cancelados; filtre `SIT = 'EM FUNCIONAMENTO NORMAL'` para o conjunto ativo. O arquivo é o retrato do último dia útil: o histórico de situação só existe nas cópias que você guardar.
- **Responsáveis.** A tabela `cad_intermed_resp` repete `TP_PARTIC`, `CNPJ` e `DENOM_SOCIAL` do participante em cada linha e tem uma linha por responsável; `TP_RESP` é nulo em 1.787 das 5.581 linhas (contatos sem tipo informado).
- **Dados de contato e identificação.** O cadastro traz endereço, telefone, e-mail e nome de responsáveis (`RESP`, `EMAIL_RESP`); parte pode ser de pessoa física. O fetcher e o lake preservam o que a fonte publica.
- **CEP, DDD, telefone e CPF viram número.** O conversor infere o tipo de cada CSV e lê `CEP`, `DDD_TEL`, `TEL`, `DDD_FAX`, `FAX` como inteiro, o que descarta zeros à esquerda; reconstrua o texto com `lpad` quando precisar do código.

## Exemplos

Participantes ativos por tipo.

```python
import duckdb

duckdb.sql("""
    SELECT TP_PARTIC, count(*) AS participantes
    FROM read_parquet('lake/cvm/intermed-cad/cad_intermed__cad_intermed.parquet')
    WHERE SIT = 'EM FUNCIONAMENTO NORMAL'
    GROUP BY 1
    ORDER BY 2 DESC
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/intermed-cad
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/INTERMED/CAD/
