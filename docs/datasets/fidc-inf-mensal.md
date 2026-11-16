---
dataset:
  id: fidc-inf-mensal
  fonte: cvm
  titulo: "FIDC: Documentos: Informe Mensal (CVM)"
  resumo: "Informe mensal dos Fundos de Investimento em Direitos Creditórios (FIDC): carteira por segmento e por prazo, inadimplência, cotistas, cotas, rentabilidade, liquidez e garantias, em 18 tabelas que seguem os itens do Anexo A da Instrução CVM 489."
  orgao: Comissão de Valores Mobiliários (CVM)
  pagina_oficial: https://dados.cvm.gov.br/dataset/fidc-doc-inf_mensal
  licenca: "Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fidc-doc-inf_mensal"
  periodicidade: "mensal (um arquivo por mês); o portal declara atualização semanal para os últimos doze meses"
  cobertura: {inicio: 2025-01, fim: em-curso}
  unidade: "o informe mensal de uma classe de FIDC; nas tabelas `tab_viii`, `tab_x_1` a `tab_x_4` e `tab_x_6`, uma linha por classe e série (ou sequencial)"
  granularidade: {espacial: "nacional (sem recorte geográfico)", temporal: "mensal (competência, `DT_COMPTC`)"}
  formato_bruto: "ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM"
  lake: {estado: convertido, particoes: [ano, mes], chave: [], colunas: 388}
  unidades_de_medida:
    PRAZO_CONVERSAO_COTA: "dias"
    PRAZO_PAGTO_RESGATE: "dias"
    TAB_I_VL_ATIVO: "moeda (R$)"
    TAB_I1_VL_DISP: "moeda (R$)"
    TAB_I2_VL_CARTEIRA: "moeda (R$)"
    TAB_I2A_VL_DIRCRED_RISCO: "moeda (R$)"
    TAB_I2A1_VL_CRED_VENC_AD: "moeda (R$)"
    TAB_I2A2_VL_CRED_VENC_INAD: "moeda (R$)"
    TAB_I2A21_VL_TOTAL_PARCELA_INAD: "moeda (R$)"
    TAB_I2A3_VL_CRED_INAD: "moeda (R$)"
    TAB_I2A4_VL_CRED_DIRCRED_PERFM: "moeda (R$)"
    TAB_I2A5_VL_CRED_VENCIDO_PENDENTE: "moeda (R$)"
    TAB_I2A6_VL_CRED_EMP_RECUP: "moeda (R$)"
    TAB_I2A7_VL_CRED_RECEITA_PUBLICA: "moeda (R$)"
    TAB_I2A8_VL_CRED_ACAO_JUDIC: "moeda (R$)"
    TAB_I2A9_VL_CRED_FATOR_RISCO: "moeda (R$)"
    TAB_I2A11_VL_REDUCAO_RECUP: "moeda (R$)"
    TAB_I2A12_PR_CEDENTE_1: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_2: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_3: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_4: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_5: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_6: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_7: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_8: "percentual (%)"
    TAB_I2A12_PR_CEDENTE_9: "percentual (%)"
    TAB_I2B_VL_DIRCRED_SEM_RISCO: "moeda (R$)"
    TAB_I2B1_VL_CRED_VENC_AD: "moeda (R$)"
    TAB_I2B2_VL_CRED_VENC_INAD: "moeda (R$)"
    TAB_I2B21_VL_TOTAL_PARCELA_INAD: "moeda (R$)"
    TAB_I2B3_VL_CRED_INAD: "moeda (R$)"
    TAB_I2B4_VL_CRED_DIRCRED_PERFM: "moeda (R$)"
    TAB_I2B5_VL_CRED_VENCIDO_PENDENTE: "moeda (R$)"
    TAB_I2B6_VL_CRED_EMP_RECUP: "moeda (R$)"
    TAB_I2B7_VL_CRED_RECEITA_PUBLICA: "moeda (R$)"
    TAB_I2B8_VL_CRED_ACAO_JUDIC: "moeda (R$)"
    TAB_I2B9_VL_CRED_FATOR_RISCO: "moeda (R$)"
    TAB_I2B11_VL_REDUCAO_RECUP: "moeda (R$)"
    TAB_I2B12_PR_CEDENTE_1: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_2: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_3: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_4: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_5: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_6: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_7: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_8: "percentual (%)"
    TAB_I2B12_PR_CEDENTE_9: "percentual (%)"
    TAB_I2C_VL_VLMOB: "moeda (R$)"
    TAB_I2C1_VL_DEBENTURE: "moeda (R$)"
    TAB_I2C2_VL_CRI: "moeda (R$)"
    TAB_I2C3_VL_NP_COMERC: "moeda (R$)"
    TAB_I2C4_VL_LETRA_FINANC: "moeda (R$)"
    TAB_I2C5_VL_COTA_FIF: "moeda (R$)"
    TAB_I2C6_VL_OUTRO: "moeda (R$)"
    TAB_I2D_VL_TITPUB_FED: "moeda (R$)"
    TAB_I2E_VL_CDB: "moeda (R$)"
    TAB_I2F_VL_OPER_COMPROM: "moeda (R$)"
    TAB_I2G_VL_OUTRO_RF: "moeda (R$)"
    TAB_I2H_VL_COTA_FIDC: "moeda (R$)"
    TAB_I2J_VL_CONTRATO_FUTURO: "moeda (R$)"
    TAB_I2_DEBENTURE_CRI: "moeda (R$)"
    TAB_I2_COTA_FIDC: "moeda (R$)"
    TAB_I2_VL_OUTRO_ATIVO: "moeda (R$)"
    TAB_I3_VL_POSICAO_DERIV: "moeda (R$)"
    TAB_I3A_VL_MERCADO_TERMO: "moeda (R$)"
    TAB_I3B_VL_MERCADO_OPCAO: "moeda (R$)"
    TAB_I3C_VL_MERCADO_FUTURO: "moeda (R$)"
    TAB_I3D_VL_DIFER_SWAP: "moeda (R$)"
    TAB_I3E_VL_COBERTURA: "moeda (R$)"
    TAB_I3F_VL_DEPOSITO_MARGEM: "moeda (R$)"
    TAB_I4_VL_OUTRO_ATIVO: "moeda (R$)"
    TAB_I4A_VL_CPRAZO: "moeda (R$)"
    TAB_I4B_VL_LPRAZO: "moeda (R$)"
    TAB_II_VL_CARTEIRA: "moeda (R$)"
    TAB_II_A_VL_INDUST: "moeda (R$)"
    TAB_II_B_VL_IMOBIL: "moeda (R$)"
    TAB_II_C_VL_COMERC: "moeda (R$)"
    TAB_II_C1_VL_COMERC: "moeda (R$)"
    TAB_II_C2_VL_VAREJO: "moeda (R$)"
    TAB_II_C3_VL_ARREND: "moeda (R$)"
    TAB_II_D_VL_SERV: "moeda (R$)"
    TAB_II_D1_VL_SERV: "moeda (R$)"
    TAB_II_D2_VL_SERV_PUBLICO: "moeda (R$)"
    TAB_II_D3_VL_SERV_EDUC: "moeda (R$)"
    TAB_II_D4_VL_ENTRET: "moeda (R$)"
    TAB_II_E_VL_AGRONEG: "moeda (R$)"
    TAB_II_F_VL_FINANC: "moeda (R$)"
    TAB_II_F1_VL_CRED_PESSOA: "moeda (R$)"
    TAB_II_F2_VL_CRED_PESSOA_CONSIG: "moeda (R$)"
    TAB_II_F3_VL_CRED_CORP: "moeda (R$)"
    TAB_II_F4_VL_MIDMARKET: "moeda (R$)"
    TAB_II_F5_VL_VEICULO: "moeda (R$)"
    TAB_II_F6_VL_IMOBIL_EMPRESA: "moeda (R$)"
    TAB_II_F7_VL_IMOBIL_RESID: "moeda (R$)"
    TAB_II_F8_VL_OUTRO: "moeda (R$)"
    TAB_II_G_VL_CREDITO: "moeda (R$)"
    TAB_II_H_VL_FACTOR: "moeda (R$)"
    TAB_II_H1_VL_PESSOA: "moeda (R$)"
    TAB_II_H2_VL_CORP: "moeda (R$)"
    TAB_II_I_VL_SETOR_PUBLICO: "moeda (R$)"
    TAB_II_I1_VL_PRECAT: "moeda (R$)"
    TAB_II_I2_VL_TRIBUT: "moeda (R$)"
    TAB_II_I3_VL_ROYALTIES: "moeda (R$)"
    TAB_II_I4_VL_OUTRO: "moeda (R$)"
    TAB_II_J_VL_JUDICIAL: "moeda (R$)"
    TAB_II_K_VL_MARCA: "moeda (R$)"
    TAB_III_VL_PASSIVO: "moeda (R$)"
    TAB_III_A_VL_PAGAR: "moeda (R$)"
    TAB_III_A1_VL_CPRAZO: "moeda (R$)"
    TAB_III_A2_VL_LPRAZO: "moeda (R$)"
    TAB_III_B_VL_POSICAO_DERIV: "moeda (R$)"
    TAB_III_B1_VL_TERMO: "moeda (R$)"
    TAB_III_B2_VL_OPCAO: "moeda (R$)"
    TAB_III_B3_VL_FUTURO: "moeda (R$)"
    TAB_III_B4_VL_SWAP_PAGAR: "moeda (R$)"
    TAB_IV_A_VL_PL: "moeda (R$)"
    TAB_IV_B_VL_PL_MEDIO: "moeda (R$)"
    TAB_IX_A1_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_A1_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_A1_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_A1_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_A1_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_A1_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_A2_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_A2_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_A2_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_A2_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_A2_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_A2_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_B1_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_B1_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_B1_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_B1_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_B1_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_B1_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_B2_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_B2_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_B2_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_B2_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_B2_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_B2_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_C1_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_C1_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_C1_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_C1_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_C1_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_C1_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_C2_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_C2_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_C2_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_C2_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_C2_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_C2_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_D1_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_D1_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_D1_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_D1_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_D1_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_D1_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_D2_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_D2_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_D2_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_D2_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_D2_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_D2_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_E1_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_E1_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_E1_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_E1_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_E1_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_E1_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_E2_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_E2_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_E2_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_E2_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_E2_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_E2_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_F1_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_F1_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_F1_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_F1_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_F1_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_F1_2_3_VENDA_MAX: "moeda (R$)"
    TAB_IX_F2_1_1_COMPRA_MIN: "moeda (R$)"
    TAB_IX_F2_1_2_COMPRA_MEDIA: "moeda (R$)"
    TAB_IX_F2_1_3_COMPRA_MAX: "moeda (R$)"
    TAB_IX_F2_2_1_VENDA_MIN: "moeda (R$)"
    TAB_IX_F2_2_2_VENDA_MEDIA: "moeda (R$)"
    TAB_IX_F2_2_3_VENDA_MAX: "moeda (R$)"
    TAB_V_A_VL_DIRCRED_PRAZO: "moeda (R$)"
    TAB_V_A1_VL_PRAZO_VENC_30: "moeda (R$)"
    TAB_V_A2_VL_PRAZO_VENC_60: "moeda (R$)"
    TAB_V_A3_VL_PRAZO_VENC_90: "moeda (R$)"
    TAB_V_A4_VL_PRAZO_VENC_120: "moeda (R$)"
    TAB_V_A5_VL_PRAZO_VENC_150: "moeda (R$)"
    TAB_V_A6_VL_PRAZO_VENC_180: "moeda (R$)"
    TAB_V_A7_VL_PRAZO_VENC_360: "moeda (R$)"
    TAB_V_A8_VL_PRAZO_VENC_720: "moeda (R$)"
    TAB_V_A9_VL_PRAZO_VENC_1080: "moeda (R$)"
    TAB_V_A10_VL_PRAZO_VENC_MAIOR_1080: "moeda (R$)"
    TAB_V_B_VL_DIRCRED_INAD: "moeda (R$)"
    TAB_V_B1_VL_INAD_30: "moeda (R$)"
    TAB_V_B2_VL_INAD_60: "moeda (R$)"
    TAB_V_B3_VL_INAD_90: "moeda (R$)"
    TAB_V_B4_VL_INAD_120: "moeda (R$)"
    TAB_V_B5_VL_INAD_150: "moeda (R$)"
    TAB_V_B6_VL_INAD_180: "moeda (R$)"
    TAB_V_B7_VL_INAD_360: "moeda (R$)"
    TAB_V_B8_VL_INAD_720: "moeda (R$)"
    TAB_V_B9_VL_INAD_1080: "moeda (R$)"
    TAB_V_B10_VL_INAD_MAIOR_1080: "moeda (R$)"
    TAB_V_C_VL_DIRCRED_ANTECIPADO: "moeda (R$)"
    TAB_V_C1_VL_ANTECIPADO_30: "moeda (R$)"
    TAB_V_C2_VL_ANTECIPADO_60: "moeda (R$)"
    TAB_V_C3_VL_ANTECIPADO_90: "moeda (R$)"
    TAB_V_C4_VL_ANTECIPADO_120: "moeda (R$)"
    TAB_V_C5_VL_ANTECIPADO_150: "moeda (R$)"
    TAB_V_C6_VL_ANTECIPADO_180: "moeda (R$)"
    TAB_V_C7_VL_ANTECIPADO_360: "moeda (R$)"
    TAB_V_C8_VL_ANTECIPADO_720: "moeda (R$)"
    TAB_V_C9_VL_ANTECIPADO_1080: "moeda (R$)"
    TAB_V_C10_VL_ANTECIPADO_MAIOR_1080: "moeda (R$)"
    TAB_VI_A_VL_DIRCRED_PRAZO: "moeda (R$)"
    TAB_VI_A1_VL_PRAZO_VENC_30: "moeda (R$)"
    TAB_VI_A2_VL_PRAZO_VENC_60: "moeda (R$)"
    TAB_VI_A3_VL_PRAZO_VENC_90: "moeda (R$)"
    TAB_VI_A4_VL_PRAZO_VENC_120: "moeda (R$)"
    TAB_VI_A5_VL_PRAZO_VENC_150: "moeda (R$)"
    TAB_VI_A6_VL_PRAZO_VENC_180: "moeda (R$)"
    TAB_VI_A7_VL_PRAZO_VENC_360: "moeda (R$)"
    TAB_VI_A8_VL_PRAZO_VENC_720: "moeda (R$)"
    TAB_VI_A9_VL_PRAZO_VENC_1080: "moeda (R$)"
    TAB_VI_A10_VL_PRAZO_VENC_MAIOR_1080: "moeda (R$)"
    TAB_VI_B_VL_DIRCRED_INAD: "moeda (R$)"
    TAB_VI_B1_VL_INAD_30: "moeda (R$)"
    TAB_VI_B2_VL_INAD_60: "moeda (R$)"
    TAB_VI_B3_VL_INAD_90: "moeda (R$)"
    TAB_VI_B4_VL_INAD_120: "moeda (R$)"
    TAB_VI_B5_VL_INAD_150: "moeda (R$)"
    TAB_VI_B6_VL_INAD_180: "moeda (R$)"
    TAB_VI_B7_VL_INAD_360: "moeda (R$)"
    TAB_VI_B8_VL_INAD_720: "moeda (R$)"
    TAB_VI_B9_VL_INAD_1080: "moeda (R$)"
    TAB_VI_B10_VL_INAD_MAIOR_1080: "moeda (R$)"
    TAB_VI_C_VL_DIRCRED_ANTECIPADO: "moeda (R$)"
    TAB_VI_C1_VL_ANTECIPADO_30: "moeda (R$)"
    TAB_VI_C2_VL_ANTECIPADO_60: "moeda (R$)"
    TAB_VI_C3_VL_ANTECIPADO_90: "moeda (R$)"
    TAB_VI_C4_VL_ANTECIPADO_120: "moeda (R$)"
    TAB_VI_C5_VL_ANTECIPADO_150: "moeda (R$)"
    TAB_VI_C6_VL_ANTECIPADO_180: "moeda (R$)"
    TAB_VI_C7_VL_ANTECIPADO_360: "moeda (R$)"
    TAB_VI_C8_VL_ANTECIPADO_720: "moeda (R$)"
    TAB_VI_C9_VL_ANTECIPADO_1080: "moeda (R$)"
    TAB_VI_C10_VL_ANTECIPADO_MAIOR_1080: "moeda (R$)"
    TAB_VII_A1_1_QT_DIRCRED_RISCO: "quantidade"
    TAB_VII_A1_2_VL_DIRCRED_RISCO: "moeda (R$)"
    TAB_VII_A2_1_QT_DIRCRED_SEM_RISCO: "quantidade"
    TAB_VII_A2_2_VL_DIRCRED_SEM_RISCO: "moeda (R$)"
    TAB_VII_A3_1_QT_DIRCRED_VENC_AD: "quantidade"
    TAB_VII_A3_2_VL_DIRCRED_VENC_AD: "moeda (R$)"
    TAB_VII_A4_1_QT_DIRCRED_VENC_INAD: "quantidade"
    TAB_VII_A4_2_VL_DIRCRED_VENC_INAD: "moeda (R$)"
    TAB_VII_A5_1_QT_DIRCRED_INAD: "quantidade"
    TAB_VII_A5_2_VL_DIRCRED_INAD: "moeda (R$)"
    TAB_VII_B1_1_QT_CEDENTE: "quantidade"
    TAB_VII_B1_2_VL_CEDENTE: "moeda (R$)"
    TAB_VII_B1_3_VL_CONTAB_CEDENTE: "moeda (R$)"
    TAB_VII_B2_1_QT_PREST: "quantidade"
    TAB_VII_B2_2_VL_PREST: "moeda (R$)"
    TAB_VII_B2_3_VL_CONTAB_PREST: "moeda (R$)"
    TAB_VII_B3_1_QT_TERCEIRO: "quantidade"
    TAB_VII_B3_2_VL_TERCEIRO: "moeda (R$)"
    TAB_VII_B3_3_VL_CONTAB_TERCEIRO: "moeda (R$)"
    TAB_VII_C_1_QT_SUBST: "quantidade"
    TAB_VII_C_2_VL_SUBST: "moeda (R$)"
    TAB_VII_C_3_VL_CONTAB_SUBST: "moeda (R$)"
    TAB_VII_D_1_QT_RECOMPRA: "quantidade"
    TAB_VII_D_2_VL_RECOMPRA: "moeda (R$)"
    TAB_VII_D_3_VL_CONTAB_RECOMPRA: "moeda (R$)"
    SEQUENCIAL: "código ou número de identificação (sem unidade)"
    VALOR: "moeda (R$)"
    TAB_X_NR_COTST_SENIOR_PF: "quantidade"
    TAB_X_NR_COTST_SENIOR_PJ_NAO_FINANC: "quantidade"
    TAB_X_NR_COTST_SENIOR_BANCO: "quantidade"
    TAB_X_NR_COTST_SENIOR_CORRETORA_DISTRIB: "quantidade"
    TAB_X_NR_COTST_SENIOR_PJ_FINANC: "quantidade"
    TAB_X_NR_COTST_SENIOR_INVNR: "quantidade"
    TAB_X_NR_COTST_SENIOR_EAPC: "quantidade"
    TAB_X_NR_COTST_SENIOR_EFPC: "quantidade"
    TAB_X_NR_COTST_SENIOR_RPPS: "quantidade"
    TAB_X_NR_COTST_SENIOR_SEGUR: "quantidade"
    TAB_X_NR_COTST_SENIOR_CAPITALIZ: "quantidade"
    TAB_X_NR_COTST_SENIOR_COTA_FIDC: "quantidade"
    TAB_X_NR_COTST_SENIOR_FII: "quantidade"
    TAB_X_NR_COTST_SENIOR_OUTRO_FI: "quantidade"
    TAB_X_NR_COTST_SENIOR_CLUBE: "quantidade"
    TAB_X_NR_COTST_SENIOR_OUTRO: "quantidade"
    TAB_X_NR_COTST_SUBORD_PF: "quantidade"
    TAB_X_NR_COTST_SUBORD_PJ_NAO_FINANC: "quantidade"
    TAB_X_NR_COTST_SUBORD_BANCO: "quantidade"
    TAB_X_NR_COTST_SUBORD_CORRETORA_DISTRIB: "quantidade"
    TAB_X_NR_COTST_SUBORD_PJ_FINANC: "quantidade"
    TAB_X_NR_COTST_SUBORD_INVNR: "quantidade"
    TAB_X_NR_COTST_SUBORD_EAPC: "quantidade"
    TAB_X_NR_COTST_SUBORD_EFPC: "quantidade"
    TAB_X_NR_COTST_SUBORD_RPPS: "quantidade"
    TAB_X_NR_COTST_SUBORD_SEGUR: "quantidade"
    TAB_X_NR_COTST_SUBORD_CAPITALIZ: "quantidade"
    TAB_X_NR_COTST_SUBORD_COTA_FIDC: "quantidade"
    TAB_X_NR_COTST_SUBORD_FII: "quantidade"
    TAB_X_NR_COTST_SUBORD_OUTRO_FI: "quantidade"
    TAB_X_NR_COTST_SUBORD_CLUBE: "quantidade"
    TAB_X_NR_COTST_SUBORD_OUTRO: "quantidade"
    TAB_X_NR_COTST: "quantidade"
    TAB_X_SCR_RISCO_DEVEDOR_AA: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_A: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_B: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_C: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_D: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_E: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_F: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_G: "moeda (R$)"
    TAB_X_SCR_RISCO_DEVEDOR_H: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_AA: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_A: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_B: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_C: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_D: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_E: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_F: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_G: "moeda (R$)"
    TAB_X_SCR_RISCO_OPER_H: "moeda (R$)"
    TAB_X_DEBITO_TRIBUT: "moeda (R$)"
    TAB_X_QT_COTA: "quantidade"
    TAB_X_VL_COTA: "moeda (R$)"
    TAB_X_VL_RENTAB_MES: "percentual (%)"
    TAB_X_VL_TOTAL: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_0: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_30: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_60: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_90: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_180: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_360: "moeda (R$)"
    TAB_X_VL_LIQUIDEZ_MAIOR_360: "moeda (R$)"
    TAB_X_PR_DESEMP_ESPERADO: "percentual (%)"
    TAB_X_PR_DESEMP_REAL: "percentual (%)"
    TAB_X_VL_GARANTIA_DIRCRED: "moeda (R$)"
    TAB_X_PR_GARANTIA_DIRCRED: "percentual (%)"
  dados_pessoais:
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_1, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_2, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_3, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_4, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_5, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_6, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_7, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_8, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2A12_CPF_CNPJ_CEDENTE_9, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_1, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_2, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_3, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_4, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_5, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_6, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_7, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_8, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
    - {coluna: TAB_I2B12_CPF_CNPJ_CEDENTE_9, categoria: "endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)"}
  eras: []
  revisado_em: 2026-11-16
  versao_fetcher: 0.4.0
---

# FIDC: Documentos: Informe Mensal

## Resumo

Informe mensal dos Fundos de Investimento em Direitos Creditórios (FIDC): carteira por segmento e por prazo, inadimplência, cotistas, cotas, rentabilidade, liquidez e garantias, em 18 tabelas que seguem os itens do Anexo A da Instrução CVM 489.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `cvm/fidc-inf-mensal` |
| Órgão | Comissão de Valores Mobiliários (CVM) |
| Página oficial | https://dados.cvm.gov.br/dataset/fidc-doc-inf_mensal |
| Licença | Open Data Commons Open Database License (ODbL), conforme o portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fidc-doc-inf_mensal |
| Periodicidade | mensal (um arquivo por mês); o portal declara atualização semanal para os últimos doze meses |
| Cobertura | 2025-01 a em-curso |
| Unidade (uma linha) | o informe mensal de uma classe de FIDC; nas tabelas `tab_viii`, `tab_x_1` a `tab_x_4` e `tab_x_6`, uma linha por classe e série (ou sequencial) |
| Granularidade | espacial: nacional (sem recorte geográfico); temporal: mensal (competência, `DT_COMPTC`) |
| Formato bruto | ZIP com um CSV por tabela (ponto e vírgula), um arquivo por período, no espelho público da CVM |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 388 |
| Unidades de medida | `PRAZO_CONVERSAO_COTA`: dias; `PRAZO_PAGTO_RESGATE`: dias; `TAB_I_VL_ATIVO`: moeda (R$); `TAB_I1_VL_DISP`: moeda (R$); `TAB_I2_VL_CARTEIRA`: moeda (R$); `TAB_I2A_VL_DIRCRED_RISCO`: moeda (R$); `TAB_I2A1_VL_CRED_VENC_AD`: moeda (R$); `TAB_I2A2_VL_CRED_VENC_INAD`: moeda (R$); `TAB_I2A21_VL_TOTAL_PARCELA_INAD`: moeda (R$); `TAB_I2A3_VL_CRED_INAD`: moeda (R$); `TAB_I2A4_VL_CRED_DIRCRED_PERFM`: moeda (R$); `TAB_I2A5_VL_CRED_VENCIDO_PENDENTE`: moeda (R$); `TAB_I2A6_VL_CRED_EMP_RECUP`: moeda (R$); `TAB_I2A7_VL_CRED_RECEITA_PUBLICA`: moeda (R$); `TAB_I2A8_VL_CRED_ACAO_JUDIC`: moeda (R$); `TAB_I2A9_VL_CRED_FATOR_RISCO`: moeda (R$); `TAB_I2A11_VL_REDUCAO_RECUP`: moeda (R$); `TAB_I2A12_PR_CEDENTE_1`: percentual (%); `TAB_I2A12_PR_CEDENTE_2`: percentual (%); `TAB_I2A12_PR_CEDENTE_3`: percentual (%); `TAB_I2A12_PR_CEDENTE_4`: percentual (%); `TAB_I2A12_PR_CEDENTE_5`: percentual (%); `TAB_I2A12_PR_CEDENTE_6`: percentual (%); `TAB_I2A12_PR_CEDENTE_7`: percentual (%); `TAB_I2A12_PR_CEDENTE_8`: percentual (%); `TAB_I2A12_PR_CEDENTE_9`: percentual (%); `TAB_I2B_VL_DIRCRED_SEM_RISCO`: moeda (R$); `TAB_I2B1_VL_CRED_VENC_AD`: moeda (R$); `TAB_I2B2_VL_CRED_VENC_INAD`: moeda (R$); `TAB_I2B21_VL_TOTAL_PARCELA_INAD`: moeda (R$); `TAB_I2B3_VL_CRED_INAD`: moeda (R$); `TAB_I2B4_VL_CRED_DIRCRED_PERFM`: moeda (R$); `TAB_I2B5_VL_CRED_VENCIDO_PENDENTE`: moeda (R$); `TAB_I2B6_VL_CRED_EMP_RECUP`: moeda (R$); `TAB_I2B7_VL_CRED_RECEITA_PUBLICA`: moeda (R$); `TAB_I2B8_VL_CRED_ACAO_JUDIC`: moeda (R$); `TAB_I2B9_VL_CRED_FATOR_RISCO`: moeda (R$); `TAB_I2B11_VL_REDUCAO_RECUP`: moeda (R$); `TAB_I2B12_PR_CEDENTE_1`: percentual (%); `TAB_I2B12_PR_CEDENTE_2`: percentual (%); `TAB_I2B12_PR_CEDENTE_3`: percentual (%); `TAB_I2B12_PR_CEDENTE_4`: percentual (%); `TAB_I2B12_PR_CEDENTE_5`: percentual (%); `TAB_I2B12_PR_CEDENTE_6`: percentual (%); `TAB_I2B12_PR_CEDENTE_7`: percentual (%); `TAB_I2B12_PR_CEDENTE_8`: percentual (%); `TAB_I2B12_PR_CEDENTE_9`: percentual (%); `TAB_I2C_VL_VLMOB`: moeda (R$); `TAB_I2C1_VL_DEBENTURE`: moeda (R$); `TAB_I2C2_VL_CRI`: moeda (R$); `TAB_I2C3_VL_NP_COMERC`: moeda (R$); `TAB_I2C4_VL_LETRA_FINANC`: moeda (R$); `TAB_I2C5_VL_COTA_FIF`: moeda (R$); `TAB_I2C6_VL_OUTRO`: moeda (R$); `TAB_I2D_VL_TITPUB_FED`: moeda (R$); `TAB_I2E_VL_CDB`: moeda (R$); `TAB_I2F_VL_OPER_COMPROM`: moeda (R$); `TAB_I2G_VL_OUTRO_RF`: moeda (R$); `TAB_I2H_VL_COTA_FIDC`: moeda (R$); `TAB_I2J_VL_CONTRATO_FUTURO`: moeda (R$); `TAB_I2_DEBENTURE_CRI`: moeda (R$); `TAB_I2_COTA_FIDC`: moeda (R$); `TAB_I2_VL_OUTRO_ATIVO`: moeda (R$); `TAB_I3_VL_POSICAO_DERIV`: moeda (R$); `TAB_I3A_VL_MERCADO_TERMO`: moeda (R$); `TAB_I3B_VL_MERCADO_OPCAO`: moeda (R$); `TAB_I3C_VL_MERCADO_FUTURO`: moeda (R$); `TAB_I3D_VL_DIFER_SWAP`: moeda (R$); `TAB_I3E_VL_COBERTURA`: moeda (R$); `TAB_I3F_VL_DEPOSITO_MARGEM`: moeda (R$); `TAB_I4_VL_OUTRO_ATIVO`: moeda (R$); `TAB_I4A_VL_CPRAZO`: moeda (R$); `TAB_I4B_VL_LPRAZO`: moeda (R$); `TAB_II_VL_CARTEIRA`: moeda (R$); `TAB_II_A_VL_INDUST`: moeda (R$); `TAB_II_B_VL_IMOBIL`: moeda (R$); `TAB_II_C_VL_COMERC`: moeda (R$); `TAB_II_C1_VL_COMERC`: moeda (R$); `TAB_II_C2_VL_VAREJO`: moeda (R$); `TAB_II_C3_VL_ARREND`: moeda (R$); `TAB_II_D_VL_SERV`: moeda (R$); `TAB_II_D1_VL_SERV`: moeda (R$); `TAB_II_D2_VL_SERV_PUBLICO`: moeda (R$); `TAB_II_D3_VL_SERV_EDUC`: moeda (R$); `TAB_II_D4_VL_ENTRET`: moeda (R$); `TAB_II_E_VL_AGRONEG`: moeda (R$); `TAB_II_F_VL_FINANC`: moeda (R$); `TAB_II_F1_VL_CRED_PESSOA`: moeda (R$); `TAB_II_F2_VL_CRED_PESSOA_CONSIG`: moeda (R$); `TAB_II_F3_VL_CRED_CORP`: moeda (R$); `TAB_II_F4_VL_MIDMARKET`: moeda (R$); `TAB_II_F5_VL_VEICULO`: moeda (R$); `TAB_II_F6_VL_IMOBIL_EMPRESA`: moeda (R$); `TAB_II_F7_VL_IMOBIL_RESID`: moeda (R$); `TAB_II_F8_VL_OUTRO`: moeda (R$); `TAB_II_G_VL_CREDITO`: moeda (R$); `TAB_II_H_VL_FACTOR`: moeda (R$); `TAB_II_H1_VL_PESSOA`: moeda (R$); `TAB_II_H2_VL_CORP`: moeda (R$); `TAB_II_I_VL_SETOR_PUBLICO`: moeda (R$); `TAB_II_I1_VL_PRECAT`: moeda (R$); `TAB_II_I2_VL_TRIBUT`: moeda (R$); `TAB_II_I3_VL_ROYALTIES`: moeda (R$); `TAB_II_I4_VL_OUTRO`: moeda (R$); `TAB_II_J_VL_JUDICIAL`: moeda (R$); `TAB_II_K_VL_MARCA`: moeda (R$); `TAB_III_VL_PASSIVO`: moeda (R$); `TAB_III_A_VL_PAGAR`: moeda (R$); `TAB_III_A1_VL_CPRAZO`: moeda (R$); `TAB_III_A2_VL_LPRAZO`: moeda (R$); `TAB_III_B_VL_POSICAO_DERIV`: moeda (R$); `TAB_III_B1_VL_TERMO`: moeda (R$); `TAB_III_B2_VL_OPCAO`: moeda (R$); `TAB_III_B3_VL_FUTURO`: moeda (R$); `TAB_III_B4_VL_SWAP_PAGAR`: moeda (R$); `TAB_IV_A_VL_PL`: moeda (R$); `TAB_IV_B_VL_PL_MEDIO`: moeda (R$); `TAB_IX_A1_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_A1_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_A1_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_A1_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_A1_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_A1_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_A2_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_A2_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_A2_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_A2_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_A2_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_A2_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_B1_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_B1_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_B1_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_B1_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_B1_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_B1_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_B2_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_B2_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_B2_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_B2_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_B2_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_B2_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_C1_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_C1_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_C1_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_C1_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_C1_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_C1_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_C2_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_C2_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_C2_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_C2_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_C2_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_C2_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_D1_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_D1_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_D1_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_D1_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_D1_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_D1_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_D2_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_D2_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_D2_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_D2_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_D2_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_D2_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_E1_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_E1_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_E1_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_E1_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_E1_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_E1_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_E2_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_E2_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_E2_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_E2_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_E2_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_E2_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_F1_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_F1_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_F1_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_F1_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_F1_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_F1_2_3_VENDA_MAX`: moeda (R$); `TAB_IX_F2_1_1_COMPRA_MIN`: moeda (R$); `TAB_IX_F2_1_2_COMPRA_MEDIA`: moeda (R$); `TAB_IX_F2_1_3_COMPRA_MAX`: moeda (R$); `TAB_IX_F2_2_1_VENDA_MIN`: moeda (R$); `TAB_IX_F2_2_2_VENDA_MEDIA`: moeda (R$); `TAB_IX_F2_2_3_VENDA_MAX`: moeda (R$); `TAB_V_A_VL_DIRCRED_PRAZO`: moeda (R$); `TAB_V_A1_VL_PRAZO_VENC_30`: moeda (R$); `TAB_V_A2_VL_PRAZO_VENC_60`: moeda (R$); `TAB_V_A3_VL_PRAZO_VENC_90`: moeda (R$); `TAB_V_A4_VL_PRAZO_VENC_120`: moeda (R$); `TAB_V_A5_VL_PRAZO_VENC_150`: moeda (R$); `TAB_V_A6_VL_PRAZO_VENC_180`: moeda (R$); `TAB_V_A7_VL_PRAZO_VENC_360`: moeda (R$); `TAB_V_A8_VL_PRAZO_VENC_720`: moeda (R$); `TAB_V_A9_VL_PRAZO_VENC_1080`: moeda (R$); `TAB_V_A10_VL_PRAZO_VENC_MAIOR_1080`: moeda (R$); `TAB_V_B_VL_DIRCRED_INAD`: moeda (R$); `TAB_V_B1_VL_INAD_30`: moeda (R$); `TAB_V_B2_VL_INAD_60`: moeda (R$); `TAB_V_B3_VL_INAD_90`: moeda (R$); `TAB_V_B4_VL_INAD_120`: moeda (R$); `TAB_V_B5_VL_INAD_150`: moeda (R$); `TAB_V_B6_VL_INAD_180`: moeda (R$); `TAB_V_B7_VL_INAD_360`: moeda (R$); `TAB_V_B8_VL_INAD_720`: moeda (R$); `TAB_V_B9_VL_INAD_1080`: moeda (R$); `TAB_V_B10_VL_INAD_MAIOR_1080`: moeda (R$); `TAB_V_C_VL_DIRCRED_ANTECIPADO`: moeda (R$); `TAB_V_C1_VL_ANTECIPADO_30`: moeda (R$); `TAB_V_C2_VL_ANTECIPADO_60`: moeda (R$); `TAB_V_C3_VL_ANTECIPADO_90`: moeda (R$); `TAB_V_C4_VL_ANTECIPADO_120`: moeda (R$); `TAB_V_C5_VL_ANTECIPADO_150`: moeda (R$); `TAB_V_C6_VL_ANTECIPADO_180`: moeda (R$); `TAB_V_C7_VL_ANTECIPADO_360`: moeda (R$); `TAB_V_C8_VL_ANTECIPADO_720`: moeda (R$); `TAB_V_C9_VL_ANTECIPADO_1080`: moeda (R$); `TAB_V_C10_VL_ANTECIPADO_MAIOR_1080`: moeda (R$); `TAB_VI_A_VL_DIRCRED_PRAZO`: moeda (R$); `TAB_VI_A1_VL_PRAZO_VENC_30`: moeda (R$); `TAB_VI_A2_VL_PRAZO_VENC_60`: moeda (R$); `TAB_VI_A3_VL_PRAZO_VENC_90`: moeda (R$); `TAB_VI_A4_VL_PRAZO_VENC_120`: moeda (R$); `TAB_VI_A5_VL_PRAZO_VENC_150`: moeda (R$); `TAB_VI_A6_VL_PRAZO_VENC_180`: moeda (R$); `TAB_VI_A7_VL_PRAZO_VENC_360`: moeda (R$); `TAB_VI_A8_VL_PRAZO_VENC_720`: moeda (R$); `TAB_VI_A9_VL_PRAZO_VENC_1080`: moeda (R$); `TAB_VI_A10_VL_PRAZO_VENC_MAIOR_1080`: moeda (R$); `TAB_VI_B_VL_DIRCRED_INAD`: moeda (R$); `TAB_VI_B1_VL_INAD_30`: moeda (R$); `TAB_VI_B2_VL_INAD_60`: moeda (R$); `TAB_VI_B3_VL_INAD_90`: moeda (R$); `TAB_VI_B4_VL_INAD_120`: moeda (R$); `TAB_VI_B5_VL_INAD_150`: moeda (R$); `TAB_VI_B6_VL_INAD_180`: moeda (R$); `TAB_VI_B7_VL_INAD_360`: moeda (R$); `TAB_VI_B8_VL_INAD_720`: moeda (R$); `TAB_VI_B9_VL_INAD_1080`: moeda (R$); `TAB_VI_B10_VL_INAD_MAIOR_1080`: moeda (R$); `TAB_VI_C_VL_DIRCRED_ANTECIPADO`: moeda (R$); `TAB_VI_C1_VL_ANTECIPADO_30`: moeda (R$); `TAB_VI_C2_VL_ANTECIPADO_60`: moeda (R$); `TAB_VI_C3_VL_ANTECIPADO_90`: moeda (R$); `TAB_VI_C4_VL_ANTECIPADO_120`: moeda (R$); `TAB_VI_C5_VL_ANTECIPADO_150`: moeda (R$); `TAB_VI_C6_VL_ANTECIPADO_180`: moeda (R$); `TAB_VI_C7_VL_ANTECIPADO_360`: moeda (R$); `TAB_VI_C8_VL_ANTECIPADO_720`: moeda (R$); `TAB_VI_C9_VL_ANTECIPADO_1080`: moeda (R$); `TAB_VI_C10_VL_ANTECIPADO_MAIOR_1080`: moeda (R$); `TAB_VII_A1_1_QT_DIRCRED_RISCO`: quantidade; `TAB_VII_A1_2_VL_DIRCRED_RISCO`: moeda (R$); `TAB_VII_A2_1_QT_DIRCRED_SEM_RISCO`: quantidade; `TAB_VII_A2_2_VL_DIRCRED_SEM_RISCO`: moeda (R$); `TAB_VII_A3_1_QT_DIRCRED_VENC_AD`: quantidade; `TAB_VII_A3_2_VL_DIRCRED_VENC_AD`: moeda (R$); `TAB_VII_A4_1_QT_DIRCRED_VENC_INAD`: quantidade; `TAB_VII_A4_2_VL_DIRCRED_VENC_INAD`: moeda (R$); `TAB_VII_A5_1_QT_DIRCRED_INAD`: quantidade; `TAB_VII_A5_2_VL_DIRCRED_INAD`: moeda (R$); `TAB_VII_B1_1_QT_CEDENTE`: quantidade; `TAB_VII_B1_2_VL_CEDENTE`: moeda (R$); `TAB_VII_B1_3_VL_CONTAB_CEDENTE`: moeda (R$); `TAB_VII_B2_1_QT_PREST`: quantidade; `TAB_VII_B2_2_VL_PREST`: moeda (R$); `TAB_VII_B2_3_VL_CONTAB_PREST`: moeda (R$); `TAB_VII_B3_1_QT_TERCEIRO`: quantidade; `TAB_VII_B3_2_VL_TERCEIRO`: moeda (R$); `TAB_VII_B3_3_VL_CONTAB_TERCEIRO`: moeda (R$); `TAB_VII_C_1_QT_SUBST`: quantidade; `TAB_VII_C_2_VL_SUBST`: moeda (R$); `TAB_VII_C_3_VL_CONTAB_SUBST`: moeda (R$); `TAB_VII_D_1_QT_RECOMPRA`: quantidade; `TAB_VII_D_2_VL_RECOMPRA`: moeda (R$); `TAB_VII_D_3_VL_CONTAB_RECOMPRA`: moeda (R$); `SEQUENCIAL`: código ou número de identificação (sem unidade); `VALOR`: moeda (R$); `TAB_X_NR_COTST_SENIOR_PF`: quantidade; `TAB_X_NR_COTST_SENIOR_PJ_NAO_FINANC`: quantidade; `TAB_X_NR_COTST_SENIOR_BANCO`: quantidade; `TAB_X_NR_COTST_SENIOR_CORRETORA_DISTRIB`: quantidade; `TAB_X_NR_COTST_SENIOR_PJ_FINANC`: quantidade; `TAB_X_NR_COTST_SENIOR_INVNR`: quantidade; `TAB_X_NR_COTST_SENIOR_EAPC`: quantidade; `TAB_X_NR_COTST_SENIOR_EFPC`: quantidade; `TAB_X_NR_COTST_SENIOR_RPPS`: quantidade; `TAB_X_NR_COTST_SENIOR_SEGUR`: quantidade; `TAB_X_NR_COTST_SENIOR_CAPITALIZ`: quantidade; `TAB_X_NR_COTST_SENIOR_COTA_FIDC`: quantidade; `TAB_X_NR_COTST_SENIOR_FII`: quantidade; `TAB_X_NR_COTST_SENIOR_OUTRO_FI`: quantidade; `TAB_X_NR_COTST_SENIOR_CLUBE`: quantidade; `TAB_X_NR_COTST_SENIOR_OUTRO`: quantidade; `TAB_X_NR_COTST_SUBORD_PF`: quantidade; `TAB_X_NR_COTST_SUBORD_PJ_NAO_FINANC`: quantidade; `TAB_X_NR_COTST_SUBORD_BANCO`: quantidade; `TAB_X_NR_COTST_SUBORD_CORRETORA_DISTRIB`: quantidade; `TAB_X_NR_COTST_SUBORD_PJ_FINANC`: quantidade; `TAB_X_NR_COTST_SUBORD_INVNR`: quantidade; `TAB_X_NR_COTST_SUBORD_EAPC`: quantidade; `TAB_X_NR_COTST_SUBORD_EFPC`: quantidade; `TAB_X_NR_COTST_SUBORD_RPPS`: quantidade; `TAB_X_NR_COTST_SUBORD_SEGUR`: quantidade; `TAB_X_NR_COTST_SUBORD_CAPITALIZ`: quantidade; `TAB_X_NR_COTST_SUBORD_COTA_FIDC`: quantidade; `TAB_X_NR_COTST_SUBORD_FII`: quantidade; `TAB_X_NR_COTST_SUBORD_OUTRO_FI`: quantidade; `TAB_X_NR_COTST_SUBORD_CLUBE`: quantidade; `TAB_X_NR_COTST_SUBORD_OUTRO`: quantidade; `TAB_X_NR_COTST`: quantidade; `TAB_X_SCR_RISCO_DEVEDOR_AA`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_A`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_B`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_C`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_D`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_E`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_F`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_G`: moeda (R$); `TAB_X_SCR_RISCO_DEVEDOR_H`: moeda (R$); `TAB_X_SCR_RISCO_OPER_AA`: moeda (R$); `TAB_X_SCR_RISCO_OPER_A`: moeda (R$); `TAB_X_SCR_RISCO_OPER_B`: moeda (R$); `TAB_X_SCR_RISCO_OPER_C`: moeda (R$); `TAB_X_SCR_RISCO_OPER_D`: moeda (R$); `TAB_X_SCR_RISCO_OPER_E`: moeda (R$); `TAB_X_SCR_RISCO_OPER_F`: moeda (R$); `TAB_X_SCR_RISCO_OPER_G`: moeda (R$); `TAB_X_SCR_RISCO_OPER_H`: moeda (R$); `TAB_X_DEBITO_TRIBUT`: moeda (R$); `TAB_X_QT_COTA`: quantidade; `TAB_X_VL_COTA`: moeda (R$); `TAB_X_VL_RENTAB_MES`: percentual (%); `TAB_X_VL_TOTAL`: moeda (R$); `TAB_X_VL_LIQUIDEZ_0`: moeda (R$); `TAB_X_VL_LIQUIDEZ_30`: moeda (R$); `TAB_X_VL_LIQUIDEZ_60`: moeda (R$); `TAB_X_VL_LIQUIDEZ_90`: moeda (R$); `TAB_X_VL_LIQUIDEZ_180`: moeda (R$); `TAB_X_VL_LIQUIDEZ_360`: moeda (R$); `TAB_X_VL_LIQUIDEZ_MAIOR_360`: moeda (R$); `TAB_X_PR_DESEMP_ESPERADO`: percentual (%); `TAB_X_PR_DESEMP_REAL`: percentual (%); `TAB_X_VL_GARANTIA_DIRCRED`: moeda (R$); `TAB_X_PR_GARANTIA_DIRCRED`: percentual (%) |
| Dados pessoais | `TAB_I2A12_CPF_CNPJ_CEDENTE_1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_4` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_5` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_6` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_7` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_8` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2A12_CPF_CNPJ_CEDENTE_9` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_1` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_2` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_3` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_4` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_5` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_6` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_7` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_8` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)); `TAB_I2B12_CPF_CNPJ_CEDENTE_9` (endereço, telefone, e-mail ou CPF (pode ser de pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-16 |
| Versão do fetcher | 0.4.0 |

## Origem e coleta

- Fonte: Portal de Dados Abertos da CVM (https://dados.cvm.gov.br/dataset/fidc-doc-inf_mensal). Os arquivos ficam no espelho público `https://dados.cvm.gov.br/dados/FIDC/DOC/INF_MENSAL/DADOS/`.
- O catálogo do fetcher lista 23 arquivo(s): de `inf_mensal_fidc_202501.zip` a `inf_mensal_fidc_202611.zip`.
- Em 2026-11-16 conferimos 54 arquivos Parquet convertidos de 3 arquivo(s) de origem (amostra: 2025-01, 2025-12, 2026-10).
- No bruto, o arquivo fica em `fidc-inf-mensal/<arquivo>@AAAAMMDD.<csv|zip>`; o carimbo é a data da coleta, e a CVM reenvia os arquivos do ano ou mês corrente todos os dias.
- O dicionário de dados (arquivos `META` da CVM, em `.../META/`) não é baixado pelo fetcher; as descrições da seção Variáveis vêm dele, conferidas contra os cabeçalhos dos arquivos.

## Conteúdo

- Unidade de análise: o informe mensal de uma classe de FIDC; nas tabelas `tab_viii`, `tab_x_1` a `tab_x_4` e `tab_x_6`, uma linha por classe e série (ou sequencial).
- Particionado por `ano` e `mes`; o catálogo cobre 2025-01 a 2026-11, e conferimos as amostras 2025-01, 2025-12, 2026-10.
- Em 2026-10 há 4.490 classes (uma linha por classe nas tabelas de item único) e 41.210 linhas em `tab_viii`; em 2025-01, 3.214 linhas para 3.198 classes (16 linhas a mais que classes). O portal descreve novos campos a partir de 2019-11 (Instrução CVM 576) e uma mudança de versão do documento na competência 2023-10 (novas colunas `CLASSE_UNICA`, `CLASSE`, `CNPJ_CLASSE` e `TAB_I2C5_VL_COTA_FIF` em `tab_i`); o catálogo do fetcher parte de 2025-01, quando o layout novo já vigorava (o histórico do portal começa em 2013).
- Os valores de cotas, patrimônio e carteira ficam em muitas colunas `TAB_*`, cujos nomes seguem a numeração dos itens do informe (por exemplo, `TAB_IV_A_VL_PL` é o item IV.a, patrimônio líquido).
- Este dataset reúne 18 tabelas (um arquivo por tabela em cada período), gravadas como arquivos Parquet separados no mesmo dataset; o nome do arquivo no lake é `<arquivo de origem>__<csv>.parquet` (ou só o nome do CSV, quando o arquivo não é ZIP):

| Tabela (nome do CSV sem o período) | Colunas | Linhas no maior arquivo convertido | Chave candidata (única no arquivo mais recente convertido) | O que é |
|---|---|---|---|---|
| `inf_mensal_fidc_tab_i` | 109 | 4.490 | `CNPJ_FUNDO_CLASSE` | identificação da classe (administrador, condomínio, classe única) e itens de ativo, incluindo os principais cedentes (I.2.a e I.2.b) |
| `inf_mensal_fidc_tab_ii` | 37 | 4.490 | `CNPJ_FUNDO_CLASSE` | carteira de direitos creditórios por segmento: industrial, imobiliário, comercial e outros (II.a a II.h) |
| `inf_mensal_fidc_tab_iii` | 13 | 4.490 | `CNPJ_FUNDO_CLASSE` | valores a pagar, de curto e de longo prazo (III) |
| `inf_mensal_fidc_tab_iv` | 6 | 4.490 | `CNPJ_FUNDO_CLASSE` | patrimônio líquido e patrimônio líquido médio dos últimos três meses (IV) |
| `inf_mensal_fidc_tab_ix` | 76 | 4.490 | `CNPJ_FUNDO_CLASSE` | preços mínimo, médio e máximo de compra e venda de direitos creditórios (IX) |
| `inf_mensal_fidc_tab_v` | 37 | 4.490 | `CNPJ_FUNDO_CLASSE` | valores por prazo de vencimento, de até 30 dias a acima de 1.080 dias (V.a) |
| `inf_mensal_fidc_tab_vi` | 37 | 4.490 | `CNPJ_FUNDO_CLASSE` | valores por prazo de vencimento, de até 30 dias a acima de 1.080 dias (VI.a) |
| `inf_mensal_fidc_tab_vii` | 29 | 4.490 | `CNPJ_FUNDO_CLASSE` | aquisições e alienações de direitos creditórios, em quantidade e valor (VII) |
| `inf_mensal_fidc_tab_viii` | 6 | 41.210 | `CNPJ_FUNDO_CLASSE`, `SEQUENCIAL` | valores sequenciais (VIII); o dicionário não descreve as colunas `VALOR` e `SEQUENCIAL` |
| `inf_mensal_fidc_tab_x` | 23 | 4.490 | `CNPJ_FUNDO_CLASSE` | direitos creditórios reportados ao SCR por faixa de risco do devedor e débito tributário (X.8 e X.9) |
| `inf_mensal_fidc_tab_x_1` | 7 | 11.976 | `CNPJ_FUNDO_CLASSE`, `TAB_X_CLASSE_SERIE` | número de cotistas por classe e série (X.1) |
| `inf_mensal_fidc_tab_x_1_1` | 36 | 4.490 | `CNPJ_FUNDO_CLASSE` | número de cotistas por tipo de cotista, nas classes sênior e subordinada (X.1.1) |
| `inf_mensal_fidc_tab_x_2` | 7 | 12.395 | `CNPJ_FUNDO_CLASSE`, `TAB_X_CLASSE_SERIE` | quantidade de cotas por classe e série (X.2) |
| `inf_mensal_fidc_tab_x_3` | 6 | 12.342 | `CNPJ_FUNDO_CLASSE`, `TAB_X_CLASSE_SERIE` | rentabilidade apurada no mês por classe e série (X.3) |
| `inf_mensal_fidc_tab_x_4` | 8 | 47.364 | `CNPJ_FUNDO_CLASSE`, `TAB_X_TP_OPER`, `TAB_X_CLASSE_SERIE` | operações com cotas por tipo de operação, classe e série (X.4) |
| `inf_mensal_fidc_tab_x_5` | 11 | 4.490 | `CNPJ_FUNDO_CLASSE` | liquidez dos ativos por faixa de prazo (X.5) |
| `inf_mensal_fidc_tab_x_6` | 7 | 12.136 | `CNPJ_FUNDO_CLASSE`, `TAB_X_CLASSE_SERIE` | desempenho esperado e realizado por classe e série (X.6) |
| `inf_mensal_fidc_tab_x_7` | 6 | 4.490 | `CNPJ_FUNDO_CLASSE` | garantias dos direitos creditórios (X.7) |

- Não há uma chave única comum às tabelas: cada tabela tem a sua (coluna acima).

## Variáveis

Descrições do dicionário de dados (arquivos `META`) da CVM. Os nomes de coluna são os do arquivo, sem normalização. Colunas que não existem em todas as tabelas dizem em quais tabelas aparecem. A coluna Período mostra os períodos das amostras convertidas em que a coluna aparece (`todo` = em todos os arquivos das tabelas em que existe).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `TP_FUNDO_CLASSE` | `TP_FUNDO_CLASSE` | texto | Tipo de fundo/classe | — | todo |
| `CNPJ_FUNDO_CLASSE` | `CNPJ_FUNDO_CLASSE` | texto | CNPJ do fundo/classe | — | todo |
| `DENOM_SOCIAL` | `DENOM_SOCIAL` | texto | Denominação Social | — | todo |
| `DT_COMPTC` | `DT_COMPTC` | texto | Data de competência do documento | — | todo |
| `CLASSE_UNICA` | `CLASSE_UNICA` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: classe unica (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `CNPJ_ADMIN` | `CNPJ_ADMIN` | texto | CNPJ do Administrador (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `ADMIN` | `ADMIN` | texto | Nome do Administrador (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `CLASSE` | `CLASSE` | texto | Classe (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `CNPJ_CLASSE` | `CNPJ_CLASSE` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: cnpj classe (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `CONDOM` | `CONDOM` | texto | Forma de condomínio (só em: `inf_mensal_fidc_tab_i`) | Aberto/Fechado | todo |
| `FUNDO_EXCLUSIVO` | `FUNDO_EXCLUSIVO` | texto | Indica se é fundo exclusivo (só em: `inf_mensal_fidc_tab_i`) | S/N | todo |
| `COTST_INTERESSE` | `COTST_INTERESSE` | texto | Indica se todos os cotistas são vinculados por interesse único e indissociável (só em: `inf_mensal_fidc_tab_i`) | S/N | todo |
| `PRAZO_CONVERSAO_COTA` | `PRAZO_CONVERSAO_COTA` | inteiro | Prazo mínimo entre a data do pedido de resgate e a correspondente conversão em quantidade de cotas (só em: `inf_mensal_fidc_tab_i`) | dias | todo |
| `TP_PRAZO_CONVERSAO_COTA` | `TP_PRAZO_CONVERSAO_COTA` | texto | Tipo do prazo para conversão em quantidade de cotas (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `PRAZO_PAGTO_RESGATE` | `PRAZO_PAGTO_RESGATE` | inteiro | Prazo para o pagamento do resgate após a conversão em quantidade de cotas (só em: `inf_mensal_fidc_tab_i`) | dias | todo |
| `TP_PRAZO_PAGTO_RESGATE` | `TP_PRAZO_PAGTO_RESGATE` | texto | Tipo do prazo para o pagamento do resgate (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I_VL_ATIVO` | `TAB_I_VL_ATIVO` | decimal | (Tabela I) Ativo (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I1_VL_DISP` | `TAB_I1_VL_DISP` | decimal | (I.1) Disponibilidades (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2_VL_CARTEIRA` | `TAB_I2_VL_CARTEIRA` | decimal | (I.2) Carteira (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A_VL_DIRCRED_RISCO` | `TAB_I2A_VL_DIRCRED_RISCO` | decimal | (I.2.a) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A1_VL_CRED_VENC_AD` | `TAB_I2A1_VL_CRED_VENC_AD` | decimal | (I.2.a.1) Créditos Existentes a Vencer e Adimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A2_VL_CRED_VENC_INAD` | `TAB_I2A2_VL_CRED_VENC_INAD` | decimal | (I.2.a.2) Créditos Existentes a Vencer com Parcelas Inadimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A21_VL_TOTAL_PARCELA_INAD` | `TAB_I2A21_VL_TOTAL_PARCELA_INAD` | decimal | (I.2.a.2.1) Valor Total das Parcelas Inadimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A3_VL_CRED_INAD` | `TAB_I2A3_VL_CRED_INAD` | decimal | (I.2.a.3) Créditos Existentes Inadimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A4_VL_CRED_DIRCRED_PERFM` | `TAB_I2A4_VL_CRED_DIRCRED_PERFM` | decimal | (I.2.a.4) Créditos Referentes a Direitos Creditórios a Performar (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A5_VL_CRED_VENCIDO_PENDENTE` | `TAB_I2A5_VL_CRED_VENCIDO_PENDENTE` | decimal | (I.2.a.5) Créditos que estejam vencidos e pendentes de pagamento quando da sua cessão para o fundo (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A6_VL_CRED_EMP_RECUP` | `TAB_I2A6_VL_CRED_EMP_RECUP` | decimal | (I.2.a.6) Créditos Originados de Empresas em Processo de Recuperação Judicial ou Extrajudicial (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A7_VL_CRED_RECEITA_PUBLICA` | `TAB_I2A7_VL_CRED_RECEITA_PUBLICA` | decimal | (I.2.a.7) Créditos decorrentes de receitas públicas originárias ou derivadas da União, Estados, Distrito Federal e Municípios, suas Autarquias e Fundações (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A8_VL_CRED_ACAO_JUDIC` | `TAB_I2A8_VL_CRED_ACAO_JUDIC` | decimal | (I.2.a.8) Créditos que resultem de ações judiciais em curso, constituam seu objeto de litígio ou tenham sido judicialmente penhorados ou dados em garantia (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A9_VL_CRED_FATOR_RISCO` | `TAB_I2A9_VL_CRED_FATOR_RISCO` | decimal | (I.2.a.9) Créditos cuja constituição ou validade jurídica da cessão para o fundo seja considerada um fator preponderante de risco (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A10_VL_CRED_DIVERSO` | `TAB_I2A10_VL_CRED_DIVERSO` | texto | (I.2.a.10) Outros créditos, de natureza diversa, não enquadráveis no disposto no inciso I do art. 2º da ICVM 356 (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A11_VL_REDUCAO_RECUP` | `TAB_I2A11_VL_REDUCAO_RECUP` | decimal | (I.2.a.11) Provisão para Redução no Valor de Recuperação (-) (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_1` | `TAB_I2A12_CPF_CNPJ_CEDENTE_1` | texto | (I.2.a.12) Direitos Creditórios: Cedente 1 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_1` | `TAB_I2A12_PR_CEDENTE_1` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 1 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_2` | `TAB_I2A12_CPF_CNPJ_CEDENTE_2` | texto | (I.2.a.12) Direitos Creditórios: Cedente 2 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_2` | `TAB_I2A12_PR_CEDENTE_2` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 2 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_3` | `TAB_I2A12_CPF_CNPJ_CEDENTE_3` | texto | (I.2.a.12) Direitos Creditórios: Cedente 3 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_3` | `TAB_I2A12_PR_CEDENTE_3` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 3 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_4` | `TAB_I2A12_CPF_CNPJ_CEDENTE_4` | texto | (I.2.a.12) Direitos Creditórios: Cedente 4 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_4` | `TAB_I2A12_PR_CEDENTE_4` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 4 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_5` | `TAB_I2A12_CPF_CNPJ_CEDENTE_5` | texto | (I.2.a.12) Direitos Creditórios: Cedente 5 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_5` | `TAB_I2A12_PR_CEDENTE_5` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 5 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_6` | `TAB_I2A12_CPF_CNPJ_CEDENTE_6` | texto | (I.2.a.12) Direitos Creditórios: Cedente 6 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_6` | `TAB_I2A12_PR_CEDENTE_6` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 6 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_7` | `TAB_I2A12_CPF_CNPJ_CEDENTE_7` | texto | (I.2.a.12) Direitos Creditórios: Cedente 7 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_7` | `TAB_I2A12_PR_CEDENTE_7` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 7 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_8` | `TAB_I2A12_CPF_CNPJ_CEDENTE_8` | texto | (I.2.a.12) Direitos Creditórios: Cedente 8 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_8` | `TAB_I2A12_PR_CEDENTE_8` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 8 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2A12_CPF_CNPJ_CEDENTE_9` | `TAB_I2A12_CPF_CNPJ_CEDENTE_9` | texto | (I.2.a.12) Direitos Creditórios: Cedente 9 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2A12_PR_CEDENTE_9` | `TAB_I2A12_PR_CEDENTE_9` | decimal | (I.2.a.12) Direitos Creditórios: Cedente 9 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B_VL_DIRCRED_SEM_RISCO` | `TAB_I2B_VL_DIRCRED_SEM_RISCO` | decimal | (I.2.b) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B1_VL_CRED_VENC_AD` | `TAB_I2B1_VL_CRED_VENC_AD` | decimal | (I.2.b.1) Créditos Existentes a Vencer e Adimplentes (ICVM 576) (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B2_VL_CRED_VENC_INAD` | `TAB_I2B2_VL_CRED_VENC_INAD` | decimal | (I.2.b.2) Créditos Existentes a Vencer com Parcelas Inadimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B21_VL_TOTAL_PARCELA_INAD` | `TAB_I2B21_VL_TOTAL_PARCELA_INAD` | decimal | (I.2.b.2.1) Valor Total das Parcelas Inadimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B3_VL_CRED_INAD` | `TAB_I2B3_VL_CRED_INAD` | decimal | (I.2.b.3) Créditos Existentes Inadimplentes (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B4_VL_CRED_DIRCRED_PERFM` | `TAB_I2B4_VL_CRED_DIRCRED_PERFM` | decimal | (I.2.b.4) Créditos Referentes a Direitos Creditórios a Performar (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B5_VL_CRED_VENCIDO_PENDENTE` | `TAB_I2B5_VL_CRED_VENCIDO_PENDENTE` | decimal | (I.2.b.5) Créditos que estejam vencidos e pendentes de pagamento quando da sua cessão para o fundo (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B6_VL_CRED_EMP_RECUP` | `TAB_I2B6_VL_CRED_EMP_RECUP` | decimal | (I.2.b.6) Créditos Originados de Empresas em Processo de Recuperação Judicial ou Extrajudicial (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B7_VL_CRED_RECEITA_PUBLICA` | `TAB_I2B7_VL_CRED_RECEITA_PUBLICA` | decimal | (I.2.b.7) Créditos decorrentes de receitas públicas originárias ou derivadas da União, Estados, Distrito Federal e Municípios, suas Autarquias e Fundações (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B8_VL_CRED_ACAO_JUDIC` | `TAB_I2B8_VL_CRED_ACAO_JUDIC` | decimal | (I.2.b.8) Créditos que resultem de ações judiciais em curso, constituam seu objeto de litígio ou tenham sido judicialmente penhorados ou dados em garantia (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B9_VL_CRED_FATOR_RISCO` | `TAB_I2B9_VL_CRED_FATOR_RISCO` | decimal | (I.2.b.9) Créditos cuja constituição ou validade jurídica da cessão para o fundo seja considerada um fator preponderante de risco (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B10_VL_CRED_DIVERSO` | `TAB_I2B10_VL_CRED_DIVERSO` | texto | (I.2.b.10) Outros créditos, de natureza diversa, não enquadráveis no disposto no inciso I do art. 2º da ICVM 356 (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B11_VL_REDUCAO_RECUP` | `TAB_I2B11_VL_REDUCAO_RECUP` | decimal | (I.2.b.11) Provisão para Redução no Valor de Recuperação (-) (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_1` | `TAB_I2B12_CPF_CNPJ_CEDENTE_1` | texto | (I.2.b.12) Direitos Creditórios: Cedente 1 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_1` | `TAB_I2B12_PR_CEDENTE_1` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 1 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_2` | `TAB_I2B12_CPF_CNPJ_CEDENTE_2` | texto | (I.2.b.12) Direitos Creditórios: Cedente 2 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_2` | `TAB_I2B12_PR_CEDENTE_2` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 2 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_3` | `TAB_I2B12_CPF_CNPJ_CEDENTE_3` | texto | (I.2.b.12) Direitos Creditórios: Cedente 3 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_3` | `TAB_I2B12_PR_CEDENTE_3` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 3 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_4` | `TAB_I2B12_CPF_CNPJ_CEDENTE_4` | texto | (I.2.b.12) Direitos Creditórios: Cedente 4 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_4` | `TAB_I2B12_PR_CEDENTE_4` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 4 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_5` | `TAB_I2B12_CPF_CNPJ_CEDENTE_5` | texto | (I.2.b.12) Direitos Creditórios: Cedente 5 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_5` | `TAB_I2B12_PR_CEDENTE_5` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 5 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_6` | `TAB_I2B12_CPF_CNPJ_CEDENTE_6` | texto | (I.2.b.12) Direitos Creditórios: Cedente 6 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_6` | `TAB_I2B12_PR_CEDENTE_6` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 6 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_7` | `TAB_I2B12_CPF_CNPJ_CEDENTE_7` | texto | (I.2.b.12) Direitos Creditórios: Cedente 7 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_7` | `TAB_I2B12_PR_CEDENTE_7` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 7 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_8` | `TAB_I2B12_CPF_CNPJ_CEDENTE_8` | texto | (I.2.b.12) Direitos Creditórios: Cedente 8 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_8` | `TAB_I2B12_PR_CEDENTE_8` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 8 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2B12_CPF_CNPJ_CEDENTE_9` | `TAB_I2B12_CPF_CNPJ_CEDENTE_9` | texto | (I.2.b.12) Direitos Creditórios: Cedente 9 - CPF ou CNPJ (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2B12_PR_CEDENTE_9` | `TAB_I2B12_PR_CEDENTE_9` | decimal | (I.2.b.12) Direitos Creditórios: Cedente 9 - Valor do Percentual de Participação (só em: `inf_mensal_fidc_tab_i`) | percentual (%) | todo |
| `TAB_I2C_VL_VLMOB` | `TAB_I2C_VL_VLMOB` | decimal | (I.2.c) Valores Mobiliários (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2C1_VL_DEBENTURE` | `TAB_I2C1_VL_DEBENTURE` | decimal | (I.2.c.1) Debêntures (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2C2_VL_CRI` | `TAB_I2C2_VL_CRI` | decimal | (I.2.c.2) CRI (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2C3_VL_NP_COMERC` | `TAB_I2C3_VL_NP_COMERC` | decimal | (I.2.c.3) Notas Promissórias Comerciais (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2C4_VL_LETRA_FINANC` | `TAB_I2C4_VL_LETRA_FINANC` | decimal | (I.2.c.4) Letras Financeiras (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2C5_VL_COTA_FUNDO_ICVM555` | `TAB_I2C5_VL_COTA_FUNDO_ICVM555` | texto | (I.2.c.5) Cotas de Fundos da ICVM 555 (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2C5_VL_COTA_FIF` | `TAB_I2C5_VL_COTA_FIF` | decimal | (I.2.c.5) Classes de Cotas dos FIF - Anexo I da RCVM 175 (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2C6_VL_OUTRO` | `TAB_I2C6_VL_OUTRO` | decimal | (I.2.c.6) Outros (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2D_VL_TITPUB_FED` | `TAB_I2D_VL_TITPUB_FED` | decimal | (I.2.d) Títulos Públicos Federais (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2E_VL_CDB` | `TAB_I2E_VL_CDB` | decimal | (I.2.e) Certificados de Depósitos Bancários (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2F_VL_OPER_COMPROM` | `TAB_I2F_VL_OPER_COMPROM` | decimal | (I.2.f) Aplicações em Operações Compromissadas (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2G_VL_OUTRO_RF` | `TAB_I2G_VL_OUTRO_RF` | decimal | (I.2.g) Outros Ativos Financeiros de Renda Fixa (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2H_VL_COTA_FIDC` | `TAB_I2H_VL_COTA_FIDC` | decimal | (I.2.h) Cotas de Fundos de Investimento em Direitos Creditórios (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2I_VL_COTA_FIDC_NP` | `TAB_I2I_VL_COTA_FIDC_NP` | texto | (I.2.i) Cotas de Fundos de Investimento em Direitos Creditórios Não Padronizados (só em: `inf_mensal_fidc_tab_i`) | — | todo |
| `TAB_I2J_VL_CONTRATO_FUTURO` | `TAB_I2J_VL_CONTRATO_FUTURO` | decimal | (I.2.j) Warrants, Contrato de Compra e Venda de Produtos, Mercadorias e/ou Serviços para Entrega ou Prestação Futura (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2_DEBENTURE_CRI` | `TAB_I2_DEBENTURE_CRI` | decimal | (I.2) (-) Provisões sobre Debêntures, CRI, Notas Promissórias e Letras Financeiras (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2_COTA_FIDC` | `TAB_I2_COTA_FIDC` | decimal | (I.2) (-) Provisões sobre Cotas de Fundos de Investimento em Direitos Creditórios (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I2_VL_OUTRO_ATIVO` | `TAB_I2_VL_OUTRO_ATIVO` | decimal | (I.2) (-) Provisões sobre outros ativos (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3_VL_POSICAO_DERIV` | `TAB_I3_VL_POSICAO_DERIV` | decimal | (I.3) Posições Mantidas em Mercados de Derivativos (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3A_VL_MERCADO_TERMO` | `TAB_I3A_VL_MERCADO_TERMO` | decimal | (I.3.a) Mercado a Termo - Posições Compradas (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3B_VL_MERCADO_OPCAO` | `TAB_I3B_VL_MERCADO_OPCAO` | decimal | (I.3.b) Mercado de Opções - Posições Titulares (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3C_VL_MERCADO_FUTURO` | `TAB_I3C_VL_MERCADO_FUTURO` | decimal | (I.3.c) Mercado Futuro - Ajustes Positivos (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3D_VL_DIFER_SWAP` | `TAB_I3D_VL_DIFER_SWAP` | decimal | (I.3.d) Diferencial de Swap a Receber (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3E_VL_COBERTURA` | `TAB_I3E_VL_COBERTURA` | decimal | (I.3.e) Coberturas Prestadas (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I3F_VL_DEPOSITO_MARGEM` | `TAB_I3F_VL_DEPOSITO_MARGEM` | decimal | (I.3.f) Depósitos de Margem (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I4_VL_OUTRO_ATIVO` | `TAB_I4_VL_OUTRO_ATIVO` | decimal | (I.4) Outros Ativos (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I4A_VL_CPRAZO` | `TAB_I4A_VL_CPRAZO` | decimal | (I.4.a) Curto Prazo (realização em até 12 meses da data do informe) (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_I4B_VL_LPRAZO` | `TAB_I4B_VL_LPRAZO` | decimal | (I.4.b) Longo Prazo (realização após 12 meses da data do informe) (só em: `inf_mensal_fidc_tab_i`) | moeda (R$) | todo |
| `TAB_II_VL_CARTEIRA` | `TAB_II_VL_CARTEIRA` | decimal | (Tabela II) Carteira por Segmento (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_A_VL_INDUST` | `TAB_II_A_VL_INDUST` | decimal | (II.a) Industrial (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_B_VL_IMOBIL` | `TAB_II_B_VL_IMOBIL` | decimal | (II.b) Mercado Imobiliário (não financeiro - ver itens f6 e f7) (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_C_VL_COMERC` | `TAB_II_C_VL_COMERC` | decimal | (II.c) Comercial (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_C1_VL_COMERC` | `TAB_II_C1_VL_COMERC` | decimal | (II.c.1) Comercial (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_C2_VL_VAREJO` | `TAB_II_C2_VL_VAREJO` | decimal | (II.c.2) Comercial - Varejo (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_C3_VL_ARREND` | `TAB_II_C3_VL_ARREND` | decimal | (II.c.3) Arrendamento Mercantil (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_D_VL_SERV` | `TAB_II_D_VL_SERV` | decimal | (II.d) Serviços (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_D1_VL_SERV` | `TAB_II_D1_VL_SERV` | decimal | (II.d.1) Serviços (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_D2_VL_SERV_PUBLICO` | `TAB_II_D2_VL_SERV_PUBLICO` | decimal | (II.d.2) Serviços Públicos (eletricidade, telefonia, transporte, saneamento, etc) (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_D3_VL_SERV_EDUC` | `TAB_II_D3_VL_SERV_EDUC` | decimal | (II.d.3) Serviços Educacionais (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_D4_VL_ENTRET` | `TAB_II_D4_VL_ENTRET` | decimal | (II.d.4) Entretenimento (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_E_VL_AGRONEG` | `TAB_II_E_VL_AGRONEG` | decimal | (II.e) Agronegócio (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F_VL_FINANC` | `TAB_II_F_VL_FINANC` | decimal | (II.f) Financeiro (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F1_VL_CRED_PESSOA` | `TAB_II_F1_VL_CRED_PESSOA` | decimal | (II.f.1) Crédito Pessoal (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F2_VL_CRED_PESSOA_CONSIG` | `TAB_II_F2_VL_CRED_PESSOA_CONSIG` | decimal | (II.f.2) Crédito Pessoal Consignado (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F3_VL_CRED_CORP` | `TAB_II_F3_VL_CRED_CORP` | decimal | (II.f.3) Direitos Crédito Corporativo (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F4_VL_MIDMARKET` | `TAB_II_F4_VL_MIDMARKET` | decimal | (II.f.4) Middle Market (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F5_VL_VEICULO` | `TAB_II_F5_VL_VEICULO` | decimal | (II.f.5) Veículos (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F6_VL_IMOBIL_EMPRESA` | `TAB_II_F6_VL_IMOBIL_EMPRESA` | decimal | (II.f.6) Carteira Imobiliária - Empresarial (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F7_VL_IMOBIL_RESID` | `TAB_II_F7_VL_IMOBIL_RESID` | decimal | (II.f.7) Carteira Imobiliária - Residencial (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_F8_VL_OUTRO` | `TAB_II_F8_VL_OUTRO` | decimal | (II.f.8) Outros (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_G_VL_CREDITO` | `TAB_II_G_VL_CREDITO` | decimal | (II.g) Cartão de Crédito (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_H_VL_FACTOR` | `TAB_II_H_VL_FACTOR` | decimal | (II.h) Factoring (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_H1_VL_PESSOA` | `TAB_II_H1_VL_PESSOA` | decimal | (II.h.1) Factoring - Pessoal (Perfil do Sacado) (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_H2_VL_CORP` | `TAB_II_H2_VL_CORP` | decimal | (II.h.2) Factoring - Corporativo (Perfil do Sacado) (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_I_VL_SETOR_PUBLICO` | `TAB_II_I_VL_SETOR_PUBLICO` | decimal | (II.i) Setor Público (art. 1º, §1º, II, ICVM 444) (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_I1_VL_PRECAT` | `TAB_II_I1_VL_PRECAT` | decimal | (II.i.1) Precatórios (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_I2_VL_TRIBUT` | `TAB_II_I2_VL_TRIBUT` | decimal | (II.i.2) Créditos Tributários (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_I3_VL_ROYALTIES` | `TAB_II_I3_VL_ROYALTIES` | decimal | (II.i.3) Royalties (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_I4_VL_OUTRO` | `TAB_II_I4_VL_OUTRO` | decimal | (II.i.4) Outros (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_J_VL_JUDICIAL` | `TAB_II_J_VL_JUDICIAL` | decimal | (II.j) Ações Judiciais (art. 1º, §1º, III, ICVM 444) (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_II_K_VL_MARCA` | `TAB_II_K_VL_MARCA` | decimal | (II.k) Propriedade Intelectual e Marcas & Patentes (só em: `inf_mensal_fidc_tab_ii`) | moeda (R$) | todo |
| `TAB_III_VL_PASSIVO` | `TAB_III_VL_PASSIVO` | decimal | (Tabela III) Passivo (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_A_VL_PAGAR` | `TAB_III_A_VL_PAGAR` | decimal | (III.a) Valores a pagar (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_A1_VL_CPRAZO` | `TAB_III_A1_VL_CPRAZO` | decimal | (III.a.1) Curto Prazo (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_A2_VL_LPRAZO` | `TAB_III_A2_VL_LPRAZO` | decimal | (III.a.2) Longo Prazo (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_B_VL_POSICAO_DERIV` | `TAB_III_B_VL_POSICAO_DERIV` | decimal | (III.b) Posições Mantidas em Mercado de Derivativos (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_B1_VL_TERMO` | `TAB_III_B1_VL_TERMO` | decimal | (III.b.1) Mercado a termo (Posições vendidas) (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_B2_VL_OPCAO` | `TAB_III_B2_VL_OPCAO` | decimal | (III.b.2) Mercado de Opções (Posições Lançadas) (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_B3_VL_FUTURO` | `TAB_III_B3_VL_FUTURO` | decimal | (III.b.3) Mercado Futuro (Ajustes Negativos) (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_III_B4_VL_SWAP_PAGAR` | `TAB_III_B4_VL_SWAP_PAGAR` | decimal | (III.b.4) Diferencial de Swap a Pagar (só em: `inf_mensal_fidc_tab_iii`) | moeda (R$) | todo |
| `TAB_IV_A_VL_PL` | `TAB_IV_A_VL_PL` | decimal | (IV.a) Valor do Patrimônio Líquido (só em: `inf_mensal_fidc_tab_iv`) | moeda (R$) | todo |
| `TAB_IV_B_VL_PL_MEDIO` | `TAB_IV_B_VL_PL_MEDIO` | decimal | (IV.b) Valor do Patrimônio Líquido Médio (últimos três meses) (só em: `inf_mensal_fidc_tab_iv`) | moeda (R$) | todo |
| `TAB_IX_A1_1_1_COMPRA_MIN` | `TAB_IX_A1_1_1_COMPRA_MIN` | decimal | (IX.a.1.1.1) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A1_1_2_COMPRA_MEDIA` | `TAB_IX_A1_1_2_COMPRA_MEDIA` | decimal | (IX.a.1.1.2) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A1_1_3_COMPRA_MAX` | `TAB_IX_A1_1_3_COMPRA_MAX` | decimal | (IX.a.1.1.3) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A1_2_1_VENDA_MIN` | `TAB_IX_A1_2_1_VENDA_MIN` | decimal | (IX.a.1.2.1) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A1_2_2_VENDA_MEDIA` | `TAB_IX_A1_2_2_VENDA_MEDIA` | decimal | (IX.a.1.2.2) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A1_2_3_VENDA_MAX` | `TAB_IX_A1_2_3_VENDA_MAX` | decimal | (IX.a.1.2.3) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A2_1_1_COMPRA_MIN` | `TAB_IX_A2_1_1_COMPRA_MIN` | decimal | (IX.a.2.1.1) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A2_1_2_COMPRA_MEDIA` | `TAB_IX_A2_1_2_COMPRA_MEDIA` | decimal | (IX.a.2.1.2) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A2_1_3_COMPRA_MAX` | `TAB_IX_A2_1_3_COMPRA_MAX` | decimal | (IX.a.2.1.3) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A2_2_1_VENDA_MIN` | `TAB_IX_A2_2_1_VENDA_MIN` | decimal | (IX.a.2.2.1) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A2_2_2_VENDA_MEDIA` | `TAB_IX_A2_2_2_VENDA_MEDIA` | decimal | (IX.a.2.2.2) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_A2_2_3_VENDA_MAX` | `TAB_IX_A2_2_3_VENDA_MAX` | decimal | (IX.a.2.2.3) Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B1_1_1_COMPRA_MIN` | `TAB_IX_B1_1_1_COMPRA_MIN` | decimal | (IX.b.1.1.1) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B1_1_2_COMPRA_MEDIA` | `TAB_IX_B1_1_2_COMPRA_MEDIA` | decimal | (IX.b.1.1.2) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B1_1_3_COMPRA_MAX` | `TAB_IX_B1_1_3_COMPRA_MAX` | decimal | (IX.b.1.1.3) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B1_2_1_VENDA_MIN` | `TAB_IX_B1_2_1_VENDA_MIN` | decimal | (IX.b.1.2.1) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B1_2_2_VENDA_MEDIA` | `TAB_IX_B1_2_2_VENDA_MEDIA` | decimal | (IX.b.1.2.2) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B1_2_3_VENDA_MAX` | `TAB_IX_B1_2_3_VENDA_MAX` | decimal | (IX.b.1.2.3) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa desconto (da aquisição) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B2_1_1_COMPRA_MIN` | `TAB_IX_B2_1_1_COMPRA_MIN` | decimal | (IX.b.2.1.1) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B2_1_2_COMPRA_MEDIA` | `TAB_IX_B2_1_2_COMPRA_MEDIA` | decimal | (IX.b.2.1.2) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B2_1_3_COMPRA_MAX` | `TAB_IX_B2_1_3_COMPRA_MAX` | decimal | (IX.b.2.1.3) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B2_2_1_VENDA_MIN` | `TAB_IX_B2_2_1_VENDA_MIN` | decimal | (IX.b.2.2.1) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B2_2_2_VENDA_MEDIA` | `TAB_IX_B2_2_2_VENDA_MEDIA` | decimal | (IX.b.2.2.2) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_B2_2_3_VENDA_MAX` | `TAB_IX_B2_2_3_VENDA_MAX` | decimal | (IX.b.2.2.3) Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Taxa de Juros(dos direitos creditórios) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C1_1_1_COMPRA_MIN` | `TAB_IX_C1_1_1_COMPRA_MIN` | decimal | (IX.c.1.1.1) Valores Mobiliários / Taxa desconto (da aquisição) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C1_1_2_COMPRA_MEDIA` | `TAB_IX_C1_1_2_COMPRA_MEDIA` | decimal | (IX.c.1.1.2) Valores Mobiliários / Taxa desconto (da aquisição) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C1_1_3_COMPRA_MAX` | `TAB_IX_C1_1_3_COMPRA_MAX` | decimal | (IX.c.1.1.3) Valores Mobiliários / Taxa desconto (da aquisição) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C1_2_1_VENDA_MIN` | `TAB_IX_C1_2_1_VENDA_MIN` | decimal / inteiro | (IX.c.1.2.1) Valores Mobiliários / Taxa desconto (da aquisição) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C1_2_2_VENDA_MEDIA` | `TAB_IX_C1_2_2_VENDA_MEDIA` | decimal / inteiro | (IX.c.1.2.2) Valores Mobiliários / Taxa desconto (da aquisição) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C1_2_3_VENDA_MAX` | `TAB_IX_C1_2_3_VENDA_MAX` | decimal | (IX.c.1.2.3) Valores Mobiliários / Taxa desconto (da aquisição) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C2_1_1_COMPRA_MIN` | `TAB_IX_C2_1_1_COMPRA_MIN` | inteiro | (IX.c.2.1.1) Valores Mobiliários / Taxa de Juros / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C2_1_2_COMPRA_MEDIA` | `TAB_IX_C2_1_2_COMPRA_MEDIA` | inteiro | (IX.c.2.1.2) Valores Mobiliários / Taxa de Juros / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C2_1_3_COMPRA_MAX` | `TAB_IX_C2_1_3_COMPRA_MAX` | inteiro | (IX.c.2.1.3) Valores Mobiliários / Taxa de Juros / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C2_2_1_VENDA_MIN` | `TAB_IX_C2_2_1_VENDA_MIN` | inteiro | (IX.c.2.2.1) Valores Mobiliários / Taxa de Juros / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C2_2_2_VENDA_MEDIA` | `TAB_IX_C2_2_2_VENDA_MEDIA` | inteiro | (IX.c.2.2.2) Valores Mobiliários / Taxa de Juros / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_C2_2_3_VENDA_MAX` | `TAB_IX_C2_2_3_VENDA_MAX` | inteiro | (IX.c.2.2.3) Valores Mobiliários / Taxa de Juros / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D1_1_1_COMPRA_MIN` | `TAB_IX_D1_1_1_COMPRA_MIN` | decimal | (IX.d.1.1.1) Títulos Públicos Federais / Taxa desconto (da aquisição) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D1_1_2_COMPRA_MEDIA` | `TAB_IX_D1_1_2_COMPRA_MEDIA` | decimal | (IX.d.1.1.2) Títulos Públicos Federais / Taxa desconto (da aquisição) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D1_1_3_COMPRA_MAX` | `TAB_IX_D1_1_3_COMPRA_MAX` | decimal | (IX.d.1.1.3) Títulos Públicos Federais / Taxa desconto (da aquisição) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D1_2_1_VENDA_MIN` | `TAB_IX_D1_2_1_VENDA_MIN` | decimal / inteiro | (IX.d.1.2.1) Títulos Públicos Federais / Taxa desconto (da aquisição) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D1_2_2_VENDA_MEDIA` | `TAB_IX_D1_2_2_VENDA_MEDIA` | decimal / inteiro | (IX.d.1.2.2) Títulos Públicos Federais / Taxa desconto (da aquisição) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D1_2_3_VENDA_MAX` | `TAB_IX_D1_2_3_VENDA_MAX` | decimal / inteiro | (IX.d.1.2.3) Títulos Públicos Federais / Taxa desconto (da aquisição) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D2_1_1_COMPRA_MIN` | `TAB_IX_D2_1_1_COMPRA_MIN` | decimal | (IX.d.2.1.1) Títulos Públicos Federais / Taxa de Juros / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D2_1_2_COMPRA_MEDIA` | `TAB_IX_D2_1_2_COMPRA_MEDIA` | decimal | (IX.d.2.1.2) Títulos Públicos Federais / Taxa de Juros / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D2_1_3_COMPRA_MAX` | `TAB_IX_D2_1_3_COMPRA_MAX` | decimal | (IX.d.2.1.3) Títulos Públicos Federais / Taxa de Juros / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D2_2_1_VENDA_MIN` | `TAB_IX_D2_2_1_VENDA_MIN` | inteiro | (IX.d.2.2.1) Títulos Públicos Federais / Taxa de Juros / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D2_2_2_VENDA_MEDIA` | `TAB_IX_D2_2_2_VENDA_MEDIA` | inteiro | (IX.d.2.2.2) Títulos Públicos Federais / Taxa de Juros / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_D2_2_3_VENDA_MAX` | `TAB_IX_D2_2_3_VENDA_MAX` | inteiro | (IX.d.2.2.3) Títulos Públicos Federais / Taxa de Juros / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E1_1_1_COMPRA_MIN` | `TAB_IX_E1_1_1_COMPRA_MIN` | inteiro | (IX.e.1.1.1) Certificados de Depósitos Bancários / Taxa desconto (da aquisição) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E1_1_2_COMPRA_MEDIA` | `TAB_IX_E1_1_2_COMPRA_MEDIA` | inteiro | (IX.e.1.1.2) Certificados de Depósitos Bancários / Taxa desconto (da aquisição) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E1_1_3_COMPRA_MAX` | `TAB_IX_E1_1_3_COMPRA_MAX` | inteiro | (IX.e.1.1.3) Certificados de Depósitos Bancários / Taxa desconto (da aquisição) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E1_2_1_VENDA_MIN` | `TAB_IX_E1_2_1_VENDA_MIN` | inteiro | (IX.e.1.2.1) Certificados de Depósitos Bancários / Taxa desconto (da aquisição) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E1_2_2_VENDA_MEDIA` | `TAB_IX_E1_2_2_VENDA_MEDIA` | inteiro | (IX.e.1.2.2) Certificados de Depósitos Bancários / Taxa desconto (da aquisição) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E1_2_3_VENDA_MAX` | `TAB_IX_E1_2_3_VENDA_MAX` | inteiro | (IX.e.1.2.3) Certificados de Depósitos Bancários / Taxa desconto (da aquisição) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E2_1_1_COMPRA_MIN` | `TAB_IX_E2_1_1_COMPRA_MIN` | inteiro | (IX.e.2.1.1) Certificados de Depósitos Bancários / Taxa de Juros / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E2_1_2_COMPRA_MEDIA` | `TAB_IX_E2_1_2_COMPRA_MEDIA` | inteiro | (IX.e.2.1.2) Certificados de Depósitos Bancários / Taxa de Juros / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E2_1_3_COMPRA_MAX` | `TAB_IX_E2_1_3_COMPRA_MAX` | inteiro | (IX.e.2.1.3) Certificados de Depósitos Bancários / Taxa de Juros / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E2_2_1_VENDA_MIN` | `TAB_IX_E2_2_1_VENDA_MIN` | inteiro | (IX.e.2.2.1) Certificados de Depósitos Bancários / Taxa de Juros / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E2_2_2_VENDA_MEDIA` | `TAB_IX_E2_2_2_VENDA_MEDIA` | inteiro | (IX.e.2.2.2) Certificados de Depósitos Bancários / Taxa de Juros / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_E2_2_3_VENDA_MAX` | `TAB_IX_E2_2_3_VENDA_MAX` | inteiro | (IX.e.2.2.3) Certificados de Depósitos Bancários / Taxa de Juros / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F1_1_1_COMPRA_MIN` | `TAB_IX_F1_1_1_COMPRA_MIN` | decimal | (IX.f.1.1.1) Outros Ativos Financeiros de Renda Fixa / Taxa desconto (da aquisição) / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F1_1_2_COMPRA_MEDIA` | `TAB_IX_F1_1_2_COMPRA_MEDIA` | decimal | (IX.f.1.1.2) Outros Ativos Financeiros de Renda Fixa / Taxa desconto (da aquisição) / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F1_1_3_COMPRA_MAX` | `TAB_IX_F1_1_3_COMPRA_MAX` | decimal | (IX.f.1.1.3) Outros Ativos Financeiros de Renda Fixa / Taxa desconto (da aquisição) / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F1_2_1_VENDA_MIN` | `TAB_IX_F1_2_1_VENDA_MIN` | decimal / inteiro | (IX.f.1.2.1) Outros Ativos Financeiros de Renda Fixa / Taxa desconto (da aquisição) / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F1_2_2_VENDA_MEDIA` | `TAB_IX_F1_2_2_VENDA_MEDIA` | decimal / inteiro | (IX.f.1.2.2) Outros Ativos Financeiros de Renda Fixa / Taxa desconto (da aquisição) / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F1_2_3_VENDA_MAX` | `TAB_IX_F1_2_3_VENDA_MAX` | decimal / inteiro | (IX.f.1.2.3) Outros Ativos Financeiros de Renda Fixa / Taxa desconto (da aquisição) / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F2_1_1_COMPRA_MIN` | `TAB_IX_F2_1_1_COMPRA_MIN` | decimal | (IX.f.2.1.1) Outros Ativos Financeiros de Renda Fixa / Taxa de Juros / Compra / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F2_1_2_COMPRA_MEDIA` | `TAB_IX_F2_1_2_COMPRA_MEDIA` | decimal | (IX.f.2.1.2) Outros Ativos Financeiros de Renda Fixa / Taxa de Juros / Compra / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F2_1_3_COMPRA_MAX` | `TAB_IX_F2_1_3_COMPRA_MAX` | decimal | (IX.f.2.1.3) Outros Ativos Financeiros de Renda Fixa / Taxa de Juros / Compra / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F2_2_1_VENDA_MIN` | `TAB_IX_F2_2_1_VENDA_MIN` | inteiro | (IX.f.2.2.1) Outros Ativos Financeiros de Renda Fixa / Taxa de Juros / Venda / Mínina (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F2_2_2_VENDA_MEDIA` | `TAB_IX_F2_2_2_VENDA_MEDIA` | inteiro | (IX.f.2.2.2) Outros Ativos Financeiros de Renda Fixa / Taxa de Juros / Venda / Média (Ponderada) (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_IX_F2_2_3_VENDA_MAX` | `TAB_IX_F2_2_3_VENDA_MAX` | inteiro | (IX.f.2.2.3) Outros Ativos Financeiros de Renda Fixa / Taxa de Juros / Venda / Máxima (só em: `inf_mensal_fidc_tab_ix`) | moeda (R$) | todo |
| `TAB_V_A_VL_DIRCRED_PRAZO` | `TAB_V_A_VL_DIRCRED_PRAZO` | decimal | (V.a) Por Prazo de Vencimento (R$) (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A1_VL_PRAZO_VENC_30` | `TAB_V_A1_VL_PRAZO_VENC_30` | decimal | (V.a.1) Até 30 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A2_VL_PRAZO_VENC_60` | `TAB_V_A2_VL_PRAZO_VENC_60` | decimal | (V.a.2) De 31 a 60 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A3_VL_PRAZO_VENC_90` | `TAB_V_A3_VL_PRAZO_VENC_90` | decimal | (V.a.3)  De 61 a 90 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A4_VL_PRAZO_VENC_120` | `TAB_V_A4_VL_PRAZO_VENC_120` | decimal | (V.a.4) De 91 a 120 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A5_VL_PRAZO_VENC_150` | `TAB_V_A5_VL_PRAZO_VENC_150` | decimal | (V.a.5) De 121 a 150 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A6_VL_PRAZO_VENC_180` | `TAB_V_A6_VL_PRAZO_VENC_180` | decimal | (V.a.6) De 151 a 180 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A7_VL_PRAZO_VENC_360` | `TAB_V_A7_VL_PRAZO_VENC_360` | decimal | (V.a.7) De 181 a 360 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A8_VL_PRAZO_VENC_720` | `TAB_V_A8_VL_PRAZO_VENC_720` | decimal | (V.a.8) De 361 a 720 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A9_VL_PRAZO_VENC_1080` | `TAB_V_A9_VL_PRAZO_VENC_1080` | decimal | (V.a.9) De 721 a 1080 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_A10_VL_PRAZO_VENC_MAIOR_1080` | `TAB_V_A10_VL_PRAZO_VENC_MAIOR_1080` | decimal | (V.a.10) Acima de 1080 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B_VL_DIRCRED_INAD` | `TAB_V_B_VL_DIRCRED_INAD` | decimal | (V.b) Inadimplentes (Valor das Parcelas Inadimplentes, em R$) (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B1_VL_INAD_30` | `TAB_V_B1_VL_INAD_30` | decimal | (V.b.1) Vencidos e não Pagos entre 1 e 30 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B2_VL_INAD_60` | `TAB_V_B2_VL_INAD_60` | decimal | (V.b.2) Vencidos e não Pagos entre 31 e 60 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B3_VL_INAD_90` | `TAB_V_B3_VL_INAD_90` | decimal | (V.b.3) Vencidos e não Pagos entre 61 e 90 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B4_VL_INAD_120` | `TAB_V_B4_VL_INAD_120` | decimal | (V.b.4) Vencidos e não Pagos entre 91 e 120 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B5_VL_INAD_150` | `TAB_V_B5_VL_INAD_150` | decimal | (V.b.5) Vencidos e não Pagos entre 121 e 150 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B6_VL_INAD_180` | `TAB_V_B6_VL_INAD_180` | decimal | (V.b.6) Vencidos e não Pagos entre 151 e 180 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B7_VL_INAD_360` | `TAB_V_B7_VL_INAD_360` | decimal | (V.b.7) Vencidos e não Pagos entre 181 e 360 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B8_VL_INAD_720` | `TAB_V_B8_VL_INAD_720` | decimal | (V.b.8) Vencidos e não Pagos entre 361 e 720 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B9_VL_INAD_1080` | `TAB_V_B9_VL_INAD_1080` | decimal | (V.b.9) Vencidos e não Pagos entre 721 e 1080 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_B10_VL_INAD_MAIOR_1080` | `TAB_V_B10_VL_INAD_MAIOR_1080` | decimal | (V.b.10) Vencidos e não Pagos acima de 1080 dias (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C_VL_DIRCRED_ANTECIPADO` | `TAB_V_C_VL_DIRCRED_ANTECIPADO` | decimal | (V.c) Pagos Antecipadamente (R$) (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C1_VL_ANTECIPADO_30` | `TAB_V_C1_VL_ANTECIPADO_30` | decimal | (V.c.1) Pagos Antecipadamente entre 1 e 30 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C2_VL_ANTECIPADO_60` | `TAB_V_C2_VL_ANTECIPADO_60` | decimal | (V.c.2) Pagos Antecipadamente entre 31 e 60 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C3_VL_ANTECIPADO_90` | `TAB_V_C3_VL_ANTECIPADO_90` | decimal | (V.c.3) Pagos Antecipadamente entre 61 e 90 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C4_VL_ANTECIPADO_120` | `TAB_V_C4_VL_ANTECIPADO_120` | decimal | (V.c.4) Pagos Antecipadamente entre 91 e 120 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C5_VL_ANTECIPADO_150` | `TAB_V_C5_VL_ANTECIPADO_150` | decimal | (V.c.5) Pagos Antecipadamente entre 121 e 150 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C6_VL_ANTECIPADO_180` | `TAB_V_C6_VL_ANTECIPADO_180` | decimal | (V.c.6) Pagos Antecipadamente entre 151 e 180 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C7_VL_ANTECIPADO_360` | `TAB_V_C7_VL_ANTECIPADO_360` | decimal | (V.c.7) Pagos Antecipadamente entre 181 e 360 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C8_VL_ANTECIPADO_720` | `TAB_V_C8_VL_ANTECIPADO_720` | decimal | (V.c.8) Pagos Antecipadamente entre 361 e 720 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C9_VL_ANTECIPADO_1080` | `TAB_V_C9_VL_ANTECIPADO_1080` | decimal | (V.c.9) Pagos Antecipadamente entre 721 e 1080 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_V_C10_VL_ANTECIPADO_MAIOR_1080` | `TAB_V_C10_VL_ANTECIPADO_MAIOR_1080` | decimal | (V.c.10) Pagos Antecipadamente acima de 1080 dias do vencimento (só em: `inf_mensal_fidc_tab_v`) | moeda (R$) | todo |
| `TAB_VI_A_VL_DIRCRED_PRAZO` | `TAB_VI_A_VL_DIRCRED_PRAZO` | decimal | (VI.a) Por Prazo de Vencimento (R$) (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A1_VL_PRAZO_VENC_30` | `TAB_VI_A1_VL_PRAZO_VENC_30` | decimal | (VI.a.1) Até 30 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A2_VL_PRAZO_VENC_60` | `TAB_VI_A2_VL_PRAZO_VENC_60` | decimal | (VI.a.2) De 31 a 60 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A3_VL_PRAZO_VENC_90` | `TAB_VI_A3_VL_PRAZO_VENC_90` | decimal | (VI.a.3)  De 61 a 90 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A4_VL_PRAZO_VENC_120` | `TAB_VI_A4_VL_PRAZO_VENC_120` | decimal | (VI.a.4) De 91 a 120 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A5_VL_PRAZO_VENC_150` | `TAB_VI_A5_VL_PRAZO_VENC_150` | decimal | (VI.a.5) De 121 a 150 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A6_VL_PRAZO_VENC_180` | `TAB_VI_A6_VL_PRAZO_VENC_180` | decimal | (VI.a.6) De 151 a 180 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A7_VL_PRAZO_VENC_360` | `TAB_VI_A7_VL_PRAZO_VENC_360` | decimal | (VI.a.7) De 181 a 360 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A8_VL_PRAZO_VENC_720` | `TAB_VI_A8_VL_PRAZO_VENC_720` | decimal | (VI.a.8) De 361 a 720 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A9_VL_PRAZO_VENC_1080` | `TAB_VI_A9_VL_PRAZO_VENC_1080` | decimal | (VI.a.9) De 721 a 1080 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_A10_VL_PRAZO_VENC_MAIOR_1080` | `TAB_VI_A10_VL_PRAZO_VENC_MAIOR_1080` | decimal | (VI.a.10) Acima de 1080 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B_VL_DIRCRED_INAD` | `TAB_VI_B_VL_DIRCRED_INAD` | decimal | (VI.b) Inadimplentes (Valor das Parcelas Inadimplentes, em R$) (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B1_VL_INAD_30` | `TAB_VI_B1_VL_INAD_30` | decimal | (VI.b.1) Vencidos e não Pagos entre 1 e 30 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B2_VL_INAD_60` | `TAB_VI_B2_VL_INAD_60` | decimal | (VI.b.2) Vencidos e não Pagos entre 31 e 60 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B3_VL_INAD_90` | `TAB_VI_B3_VL_INAD_90` | decimal | (VI.b.3) Vencidos e não Pagos entre 61 e 90 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B4_VL_INAD_120` | `TAB_VI_B4_VL_INAD_120` | decimal | (VI.b.4) Vencidos e não Pagos entre 91 e 120 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B5_VL_INAD_150` | `TAB_VI_B5_VL_INAD_150` | decimal | (VI.b.5) Vencidos e não Pagos entre 121 e 150 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B6_VL_INAD_180` | `TAB_VI_B6_VL_INAD_180` | decimal | (VI.b.6) Vencidos e não Pagos entre 151 e 180 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B7_VL_INAD_360` | `TAB_VI_B7_VL_INAD_360` | decimal | (VI.b.7) Vencidos e não Pagos entre 181 e 360 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B8_VL_INAD_720` | `TAB_VI_B8_VL_INAD_720` | decimal | (VI.b.8) Vencidos e não Pagos entre 361 e 720 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B9_VL_INAD_1080` | `TAB_VI_B9_VL_INAD_1080` | decimal | (VI.b.9) Vencidos e não Pagos entre 721 e 1080 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_B10_VL_INAD_MAIOR_1080` | `TAB_VI_B10_VL_INAD_MAIOR_1080` | decimal | (VI.b.10) Vencidos e não Pagos acima de 1080 dias (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C_VL_DIRCRED_ANTECIPADO` | `TAB_VI_C_VL_DIRCRED_ANTECIPADO` | decimal | (VI.c) Pagos Antecipadamente (R$) (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C1_VL_ANTECIPADO_30` | `TAB_VI_C1_VL_ANTECIPADO_30` | decimal | (VI.c.1) Pagos Antecipadamente entre 1 e 30 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C2_VL_ANTECIPADO_60` | `TAB_VI_C2_VL_ANTECIPADO_60` | decimal | (VI.c.2) Pagos Antecipadamente entre 31 e 60 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C3_VL_ANTECIPADO_90` | `TAB_VI_C3_VL_ANTECIPADO_90` | decimal | (VI.c.3) Pagos Antecipadamente entre 61 e 90 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C4_VL_ANTECIPADO_120` | `TAB_VI_C4_VL_ANTECIPADO_120` | decimal | (VI.c.4) Pagos Antecipadamente entre 91 e 120 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C5_VL_ANTECIPADO_150` | `TAB_VI_C5_VL_ANTECIPADO_150` | decimal | (VI.c.5) Pagos Antecipadamente entre 121 e 150 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C6_VL_ANTECIPADO_180` | `TAB_VI_C6_VL_ANTECIPADO_180` | decimal | (VI.c.6) Pagos Antecipadamente entre 151 e 180 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C7_VL_ANTECIPADO_360` | `TAB_VI_C7_VL_ANTECIPADO_360` | decimal | (VI.c.7) Pagos Antecipadamente entre 181 e 360 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C8_VL_ANTECIPADO_720` | `TAB_VI_C8_VL_ANTECIPADO_720` | decimal | (VI.c.8) Pagos Antecipadamente entre 361 e 720 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C9_VL_ANTECIPADO_1080` | `TAB_VI_C9_VL_ANTECIPADO_1080` | decimal | (VI.c.9) Pagos Antecipadamente entre 721 e 1080 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VI_C10_VL_ANTECIPADO_MAIOR_1080` | `TAB_VI_C10_VL_ANTECIPADO_MAIOR_1080` | decimal | (VI.c.10) Pagos Antecipadamente acima de 1080 dias do vencimento (só em: `inf_mensal_fidc_tab_vi`) | moeda (R$) | todo |
| `TAB_VII_A1_1_QT_DIRCRED_RISCO` | `TAB_VII_A1_1_QT_DIRCRED_RISCO` | decimal | (VII.a.1.1) Aquisições / Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_A1_2_VL_DIRCRED_RISCO` | `TAB_VII_A1_2_VL_DIRCRED_RISCO` | decimal | (VII.a.1.2) Aquisições / Direitos Creditórios com Aquisição Substancial dos Riscos e Benefícios / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_A2_1_QT_DIRCRED_SEM_RISCO` | `TAB_VII_A2_1_QT_DIRCRED_SEM_RISCO` | decimal | (VII.a.2.1) Aquisições / Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_A2_2_VL_DIRCRED_SEM_RISCO` | `TAB_VII_A2_2_VL_DIRCRED_SEM_RISCO` | decimal | (VII.a.2.2) Aquisições / Direitos Creditórios sem Aquisição Substancial dos Riscos e Benefícios / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_A3_1_QT_DIRCRED_VENC_AD` | `TAB_VII_A3_1_QT_DIRCRED_VENC_AD` | decimal | (VII.a.3.1) Aquisições / Direitos Creditórios a Vencer e com parcela(s) Adimplentes / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_A3_2_VL_DIRCRED_VENC_AD` | `TAB_VII_A3_2_VL_DIRCRED_VENC_AD` | decimal | (VII.a.3.2) Aquisições / Direitos Creditórios a Vencer e com parcela(s) Adimplentes / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_A4_1_QT_DIRCRED_VENC_INAD` | `TAB_VII_A4_1_QT_DIRCRED_VENC_INAD` | decimal | (VII.a.4.1) Aquisições / Direitos Creditórios a Vencer com Parcelas Inadimplentes / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_A4_2_VL_DIRCRED_VENC_INAD` | `TAB_VII_A4_2_VL_DIRCRED_VENC_INAD` | decimal | (VII.a.4.2) Aquisições / Direitos Creditórios a Vencer com Parcelas Inadimplentes / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_A5_1_QT_DIRCRED_INAD` | `TAB_VII_A5_1_QT_DIRCRED_INAD` | decimal | (VII.a.5.1) Aquisições / Direitos Creditórios Inadimplentes / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_A5_2_VL_DIRCRED_INAD` | `TAB_VII_A5_2_VL_DIRCRED_INAD` | decimal | (VII.a.5.2) Aquisições / Direitos Creditórios Inadimplentes / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_B1_1_QT_CEDENTE` | `TAB_VII_B1_1_QT_CEDENTE` | decimal | (VII.b.1.1) Alienações / Para o Cedente e Partes Relacionadas aos Cedentes / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_B1_2_VL_CEDENTE` | `TAB_VII_B1_2_VL_CEDENTE` | decimal | (VII.b.1.2) Alienações / Para o Cedente e Partes Relacionadas aos Cedentes / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_B1_3_VL_CONTAB_CEDENTE` | `TAB_VII_B1_3_VL_CONTAB_CEDENTE` | decimal | (VII.b.1.3) Alienações / Para o Cedente e Partes Relacionadas aos Cedentes / Valor Contábil (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_B2_1_QT_PREST` | `TAB_VII_B2_1_QT_PREST` | decimal | (VII.b.2.1) Alienações / Para os Prestadores de Serviços e Partes Relacionadas aos Prestadores de Serviços / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_B2_2_VL_PREST` | `TAB_VII_B2_2_VL_PREST` | decimal | (VII.b.2.2) Alienações / Para os Prestadores de Serviços e Partes Relacionadas aos Prestadores de Serviços / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_B2_3_VL_CONTAB_PREST` | `TAB_VII_B2_3_VL_CONTAB_PREST` | decimal | (VII.b.2.3) Alienações / Para os Prestadores de Serviços e Partes Relacionadas aos Prestadores de Serviços / Valor Contábil (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_B3_1_QT_TERCEIRO` | `TAB_VII_B3_1_QT_TERCEIRO` | decimal | (VII.b.3.1) Alienações / Para Terceiros / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_B3_2_VL_TERCEIRO` | `TAB_VII_B3_2_VL_TERCEIRO` | decimal | (VII.b.3.2) Alienações / Para Terceiros / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_B3_3_VL_CONTAB_TERCEIRO` | `TAB_VII_B3_3_VL_CONTAB_TERCEIRO` | decimal | (VII.b.3.3) Alienações / Para Terceiros / Valor Contábil (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_C_1_QT_SUBST` | `TAB_VII_C_1_QT_SUBST` | decimal | (VII.c.1) Substituições / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_C_2_VL_SUBST` | `TAB_VII_C_2_VL_SUBST` | decimal | (VII.c.2) Substituições / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_C_3_VL_CONTAB_SUBST` | `TAB_VII_C_3_VL_CONTAB_SUBST` | decimal | (VII.c.3) Substituições / Valor Contábil (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_D_1_QT_RECOMPRA` | `TAB_VII_D_1_QT_RECOMPRA` | decimal | (VII.d.1) Recompras / Quantidade (só em: `inf_mensal_fidc_tab_vii`) | quantidade | todo |
| `TAB_VII_D_2_VL_RECOMPRA` | `TAB_VII_D_2_VL_RECOMPRA` | decimal | (VII.d.2) Recompras / Valor (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `TAB_VII_D_3_VL_CONTAB_RECOMPRA` | `TAB_VII_D_3_VL_CONTAB_RECOMPRA` | decimal | (VII.d.3) Recompras / Valor Contábil (só em: `inf_mensal_fidc_tab_vii`) | moeda (R$) | todo |
| `SEQUENCIAL` | `SEQUENCIAL` | inteiro | Sem descrição no dicionário da CVM; pelo nome da coluna: sequencial (só em: `inf_mensal_fidc_tab_viii`) | código ou número de identificação (sem unidade) | todo |
| `VALOR` | `VALOR` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: valor (só em: `inf_mensal_fidc_tab_viii`) | moeda (R$) | todo |
| `TAB_X_NR_COTST_SENIOR_PF` | `TAB_X_NR_COTST_SENIOR_PF` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Pessoa física (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_PJ_NAO_FINANC` | `TAB_X_NR_COTST_SENIOR_PJ_NAO_FINANC` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Pessoa jurídica não-financeira (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_BANCO` | `TAB_X_NR_COTST_SENIOR_BANCO` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Banco comercial (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_CORRETORA_DISTRIB` | `TAB_X_NR_COTST_SENIOR_CORRETORA_DISTRIB` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Corretora ou distribuidora (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_PJ_FINANC` | `TAB_X_NR_COTST_SENIOR_PJ_FINANC` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Outras pessoas jurídicas financeiras (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_INVNR` | `TAB_X_NR_COTST_SENIOR_INVNR` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Investidores não residentes (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_EAPC` | `TAB_X_NR_COTST_SENIOR_EAPC` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Entidade aberta de previdência complementar (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_EFPC` | `TAB_X_NR_COTST_SENIOR_EFPC` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Entidade fechada de previdência complementar (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_RPPS` | `TAB_X_NR_COTST_SENIOR_RPPS` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Regime próprio de previdência dos servidores públicos (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_SEGUR` | `TAB_X_NR_COTST_SENIOR_SEGUR` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Sociedade seguradora ou resseguradora (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_CAPITALIZ` | `TAB_X_NR_COTST_SENIOR_CAPITALIZ` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Sociedade de capitalização e de arrendamento mercantil (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_COTA_FIDC` | `TAB_X_NR_COTST_SENIOR_COTA_FIDC` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Fundos de investimento em cotas de FIDC (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_FII` | `TAB_X_NR_COTST_SENIOR_FII` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Fundos de investimento imobiliário (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_OUTRO_FI` | `TAB_X_NR_COTST_SENIOR_OUTRO_FI` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Outros fundos de investimento (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_CLUBE` | `TAB_X_NR_COTST_SENIOR_CLUBE` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Clubes de investimento (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SENIOR_OUTRO` | `TAB_X_NR_COTST_SENIOR_OUTRO` | inteiro | (X.1.1) Número de Cotistas (Classe Sênior) - Outros (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_PF` | `TAB_X_NR_COTST_SUBORD_PF` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Pessoa física (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_PJ_NAO_FINANC` | `TAB_X_NR_COTST_SUBORD_PJ_NAO_FINANC` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Pessoa jurídica não-financeira (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_BANCO` | `TAB_X_NR_COTST_SUBORD_BANCO` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Banco comercial (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_CORRETORA_DISTRIB` | `TAB_X_NR_COTST_SUBORD_CORRETORA_DISTRIB` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Corretora ou distribuidora (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_PJ_FINANC` | `TAB_X_NR_COTST_SUBORD_PJ_FINANC` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Outras pessoas jurídicas financeiras (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_INVNR` | `TAB_X_NR_COTST_SUBORD_INVNR` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Investidores não residentes (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_EAPC` | `TAB_X_NR_COTST_SUBORD_EAPC` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Entidade aberta de previdência complementar (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_EFPC` | `TAB_X_NR_COTST_SUBORD_EFPC` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Entidade fechada de previdência complementar (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_RPPS` | `TAB_X_NR_COTST_SUBORD_RPPS` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Regime próprio de previdência dos servidores públicos (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_SEGUR` | `TAB_X_NR_COTST_SUBORD_SEGUR` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Sociedade seguradora ou resseguradora (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_CAPITALIZ` | `TAB_X_NR_COTST_SUBORD_CAPITALIZ` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Sociedade de capitalização e de arrendamento mercantil (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_COTA_FIDC` | `TAB_X_NR_COTST_SUBORD_COTA_FIDC` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Fundos de investimento em cotas de FIDC (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_FII` | `TAB_X_NR_COTST_SUBORD_FII` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Fundos de investimento imobiliário (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_OUTRO_FI` | `TAB_X_NR_COTST_SUBORD_OUTRO_FI` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Outros fundos de investimento (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_CLUBE` | `TAB_X_NR_COTST_SUBORD_CLUBE` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Clubes de investimento (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_NR_COTST_SUBORD_OUTRO` | `TAB_X_NR_COTST_SUBORD_OUTRO` | inteiro | (X.1.2) Número de Cotistas (Classe Subordinada) - Outros (só em: `inf_mensal_fidc_tab_x_1_1`) | quantidade | todo |
| `TAB_X_CLASSE_SERIE` | `TAB_X_CLASSE_SERIE` | texto | (X) Classe/Série (só em: `inf_mensal_fidc_tab_x_1`, `inf_mensal_fidc_tab_x_2`, `inf_mensal_fidc_tab_x_3`, `inf_mensal_fidc_tab_x_4` e mais 1) | — | todo |
| `ID_SUBCLASSE` | `ID_SUBCLASSE` | texto | Sem descrição no dicionário da CVM; pelo nome da coluna: id subclasse (só em: `inf_mensal_fidc_tab_x_1`) | — | todo |
| `TAB_X_NR_COTST` | `TAB_X_NR_COTST` | inteiro | (X.1) Número de Cotistas (só em: `inf_mensal_fidc_tab_x_1`) | quantidade | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_AA` | `TAB_X_SCR_RISCO_DEVEDOR_AA` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - AA (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_A` | `TAB_X_SCR_RISCO_DEVEDOR_A` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - A (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_B` | `TAB_X_SCR_RISCO_DEVEDOR_B` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - B (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_C` | `TAB_X_SCR_RISCO_DEVEDOR_C` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - C (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_D` | `TAB_X_SCR_RISCO_DEVEDOR_D` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - D (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_E` | `TAB_X_SCR_RISCO_DEVEDOR_E` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - E (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_F` | `TAB_X_SCR_RISCO_DEVEDOR_F` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - F (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_G` | `TAB_X_SCR_RISCO_DEVEDOR_G` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - G (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_DEVEDOR_H` | `TAB_X_SCR_RISCO_DEVEDOR_H` | decimal | (X.8.1) Valor Total dos direitos creditórios reportados ao SCR com base nas classificações de riscos dos devedores - H (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_AA` | `TAB_X_SCR_RISCO_OPER_AA` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - AA (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_A` | `TAB_X_SCR_RISCO_OPER_A` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - A (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_B` | `TAB_X_SCR_RISCO_OPER_B` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - B (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_C` | `TAB_X_SCR_RISCO_OPER_C` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - C (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_D` | `TAB_X_SCR_RISCO_OPER_D` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - D (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_E` | `TAB_X_SCR_RISCO_OPER_E` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - E (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_F` | `TAB_X_SCR_RISCO_OPER_F` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - F (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_G` | `TAB_X_SCR_RISCO_OPER_G` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - G (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_SCR_RISCO_OPER_H` | `TAB_X_SCR_RISCO_OPER_H` | decimal | (X.8.2) Valor total dos direitos creditórios reportados ao SCR com base nas classificações de risco das operações - H (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_DEBITO_TRIBUT` | `TAB_X_DEBITO_TRIBUT` | decimal | (X.9.1) Valor total dos direitos creditórios cedidos por cedentes que possuem débitos tributários inscritos em dívida Ativa da União (só em: `inf_mensal_fidc_tab_x`) | moeda (R$) | todo |
| `TAB_X_QT_COTA` | `TAB_X_QT_COTA` | decimal | (X) Quantidade de Cotas (só em: `inf_mensal_fidc_tab_x_2`, `inf_mensal_fidc_tab_x_4`) | quantidade | todo |
| `TAB_X_VL_COTA` | `TAB_X_VL_COTA` | decimal | (X.2) Valor da Cota (só em: `inf_mensal_fidc_tab_x_2`) | moeda (R$) | todo |
| `TAB_X_VL_RENTAB_MES` | `TAB_X_VL_RENTAB_MES` | decimal | (X.3) Rentabilidade Apurada no Mês (só em: `inf_mensal_fidc_tab_x_3`) | percentual (%) | todo |
| `TAB_X_TP_OPER` | `TAB_X_TP_OPER` | texto | (X.4) Tipo de Operação (só em: `inf_mensal_fidc_tab_x_4`) | — | todo |
| `TAB_X_VL_TOTAL` | `TAB_X_VL_TOTAL` | decimal | (X.4) Valor Total (só em: `inf_mensal_fidc_tab_x_4`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_0` | `TAB_X_VL_LIQUIDEZ_0` | decimal | (X.5) Ativos com liquidez imediata (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_30` | `TAB_X_VL_LIQUIDEZ_30` | decimal | (X.5) Ativos que podem ser liquidados em até 30 dias (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_60` | `TAB_X_VL_LIQUIDEZ_60` | decimal | (X.5) Ativos que podem ser liquidados em até 60 dias (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_90` | `TAB_X_VL_LIQUIDEZ_90` | decimal | (X.5)  Ativos que podem ser liquidados em até 90 dias (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_180` | `TAB_X_VL_LIQUIDEZ_180` | decimal | (X.5) Ativos que podem ser liquidados em até 180 dias (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_360` | `TAB_X_VL_LIQUIDEZ_360` | decimal | (X.5) Ativos que podem ser liquidados em até 360 dias (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_VL_LIQUIDEZ_MAIOR_360` | `TAB_X_VL_LIQUIDEZ_MAIOR_360` | decimal | (X.5) Ativos que podem ser liquidados em mais de 360 dias (só em: `inf_mensal_fidc_tab_x_5`) | moeda (R$) | todo |
| `TAB_X_PR_DESEMP_ESPERADO` | `TAB_X_PR_DESEMP_ESPERADO` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: tab x pr desemp esperado (só em: `inf_mensal_fidc_tab_x_6`) | percentual (%) | todo |
| `TAB_X_PR_DESEMP_REAL` | `TAB_X_PR_DESEMP_REAL` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: tab x pr desemp real (só em: `inf_mensal_fidc_tab_x_6`) | percentual (%) | todo |
| `TAB_X_VL_GARANTIA_DIRCRED` | `TAB_X_VL_GARANTIA_DIRCRED` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: tab x vl garantia dircred (só em: `inf_mensal_fidc_tab_x_7`) | moeda (R$) | todo |
| `TAB_X_PR_GARANTIA_DIRCRED` | `TAB_X_PR_GARANTIA_DIRCRED` | decimal | Sem descrição no dicionário da CVM; pelo nome da coluna: tab x pr garantia dircred (só em: `inf_mensal_fidc_tab_x_7`) | percentual (%) | todo |
| `ano` | — (partição) | inteiro | Ano do arquivo de origem | — | todo |
| `mes` | — (partição) | inteiro | Mês do arquivo de origem | — | todo |

## No lake

- Dataset `cvm/fidc-inf-mensal`, particionado por `ano`, `mes`; um arquivo Parquet por CSV (membro do ZIP).
- O conversor lê o CSV (separador `;`, UTF-8 e, se falhar, ISO-8859-1), mantém os nomes de coluna do arquivo, deixa CNPJ, ISIN e códigos CVM como texto e **infere** os demais tipos (número ou texto): datas ficam como texto `AAAA-MM-DD`.
- Linhas com `;` dentro de um campo de texto sem aspas (que a CVM publica em alguns arquivos) são reparadas sem descartar a linha.
- A partição vem do nome do arquivo (`..._AAAA-MM`, com hífen, como o fetcher grava o bruto).

## Cuidados de uso

- **A CVM reenvia os arquivos todo dia.** Os arquivos do ano ou mês corrente mudam entre atualizações (reapresentações, correções e novos documentos); reconverta antes de fechar um período.
- **Layout de colunas muito largo.** `tab_i` tem 109 colunas e `tab_ix` 76; os nomes seguem os itens do informe, e o dicionário da CVM traz a numeração do item na descrição.
- **Classes repetidas nos meses anteriores.** Em 2025-01 e 2025-12, `CNPJ_FUNDO_CLASSE` não é único nas tabelas de item único (3.214 linhas para 3.198 classes em 2025-01); no arquivo de 2026-10 é único. Confirme a unicidade por mês antes de juntar tabelas.
- **Colunas quase vazias.** 28 colunas de `tab_i` (as de cedentes de ordem 4 em diante e `TAB_I2A10_VL_CRED_DIVERSO`, por exemplo) têm mais de 98% de nulos em 2026-10.
- **`CNPJ_FUNDO_CLASSE` com máscara; `CNPJ_CLASSE` e os CPF/CNPJ de cedentes, na maioria, só com dígitos.** Há CPF de cedentes pessoa física em `TAB_I2A12_CPF_CNPJ_CEDENTE_*` e `TAB_I2B12_CPF_CNPJ_CEDENTE_*`. O fetcher e o lake preservam o que a fonte publica.
- **Tipo inferido varia entre arquivos.** 8 coluna(s) (`TAB_IX_C1_2_1_VENDA_MIN`, `TAB_IX_C1_2_2_VENDA_MEDIA`, `TAB_IX_D1_2_1_VENDA_MIN`...) ficam com tipos diferentes em arquivos diferentes (por exemplo, número num arquivo e texto noutro, ou texto quando o arquivo traz a coluna toda vazia), porque o conversor infere o tipo de cada CSV. Converta com `CAST` ao ler vários arquivos.

## Exemplos

Patrimônio líquido total dos FIDC por mês (item IV.a).

```python
import duckdb

duckdb.sql("""
    SELECT ano, mes, count(*) AS classes, sum(TAB_IV_A_VL_PL) AS pl
    FROM read_parquet('lake/cvm/fidc-inf-mensal/**/*__inf_mensal_fidc_tab_iv_*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Conjunto no portal de dados abertos da CVM: https://dados.cvm.gov.br/dataset/fidc-doc-inf_mensal
- Dados e dicionário (`META`): https://dados.cvm.gov.br/dados/FIDC/DOC/INF_MENSAL/
