---
dataset:
  id: cia-dfp
  fonte: cvm
  titulo: "Cias Abertas: Documentos: Formulário de Demonstrações Financeiras Padr (CVM)"
  resumo: "Demonstrações Financeiras Padronizadas (DFP) das companhias abertas: balanço patrimonial, demonstrações do resultado, dos fluxos de caixa, das mutações do patrimônio líquido e do valor adicionado, em versões consolidada e individual."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp"
  periodicidade: "anual (um arquivo por exercício; a CVM atualiza todos os dias)"
  cobertura: {inicio: 2010, fim: em-curso}
  unidade: "uma conta de uma demonstração de uma companhia em um exercício (nas tabelas de demonstrações); um documento entregue (nas tabelas de cadastro)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (exercício social)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 30}
  unidades_de_medida:
    ID_DOC: "código ou número de identificação (sem unidade)"
    NUM_ITEM_PARECER_DECL: "quantidade"
    QT_ACAO_ORDIN_CAP_INTEGR: "quantidade"
    QT_ACAO_PREF_CAP_INTEGR: "quantidade"
    QT_ACAO_TOTAL_CAP_INTEGR: "quantidade"
    QT_ACAO_ORDIN_TESOURO: "quantidade"
    QT_ACAO_PREF_TESOURO: "quantidade"
    QT_ACAO_TOTAL_TESOURO: "quantidade"
  dados_pessoais: nenhum
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.0.0
---

# Cias Abertas: Documentos: Formulário de Demonstrações Financeiras Padr

## Resumo

Demonstrações Financeiras Padronizadas (DFP) das companhias abertas: balanço patrimonial, demonstrações do resultado, dos fluxos de caixa, das mutações do patrimônio líquido e do valor adicionado, em versões consolidada e individual.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/cia-dfp` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp |
| Periodicidade | anual (um arquivo por exercício; a CVM atualiza todos os dias) |
| Cobertura | 2010 a em-curso |
| Unidade (uma linha) | uma conta de uma demonstração de uma companhia em um exercício (nas tabelas de demonstrações); um documento entregue (nas tabelas de cadastro) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (exercício social) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 30 |
| Unidades de medida | `ID_DOC`: código ou número de identificação (sem unidade); `NUM_ITEM_PARECER_DECL`: quantidade; `QT_ACAO_ORDIN_CAP_INTEGR`: quantidade; `QT_ACAO_PREF_CAP_INTEGR`: quantidade; `QT_ACAO_TOTAL_CAP_INTEGR`: quantidade; `QT_ACAO_ORDIN_TESOURO`: quantidade; `QT_ACAO_PREF_TESOURO`: quantidade; `QT_ACAO_TOTAL_TESOURO`: quantidade |
| Dados pessoais | nenhum |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.0.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/`.
- O catálogo do fetcher lista 17 arquivo(s): de `dfp_cia_aberta_2010.zip` a `dfp_cia_aberta_2026.zip`. Em 2026-11-15 conferimos 111 arquivos Parquet convertidos de 6 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `cia-dfp/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: uma conta de uma demonstração de uma companhia em um exercício (nas tabelas de demonstrações); um documento entregue (nas tabelas de cadastro).
- Particionado por `ano`; anos convertidos: 2010 a 2026.
- Este dataset reúne 19 tabelas (um CSV por tabela em cada ZIP), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<zip>__<csv>.parquet`:

| Tabela (nome do CSV sem o ano) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no maior arquivo) |
|---|---|---|---|
| `dfp_cia_aberta` | 9 | 1.113 | `ID_DOC` |
| `dfp_cia_aberta_bpa_con` | 14 | 63.776 | não determinada |
| `dfp_cia_aberta_bpa_ind` | 14 | 97.087 | não determinada |
| `dfp_cia_aberta_bpp_con` | 14 | 109.084 | não determinada |
| `dfp_cia_aberta_bpp_ind` | 14 | 164.276 | não determinada |
| `dfp_cia_aberta_composicao_capital` | 10 | 731 | `CNPJ_CIA`, `DT_REFER` |
| `dfp_cia_aberta_dfc_md_con` | 15 | 992 | não determinada |
| `dfp_cia_aberta_dfc_md_ind` | 15 | 1.376 | não determinada |
| `dfp_cia_aberta_dfc_mi_con` | 15 | 49.576 | não determinada |
| `dfp_cia_aberta_dfc_mi_ind` | 15 | 66.607 | não determinada |
| `dfp_cia_aberta_dmpl_con` | 16 | 233.029 | não determinada |
| `dfp_cia_aberta_dmpl_ind` | 16 | 260.370 | não determinada |
| `dfp_cia_aberta_dra_con` | 15 | 6.944 | não determinada |
| `dfp_cia_aberta_dra_ind` | 15 | 7.173 | não determinada |
| `dfp_cia_aberta_dre_con` | 15 | 33.784 | não determinada |
| `dfp_cia_aberta_dre_ind` | 15 | 48.232 | não determinada |
| `dfp_cia_aberta_dva_con` | 15 | 42.104 | não determinada |
| `dfp_cia_aberta_dva_ind` | 15 | 61.951 | não determinada |
| `dfp_cia_aberta_parecer` | 8 | 4.057 | não determinada |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima). Os arquivos de uma mesma competência ligam-se por identificador do documento ou do fundo (veja as colunas de cada tabela).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_CIA` | `CNPJ_CIA` | texto | CNPJ da companhia | — | todo |
| `DT_REFER` | `DT_REFER` | texto | Data de referência do documento | — | todo |
| `VERSAO` | `VERSAO` | inteiro / texto | Versão do documento | — | todo |
| `DENOM_CIA` | `DENOM_CIA` | texto | Nome empresarial da companhia | — | todo |
| `CD_CVM` | `CD_CVM` | texto | Código CVM (só em: `dfp_cia_aberta`, `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con` e mais 13) | — | todo |
| `CATEG_DOC` | `CATEG_DOC` | texto | Categoria do documento (só em: `dfp_cia_aberta`) | — | todo |
| `ID_DOC` | `ID_DOC` | inteiro | Identificador do documento (só em: `dfp_cia_aberta`) | código ou número de identificação (sem unidade) | todo |
| `DT_RECEB` | `DT_RECEB` | texto | Data da recebimento do documento (só em: `dfp_cia_aberta`) | — | todo |
| `LINK_DOC` | `LINK_DOC` | texto | Endereço para download do documento (só em: `dfp_cia_aberta`) | — | todo |
| `GRUPO_DFP` | `GRUPO_DFP` | texto | Nome e nível de agregação da demonstração (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `MOEDA` | `MOEDA` | texto | Moeda (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `ESCALA_MOEDA` | `ESCALA_MOEDA` | texto | Escala monetária (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `ORDEM_EXERC` | `ORDEM_EXERC` | texto | Ordem do exercício social (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `DT_FIM_EXERC` | `DT_FIM_EXERC` | texto | Data fim do exercício social (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `CD_CONTA` | `CD_CONTA` | texto | Código da conta (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `DS_CONTA` | `DS_CONTA` | texto | Descrição da conta (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `VL_CONTA` | `VL_CONTA` | decimal / texto | Valor da conta (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | — | todo |
| `ST_CONTA_FIXA` | `ST_CONTA_FIXA` | texto | Indica se é conta fixa ou não (só em: `dfp_cia_aberta_bpa_con`, `dfp_cia_aberta_bpa_ind`, `dfp_cia_aberta_bpp_con`, `dfp_cia_aberta_bpp_ind` e mais 12) | S/N | todo |
| `DT_INI_EXERC` | `DT_INI_EXERC` | texto | Data início do exercício social (só em: `dfp_cia_aberta_dfc_md_con`, `dfp_cia_aberta_dfc_md_ind`, `dfp_cia_aberta_dfc_mi_con`, `dfp_cia_aberta_dfc_mi_ind` e mais 8) | — | todo |
| `COLUNA_DF` | `COLUNA_DF` | texto | Coluna da demonstração financeira (só em: `dfp_cia_aberta_dmpl_con`, `dfp_cia_aberta_dmpl_ind`) | — | todo |
| `TP_RELAT_AUD` | `TP_RELAT_AUD` | texto | Tipo Relatório do Auditor Independente (só em: `dfp_cia_aberta_parecer`) | — | todo |
| `TP_PARECER_DECL` | `TP_PARECER_DECL` | texto | Tipo do Parecer/Declaração (só em: `dfp_cia_aberta_parecer`) | — | todo |
| `NUM_ITEM_PARECER_DECL` | `NUM_ITEM_PARECER_DECL` | inteiro | Número da linha do texto do Parecer/Declaração (só em: `dfp_cia_aberta_parecer`) | quantidade | todo |
| `TXT_PARECER_DECL` | `TXT_PARECER_DECL` | texto | Texto do Parecer/Declaração (só em: `dfp_cia_aberta_parecer`) | — | todo |
| `QT_ACAO_ORDIN_CAP_INTEGR` | `QT_ACAO_ORDIN_CAP_INTEGR` | inteiro | Domínio : (só em: `dfp_cia_aberta_composicao_capital`) | quantidade | 2022 a 2026 |
| `QT_ACAO_PREF_CAP_INTEGR` | `QT_ACAO_PREF_CAP_INTEGR` | inteiro | Domínio : (só em: `dfp_cia_aberta_composicao_capital`) | quantidade | 2022 a 2026 |
| `QT_ACAO_TOTAL_CAP_INTEGR` | `QT_ACAO_TOTAL_CAP_INTEGR` | inteiro | Domínio : (só em: `dfp_cia_aberta_composicao_capital`) | quantidade | 2022 a 2026 |
| `QT_ACAO_ORDIN_TESOURO` | `QT_ACAO_ORDIN_TESOURO` | inteiro | Domínio : (só em: `dfp_cia_aberta_composicao_capital`) | quantidade | 2022 a 2026 |
| `QT_ACAO_PREF_TESOURO` | `QT_ACAO_PREF_TESOURO` | inteiro | Domínio : (só em: `dfp_cia_aberta_composicao_capital`) | quantidade | 2022 a 2026 |
| `QT_ACAO_TOTAL_TESOURO` | `QT_ACAO_TOTAL_TESOURO` | inteiro | Domínio : (só em: `dfp_cia_aberta_composicao_capital`) | quantidade | 2022 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/cia-dfp`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Reapresentações.** A mesma companhia e o mesmo exercício podem ter mais de uma versão do documento (campo `VERSAO`); para somar ou comparar, escolha a maior `VERSAO` de cada `CNPJ_CIA` e `DT_REFER`.
- **Valores em moeda com escala.** Os valores (`VL_CONTA`) vêm na moeda de `MOEDA` e na escala de `ESCALA_MOEDA` (`UNIDADE` ou `MIL`); aplique a escala antes de somar companhias.
- **Consolidado e individual.** As tabelas terminam em `_con` (consolidado) ou `_ind` (individual) e têm os mesmos nomes de coluna; não some as duas.
- **Exercício atual e anterior.** `ORDEM_EXERC` separa o exercício corrente (`ÚLTIMO`) do anterior (`PENÚLTIMO`) dentro do mesmo arquivo; o penúltimo repete valores já publicados no ano anterior.
- **Tipo inferido varia entre arquivos.** 2 coluna(s) (`VERSAO`, ...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Ativo total consolidado (conta 1) das cinco maiores companhias no exercício de 2025, em R$ mil, na última versão de cada documento.

```python
import duckdb

duckdb.sql("""
    SELECT DENOM_CIA, ESCALA_MOEDA, VL_CONTA
    FROM read_parquet('lake/cvm/cia-dfp/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    WHERE ano = 2025 AND CD_CONTA = '1' AND ORDEM_EXERC = 'ÚLTIMO' AND filename ILIKE '%bpa_con%'
    ORDER BY CASE ESCALA_MOEDA WHEN 'MIL' THEN VL_CONTA * 1000 ELSE VL_CONTA END DESC
    LIMIT 5
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/
