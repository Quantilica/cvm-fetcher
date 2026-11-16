---
dataset:
  id: cia-fre
  fonte: cvm
  titulo: "Cias Abertas: Documentos: Formulário de Referência (FRE) - Conjunto de (CVM)"
  resumo: "Formulário de Referência (FRE) das companhias abertas: capital social, administração, remuneração, empregados, partes relacionadas e outros itens do formulário, em cerca de 50 tabelas."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre"
  periodicidade: "anual (um arquivo por ano; a CVM atualiza todos os dias)"
  cobertura: {inicio: 2010, fim: em-curso}
  unidade: "um documento FRE entregue, ou um item do formulário dentro dele (conforme a tabela)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "anual (ano de entrega)"}
  formato_bruto: "CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano], chave: [], colunas: 389}
  unidades_de_medida:
    VERSAO: "código ou número de identificação (sem unidade)"
    ID_DOC: "código ou número de identificação (sem unidade)"
    Versao: "código ou número de identificação (sem unidade)"
    ID_Documento: "código ou número de identificação (sem unidade)"
    ID_Auditor: "código ou número de identificação (sem unidade)"
    CPF_Auditor: "código ou número de identificação (sem unidade)"
    CPF_Responsavel_Tecnico: "código ou número de identificação (sem unidade)"
    CEP: "código ou número de identificação (sem unidade)"
    DDD_Telefone: "código ou número de identificação (sem unidade)"
    ID_Capital_Social: "código ou número de identificação (sem unidade)"
    Valor_Capital: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Acoes_Ordinarias: "quantidade"
    Quantidade_Acoes_Preferenciais: "quantidade"
    Quantidade_Total_Acoes: "quantidade"
    ID_Capital_Social_Aumento: "código ou número de identificação (sem unidade)"
    Valor_Total_Emissao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Subscricao_Capital_Anterior: "ver a descrição"
    Preco_Emissao: "ver a descrição"
    Quantidade_Acoes: "quantidade"
    ID_Capital_Social_Desdobramento: "código ou número de identificação (sem unidade)"
    Quantidade_Acoes_Ordinarias_Antes_Aprovacao: "quantidade"
    Quantidade_Acoes_Preferenciais_Antes_Aprovacao: "quantidade"
    Quantidade_Total_Acoes_Antes_Aprovacao: "quantidade"
    Quantidade_Acoes_Ordinarias_Depois_Aprovacao: "quantidade"
    Quantidade_Acoes_Preferenciais_Depois_Aprovacao: "quantidade"
    Quantidade_Total_Acoes_Depois_Aprovacao: "quantidade"
    Quantidade_Acoes_Antes_Aprovacao: "quantidade"
    Quantidade_Acoes_Depois_Aprovacao: "quantidade"
    ID_Capital_Social_Reducao: "código ou número de identificação (sem unidade)"
    Valor_Total_Reducao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Reducao_Capital_Anterior: "ver a descrição"
    Valor_Restituido_Por_Acao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Percentual_Tag_Along: "ver a descrição"
    Quantidade_Acionistas_PF: "quantidade"
    Quantidade_Acionistas_PJ: "quantidade"
    Quantidade_Acionistas_Investidores_Institucionais: "quantidade"
    Quantidade_Acoes_Ordinarias_Circulacao: "quantidade"
    Percentual_Acoes_Ordinarias_Circulacao: "%"
    Quantidade_Acoes_Preferenciais_Circulacao: "quantidade"
    Percentual_Acoes_Preferenciais_Circulacao: "%"
    Quantidade_Total_Acoes_Circulacao: "quantidade"
    Percentual_Total_Acoes_Circulacao: "%"
    Lucro_Liquido_Ajustado: "ver a descrição"
    Taxa_Retorno_Patrimonio_Liquido_Emissor: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Lucro_Liquido_Retido: "ver a descrição"
    Dividendo_Distribuido_Lucro_Liquido_Ajustado: "ver a descrição"
    Dividendo_Distribuido_Total: "ver a descrição"
    Montante: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Passivo: "ver a descrição"
    Indice_Endividamento: "ver a descrição"
    Valor: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Divida_Inferior_1_Ano: "ver a descrição"
    Divida_1a3Anos: "ver a descrição"
    Divida_3a5Anos: "ver a descrição"
    Divida_Superior_5Anos: "ver a descrição"
    Divida_Total: "ver a descrição"
    Quantidade: "quantidade"
    ID_Sociedade: "código ou número de identificação (sem unidade)"
    Participacao_Emissor: "ver a descrição"
    Variacao_Percentual_Valor_Contabil: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Variacao_Percentual_Valor_Mercado: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Valor_Montante_Dividendos_Recebidos: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    ID_Plano_Recompra: "código ou número de identificação (sem unidade)"
    Valor_Reserva_Disponivel_Recompra: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Adquirida: "quantidade"
    Quantidade_Prevista: "quantidade"
    Valor_Preco_Medio: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Percentual_Previsto: "ver a descrição"
    Percentual_Adquirido: "ver a descrição"
    ID_Politica: "código ou número de identificação (sem unidade)"
    ID_Acionista: "código ou número de identificação (sem unidade)"
    ID_Acionista_Relacionado: "código ou número de identificação (sem unidade)"
    Quantidade_Acao_Ordinaria_Circulacao: "quantidade"
    Percentual_Acao_Ordinaria_Circulacao: "%"
    Quantidade_Acao_Preferencial_Circulacao: "quantidade"
    Percentual_Acao_Preferencial_Circulacao: "%"
    Percentual_Acoes: "ver a descrição"
    Numero_Membros: "quantidade"
    Valor_Maior_Remuneracao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Valor_Menor_Remuneracao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Valor_Medio_Remuneracao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Total_Remuneracao: "ver a descrição"
    Total_Remuneracao_Orgao: "ver a descrição"
    Salario: "ver a descrição"
    Beneficios_Diretos_Indiretos: "ver a descrição"
    Participacoes_Comites: "ver a descrição"
    Outros_Valores_Fixos: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Bonus: "ver a descrição"
    Participacao_Resultados: "ver a descrição"
    Participacao_Reunioes: "ver a descrição"
    Outros_Valores_Variaveis: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Comissoes: "ver a descrição"
    Pos_emprego: "ver a descrição"
    Cessacao_Cargo: "ver a descrição"
    Baseada_Acoes: "ver a descrição"
    Montante_Envolvido: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Inicial: "quantidade"
    Valor_Preco_Medio_Adquirido: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Alienada: "quantidade"
    Valor_Preco_Medio_Alienado: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Cancelada: "quantidade"
    Quantidade_Final: "quantidade"
    Quantidade_Valor_Mobiliario: "quantidade"
    Percentual_Circulacao: "ver a descrição"
    Valor_Volume_Negociado: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Valor_Maior_Cotacao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Valor_Menor_Cotacao: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Investidor: "quantidade"
    Valor_Nominal: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Percentual: "ver a descrição"
    Quantidade_Total_Membros: "quantidade"
    Quantidade_Membros_Remunerados: "quantidade"
    Preco_Medio_Ponderado_Aquisicao: "ver a descrição"
    Preco_Medio_Ponderado_Mercado: "ver a descrição"
    Valor_Diferenca_Aquisicao_Mercado: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Quantidade_Feminino: "quantidade"
    Quantidade_Masculino: "quantidade"
    Quantidade_Nao_Binario: "quantidade"
    Quantidade_Outros: "quantidade"
    Quantidade_Sem_Resposta: "quantidade"
    Quantidade_Amarelo: "quantidade"
    Quantidade_Branco: "quantidade"
    Quantidade_Preto: "quantidade"
    Quantidade_Pardo: "quantidade"
    Quantidade_Indigena: "quantidade"
    Quantidade_PCD: "quantidade"
    Quantidade_Nao_PCD: "quantidade"
    Quantidade_Ate30Anos: "quantidade"
    Quantidade_30a50Anos: "quantidade"
    Quantidade_Acima50Anos: "quantidade"
    Codigo_Posicao: "código ou número de identificação (sem unidade)"
    Quantidade_Norte: "quantidade"
    Quantidade_Nordeste: "quantidade"
    Quantidade_Centro_Oeste: "quantidade"
    Quantidade_Sudeste: "quantidade"
    Quantidade_Sul: "quantidade"
    Quantidade_Exterior: "quantidade"
    Diluicao_Potencial: "ver a descrição"
    Preco_Medio_Ponderado_Opcoes_Em_Aberto: "ver a descrição"
    Preco_Medio_Ponderado_Opcoes_Perdidas: "ver a descrição"
    Preco_Medio_Ponderado_Opcoes_Exercidas: "ver a descrição"
    Bonus_Valor_Minimo: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Bonus_Valor_Maximo: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Bonus_Valor_Metas_Atingidas: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Bonus_Valor_Efetivo: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Participacao_Valor_Minimo: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Participacao_Valor_Maximo: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Participacao_Valor_Metas_Atingidas: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
    Participacao_Valor_Efetivo: "moeda (ver ESCALA_MOEDA, quando houver; senão R$)"
  dados_pessoais:
    - {coluna: CPF, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Complemento_Cargo_Eletivo_Ocupado, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_Auditor, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_Responsavel_Tecnico, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Logradouro, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Complemento, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CEP, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDI_Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: DDD_Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Telefone, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: Email, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_Acionista, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_Acionista_Relacionado, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_CNPJ_Representante_legal, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_Administrador, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: CPF_Pessoa_Relacionada, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-15
  versao_fetcher: 0.0.0
---

# Cias Abertas: Documentos: Formulário de Referência (FRE) - Conjunto de

## Resumo

Formulário de Referência (FRE) das companhias abertas: capital social, administração, remuneração, empregados, partes relacionadas e outros itens do formulário, em cerca de 50 tabelas.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/cia-fre` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre |
| Periodicidade | anual (um arquivo por ano; a CVM atualiza todos os dias) |
| Cobertura | 2010 a em-curso |
| Unidade (uma linha) | um documento FRE entregue, ou um item do formulário dentro dele (conforme a tabela) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: anual (ano de entrega) |
| Formato bruto | CSV com ponto e vírgula, em arquivo CSV ou ZIP (um CSV por tabela dentro do ZIP) no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 389 |
| Unidades de medida | `VERSAO`: código ou número de identificação (sem unidade); `ID_DOC`: código ou número de identificação (sem unidade); `Versao`: código ou número de identificação (sem unidade); `ID_Documento`: código ou número de identificação (sem unidade); `ID_Auditor`: código ou número de identificação (sem unidade); `CPF_Auditor`: código ou número de identificação (sem unidade); `CPF_Responsavel_Tecnico`: código ou número de identificação (sem unidade); `CEP`: código ou número de identificação (sem unidade); `DDD_Telefone`: código ou número de identificação (sem unidade); `ID_Capital_Social`: código ou número de identificação (sem unidade); `Valor_Capital`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Acoes_Ordinarias`: quantidade; `Quantidade_Acoes_Preferenciais`: quantidade; `Quantidade_Total_Acoes`: quantidade; `ID_Capital_Social_Aumento`: código ou número de identificação (sem unidade); `Valor_Total_Emissao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Subscricao_Capital_Anterior`: ver a descrição; `Preco_Emissao`: ver a descrição; `Quantidade_Acoes`: quantidade; `ID_Capital_Social_Desdobramento`: código ou número de identificação (sem unidade); `Quantidade_Acoes_Ordinarias_Antes_Aprovacao`: quantidade; `Quantidade_Acoes_Preferenciais_Antes_Aprovacao`: quantidade; `Quantidade_Total_Acoes_Antes_Aprovacao`: quantidade; `Quantidade_Acoes_Ordinarias_Depois_Aprovacao`: quantidade; `Quantidade_Acoes_Preferenciais_Depois_Aprovacao`: quantidade; `Quantidade_Total_Acoes_Depois_Aprovacao`: quantidade; `Quantidade_Acoes_Antes_Aprovacao`: quantidade; `Quantidade_Acoes_Depois_Aprovacao`: quantidade; `ID_Capital_Social_Reducao`: código ou número de identificação (sem unidade); `Valor_Total_Reducao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Reducao_Capital_Anterior`: ver a descrição; `Valor_Restituido_Por_Acao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Percentual_Tag_Along`: ver a descrição; `Quantidade_Acionistas_PF`: quantidade; `Quantidade_Acionistas_PJ`: quantidade; `Quantidade_Acionistas_Investidores_Institucionais`: quantidade; `Quantidade_Acoes_Ordinarias_Circulacao`: quantidade; `Percentual_Acoes_Ordinarias_Circulacao`: %; `Quantidade_Acoes_Preferenciais_Circulacao`: quantidade; `Percentual_Acoes_Preferenciais_Circulacao`: %; `Quantidade_Total_Acoes_Circulacao`: quantidade; `Percentual_Total_Acoes_Circulacao`: %; `Lucro_Liquido_Ajustado`: ver a descrição; `Taxa_Retorno_Patrimonio_Liquido_Emissor`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Lucro_Liquido_Retido`: ver a descrição; `Dividendo_Distribuido_Lucro_Liquido_Ajustado`: ver a descrição; `Dividendo_Distribuido_Total`: ver a descrição; `Montante`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Passivo`: ver a descrição; `Indice_Endividamento`: ver a descrição; `Valor`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Divida_Inferior_1_Ano`: ver a descrição; `Divida_1a3Anos`: ver a descrição; `Divida_3a5Anos`: ver a descrição; `Divida_Superior_5Anos`: ver a descrição; `Divida_Total`: ver a descrição; `Quantidade`: quantidade; `ID_Sociedade`: código ou número de identificação (sem unidade); `Participacao_Emissor`: ver a descrição; `Variacao_Percentual_Valor_Contabil`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Variacao_Percentual_Valor_Mercado`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Valor_Montante_Dividendos_Recebidos`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `ID_Plano_Recompra`: código ou número de identificação (sem unidade); `Valor_Reserva_Disponivel_Recompra`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Adquirida`: quantidade; `Quantidade_Prevista`: quantidade; `Valor_Preco_Medio`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Percentual_Previsto`: ver a descrição; `Percentual_Adquirido`: ver a descrição; `ID_Politica`: código ou número de identificação (sem unidade); `ID_Acionista`: código ou número de identificação (sem unidade); `ID_Acionista_Relacionado`: código ou número de identificação (sem unidade); `Quantidade_Acao_Ordinaria_Circulacao`: quantidade; `Percentual_Acao_Ordinaria_Circulacao`: %; `Quantidade_Acao_Preferencial_Circulacao`: quantidade; `Percentual_Acao_Preferencial_Circulacao`: %; `Percentual_Acoes`: ver a descrição; `Numero_Membros`: quantidade; `Valor_Maior_Remuneracao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Valor_Menor_Remuneracao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Valor_Medio_Remuneracao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Total_Remuneracao`: ver a descrição; `Total_Remuneracao_Orgao`: ver a descrição; `Salario`: ver a descrição; `Beneficios_Diretos_Indiretos`: ver a descrição; `Participacoes_Comites`: ver a descrição; `Outros_Valores_Fixos`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Bonus`: ver a descrição; `Participacao_Resultados`: ver a descrição; `Participacao_Reunioes`: ver a descrição; `Outros_Valores_Variaveis`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Comissoes`: ver a descrição; `Pos_emprego`: ver a descrição; `Cessacao_Cargo`: ver a descrição; `Baseada_Acoes`: ver a descrição; `Montante_Envolvido`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Inicial`: quantidade; `Valor_Preco_Medio_Adquirido`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Alienada`: quantidade; `Valor_Preco_Medio_Alienado`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Cancelada`: quantidade; `Quantidade_Final`: quantidade; `Quantidade_Valor_Mobiliario`: quantidade; `Percentual_Circulacao`: ver a descrição; `Valor_Volume_Negociado`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Valor_Maior_Cotacao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Valor_Menor_Cotacao`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Investidor`: quantidade; `Valor_Nominal`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Percentual`: ver a descrição; `Quantidade_Total_Membros`: quantidade; `Quantidade_Membros_Remunerados`: quantidade; `Preco_Medio_Ponderado_Aquisicao`: ver a descrição; `Preco_Medio_Ponderado_Mercado`: ver a descrição; `Valor_Diferenca_Aquisicao_Mercado`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Quantidade_Feminino`: quantidade; `Quantidade_Masculino`: quantidade; `Quantidade_Nao_Binario`: quantidade; `Quantidade_Outros`: quantidade; `Quantidade_Sem_Resposta`: quantidade; `Quantidade_Amarelo`: quantidade; `Quantidade_Branco`: quantidade; `Quantidade_Preto`: quantidade; `Quantidade_Pardo`: quantidade; `Quantidade_Indigena`: quantidade; `Quantidade_PCD`: quantidade; `Quantidade_Nao_PCD`: quantidade; `Quantidade_Ate30Anos`: quantidade; `Quantidade_30a50Anos`: quantidade; `Quantidade_Acima50Anos`: quantidade; `Codigo_Posicao`: código ou número de identificação (sem unidade); `Quantidade_Norte`: quantidade; `Quantidade_Nordeste`: quantidade; `Quantidade_Centro_Oeste`: quantidade; `Quantidade_Sudeste`: quantidade; `Quantidade_Sul`: quantidade; `Quantidade_Exterior`: quantidade; `Diluicao_Potencial`: ver a descrição; `Preco_Medio_Ponderado_Opcoes_Em_Aberto`: ver a descrição; `Preco_Medio_Ponderado_Opcoes_Perdidas`: ver a descrição; `Preco_Medio_Ponderado_Opcoes_Exercidas`: ver a descrição; `Bonus_Valor_Minimo`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Bonus_Valor_Maximo`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Bonus_Valor_Metas_Atingidas`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Bonus_Valor_Efetivo`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Participacao_Valor_Minimo`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Participacao_Valor_Maximo`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Participacao_Valor_Metas_Atingidas`: moeda (ver ESCALA_MOEDA, quando houver; senão R$); `Participacao_Valor_Efetivo`: moeda (ver ESCALA_MOEDA, quando houver; senão R$) |
| Dados pessoais | `CPF` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Complemento_Cargo_Eletivo_Ocupado` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_Auditor` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_Responsavel_Tecnico` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Logradouro` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Complemento` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CEP` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDI_Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `DDD_Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Telefone` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `Email` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_Acionista` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_Acionista_Relacionado` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_CNPJ_Representante_legal` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_Administrador` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `CPF_Pessoa_Relacionada` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 0.0.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/DADOS/`.
- O catálogo do fetcher lista 17 arquivo(s): de `fre_cia_aberta_2010.zip` a `fre_cia_aberta_2026.zip`. Em 2026-11-15 conferimos 249 arquivos Parquet convertidos de 6 arquivo(s) de origem (amostra: primeiro, intermediários e os dois últimos).
- No bruto, o arquivo fica em `cia-fre/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: um documento FRE entregue, ou um item do formulário dentro dele (conforme a tabela).
- Particionado por `ano`; anos convertidos: 2010 a 2026.
- Este dataset reúne 61 tabelas (um CSV por tabela em cada ZIP), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<zip>__<csv>.parquet`:

| Tabela (nome do CSV sem o ano) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no maior arquivo) |
|---|---|---|---|
| `fre_cia_aberta` | 9 | 5.077 | `ID_DOC` |
| `fre_cia_aberta_acao_entregue` | 14 | 1.304 | não determinada |
| `fre_cia_aberta_administrador_declaracao_genero` | 12 | 3.470 | não determinada |
| `fre_cia_aberta_administrador_declaracao_raca` | 14 | 3.470 | não determinada |
| `fre_cia_aberta_administrador_membro_conselho_fiscal` | 21 | 9.336 | não determinada |
| `fre_cia_aberta_administrador_pcd` | 10 | 3.495 | não determinada |
| `fre_cia_aberta_ativo_imobilizado` | 10 | 12.760 | não determinada |
| `fre_cia_aberta_ativo_intangivel` | 10 | 24.542 | não determinada |
| `fre_cia_aberta_auditor` | 18 | 1.447 | `ID_Auditor` |
| `fre_cia_aberta_auditor_responsavel` | 23 | 1.699 | não determinada |
| `fre_cia_aberta_capital_social` | 13 | 3.775 | `ID_Capital_Social` |
| `fre_cia_aberta_capital_social_aumento` | 19 | 2.831 | `ID_Capital_Social_Aumento` |
| `fre_cia_aberta_capital_social_aumento_classe_acao` | 8 | 181 | não determinada |
| `fre_cia_aberta_capital_social_classe_acao` | 8 | 469 | não determinada |
| `fre_cia_aberta_capital_social_desdobramento` | 14 | 282 | `ID_Capital_Social_Desdobramento` |
| `fre_cia_aberta_capital_social_desdobramento_classe_acao` | 9 | 43 | não determinada |
| `fre_cia_aberta_capital_social_reducao` | 16 | 163 | `ID_Capital_Social_Reducao` |
| `fre_cia_aberta_capital_social_reducao_classe_acao` | 8 | 14 | não determinada |
| `fre_cia_aberta_capital_social_titulo_conversivel` | 8 | 44 | `ID_Capital_Social`, `Condicoes_Conversao` |
| `fre_cia_aberta_direito_acao` | 21 | 848 | não determinada |
| `fre_cia_aberta_distribuicao_capital` | 15 | 761 | `ID_Documento` |
| `fre_cia_aberta_distribuicao_capital_classe_acao` | 9 | 312 | não determinada |
| `fre_cia_aberta_distribuicao_dividendos` | 13 | 1.448 | `ID_Documento`, `Data_Inicio_Exercicio_Social` |
| `fre_cia_aberta_distribuicao_dividendos_classe_acao` | 12 | 3.562 | não determinada |
| `fre_cia_aberta_empregado_local_declaracao_genero` | 11 | 3.118 | não determinada |
| `fre_cia_aberta_empregado_local_declaracao_raca` | 13 | 3.117 | não determinada |
| `fre_cia_aberta_empregado_local_faixa_etaria` | 9 | 3.117 | não determinada |
| `fre_cia_aberta_empregado_pcd` | 10 | 1.106 | `CNPJ_Companhia`, `Codigo_Posicao` |
| `fre_cia_aberta_empregado_posicao_declaracao_genero` | 11 | 1.038 | não determinada |
| `fre_cia_aberta_empregado_posicao_declaracao_raca` | 13 | 1.038 | não determinada |
| `fre_cia_aberta_empregado_posicao_faixa_etaria` | 9 | 1.040 | não determinada |
| `fre_cia_aberta_empregado_posicao_local` | 12 | 1.036 | não determinada |
| `fre_cia_aberta_endividamento` | 10 | 888 | não determinada |
| `fre_cia_aberta_grupo_economico_reestruturacao` | 8 | 1.960 | não determinada |
| `fre_cia_aberta_historico_emissor` | 12 | 762 | `ID_Documento` |
| `fre_cia_aberta_informacao_financeira` | 13 | 15.288 | `ID_Documento`, `Data_Inicio_Exercicio_Social`, `Codigo_Conta` |
| `fre_cia_aberta_membro_comite` | 21 | 4.684 | não determinada |
| `fre_cia_aberta_mercado_estrangeiro` | 17 | 152 | não determinada |
| `fre_cia_aberta_obrigacao` | 16 | 1.557 | não determinada |
| `fre_cia_aberta_outro_valor_mobiliario` | 24 | 3.931 | não determinada |
| `fre_cia_aberta_participacao_sociedade` | 21 | 6.511 | `ID_Sociedade` |
| `fre_cia_aberta_participacao_sociedade_valorizacao_acao` | 10 | 19.102 | `ID_Sociedade`, `Data_Encerramento` |
| `fre_cia_aberta_plano_recompra` | 11 | 374 | `ID_Plano_Recompra` |
| `fre_cia_aberta_plano_recompra_classe_acao` | 14 | 418 | não determinada |
| `fre_cia_aberta_politica_negociacao` | 10 | 451 | `ID_Politica` |
| `fre_cia_aberta_politica_negociacao_cargo` | 7 | 744 | não determinada |
| `fre_cia_aberta_posicao_acionaria` | 29 | 31.583 | `ID_Acionista` |
| `fre_cia_aberta_posicao_acionaria_classe_acao` | 9 | 4.211 | não determinada |
| `fre_cia_aberta_relacao_familiar` | 17 | 1.698 | não determinada |
| `fre_cia_aberta_relacao_subordinacao` | 17 | 9.972 | não determinada |
| `fre_cia_aberta_remuneracao_acao` | 14 | 1.565 | não determinada |
| `fre_cia_aberta_remuneracao_maxima_minima_media` | 14 | 3.893 | não determinada |
| `fre_cia_aberta_remuneracao_total_orgao` | 27 | 6.320 | não determinada |
| `fre_cia_aberta_remuneracao_variavel` | 18 | 3.851 | não determinada |
| `fre_cia_aberta_responsavel` | 7 | 1.413 | não determinada |
| `fre_cia_aberta_titular_valor_mobiliario` | 9 | 538 | não determinada |
| `fre_cia_aberta_titulo_exterior` | 21 | 393 | não determinada |
| `fre_cia_aberta_transacao_parte_relacionada` | 22 | 13.798 | não determinada |
| `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao` | 28 | 562 | não determinada |
| `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio` | 14 | 1.211 | não determinada |
| `fre_cia_aberta_volume_valor_mobiliario` | 19 | 5.318 | não determinada |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima). Os arquivos de uma mesma competência ligam-se por identificador do documento ou do fundo (veja as colunas de cada tabela).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CNPJ_CIA` | `CNPJ_CIA` | texto | CNPJ da companhia (só em: `fre_cia_aberta`) | — | todo |
| `DT_REFER` | `DT_REFER` | texto | Data de referência do documento (só em: `fre_cia_aberta`) | — | todo |
| `VERSAO` | `VERSAO` | inteiro | Versão do documento (só em: `fre_cia_aberta`) | código ou número de identificação (sem unidade) | todo |
| `DENOM_CIA` | `DENOM_CIA` | texto | Nome empresarial da companhia (só em: `fre_cia_aberta`) | — | todo |
| `CD_CVM` | `CD_CVM` | texto | Código CVM (só em: `fre_cia_aberta`) | — | todo |
| `CATEG_DOC` | `CATEG_DOC` | texto | Categoria do documento (só em: `fre_cia_aberta`) | — | todo |
| `ID_DOC` | `ID_DOC` | inteiro | Identificador do documento (só em: `fre_cia_aberta`) | código ou número de identificação (sem unidade) | todo |
| `DT_RECEB` | `DT_RECEB` | texto | Data da recebimento do documento (só em: `fre_cia_aberta`) | — | todo |
| `LINK_DOC` | `LINK_DOC` | texto | Endereço para download do documento (só em: `fre_cia_aberta`) | — | todo |
| `CNPJ_Companhia` | `CNPJ_Companhia` | texto | CNPJ da companhia (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_membro_conselho_fiscal` e mais 56) | — | todo |
| `Data_Referencia` | `Data_Referencia` | texto | Data de referência do documento (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_membro_conselho_fiscal` e mais 56) | — | todo |
| `Versao` | `Versao` | inteiro | Versão do documento (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_membro_conselho_fiscal` e mais 56) | código ou número de identificação (sem unidade) | todo |
| `ID_Documento` | `ID_Documento` | inteiro | Identificador do documento (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_membro_conselho_fiscal` e mais 56) | código ou número de identificação (sem unidade) | todo |
| `Nome_Companhia` | `Nome_Companhia` | texto | Nome da Companhia (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_membro_conselho_fiscal` e mais 55) | — | todo |
| `Orgao_Administracao` | `Orgao_Administracao` | texto | Órgão da administração (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_membro_conselho_fiscal` e mais 5) | — | todo |
| `Nome` | `Nome` | texto | Nome da Pessoa Física (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `CPF` | `CPF` | texto | Cadastro de Pessoas Físicas (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Profissao` | `Profissao` | texto | Profissão (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Cargo_Eletivo_Ocupado` | `Cargo_Eletivo_Ocupado` | texto | Cargo eletivo ocupado (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`) | — | todo |
| `Complemento_Cargo_Eletivo_Ocupado` | `Complemento_Cargo_Eletivo_Ocupado` | texto | Cargo eletivo ocupado (Complemento) (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`) | — | todo |
| `Data_Eleicao` | `Data_Eleicao` | texto | Data da eleição (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Data_Posse` | `Data_Posse` | texto | Data da posse (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Data_Inicio_Primeiro_Mandato` | `Data_Inicio_Primeiro_Mandato` | texto | Domínio : (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Prazo_Mandato` | `Prazo_Mandato` | texto | Prazo do mandato (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Eleito_Controlador` | `Eleito_Controlador` | texto | Indica se foi eleito pelo controlador (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`) | S/N | todo |
| `Outro_Cargo_Funcao` | `Outro_Cargo_Funcao` | texto | Outros cargos e funções exercidas (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Experiencia_Profissional` | `Experiencia_Profissional` | texto | Experiência profissional (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Data_Nascimento` | `Data_Nascimento` | texto | Data de nascimento (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Numero_Mandatos_Consecutivos` | `Numero_Mandatos_Consecutivos` | inteiro / texto | Número de mandatos consecutivos (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Percentual_Participacao_Reunioes` | `Percentual_Participacao_Reunioes` | decimal / texto | Percentual de participação nas reuniões (só em: `fre_cia_aberta_administrador_membro_conselho_fiscal`, `fre_cia_aberta_membro_comite`) | — | todo |
| `Descricao_Bem_Ativo` | `Descricao_Bem_Ativo` | texto | Domínio : (só em: `fre_cia_aberta_ativo_imobilizado`) | — | 2010 a 2022 |
| `Pais` | `Pais` | texto | País (só em: `fre_cia_aberta_ativo_imobilizado`, `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `UF` | `UF` | texto | Unidade da Federação (só em: `fre_cia_aberta_ativo_imobilizado`, `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Municipio` | `Municipio` | texto | Domínio : (só em: `fre_cia_aberta_ativo_imobilizado`) | — | 2010 a 2022 |
| `Tipo_Propriedade` | `Tipo_Propriedade` | texto | Domínio : (só em: `fre_cia_aberta_ativo_imobilizado`) | — | 2010 a 2022 |
| `Tipo_Ativo` | `Tipo_Ativo` | texto | Tipo de Ativo (Valor Mobiliário) (só em: `fre_cia_aberta_ativo_intangivel`) | — | 2010 a 2022 |
| `Descricao_Ativo` | `Descricao_Ativo` | texto | Domínio : (só em: `fre_cia_aberta_ativo_intangivel`) | — | 2010 a 2022 |
| `Duracao` | `Duracao` | texto | Domínio : (só em: `fre_cia_aberta_ativo_intangivel`) | — | 2010 a 2022 |
| `Evento_Perda_Direito` | `Evento_Perda_Direito` | texto | Domínio : (só em: `fre_cia_aberta_ativo_intangivel`) | — | 2010 a 2022 |
| `Consequencia_Perda_Direito` | `Consequencia_Perda_Direito` | texto | Domínio : (só em: `fre_cia_aberta_ativo_intangivel`) | — | 2010 a 2022 |
| `ID_Auditor` | `ID_Auditor` | inteiro | Domínio : (só em: `fre_cia_aberta_auditor`, `fre_cia_aberta_auditor_responsavel`) | código ou número de identificação (sem unidade) | todo |
| `Auditor` | `Auditor` | texto | Nome do Auditor (só em: `fre_cia_aberta_auditor`) | — | todo |
| `CPF_Auditor` | `CPF_Auditor` | inteiro | Domínio : (só em: `fre_cia_aberta_auditor`) | código ou número de identificação (sem unidade) | todo |
| `CNPJ_Auditor` | `CNPJ_Auditor` | texto | CNPJ do Auditor (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Codigo_CVM_Auditor` | `Codigo_CVM_Auditor` | texto | Código CVM do auditor (só em: `fre_cia_aberta_auditor`) | Númerico | todo |
| `Tipo_Origem_Auditor` | `Tipo_Origem_Auditor` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Data_Inicio_Contratacao` | `Data_Inicio_Contratacao` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Data_Fim_Contratacao` | `Data_Fim_Contratacao` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Data_Inicio_Prestacao_Servico` | `Data_Inicio_Prestacao_Servico` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Servico_Contratado` | `Servico_Contratado` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Remuneracao_Auditor` | `Remuneracao_Auditor` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Justificativa_Substituicao` | `Justificativa_Substituicao` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Razao_Apresentada` | `Razao_Apresentada` | texto | Domínio : (só em: `fre_cia_aberta_auditor`) | — | todo |
| `Data_Inicio_Responsavel_Tecnico` | `Data_Inicio_Responsavel_Tecnico` | texto | Domínio : (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Data_Fim_Responsavel_Tecnico` | `Data_Fim_Responsavel_Tecnico` | texto | Domínio : (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Responsavel_Tecnico` | `Responsavel_Tecnico` | texto | Responsável técnico (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `CPF_Responsavel_Tecnico` | `CPF_Responsavel_Tecnico` | inteiro | CPF do responsável técnico (só em: `fre_cia_aberta_auditor_responsavel`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Logradouro` | `Logradouro` | texto | Logradouro (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Complemento` | `Complemento` | texto | Complemento (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Bairro` | `Bairro` | texto | Bairro (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Cidade` | `Cidade` | texto | Cidade (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Sigla_UF` | `Sigla_UF` | texto | Sigla da Unidade da Federação (só em: `fre_cia_aberta_auditor_responsavel`, `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `CEP` | `CEP` | inteiro | CEP (só em: `fre_cia_aberta_auditor_responsavel`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `DDI_Telefone` | `DDI_Telefone` | texto | Código de DDI (Telefone) (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `DDD_Telefone` | `DDD_Telefone` | inteiro | Código de DDD (Telefone) (só em: `fre_cia_aberta_auditor_responsavel`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Telefone` | `Telefone` | inteiro / texto | Telefone (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Fax` | `Fax` | inteiro / texto | FAX (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `Email` | `Email` | texto | Endereço de e-mail (só em: `fre_cia_aberta_auditor_responsavel`) | — | 2010 a 2022 |
| `ID_Capital_Social` | `ID_Capital_Social` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social`, `fre_cia_aberta_capital_social_classe_acao`, `fre_cia_aberta_capital_social_titulo_conversivel`) | código ou número de identificação (sem unidade) | todo |
| `Tipo_Capital` | `Tipo_Capital` | texto | Domínio : (só em: `fre_cia_aberta_capital_social`) | — | todo |
| `Data_Autorizacao_Aprovacao` | `Data_Autorizacao_Aprovacao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social`) | — | todo |
| `Valor_Capital` | `Valor_Capital` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Prazo_Integralizacao` | `Prazo_Integralizacao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social`) | — | todo |
| `Quantidade_Acoes_Ordinarias` | `Quantidade_Acoes_Ordinarias` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social`, `fre_cia_aberta_capital_social_aumento`, `fre_cia_aberta_capital_social_reducao`) | quantidade | todo |
| `Quantidade_Acoes_Preferenciais` | `Quantidade_Acoes_Preferenciais` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social`, `fre_cia_aberta_capital_social_aumento`, `fre_cia_aberta_capital_social_reducao`) | quantidade | todo |
| `Quantidade_Total_Acoes` | `Quantidade_Total_Acoes` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social`, `fre_cia_aberta_capital_social_aumento`, `fre_cia_aberta_capital_social_reducao`) | quantidade | todo |
| `ID_Capital_Social_Aumento` | `ID_Capital_Social_Aumento` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`, `fre_cia_aberta_capital_social_aumento_classe_acao`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Data_Deliberacao` | `Data_Deliberacao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`, `fre_cia_aberta_capital_social_reducao`, `fre_cia_aberta_plano_recompra`) | — | 2010 a 2022 |
| `Orgao_Deliberacao_Aumento` | `Orgao_Deliberacao_Aumento` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | — | 2010 a 2022 |
| `Data_Emissao` | `Data_Emissao` | texto | Data de Emissão (só em: `fre_cia_aberta_capital_social_aumento`, `fre_cia_aberta_mercado_estrangeiro`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Valor_Total_Emissao` | `Valor_Total_Emissao` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Tipo_Subscricao` | `Tipo_Subscricao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | — | 2010 a 2022 |
| `Subscricao_Capital_Anterior` | `Subscricao_Capital_Anterior` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | ver a descrição | 2010 a 2022 |
| `Fator_Cotacao` | `Fator_Cotacao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | — | 2010 a 2022 |
| `Preco_Emissao` | `Preco_Emissao` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | ver a descrição | 2010 a 2022 |
| `Criterio_Determinacao_Preco_Emissao` | `Criterio_Determinacao_Preco_Emissao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | — | 2010 a 2022 |
| `Forma_Integralizacao` | `Forma_Integralizacao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento`) | — | 2010 a 2022 |
| `Tipo_Classe_Acao_Preferencial` | `Tipo_Classe_Acao_Preferencial` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_aumento_classe_acao`, `fre_cia_aberta_capital_social_classe_acao`, `fre_cia_aberta_capital_social_desdobramento_classe_acao`, `fre_cia_aberta_capital_social_reducao_classe_acao` e mais 4) | — | todo |
| `Quantidade_Acoes` | `Quantidade_Acoes` | inteiro | Domínio : (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_capital_social_aumento_classe_acao`, `fre_cia_aberta_capital_social_classe_acao`, `fre_cia_aberta_capital_social_reducao_classe_acao` e mais 1) | quantidade | todo |
| `ID_Capital_Social_Desdobramento` | `ID_Capital_Social_Desdobramento` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`, `fre_cia_aberta_capital_social_desdobramento_classe_acao`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Data_Aprovacao` | `Data_Aprovacao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`, `fre_cia_aberta_politica_negociacao`) | — | 2010 a 2022 |
| `Tipo_Evento` | `Tipo_Evento` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | — | 2010 a 2022 |
| `Quantidade_Acoes_Ordinarias_Antes_Aprovacao` | `Quantidade_Acoes_Ordinarias_Antes_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | quantidade | 2010 a 2022 |
| `Quantidade_Acoes_Preferenciais_Antes_Aprovacao` | `Quantidade_Acoes_Preferenciais_Antes_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | quantidade | 2010 a 2022 |
| `Quantidade_Total_Acoes_Antes_Aprovacao` | `Quantidade_Total_Acoes_Antes_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | quantidade | 2010 a 2022 |
| `Quantidade_Acoes_Ordinarias_Depois_Aprovacao` | `Quantidade_Acoes_Ordinarias_Depois_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | quantidade | 2010 a 2022 |
| `Quantidade_Acoes_Preferenciais_Depois_Aprovacao` | `Quantidade_Acoes_Preferenciais_Depois_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | quantidade | 2010 a 2022 |
| `Quantidade_Total_Acoes_Depois_Aprovacao` | `Quantidade_Total_Acoes_Depois_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento`) | quantidade | 2010 a 2022 |
| `Quantidade_Acoes_Antes_Aprovacao` | `Quantidade_Acoes_Antes_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento_classe_acao`) | quantidade | 2010 a 2022 |
| `Quantidade_Acoes_Depois_Aprovacao` | `Quantidade_Acoes_Depois_Aprovacao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_desdobramento_classe_acao`) | quantidade | 2010 a 2022 |
| `ID_Capital_Social_Reducao` | `ID_Capital_Social_Reducao` | inteiro | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`, `fre_cia_aberta_capital_social_reducao_classe_acao`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Data_Reducao` | `Data_Reducao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`) | — | 2010 a 2022 |
| `Valor_Total_Reducao` | `Valor_Total_Reducao` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Reducao_Capital_Anterior` | `Reducao_Capital_Anterior` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`) | ver a descrição | 2010 a 2022 |
| `Valor_Restituido_Por_Acao` | `Valor_Restituido_Por_Acao` | decimal | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Forma_Restituicao` | `Forma_Restituicao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`) | — | 2010 a 2022 |
| `Razao_Reducao` | `Razao_Reducao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_reducao`) | — | 2010 a 2022 |
| `Titulo_Conversivel_Acao` | `Titulo_Conversivel_Acao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_titulo_conversivel`) | — | todo |
| `Condicoes_Conversao` | `Condicoes_Conversao` | texto | Domínio : (só em: `fre_cia_aberta_capital_social_titulo_conversivel`) | — | todo |
| `Especie_Acao` | `Especie_Acao` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_distribuicao_dividendos_classe_acao`, `fre_cia_aberta_plano_recompra_classe_acao`, `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao` e mais 2) | — | 2010 a 2022 |
| `Classe_Acao_Preferencial` | `Classe_Acao_Preferencial` | texto | Classe de ação preferencial (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Percentual_Tag_Along` | `Percentual_Tag_Along` | decimal | Domínio : (só em: `fre_cia_aberta_direito_acao`) | ver a descrição | 2010 a 2022 |
| `Direito_Dividendo` | `Direito_Dividendo` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`) | — | 2010 a 2022 |
| `Direito_Voto` | `Direito_Voto` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`) | — | 2010 a 2022 |
| `Conversibilidade` | `Conversibilidade` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Descricao_Voto_Restrito` | `Descricao_Voto_Restrito` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`) | — | 2010 a 2022 |
| `Condicao_Conversibilidade_Efeito_Capital_Social` | `Condicao_Conversibilidade_Efeito_Capital_Social` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`) | — | todo |
| `Direito_Reembolso_Capital` | `Direito_Reembolso_Capital` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`) | — | 2010 a 2022 |
| `Restricao_Circulacao` | `Restricao_Circulacao` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Caracteristicas_Reembolso_Capital` | `Caracteristicas_Reembolso_Capital` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`) | — | 2010 a 2022 |
| `Descricao_Restricao_Circulacao` | `Descricao_Restricao_Circulacao` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Resgatavel` | `Resgatavel` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`) | — | todo |
| `Hipotese_Resgate_Formula_Calculo` | `Hipotese_Resgate_Formula_Calculo` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`) | — | todo |
| `Condicao_Alteracao_Direitos` | `Condicao_Alteracao_Direitos` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Outras_Caracteristicas_Relevantes` | `Outras_Caracteristicas_Relevantes` | texto | Domínio : (só em: `fre_cia_aberta_direito_acao`, `fre_cia_aberta_outro_valor_mobiliario`) | — | todo |
| `Quantidade_Acionistas_PF` | `Quantidade_Acionistas_PF` | inteiro | Quantidade de acionistas pessoas físicas (só em: `fre_cia_aberta_distribuicao_capital`) | quantidade | todo |
| `Quantidade_Acionistas_PJ` | `Quantidade_Acionistas_PJ` | inteiro | Quantidade de acionistas pessoas jurídicas (só em: `fre_cia_aberta_distribuicao_capital`) | quantidade | todo |
| `Quantidade_Acionistas_Investidores_Institucionais` | `Quantidade_Acionistas_Investidores_Institucionais` | inteiro | Quantidade de investidores institucionais (só em: `fre_cia_aberta_distribuicao_capital`) | quantidade | todo |
| `Quantidade_Acoes_Ordinarias_Circulacao` | `Quantidade_Acoes_Ordinarias_Circulacao` | inteiro | Quantidade de ações ordinárias em circulação (só em: `fre_cia_aberta_distribuicao_capital`) | quantidade | todo |
| `Percentual_Acoes_Ordinarias_Circulacao` | `Percentual_Acoes_Ordinarias_Circulacao` | decimal | Percentual de ações ordinárias em circulação (só em: `fre_cia_aberta_distribuicao_capital`) | % | todo |
| `Quantidade_Acoes_Preferenciais_Circulacao` | `Quantidade_Acoes_Preferenciais_Circulacao` | inteiro | Quantidade de ações preferenciais em circulação (só em: `fre_cia_aberta_distribuicao_capital`, `fre_cia_aberta_distribuicao_capital_classe_acao`) | quantidade | todo |
| `Percentual_Acoes_Preferenciais_Circulacao` | `Percentual_Acoes_Preferenciais_Circulacao` | decimal | Percentual de ações preferenciais em circulação (só em: `fre_cia_aberta_distribuicao_capital`, `fre_cia_aberta_distribuicao_capital_classe_acao`) | % | todo |
| `Quantidade_Total_Acoes_Circulacao` | `Quantidade_Total_Acoes_Circulacao` | inteiro | Quantidade total de ações em circulação (só em: `fre_cia_aberta_distribuicao_capital`, `fre_cia_aberta_posicao_acionaria`) | quantidade | todo |
| `Percentual_Total_Acoes_Circulacao` | `Percentual_Total_Acoes_Circulacao` | decimal | Percentual total de ações em circulação (só em: `fre_cia_aberta_distribuicao_capital`, `fre_cia_aberta_posicao_acionaria`) | % | todo |
| `Data_Ultima_Assembleia` | `Data_Ultima_Assembleia` | texto | Data da última assembléia geral de acionistas (só em: `fre_cia_aberta_distribuicao_capital`) | — | todo |
| `Sigla_Classe_Acoes_Preferenciais` | `Sigla_Classe_Acoes_Preferenciais` | texto | Classe de ações preferenciais (Sigla) (só em: `fre_cia_aberta_distribuicao_capital_classe_acao`) | — | todo |
| `Classe_Acoes_Preferenciais` | `Classe_Acoes_Preferenciais` | texto | Classe de ações preferenciais (só em: `fre_cia_aberta_distribuicao_capital_classe_acao`) | — | todo |
| `Data_Inicio_Exercicio_Social` | `Data_Inicio_Exercicio_Social` | texto | Data de início do Exercício Social (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_distribuicao_dividendos`, `fre_cia_aberta_distribuicao_dividendos_classe_acao`, `fre_cia_aberta_endividamento` e mais 9) | — | todo |
| `Data_Fim_Exercicio_Social` | `Data_Fim_Exercicio_Social` | texto | Data fim do Exercício Social (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_distribuicao_dividendos`, `fre_cia_aberta_distribuicao_dividendos_classe_acao`, `fre_cia_aberta_endividamento` e mais 9) | — | todo |
| `Lucro_Liquido_Ajustado` | `Lucro_Liquido_Ajustado` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos`) | ver a descrição | 2010 a 2022 |
| `Taxa_Retorno_Patrimonio_Liquido_Emissor` | `Taxa_Retorno_Patrimonio_Liquido_Emissor` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Lucro_Liquido_Retido` | `Lucro_Liquido_Retido` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos`) | ver a descrição | 2010 a 2022 |
| `Dividendo_Distribuido_Lucro_Liquido_Ajustado` | `Dividendo_Distribuido_Lucro_Liquido_Ajustado` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos`) | ver a descrição | 2010 a 2022 |
| `Dividendo_Distribuido_Total` | `Dividendo_Distribuido_Total` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos`) | ver a descrição | 2010 a 2022 |
| `Data_Aprovacao_Retencao` | `Data_Aprovacao_Retencao` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos`) | — | 2010 a 2022 |
| `Classe_Acao` | `Classe_Acao` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos_classe_acao`) | — | 2010 a 2022 |
| `Dividendo_Distribuido` | `Dividendo_Distribuido` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos_classe_acao`) | — | 2010 a 2022 |
| `Montante` | `Montante` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos_classe_acao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Data_Pagamento_Dividendo` | `Data_Pagamento_Dividendo` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_distribuicao_dividendos_classe_acao`) | — | 2010 a 2022 |
| `Passivo` | `Passivo` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_endividamento`) | ver a descrição | 2010 a 2022 |
| `Indice_Endividamento` | `Indice_Endividamento` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_endividamento`) | ver a descrição | 2010 a 2022 |
| `Tipo_Indice` | `Tipo_Indice` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_endividamento`) | — | 2010 a 2022 |
| `Descricao_Outro_Indice` | `Descricao_Outro_Indice` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_endividamento`) | — | 2010 a 2022 |
| `Data_Operacao` | `Data_Operacao` | texto | Domínio : (só em: `fre_cia_aberta_grupo_economico_reestruturacao`) | — | 2010 a 2014 |
| `Descricao_Operacao` | `Descricao_Operacao` | texto | Domínio : (só em: `fre_cia_aberta_grupo_economico_reestruturacao`) | — | 2010 a 2014 |
| `Evento_Societario` | `Evento_Societario` | texto | Domínio : (só em: `fre_cia_aberta_grupo_economico_reestruturacao`) | — | 2010 a 2014 |
| `Data_Constituicao_Emissor` | `Data_Constituicao_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Forma_Constituicao_Emissor` | `Forma_Constituicao_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Sigla_Pais_Constituicao_Emissor` | `Sigla_Pais_Constituicao_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Pais_Constituicao_Emissor` | `Pais_Constituicao_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Prazo_Duracao_Emissor` | `Prazo_Duracao_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Data_Registro_Emissor` | `Data_Registro_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Requisicao_Registro_Emissor` | `Requisicao_Registro_Emissor` | texto | Domínio : (só em: `fre_cia_aberta_historico_emissor`) | — | 2010 a 2022 |
| `Codigo_Conta` | `Codigo_Conta` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_informacao_financeira`) | — | 2010 a 2022 |
| `Descricao_Conta` | `Descricao_Conta` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_informacao_financeira`) | — | 2010 a 2022 |
| `Valor` | `Valor` | decimal | Domínio : (só em: `fre_cia_aberta_informacao_financeira`, `fre_cia_aberta_outro_valor_mobiliario`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Informacao_Financeira` | `Informacao_Financeira` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_informacao_financeira`) | — | 2010 a 2022 |
| `Tipo_Moeda` | `Tipo_Moeda` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_informacao_financeira`) | — | 2010 a 2022 |
| `Escala_Moeda` | `Escala_Moeda` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_informacao_financeira`) | — | 2010 a 2022 |
| `Tipo_Comite` | `Tipo_Comite` | texto | Tipo de comitê (só em: `fre_cia_aberta_membro_comite`) | — | todo |
| `Descricao_Outros_Comites` | `Descricao_Outros_Comites` | texto | Descrição de outros comitês (só em: `fre_cia_aberta_membro_comite`) | — | todo |
| `Cargo_Ocupado` | `Cargo_Ocupado` | texto | Cargo ocupado (só em: `fre_cia_aberta_membro_comite`) | — | todo |
| `Descricao_Outro_Cargo_Ocupado` | `Descricao_Outro_Cargo_Ocupado` | texto | Descrição de outros cargos ocupados (só em: `fre_cia_aberta_membro_comite`) | — | todo |
| `Tipo_Obrigacao` | `Tipo_Obrigacao` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | — | 2010 a 2022 |
| `Tipo_Garantia` | `Tipo_Garantia` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | — | 2010 a 2022 |
| `Descricao_Outras_Garantias` | `Descricao_Outras_Garantias` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | — | 2010 a 2022 |
| `Divida_Inferior_1_Ano` | `Divida_Inferior_1_Ano` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | ver a descrição | 2010 a 2022 |
| `Divida_1a3Anos` | `Divida_1a3Anos` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | ver a descrição | 2010 a 2022 |
| `Divida_3a5Anos` | `Divida_3a5Anos` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | ver a descrição | 2010 a 2022 |
| `Divida_Superior_5Anos` | `Divida_Superior_5Anos` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | ver a descrição | 2010 a 2022 |
| `Divida_Total` | `Divida_Total` | decimal | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_obrigacao`) | ver a descrição | 2010 a 2022 |
| `Observacao` | `Observacao` | texto | Observação (só em: `fre_cia_aberta_obrigacao`, `fre_cia_aberta_relacao_familiar`, `fre_cia_aberta_relacao_subordinacao`, `fre_cia_aberta_remuneracao_maxima_minima_media` e mais 1) | — | todo |
| `Valor_Mobiliario` | `Valor_Mobiliario` | texto | Valor mobiliário (só em: `fre_cia_aberta_mercado_estrangeiro`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titular_valor_mobiliario`, `fre_cia_aberta_titulo_exterior` e mais 3) | — | todo |
| `Identificacao_Valor_Mobiliario` | `Identificacao_Valor_Mobiliario` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`, `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Data_Vencimento` | `Data_Vencimento` | texto | Data de Vencimento (só em: `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Quantidade` | `Quantidade` | inteiro | Domínio : (só em: `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | quantidade | todo |
| `Quantidade_Pessoa_Fisica` | `Quantidade_Pessoa_Fisica` | inteiro / texto | Domínio : (só em: `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titular_valor_mobiliario`) | — | todo |
| `Quantidade_Pessoa_Juridica` | `Quantidade_Pessoa_Juridica` | inteiro / texto | Domínio : (só em: `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titular_valor_mobiliario`) | — | todo |
| `Quantidade_Investidor_Institucional` | `Quantidade_Investidor_Institucional` | inteiro / texto | Domínio : (só em: `fre_cia_aberta_outro_valor_mobiliario`) | — | todo |
| `Saldo_Devedor` | `Saldo_Devedor` | decimal / texto | Domínio : (só em: `fre_cia_aberta_outro_valor_mobiliario`, `fre_cia_aberta_titulo_exterior`) | — | todo |
| `Caracteristicas_Valores_Mobiliarios_Divida` | `Caracteristicas_Valores_Mobiliarios_Divida` | texto | Domínio : (só em: `fre_cia_aberta_outro_valor_mobiliario`) | — | todo |
| `ID_Sociedade` | `ID_Sociedade` | inteiro | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`, `fre_cia_aberta_participacao_sociedade_valorizacao_acao`) | código ou número de identificação (sem unidade) | todo |
| `Razao_Social` | `Razao_Social` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `CNPJ` | `CNPJ` | texto | Cadastro Nacional de Pessoas Jurídicas (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Tipo_Sociedade` | `Tipo_Sociedade` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Descricao_Atividades` | `Descricao_Atividades` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Pais_Sede` | `Pais_Sede` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `UF_Sede` | `UF_Sede` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Municipio_Sede` | `Municipio_Sede` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Participacao_Emissor` | `Participacao_Emissor` | decimal | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | ver a descrição | todo |
| `Possui_Registro_CVM` | `Possui_Registro_CVM` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Codigo_CVM` | `Codigo_CVM` | texto | Código CVM (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Razao_Aquisicao_Manutencao` | `Razao_Aquisicao_Manutencao` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Data_Valor_Mercado` | `Data_Valor_Mercado` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Data_Valor_Contabil` | `Data_Valor_Contabil` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Valor_Mercado` | `Valor_Mercado` | decimal / texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Valor_Contabil` | `Valor_Contabil` | decimal / texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade`) | — | todo |
| `Data_Encerramento` | `Data_Encerramento` | texto | Domínio : (só em: `fre_cia_aberta_participacao_sociedade_valorizacao_acao`) | — | 2010 a 2022 |
| `Variacao_Percentual_Valor_Contabil` | `Variacao_Percentual_Valor_Contabil` | decimal | Domínio : (só em: `fre_cia_aberta_participacao_sociedade_valorizacao_acao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Variacao_Percentual_Valor_Mercado` | `Variacao_Percentual_Valor_Mercado` | decimal | Domínio : (só em: `fre_cia_aberta_participacao_sociedade_valorizacao_acao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Valor_Montante_Dividendos_Recebidos` | `Valor_Montante_Dividendos_Recebidos` | decimal | Domínio : (só em: `fre_cia_aberta_participacao_sociedade_valorizacao_acao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `ID_Plano_Recompra` | `ID_Plano_Recompra` | inteiro | Domínio : (só em: `fre_cia_aberta_plano_recompra`, `fre_cia_aberta_plano_recompra_classe_acao`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Data_Inicio_Recompra` | `Data_Inicio_Recompra` | texto | Domínio : (só em: `fre_cia_aberta_plano_recompra`) | — | 2010 a 2022 |
| `Data_Fim_Recompra` | `Data_Fim_Recompra` | texto | Domínio : (só em: `fre_cia_aberta_plano_recompra`) | — | 2010 a 2022 |
| `Valor_Reserva_Disponivel_Recompra` | `Valor_Reserva_Disponivel_Recompra` | decimal | Domínio : (só em: `fre_cia_aberta_plano_recompra`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Outras_Caracteristicas_Importantes` | `Outras_Caracteristicas_Importantes` | texto | Domínio : (só em: `fre_cia_aberta_plano_recompra`) | — | 2010 a 2022 |
| `Quantidade_Adquirida` | `Quantidade_Adquirida` | inteiro | Domínio : (só em: `fre_cia_aberta_plano_recompra_classe_acao`, `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | quantidade | 2010 a 2022 |
| `Escala_Cotacao` | `Escala_Cotacao` | texto | Domínio : (só em: `fre_cia_aberta_plano_recompra_classe_acao`, `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`, `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio`, `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Quantidade_Prevista` | `Quantidade_Prevista` | inteiro | Domínio : (só em: `fre_cia_aberta_plano_recompra_classe_acao`) | quantidade | 2010 a 2022 |
| `Valor_Preco_Medio` | `Valor_Preco_Medio` | decimal | Domínio : (só em: `fre_cia_aberta_plano_recompra_classe_acao`, `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Percentual_Previsto` | `Percentual_Previsto` | decimal | Domínio : (só em: `fre_cia_aberta_plano_recompra_classe_acao`) | ver a descrição | 2010 a 2022 |
| `Percentual_Adquirido` | `Percentual_Adquirido` | decimal | Domínio : (só em: `fre_cia_aberta_plano_recompra_classe_acao`) | ver a descrição | 2010 a 2022 |
| `ID_Politica` | `ID_Politica` | inteiro | Domínio : (só em: `fre_cia_aberta_politica_negociacao`, `fre_cia_aberta_politica_negociacao_cargo`) | código ou número de identificação (sem unidade) | 2010 a 2022 |
| `Orgao_Aprovacao` | `Orgao_Aprovacao` | texto | Domínio : (só em: `fre_cia_aberta_politica_negociacao`) | — | 2010 a 2022 |
| `Principais_Caracteristicas` | `Principais_Caracteristicas` | texto | Domínio : (só em: `fre_cia_aberta_politica_negociacao`) | — | 2010 a 2022 |
| `Vedacao_Procedimentos_Fiscalizacao` | `Vedacao_Procedimentos_Fiscalizacao` | texto | Domínio : (só em: `fre_cia_aberta_politica_negociacao`) | — | 2010 a 2022 |
| `Cargo_Pessoa_Vinculada` | `Cargo_Pessoa_Vinculada` | texto | Domínio : (só em: `fre_cia_aberta_politica_negociacao_cargo`) | — | 2010 a 2022 |
| `ID_Acionista` | `ID_Acionista` | inteiro | Identificador único do registro de acionista (só em: `fre_cia_aberta_posicao_acionaria`, `fre_cia_aberta_posicao_acionaria_classe_acao`) | código ou número de identificação (sem unidade) | todo |
| `Acionista` | `Acionista` | texto | Nome do acionista (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Tipo_Pessoa_Acionista` | `Tipo_Pessoa_Acionista` | texto | Tipo de pessoa do acionista (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `CPF_CNPJ_Acionista` | `CPF_CNPJ_Acionista` | texto | CPF/CNPJ do acionista (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `ID_Acionista_Relacionado` | `ID_Acionista_Relacionado` | inteiro | Identificador único do acionista relacionado na hierarquia de controle (só em: `fre_cia_aberta_posicao_acionaria`) | código ou número de identificação (sem unidade) | todo |
| `Acionista_Relacionado` | `Acionista_Relacionado` | texto | Nome do acionista relacionado na hierarquia de controle (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Tipo_Pessoa_Acionista_Relacionado` | `Tipo_Pessoa_Acionista_Relacionado` | texto | Tipo de pessoa do acionista relacionado na hierarquia de controle (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `CPF_CNPJ_Acionista_Relacionado` | `CPF_CNPJ_Acionista_Relacionado` | texto | CPF/CNPJ do acionista relacionado na hierarquia de controle (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Quantidade_Acao_Ordinaria_Circulacao` | `Quantidade_Acao_Ordinaria_Circulacao` | inteiro | Quantidade de ações ordinárias em circulação (só em: `fre_cia_aberta_posicao_acionaria`) | quantidade | todo |
| `Percentual_Acao_Ordinaria_Circulacao` | `Percentual_Acao_Ordinaria_Circulacao` | decimal | Percentual de ações ordinárias em circulação (só em: `fre_cia_aberta_posicao_acionaria`) | % | todo |
| `Quantidade_Acao_Preferencial_Circulacao` | `Quantidade_Acao_Preferencial_Circulacao` | inteiro | Quantidade de ações preferenciais em circulação (só em: `fre_cia_aberta_posicao_acionaria`) | quantidade | todo |
| `Percentual_Acao_Preferencial_Circulacao` | `Percentual_Acao_Preferencial_Circulacao` | decimal | Percentual de ações preferenciais em circulação (só em: `fre_cia_aberta_posicao_acionaria`) | % | todo |
| `Nacionalidade` | `Nacionalidade` | texto | Nacionalidade (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Residente_Exterior` | `Residente_Exterior` | texto | Indica se o acionista é residente no exterior (só em: `fre_cia_aberta_posicao_acionaria`) | S/N | todo |
| `Representante_Legal` | `Representante_Legal` | texto | Nome do representante legal (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Tipo_Pessoa_Representante_Legal` | `Tipo_Pessoa_Representante_Legal` | texto | Tipo de pessoa do representante legal (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `CPF_CNPJ_Representante_legal` | `CPF_CNPJ_Representante_legal` | texto | CPF/CNPJ do representante legal (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Data_Composicao_Capital_Social` | `Data_Composicao_Capital_Social` | texto | Data de composição do capital social (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Data_Ultima_Alteracao` | `Data_Ultima_Alteracao` | texto | Data da última alteração (só em: `fre_cia_aberta_posicao_acionaria`) | — | todo |
| `Acionista_Controlador` | `Acionista_Controlador` | texto | Indica se acionista é controlador (só em: `fre_cia_aberta_posicao_acionaria`) | S/N | todo |
| `Participante_Acordo_Acionistas` | `Participante_Acordo_Acionistas` | texto | Indica se acionista participa do acordo de acionistas (só em: `fre_cia_aberta_posicao_acionaria`) | S/N | todo |
| `Percentual_Acoes` | `Percentual_Acoes` | decimal | Domínio : (só em: `fre_cia_aberta_posicao_acionaria_classe_acao`) | ver a descrição | todo |
| `Nome_Administrador` | `Nome_Administrador` | texto | Nome do administrador (só em: `fre_cia_aberta_relacao_familiar`, `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `CPF_Administrador` | `CPF_Administrador` | texto | CPF do administrador (só em: `fre_cia_aberta_relacao_familiar`, `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `Nome_Emissor` | `Nome_Emissor` | texto | Nome do Emissor (só em: `fre_cia_aberta_relacao_familiar`) | — | todo |
| `CNPJ_Emissor` | `CNPJ_Emissor` | texto | CNPJ do emissor (só em: `fre_cia_aberta_relacao_familiar`) | — | todo |
| `Cargo_Administrador` | `Cargo_Administrador` | texto | Cargo do administrador (só em: `fre_cia_aberta_relacao_familiar`, `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `Nome_Pessoa_Relacionada` | `Nome_Pessoa_Relacionada` | texto | Nome da pessoa relacionada (só em: `fre_cia_aberta_relacao_familiar`, `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `CPF_Pessoa_Relacionada` | `CPF_Pessoa_Relacionada` | texto | CPF da pessoa relacionada (só em: `fre_cia_aberta_relacao_familiar`) | — | todo |
| `Nome_Emissor_Pessoa_Relacionada` | `Nome_Emissor_Pessoa_Relacionada` | texto | Nome do emissor (Pessoa Relacionada) (só em: `fre_cia_aberta_relacao_familiar`) | — | todo |
| `CNPJ_Emissor_Pessoa_Relacionada` | `CNPJ_Emissor_Pessoa_Relacionada` | texto | Nome do emissor (Pessoa Relacionada) (só em: `fre_cia_aberta_relacao_familiar`) | — | todo |
| `Cargo_Pessoa_Relacionada` | `Cargo_Pessoa_Relacionada` | texto | Cargo da pessoa relacionada (só em: `fre_cia_aberta_relacao_familiar`, `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `Tipo_Parentesco` | `Tipo_Parentesco` | texto | Tipo de parentesco (só em: `fre_cia_aberta_relacao_familiar`) | — | todo |
| `Tipo_Pessoa_Relacionada` | `Tipo_Pessoa_Relacionada` | texto | Tipo de Pessoa Relacionada (só em: `fre_cia_aberta_relacao_subordinacao`) | PF/PJ | todo |
| `Documento_Pessoa_Relacionada` | `Documento_Pessoa_Relacionada` | texto | CPF/CNPJ da Pessoa Relacionada (só em: `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `Categoria_Pessoa_Relacionada` | `Categoria_Pessoa_Relacionada` | texto | Tipo ou categoria da Pessoa Relacionada (só em: `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `Tipo_Relacao` | `Tipo_Relacao` | texto | Tipo de Relação (só em: `fre_cia_aberta_relacao_subordinacao`) | — | todo |
| `Numero_Membros` | `Numero_Membros` | decimal | Número de membros (só em: `fre_cia_aberta_remuneracao_maxima_minima_media`, `fre_cia_aberta_remuneracao_total_orgao`) | quantidade | todo |
| `Numero_Membros_Remunerados` | `Numero_Membros_Remunerados` | decimal / texto | Número de membros remunerados (só em: `fre_cia_aberta_remuneracao_maxima_minima_media`, `fre_cia_aberta_remuneracao_total_orgao`) | — | todo |
| `Valor_Maior_Remuneracao` | `Valor_Maior_Remuneracao` | decimal | Valor da maior remuneração individual (só em: `fre_cia_aberta_remuneracao_maxima_minima_media`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Valor_Menor_Remuneracao` | `Valor_Menor_Remuneracao` | decimal | Valor da menor remuneração individual (só em: `fre_cia_aberta_remuneracao_maxima_minima_media`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Valor_Medio_Remuneracao` | `Valor_Medio_Remuneracao` | decimal | Valor médio de remuneração individual (só em: `fre_cia_aberta_remuneracao_maxima_minima_media`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Total_Remuneracao` | `Total_Remuneracao` | decimal | Total da remuneração (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Total_Remuneracao_Orgao` | `Total_Remuneracao_Orgao` | decimal | Total da remuneração do órgão (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Salario` | `Salario` | decimal | Salário (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Beneficios_Diretos_Indiretos` | `Beneficios_Diretos_Indiretos` | decimal | Benefícios diretos e indiretos (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Participacoes_Comites` | `Participacoes_Comites` | decimal | Participações em comitês (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Outros_Valores_Fixos` | `Outros_Valores_Fixos` | decimal | Outros valores fixos (só em: `fre_cia_aberta_remuneracao_total_orgao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Descricao_Outros_Remuneracoes_Fixas` | `Descricao_Outros_Remuneracoes_Fixas` | texto | Descrição de outras remunerações fixas (só em: `fre_cia_aberta_remuneracao_total_orgao`) | — | todo |
| `Bonus` | `Bonus` | decimal | Bônus (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Participacao_Resultados` | `Participacao_Resultados` | decimal | Participação de resultados (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Participacao_Reunioes` | `Participacao_Reunioes` | decimal | Participação em reuniões (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Outros_Valores_Variaveis` | `Outros_Valores_Variaveis` | decimal | Outros valores variáveis (só em: `fre_cia_aberta_remuneracao_total_orgao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Comissoes` | `Comissoes` | decimal | Comissões (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Descricao_Outros_Remuneracoes_Variaveis` | `Descricao_Outros_Remuneracoes_Variaveis` | texto | Descrição de outras remunerações variáveis (só em: `fre_cia_aberta_remuneracao_total_orgao`) | — | todo |
| `Pos_emprego` | `Pos_emprego` | decimal | Pós-Emprego (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Cessacao_Cargo` | `Cessacao_Cargo` | decimal | Cessação do cargo (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Baseada_Acoes` | `Baseada_Acoes` | decimal | Baseada em ações (só em: `fre_cia_aberta_remuneracao_total_orgao`) | ver a descrição | todo |
| `Nome_Responsavel` | `Nome_Responsavel` | texto | Domínio : (só em: `fre_cia_aberta_responsavel`) | — | todo |
| `Cargo_Responsavel` | `Cargo_Responsavel` | texto | Domínio : (só em: `fre_cia_aberta_responsavel`) | — | todo |
| `Parte_Relacionada` | `Parte_Relacionada` | texto | Parte Relacionada (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Tipo_Pessoa` | `Tipo_Pessoa` | texto | Tipo de pessoa (só em: `fre_cia_aberta_transacao_parte_relacionada`) | PF/PJ | todo |
| `Documento_Parte_Relacionada` | `Documento_Parte_Relacionada` | texto | Documento da Parte Relacionada (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Relacao_Emissor` | `Relacao_Emissor` | texto | Relação com o emissor (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Data_Transacao` | `Data_Transacao` | texto | Data da transação (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Objeto_Contrato` | `Objeto_Contrato` | texto | Objeto do contrato (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Montante_Envolvido` | `Montante_Envolvido` | decimal | Montante envolvido (só em: `fre_cia_aberta_transacao_parte_relacionada`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | todo |
| `Saldo_Existente` | `Saldo_Existente` | texto | Saldo existente (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Montante_Interesse_Parte_Relacionada` | `Montante_Interesse_Parte_Relacionada` | texto | Montante correspondente ao interesse da parte relacionada no negócio (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Garantia_Seguro` | `Garantia_Seguro` | texto | Garantias e seguros (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Duracao_Transacao` | `Duracao_Transacao` | texto | Duração da transação (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Emprestimo_Divida` | `Emprestimo_Divida` | texto | Indica se a transação é empréstimo ou outro tipo de dívida (só em: `fre_cia_aberta_transacao_parte_relacionada`) | S/N | todo |
| `Rescisao` | `Rescisao` | texto | Rescisão (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Natureza_Razao_Operacao` | `Natureza_Razao_Operacao` | texto | Natureza e razão para operação (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Taxa_Juros` | `Taxa_Juros` | decimal / texto | Taxa de juros (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Posicao_Contratual_Emissor` | `Posicao_Contratual_Emissor` | texto | Indica se o emissor é credor ou devedor (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Especificacao_Posicao_Contratual_Emissor` | `Especificacao_Posicao_Contratual_Emissor` | texto | Especificação quando a posição contratual do emissor for "Outra" (só em: `fre_cia_aberta_transacao_parte_relacionada`) | — | todo |
| `Descricao_Valor_Mobiliario` | `Descricao_Valor_Mobiliario` | texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`, `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio`) | — | 2010 a 2022 |
| `Quantidade_Inicial` | `Quantidade_Inicial` | inteiro | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | quantidade | 2010 a 2022 |
| `Valor_Total_Inicial` | `Valor_Total_Inicial` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Valor_Preco_Medio_Inicial` | `Valor_Preco_Medio_Inicial` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Valor_Total_Adquirido` | `Valor_Total_Adquirido` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Valor_Preco_Medio_Adquirido` | `Valor_Preco_Medio_Adquirido` | decimal | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Quantidade_Alienada` | `Quantidade_Alienada` | inteiro | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | quantidade | 2010 a 2022 |
| `Valor_Total_Alienado` | `Valor_Total_Alienado` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Valor_Preco_Medio_Alienado` | `Valor_Preco_Medio_Alienado` | decimal | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Quantidade_Cancelada` | `Quantidade_Cancelada` | inteiro | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | quantidade | 2010 a 2022 |
| `Valor_Total_Cancelado` | `Valor_Total_Cancelado` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Valor_Preco_Medio_Cancelado` | `Valor_Preco_Medio_Cancelado` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Quantidade_Final` | `Quantidade_Final` | inteiro | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | quantidade | 2010 a 2022 |
| `Valor_Total_Final` | `Valor_Total_Final` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Valor_Preco_Medio_Final` | `Valor_Preco_Medio_Final` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Percentual_Relacao_Valores_Mobiliarios_Circulacao` | `Percentual_Relacao_Valores_Mobiliarios_Circulacao` | decimal / texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_movimentacao`) | — | 2010 a 2022 |
| `Quantidade_Valor_Mobiliario` | `Quantidade_Valor_Mobiliario` | inteiro | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio`) | quantidade | 2010 a 2014 |
| `Data_Aquisicao` | `Data_Aquisicao` | texto | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio`) | — | 2010 a 2014 |
| `Percentual_Circulacao` | `Percentual_Circulacao` | decimal | Domínio : (só em: `fre_cia_aberta_valor_mobiliario_tesouraria_ultimo_exercicio`) | ver a descrição | 2010 a 2014 |
| `Data_Fim_Trimestre` | `Data_Fim_Trimestre` | texto | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Mercado_Valor_Mobiliario` | `Mercado_Valor_Mobiliario` | texto | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Entidade_Administradora_Mercado` | `Entidade_Administradora_Mercado` | texto | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Descricao_Outro_Valor_Mobiliario` | `Descricao_Outro_Valor_Mobiliario` | texto | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Valor_Volume_Negociado` | `Valor_Volume_Negociado` | decimal | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Valor_Maior_Cotacao` | `Valor_Maior_Cotacao` | decimal | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Valor_Menor_Cotacao` | `Valor_Menor_Cotacao` | decimal | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2010 a 2022 |
| `Valor_Cotacao_Media` | `Valor_Cotacao_Media` | decimal / texto | Domínio : (só em: `fre_cia_aberta_volume_valor_mobiliario`) | — | 2010 a 2022 |
| `Quantidade_Investidor` | `Quantidade_Investidor` | inteiro | Domínio : (só em: `fre_cia_aberta_titular_valor_mobiliario`) | quantidade | 2018 a 2026 |
| `Valor_Nominal` | `Valor_Nominal` | decimal | Domínio : (só em: `fre_cia_aberta_titulo_exterior`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2018 a 2026 |
| `Condicao_Conversibilidade` | `Condicao_Conversibilidade` | texto | Domínio : (só em: `fre_cia_aberta_titulo_exterior`) | — | 2018 a 2026 |
| `Possibilidade_Resgate` | `Possibilidade_Resgate` | texto | Domínio : (só em: `fre_cia_aberta_titulo_exterior`) | — | 2018 a 2026 |
| `Hipotese_Calculo_Resgate` | `Hipotese_Calculo_Resgate` | texto | Domínio : (só em: `fre_cia_aberta_titulo_exterior`) | — | 2018 a 2026 |
| `Caracteristicas_Divida` | `Caracteristicas_Divida` | texto | Domínio : (só em: `fre_cia_aberta_titulo_exterior`) | — | 2018 a 2026 |
| `Outras_Caracteristicas` | `Outras_Caracteristicas` | texto | Domínio : (só em: `fre_cia_aberta_titulo_exterior`) | — | 2018 a 2026 |
| `Pais_Negociacao` | `Pais_Negociacao` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Mercado` | `Mercado` | texto | Nome do Mercado (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Administradora` | `Administradora` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Data_Inicio_Listagem` | `Data_Inicio_Listagem` | texto | Data de início de listagem (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Percentual` | `Percentual` | decimal | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | ver a descrição | 2022 a 2026 |
| `Descricao_Segmento` | `Descricao_Segmento` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Descricao_Proporcao_Certificado` | `Descricao_Proporcao_Certificado` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Descricao_Banco_Depositario` | `Descricao_Banco_Depositario` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Descricao_Instituicao_Custodiante` | `Descricao_Instituicao_Custodiante` | texto | Domínio : (só em: `fre_cia_aberta_mercado_estrangeiro`) | — | 2022 a 2026 |
| `Quantidade_Total_Membros` | `Quantidade_Total_Membros` | decimal | Domínio : (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_remuneracao_acao`, `fre_cia_aberta_remuneracao_variavel`) | quantidade | 2025 a 2026 |
| `Quantidade_Membros_Remunerados` | `Quantidade_Membros_Remunerados` | decimal | Domínio : (só em: `fre_cia_aberta_acao_entregue`, `fre_cia_aberta_remuneracao_acao`, `fre_cia_aberta_remuneracao_variavel`) | quantidade | 2025 a 2026 |
| `Preco_Medio_Ponderado_Aquisicao` | `Preco_Medio_Ponderado_Aquisicao` | decimal | Domínio : (só em: `fre_cia_aberta_acao_entregue`) | ver a descrição | 2025 a 2026 |
| `Preco_Medio_Ponderado_Mercado` | `Preco_Medio_Ponderado_Mercado` | decimal | Domínio : (só em: `fre_cia_aberta_acao_entregue`) | ver a descrição | 2025 a 2026 |
| `Valor_Diferenca_Aquisicao_Mercado` | `Valor_Diferenca_Aquisicao_Mercado` | decimal | Domínio : (só em: `fre_cia_aberta_acao_entregue`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Quantidade_Feminino` | `Quantidade_Feminino` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_empregado_local_declaracao_genero`, `fre_cia_aberta_empregado_posicao_declaracao_genero`) | quantidade | 2025 a 2026 |
| `Quantidade_Masculino` | `Quantidade_Masculino` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_empregado_local_declaracao_genero`, `fre_cia_aberta_empregado_posicao_declaracao_genero`) | quantidade | 2025 a 2026 |
| `Quantidade_Nao_Binario` | `Quantidade_Nao_Binario` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_empregado_local_declaracao_genero`, `fre_cia_aberta_empregado_posicao_declaracao_genero`) | quantidade | 2025 a 2026 |
| `Quantidade_Outros` | `Quantidade_Outros` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_empregado_local_declaracao_genero`, `fre_cia_aberta_empregado_local_declaracao_raca` e mais 2) | quantidade | 2025 a 2026 |
| `Quantidade_Sem_Resposta` | `Quantidade_Sem_Resposta` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_pcd`, `fre_cia_aberta_empregado_local_declaracao_genero` e mais 4) | quantidade | 2025 a 2026 |
| `Nao_Aplicavel` | `Nao_Aplicavel` | texto | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_genero`, `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_administrador_pcd`) | — | 2025 a 2026 |
| `Quantidade_Amarelo` | `Quantidade_Amarelo` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_empregado_local_declaracao_raca`, `fre_cia_aberta_empregado_posicao_declaracao_raca`) | quantidade | 2025 a 2026 |
| `Quantidade_Branco` | `Quantidade_Branco` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_empregado_local_declaracao_raca`, `fre_cia_aberta_empregado_posicao_declaracao_raca`) | quantidade | 2025 a 2026 |
| `Quantidade_Preto` | `Quantidade_Preto` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_empregado_local_declaracao_raca`, `fre_cia_aberta_empregado_posicao_declaracao_raca`) | quantidade | 2025 a 2026 |
| `Quantidade_Pardo` | `Quantidade_Pardo` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_empregado_local_declaracao_raca`, `fre_cia_aberta_empregado_posicao_declaracao_raca`) | quantidade | 2025 a 2026 |
| `Quantidade_Indigena` | `Quantidade_Indigena` | inteiro | Domínio : (só em: `fre_cia_aberta_administrador_declaracao_raca`, `fre_cia_aberta_empregado_local_declaracao_raca`, `fre_cia_aberta_empregado_posicao_declaracao_raca`) | quantidade | 2025 a 2026 |
| `Quantidade_PCD` | `Quantidade_PCD` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_administrador_pcd`, `fre_cia_aberta_empregado_pcd`) | quantidade | 2025 a 2026 |
| `Quantidade_Nao_PCD` | `Quantidade_Nao_PCD` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_administrador_pcd`, `fre_cia_aberta_empregado_pcd`) | quantidade | 2025 a 2026 |
| `Local` | `Local` | texto | Domínio : (só em: `fre_cia_aberta_empregado_local_declaracao_genero`, `fre_cia_aberta_empregado_local_declaracao_raca`, `fre_cia_aberta_empregado_local_faixa_etaria`) | — | 2025 a 2026 |
| `Quantidade_Ate30Anos` | `Quantidade_Ate30Anos` | inteiro | Domínio : (só em: `fre_cia_aberta_empregado_local_faixa_etaria`, `fre_cia_aberta_empregado_posicao_faixa_etaria`) | quantidade | 2025 a 2026 |
| `Quantidade_30a50Anos` | `Quantidade_30a50Anos` | inteiro | Domínio : (só em: `fre_cia_aberta_empregado_local_faixa_etaria`, `fre_cia_aberta_empregado_posicao_faixa_etaria`) | quantidade | 2025 a 2026 |
| `Quantidade_Acima50Anos` | `Quantidade_Acima50Anos` | inteiro | Domínio : (só em: `fre_cia_aberta_empregado_local_faixa_etaria`, `fre_cia_aberta_empregado_posicao_faixa_etaria`) | quantidade | 2025 a 2026 |
| `Codigo_Posicao` | `Codigo_Posicao` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_pcd`) | código ou número de identificação (sem unidade) | 2025 a 2026 |
| `Posicao` | `Posicao` | texto | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_pcd`, `fre_cia_aberta_empregado_posicao_declaracao_genero`, `fre_cia_aberta_empregado_posicao_declaracao_raca`, `fre_cia_aberta_empregado_posicao_faixa_etaria` e mais 1) | — | 2025 a 2026 |
| `Quantidade_Norte` | `Quantidade_Norte` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_posicao_local`) | quantidade | 2025 a 2026 |
| `Quantidade_Nordeste` | `Quantidade_Nordeste` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_posicao_local`) | quantidade | 2025 a 2026 |
| `Quantidade_Centro_Oeste` | `Quantidade_Centro_Oeste` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_posicao_local`) | quantidade | 2025 a 2026 |
| `Quantidade_Sudeste` | `Quantidade_Sudeste` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_posicao_local`) | quantidade | 2025 a 2026 |
| `Quantidade_Sul` | `Quantidade_Sul` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_posicao_local`) | quantidade | 2025 a 2026 |
| `Quantidade_Exterior` | `Quantidade_Exterior` | inteiro | Sem descrição no dicionário oficial. (só em: `fre_cia_aberta_empregado_posicao_local`) | quantidade | 2025 a 2026 |
| `Diluicao_Potencial` | `Diluicao_Potencial` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_acao`) | ver a descrição | 2025 a 2026 |
| `Preco_Medio_Ponderado_Opcoes_Em_Aberto` | `Preco_Medio_Ponderado_Opcoes_Em_Aberto` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_acao`) | ver a descrição | 2025 a 2026 |
| `Preco_Medio_Ponderado_Opcoes_Perdidas` | `Preco_Medio_Ponderado_Opcoes_Perdidas` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_acao`) | ver a descrição | 2025 a 2026 |
| `Preco_Medio_Ponderado_Opcoes_Exercidas` | `Preco_Medio_Ponderado_Opcoes_Exercidas` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_acao`) | ver a descrição | 2025 a 2026 |
| `Bonus_Valor_Minimo` | `Bonus_Valor_Minimo` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Bonus_Valor_Maximo` | `Bonus_Valor_Maximo` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Bonus_Valor_Metas_Atingidas` | `Bonus_Valor_Metas_Atingidas` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Bonus_Valor_Efetivo` | `Bonus_Valor_Efetivo` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Participacao_Valor_Minimo` | `Participacao_Valor_Minimo` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Participacao_Valor_Maximo` | `Participacao_Valor_Maximo` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Participacao_Valor_Metas_Atingidas` | `Participacao_Valor_Metas_Atingidas` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `Participacao_Valor_Efetivo` | `Participacao_Valor_Efetivo` | decimal | Domínio : (só em: `fre_cia_aberta_remuneracao_variavel`) | moeda (ver ESCALA_MOEDA, quando houver; senão R$) | 2025 a 2026 |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/cia-fre`, particionado por `ano`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA`).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- O FRE é reentregue com frequência: o mesmo `CNPJ_Companhia` pode ter várias versões no mesmo ano (`Versao`); use a maior para o retrato mais recente.
- O formulário tem muitas tabelas que mudam de composição entre anos; a lista de tabelas da seção Conteúdo é a dos arquivos convertidos nesta página.
- **Dados de contato e identificação.** Há colunas de endereço, telefone, e-mail ou CPF (`CPF`, ...); parte pode ser de pessoa física. O fetcher e o lake preservam o que a fonte publica.
- **CEP, DDD e telefones viram número.** O conversor infere o tipo de cada CSV e lê `CEP`, `DDD_Telefone` como inteiro, o que descarta zeros à esquerda (CEP de 8 dígitos começado por zero, por exemplo); reconstrua o texto com `lpad` quando precisar do código.
- **Tipo inferido varia entre arquivos.** 22 coluna(s) (`Numero_Mandatos_Consecutivos`, ...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Linhas por ano nos arquivos convertidos.

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(*) AS linhas
    FROM read_parquet('lake/cvm/cia-fre/**/*.parquet', hive_partitioning = true, union_by_name = true, filename = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/
