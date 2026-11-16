---
dataset:
  id: consultor-cad
  fonte: cvm
  titulo: "Consultores de Valores Mobiliários: Informação Cadastral - Conjunto de (CVM)"
  resumo: "Cadastro dos consultores de valores mobiliários registrados na CVM: pessoas físicas e jurídicas, com diretores, responsáveis e sócios."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/consultor_vlmob-cad
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/consultor_vlmob-cad"
  periodicidade: "diária (a CVM atualiza os arquivos todos os dias)"
  cobertura: {inicio: 2026-11, fim: em-curso}
  unidade: "um registro de consultor, diretor, responsável ou sócio (conforme a tabela)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "retrato do dia (cadastro vigente, sem histórico)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [], chave: [], colunas: 26}
  unidades_de_medida:
    CEP: "código ou número de identificação (sem unidade)"
    DDD: "código ou número de identificação (sem unidade)"
    TEL: "código ou número de identificação (sem unidade)"
  dados_pessoais:
    - {coluna: LOGRADOURO, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDD, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: EMAIL, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.0.0
---

# Consultores de Valores Mobiliários: Informação Cadastral - Conjunto de

## Resumo

Cadastro dos consultores de valores mobiliários registrados na CVM: pessoas físicas e jurídicas, com diretores, responsáveis e sócios.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/consultor-cad` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/consultor_vlmob-cad |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/consultor_vlmob-cad |
| Periodicidade | diária (a CVM atualiza os arquivos todos os dias) |
| Cobertura | 2026-11 a em-curso |
| Unidade (uma linha) | um registro de consultor, diretor, responsável ou sócio (conforme a tabela) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: retrato do dia (cadastro vigente, sem histórico) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 26 |
| Unidades de medida | `CEP`: código ou número de identificação (sem unidade); `DDD`: código ou número de identificação (sem unidade); `TEL`: código ou número de identificação (sem unidade) |
| Dados pessoais | `LOGRADOURO` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDD` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `EMAIL` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.0.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/consultor_vlmob-cad). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CONSULTOR_VLMOB/CAD/DADOS/`.
- O catálogo do fetcher lista 1 arquivo(s): de `cad_consultor_vlmob.zip` a `cad_consultor_vlmob.zip`. Em 2026-11-15 conferimos 5 arquivos Parquet convertidos de 1 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `consultor-cad/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um registro de consultor, diretor, responsável ou sócio (conforme a tabela).
- Este dataset reúne 5 tabelas (um CSV por tabela em cada ZIP), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<zip>__<csv>.parquet`:

| Tabela (nome do CSV sem o ano) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no maior arquivo) |
|---|---|---|---|
| `cad_consultor_vlmob_diretor` | 3 | 788 | não determinada |
| `cad_consultor_vlmob_pf` | 7 | 3.993 | `NOME`, `DT_CANCEL` |
| `cad_consultor_vlmob_pj` | 20 | 1.095 | `CNPJ`, `DENOM_SOCIAL`, `DT_CANCEL` |
| `cad_consultor_vlmob_resp` | 3 | 1.682 | não determinada |
| `cad_consultor_vlmob_socios` | 2 | 2.037 | não determinada |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima). Os arquivos de uma mesma competência ligam-se por identificador do documento ou do fundo (veja as colunas de cada tabela).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ` | `CNPJ` | texto | Cadastro Nacional de Pessoas Jurídicas (só em: `cad_consultor_vlmob_diretor`, `cad_consultor_vlmob_pj`, `cad_consultor_vlmob_resp`, `cad_consultor_vlmob_socios`) | — | todo |
| `DIRETOR` | `DIRETOR` | texto | Nome do Diretor Responsável (só em: `cad_consultor_vlmob_diretor`) | — | todo |
| `DIRETOR_DEFAULT` | `DIRETOR_DEFAULT` | texto | Indica se o diretor é padrão (só em: `cad_consultor_vlmob_diretor`) | S/N | todo |
| `NOME` | `NOME` | texto | Nome da Pessoa Física (só em: `cad_consultor_vlmob_pf`) | — | todo |
| `DT_REG` | `DT_REG` | texto | Data de registro (só em: `cad_consultor_vlmob_pf`, `cad_consultor_vlmob_pj`) | — | todo |
| `DT_CANCEL` | `DT_CANCEL` | texto | Data de cancelamento (só em: `cad_consultor_vlmob_pf`, `cad_consultor_vlmob_pj`) | — | todo |
| `MOTIVO_CANCEL` | `MOTIVO_CANCEL` | texto | Motivo de cancelamento (só em: `cad_consultor_vlmob_pf`, `cad_consultor_vlmob_pj`) | — | todo |
| `SIT` | `SIT` | texto | Situação (só em: `cad_consultor_vlmob_pf`, `cad_consultor_vlmob_pj`) | — | todo |
| `DT_INI_SIT` | `DT_INI_SIT` | texto | Data início da situação (só em: `cad_consultor_vlmob_pf`, `cad_consultor_vlmob_pj`) | — | todo |
| `SITE_ADMIN` | `SITE_ADMIN` | texto | Site do administrador (só em: `cad_consultor_vlmob_pf`, `cad_consultor_vlmob_pj`) | — | todo |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `DENOM_COMERC` | `DENOM_COMERC` | texto | Denominação Comercial (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `CONTROLE_ACIONARIO` | `CONTROLE_ACIONARIO` | texto | Controle Acionário (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `TP_ENDER` | `TP_ENDER` | texto | Tipo de endereço (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `LOGRADOURO` | `LOGRADOURO` | texto | Logradouro (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `COMPL` | `COMPL` | texto | Complemento de endereço (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `BAIRRO` | `BAIRRO` | texto | Bairro (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `MUN` | `MUN` | texto | Nome do município (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `UF` | `UF` | texto | Unidade da Federação (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `CEP` | `CEP` | inteiro | CEP (só em: `cad_consultor_vlmob_pj`) | código ou número de identificação (sem unidade) | todo |
| `DDD` | `DDD` | inteiro | Código DDD (só em: `cad_consultor_vlmob_pj`) | código ou número de identificação (sem unidade) | todo |
| `TEL` | `TEL` | inteiro | Telefone (só em: `cad_consultor_vlmob_pj`) | código ou número de identificação (sem unidade) | todo |
| `EMAIL` | `EMAIL` | texto | Endereço de e-mail (só em: `cad_consultor_vlmob_pj`) | — | todo |
| `RESP` | `RESP` | texto | Nome do Responsável (só em: `cad_consultor_vlmob_resp`) | — | todo |
| `TP_RESP` | `TP_RESP` | texto | Tipo de responsável (só em: `cad_consultor_vlmob_resp`) | — | todo |
| `SOCIOS` | `SOCIOS` | texto | Domínio : (só em: `cad_consultor_vlmob_socios`) | — | todo |

## No lake

- Dataset `cvm/consultor-cad`, sem partição; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA` ou `..._AAAA-MM`); arquivos cujo nome traz o mês sem hífen (`..._AAAAMM`) ficam sem partição `ano`/`mes`.

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Dados de contato e identificação.** Há colunas de endereço, telefone, e-mail ou CPF (`LOGRADOURO`, ...); parte pode ser de pessoa física. O fetcher e o lake preservam o que a fonte publica.
- **CEP, DDD e telefones viram número.** O conversor infere o tipo de cada CSV e lê `CEP`, `DDD`, `TEL` como inteiro, o que descarta zeros à esquerda (CEP de 8 dígitos começado por zero, por exemplo); reconstrua o texto com `lpad` quando precisar do código.

## Exemplos

Linhas por arquivo de origem (tabela) no dataset.

```python
import duckdb

duckdb.sql("""
    SELECT filename, count(*) AS linhas
    FROM read_parquet('lake/cvm/consultor-cad/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/consultor_vlmob-cad
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CONSULTOR_VLMOB/CAD/
