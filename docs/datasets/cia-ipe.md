---
dataset:
  id: cia-ipe
  fonte: cvm
  titulo: "Cias Abertas: Documentos: Periódicos e Eventuais (IPE) - Conjunto de d (CVM)"
  resumo: "Informações Periódicas e Eventuais (IPE): a lista dos documentos que as companhias abertas entregam (fatos relevantes, comunicados, atas, avisos), com assunto, categoria e link."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe"
  periodicidade: "anual (um arquivo por ano; a CVM atualiza todos os dias)"
  cobertura: {inicio: 2003, fim: em-curso}
  unidade: "um documento IPE entregue por uma companhia"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (ano de entrega)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 13}
  dados_pessoais: nenhum
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.4.0
---

# Cias Abertas: Documentos: Periódicos e Eventuais (IPE) - Conjunto de d

## Resumo

Informações Periódicas e Eventuais (IPE): a lista dos documentos que as companhias abertas entregam (fatos relevantes, comunicados, atas, avisos), com assunto, categoria e link.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/cia-ipe` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe |
| Periodicidade | anual (um arquivo por ano; a CVM atualiza todos os dias) |
| Cobertura | 2003 a em-curso |
| Unidade (uma linha) | um documento IPE entregue por uma companhia |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (ano de entrega) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 13 |
| Unidades de medida | — |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/IPE/DADOS/`.
- O catálogo do fetcher lista 24 arquivo(s): de `ipe_cia_aberta_2003.zip` a `ipe_cia_aberta_2026.zip`. Em 2026-11-15 conferimos 6 arquivos Parquet convertidos de 6 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `cia-ipe/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um documento IPE entregue por uma companhia.
- Particionado por `ano`; anos convertidos: 2003 a 2026.
- Uma tabela (`ipe_cia_aberta`): 52.140 linhas no maior arquivo convertido; sem chave única determinada.

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_Companhia` | `CNPJ_Companhia` | texto | CNPJ da companhia | — | todo |
| `Nome_Companhia` | `Nome_Companhia` | texto | Nome da Companhia | — | todo |
| `Codigo_CVM` | `Codigo_CVM` | texto | Código CVM | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento | — | todo |
| `Categoria` | `Categoria` | texto | Categoria | — | todo |
| `Tipo` | `Tipo` | texto | Tipo | — | todo |
| `Especie` | `Especie` | texto | Espécie | — | todo |
| `Assunto` | `Assunto` | texto | Assunto | — | todo |
| `Data_Entrega` | `Data_Entrega` | texto | Data de entrega/recebimento do documento | — | todo |
| `Tipo_Apresentacao` | `Tipo_Apresentacao` | texto | Tipo de Apresentação | — | todo |
| `Protocolo_Entrega` | `Protocolo_Entrega` | texto | Protocolo de Entrega | — | todo |
| `Versao` | `Versao` | inteiro / texto | Versão do documento | — | todo |
| `Link_Download` | `Link_Download` | texto | Endereço para download do documento | — | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/cia-ipe`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- O arquivo traz o índice e o link do documento (`Link_Download`), não o texto dos documentos.
- **Tipo inferido varia entre arquivos.** 1 coluna(s) (`Versao`) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Linhas por ano nos arquivos convertidos.

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(*) AS linhas
    FROM read_parquet('lake/cvm/cia-ipe/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/IPE/
