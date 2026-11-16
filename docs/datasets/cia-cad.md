---
dataset:
  id: cia-cad
  fonte: cvm
  titulo: "Cias Abertas: Informação Cadastral (CVM)"
  resumo: "Cadastro vigente das companhias abertas registradas na CVM: situação do registro, setor, controle acionário, auditor e dados de contato."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/cia_aberta-cad
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-cad"
  periodicidade: "diária (a CVM atualiza os arquivos todos os dias)"
  cobertura: {inicio: 2026-11, fim: em-curso}
  unidade: "uma companhia aberta registrada (ativa ou cancelada)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "retrato do dia (cadastro vigente, sem histórico)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [], chave: [], colunas: 47}
  unidades_de_medida:
    CEP: "código ou número de identificação (sem unidade)"
    DDD_TEL: "código ou número de identificação (sem unidade)"
    TEL: "código ou número de identificação (sem unidade)"
    DDD_FAX: "código ou número de identificação (sem unidade)"
    FAX: "código ou número de identificação (sem unidade)"
    CEP_RESP: "código ou número de identificação (sem unidade)"
    DDD_TEL_RESP: "código ou número de identificação (sem unidade)"
    TEL_RESP: "código ou número de identificação (sem unidade)"
    DDD_FAX_RESP: "código ou número de identificação (sem unidade)"
    FAX_RESP: "código ou número de identificação (sem unidade)"
  dados_pessoais:
    - {coluna: LOGRADOURO, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: EMAIL, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: LOGRADOURO_RESP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: EMAIL_RESP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.4.0
---

# Cias Abertas: Informação Cadastral

## Resumo

Cadastro vigente das companhias abertas registradas na CVM: situação do registro, setor, controle acionário, auditor e dados de contato.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/cia-cad` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/cia_aberta-cad |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-cad |
| Periodicidade | diária (a CVM atualiza os arquivos todos os dias) |
| Cobertura | 2026-11 a em-curso |
| Unidade (uma linha) | uma companhia aberta registrada (ativa ou cancelada) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: retrato do dia (cadastro vigente, sem histórico) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 47 |
| Unidades de medida | `CEP`: código ou número de identificação (sem unidade); `DDD_TEL`: código ou número de identificação (sem unidade); `TEL`: código ou número de identificação (sem unidade); `DDD_FAX`: código ou número de identificação (sem unidade); `FAX`: código ou número de identificação (sem unidade); `CEP_RESP`: código ou número de identificação (sem unidade); `DDD_TEL_RESP`: código ou número de identificação (sem unidade); `TEL_RESP`: código ou número de identificação (sem unidade); `DDD_FAX_RESP`: código ou número de identificação (sem unidade); `FAX_RESP`: código ou número de identificação (sem unidade) |
| Dados pessoais | `LOGRADOURO` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `EMAIL` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `LOGRADOURO_RESP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `EMAIL_RESP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/cia_aberta-cad). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/`.
- O catálogo do fetcher lista 1 arquivo(s): de `cad_cia_aberta.csv` a `cad_cia_aberta.csv`. Em 2026-11-15 conferimos 1 arquivos Parquet convertidos de 1 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `cia-cad/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma companhia aberta registrada (ativa ou cancelada).
- Uma tabela (`cad_cia_aberta`): 2.680 linhas no maior arquivo convertido; sem chave única determinada.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_CIA` | `CNPJ_CIA` | texto | CNPJ da companhia | — | todo |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DENOM_COMERC` | `DENOM_COMERC` | texto | Denominação Comercial | — | todo |
| `DT_REG` | `DT_REG` | texto | Data de registro | — | todo |
| `DT_CONST` | `DT_CONST` | texto | Data de constituição | — | todo |
| `DT_CANCEL` | `DT_CANCEL` | texto | Data de cancelamento | — | todo |
| `MOTIVO_CANCEL` | `MOTIVO_CANCEL` | texto | Motivo de cancelamento | — | todo |
| `SIT` | `SIT` | texto | Situação | — | todo |
| `DT_INI_SIT` | `DT_INI_SIT` | texto | Data início da situação | — | todo |
| `CD_CVM` | `CD_CVM` | texto | Código CVM | — | todo |
| `SETOR_ATIV` | `SETOR_ATIV` | texto | Setor de atividade | — | todo |
| `TP_MERC` | `TP_MERC` | texto | Tipo de mercado | — | todo |
| `CATEG_REG` | `CATEG_REG` | texto | Categoria do registro | — | todo |
| `DT_INI_CATEG` | `DT_INI_CATEG` | texto | Data início da categoria do registro | — | todo |
| `SIT_EMISSOR` | `SIT_EMISSOR` | texto | Descrição da situação do emissor | — | todo |
| `DT_INI_SIT_EMISSOR` | `DT_INI_SIT_EMISSOR` | texto | Data início da situação do emissor | — | todo |
| `CONTROLE_ACIONARIO` | `CONTROLE_ACIONARIO` | texto | Controle Acionário | — | todo |
| `TP_ENDER` | `TP_ENDER` | texto | Tipo de endereço | — | todo |
| `LOGRADOURO` | `LOGRADOURO` | texto | Logradouro | — | todo |
| `COMPL` | `COMPL` | texto | Complemento de endereço | — | todo |
| `BAIRRO` | `BAIRRO` | texto | Bairro | — | todo |
| `MUN` | `MUN` | texto | Nome do município | — | todo |
| `UF` | `UF` | texto | Unidade da Federação | — | todo |
| `PAIS` | `PAIS` | texto | País | — | todo |
| `CEP` | `CEP` | inteiro | CEP | código ou número de identificação (sem unidade) | todo |
| `DDD_TEL` | `DDD_TEL` | inteiro | Código de DDD (Telefone) | código ou número de identificação (sem unidade) | todo |
| `TEL` | `TEL` | inteiro | Telefone | código ou número de identificação (sem unidade) | todo |
| `DDD_FAX` | `DDD_FAX` | inteiro | Código de DDD (FAX) | código ou número de identificação (sem unidade) | todo |
| `FAX` | `FAX` | inteiro | FAX | código ou número de identificação (sem unidade) | todo |
| `EMAIL` | `EMAIL` | texto | Endereço de e-mail | — | todo |
| `TP_RESP` | `TP_RESP` | texto | Tipo de responsável | — | todo |
| `RESP` | `RESP` | texto | Nome do Responsável | — | todo |
| `DT_INI_RESP` | `DT_INI_RESP` | texto | Data início de atuação do responsável | — | todo |
| `LOGRADOURO_RESP` | `LOGRADOURO_RESP` | texto | Logradouro do responsável | — | todo |
| `COMPL_RESP` | `COMPL_RESP` | texto | Complemento de endereço do responsável | — | todo |
| `BAIRRO_RESP` | `BAIRRO_RESP` | texto | Bairro do responsável | — | todo |
| `MUN_RESP` | `MUN_RESP` | texto | Nome do município do responsável | — | todo |
| `UF_RESP` | `UF_RESP` | texto | Unidade da Federação do responsável | — | todo |
| `PAIS_RESP` | `PAIS_RESP` | texto | País do responsável | — | todo |
| `CEP_RESP` | `CEP_RESP` | inteiro | CEP do responsável | código ou número de identificação (sem unidade) | todo |
| `DDD_TEL_RESP` | `DDD_TEL_RESP` | inteiro | Código de DDD (Telefone) do responsável | código ou número de identificação (sem unidade) | todo |
| `TEL_RESP` | `TEL_RESP` | inteiro | Telefone do responsável | código ou número de identificação (sem unidade) | todo |
| `DDD_FAX_RESP` | `DDD_FAX_RESP` | inteiro | Código de DDD (FAX) do responsável | código ou número de identificação (sem unidade) | todo |
| `FAX_RESP` | `FAX_RESP` | inteiro | FAX do responsável | código ou número de identificação (sem unidade) | todo |
| `EMAIL_RESP` | `EMAIL_RESP` | texto | Endereço de e-mail do responsável | — | todo |
| `CNPJ_AUDITOR` | `CNPJ_AUDITOR` | texto | CNPJ do Auditor | — | todo |
| `AUDITOR` | `AUDITOR` | texto | Nome do Auditor | — | todo |

## No lake

- Dataset `cvm/cia-cad`, sem partição; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA` ou `..._AAAA-MM`); arquivos cujo nome traz o mês sem hífen (`..._AAAAMM`) ficam sem partição `ano`/`mes`.

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- A CVM mantém no cadastro também as companhias com registro cancelado (`SIT` = `CANCELADA`: 1.917 de 2.680 em 2026-11-15); filtre pela situação antes de contar companhias em atividade.
- Esta tabela é o retrato do dia: não guarda histórico de mudanças de situação, setor ou auditor. Para uma série, guarde as versões do bruto.
- **Dados de contato e identificação.** Há colunas de endereço, telefone, e-mail ou CPF (`LOGRADOURO`, ...); parte pode ser de pessoa física. O fetcher e o lake preservam o que a fonte publica.
- **CEP, DDD e telefones viram número.** O conversor infere o tipo de cada CSV e lê `CEP`, `DDD_TEL`, `TEL`, `DDD_FAX`, `FAX`, `CEP_RESP` e outras como inteiro, o que descarta zeros à esquerda (CEP de 8 dígitos começado por zero, por exemplo); reconstrua o texto com `lpad` quando precisar do código.

## Exemplos

Companhias abertas por situação do registro.

```python
import duckdb

duckdb.sql("""
    SELECT SIT, count(*) AS companhias
    FROM read_parquet('lake/cvm/cia-cad/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    GROUP BY 1
    ORDER BY 2 DESC
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-cad
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/
