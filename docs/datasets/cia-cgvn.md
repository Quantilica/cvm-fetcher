---
dataset:
  id: cia-cgvn
  fonte: cvm
  titulo: "Cias Abertas: Documentos: Informe do Código de Governança (ICBGC) - Co (CVM)"
  resumo: "Informe do Código Brasileiro de Governança Corporativa (ICBGC, 'pratique ou explique'): a adoção, por cada companhia aberta, das práticas recomendadas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/cia_aberta-doc-cgvn
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-cgvn"
  periodicidade: "anual (um arquivo por ano de referência; a CVM atualiza o do ano corrente todos os dias)"
  cobertura: {inicio: 2018, fim: em-curso}
  unidade: "um informe de governança de uma companhia aberta, ou uma prática dentro do informe (conforme a tabela)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (ano de referência)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 18}
  unidades_de_medida:
    Versao: "código ou número de identificação (sem unidade)"
    ID_Documento: "código ou número de identificação (sem unidade)"
  dados_pessoais: nenhum
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.4.0
---

# Cias Abertas: Documentos: Informe do Código de Governança (ICBGC) - Co

## Resumo

Informe do Código Brasileiro de Governança Corporativa (ICBGC, 'pratique ou explique'): a adoção, por cada companhia aberta, das práticas recomendadas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/cia-cgvn` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/cia_aberta-doc-cgvn |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-cgvn |
| Periodicidade | anual (um arquivo por ano de referência; a CVM atualiza o do ano corrente todos os dias) |
| Cobertura | 2018 a em-curso |
| Unidade (uma linha) | um informe de governança de uma companhia aberta, ou uma prática dentro do informe (conforme a tabela) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (ano de referência) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 18 |
| Unidades de medida | `Versao`: código ou número de identificação (sem unidade); `ID_Documento`: código ou número de identificação (sem unidade) |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/cia_aberta-doc-cgvn). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/CGVN/DADOS/`.
- O catálogo do fetcher lista 9 arquivo(s): de `cgvn_cia_aberta_2018.zip` a `cgvn_cia_aberta_2026.zip`. Em 2026-11-15 conferimos 12 arquivos Parquet convertidos de 6 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `cia-cgvn/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um informe de governança de uma companhia aberta, ou uma prática dentro do informe (conforme a tabela).
- Particionado por `ano`; anos convertidos: 2018 a 2026.
- Este dataset reúne 2 tabelas (um CSV por tabela em cada ZIP), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<zip>__<csv>.parquet`:

| Tabela (nome do CSV sem o ano) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no maior arquivo) |
|---|---|---|---|
| `cgvn_cia_aberta` | 12 | 449 | `ID_Documento` |
| `cgvn_cia_aberta_praticas` | 11 | 23.544 | `ID_Documento`, `ID_Item` |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima). Os arquivos de uma mesma competência ligam-se por identificador do documento ou do fundo (veja as colunas de cada tabela).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Companhia` | `CNPJ_Companhia` | texto | CNPJ da companhia | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento | código ou número de identificação (sem unidade) | todo |
| `Nome_Empresarial` | `Nome_Empresarial` | texto | Nome da empresa | — | todo |
| `ID_Documento` | `ID_Documento` | inteiro | Identificador do documento | código ou número de identificação (sem unidade) | todo |
| `Codigo_CVM` | `Codigo_CVM` | texto | Código CVM (só em: `cgvn_cia_aberta`) | — | todo |
| `Categoria` | `Categoria` | texto | Categoria (só em: `cgvn_cia_aberta`) | — | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento (só em: `cgvn_cia_aberta`) | — | todo |
| `Link_Download` | `Link_Download` | texto | Endereço para download do documento (só em: `cgvn_cia_aberta`) | — | todo |
| `Data_Inicio_Exercicio_Social` | `Data_Inicio_Exercicio_Social` | texto | Data de início do Exercício Social (só em: `cgvn_cia_aberta`) | — | todo |
| `Data_Fim_Exercicio_Social` | `Data_Fim_Exercicio_Social` | texto | Data fim do Exercício Social (só em: `cgvn_cia_aberta`) | — | todo |
| `Motivo_Reapresentacao` | `Motivo_Reapresentacao` | texto | Domínio : (só em: `cgvn_cia_aberta`) | — | todo |
| `ID_Item` | `ID_Item` | texto | Domínio : (só em: `cgvn_cia_aberta_praticas`) | — | todo |
| `Capitulo` | `Capitulo` | texto | Domínio : (só em: `cgvn_cia_aberta_praticas`) | — | todo |
| `Principio` | `Principio` | texto | Domínio : (só em: `cgvn_cia_aberta_praticas`) | — | todo |
| `Pratica_Recomendada` | `Pratica_Recomendada` | texto | Domínio : (só em: `cgvn_cia_aberta_praticas`) | — | todo |
| `Pratica_Adotada` | `Pratica_Adotada` | texto | Domínio : (só em: `cgvn_cia_aberta_praticas`) | — | todo |
| `Explicacao` | `Explicacao` | texto | Domínio : (só em: `cgvn_cia_aberta_praticas`) | — | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/cia-cgvn`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.

## Exemplos

Linhas por ano nos arquivos convertidos.

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(*) AS linhas
    FROM read_parquet('lake/cvm/cia-cgvn/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-cgvn
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/CGVN/
