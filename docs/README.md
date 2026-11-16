# Comissão de Valores Mobiliários — CVM (`cvm`)

O `cvm-fetcher` coleta os dados abertos da Comissão de Valores Mobiliários (CVM), o regulador do mercado de capitais brasileiro, e os converte para o lake em Parquet particionado por ano (e mês, quando o nome do arquivo traz o hífen). Os dados cobrem os cadastros de participantes do mercado, as companhias abertas (demonstrações financeiras, formulários e documentos), os fundos de investimento (cadastro, informe diário, carteiras, balancetes), os fundos estruturados (FIAGRO, FIDC, FII, FIP), as ofertas públicas e a securitização.

O fetcher declara **31 datasets**, um por conjunto de dados do portal; muitos reúnem várias tabelas (um CSV por tabela dentro de cada ZIP).

## Cadastros de participantes do mercado

| Dataset | O que é | Arquivos no catálogo | Página |
|---|---|---|---|
| `adm-cart-cad` | Cadastro dos administradores de carteira de valores mobiliários registrados na CVM: pessoas físicas e jurídicas, com diretores, responsáveis e sócios | 1 | [adm-cart-cad](datasets/adm-cart-cad.md) |
| `agente-auton-cad` | Cadastro dos agentes autônomos de investimento registrados na CVM, em duas tabelas: pessoas físicas e pessoas jurídicas | 1 | [agente-auton-cad](datasets/agente-auton-cad.md) |
| `agente-fiduc-cad` | Cadastro dos agentes fiduciários registrados na CVM (Resolução CVM 17), em duas tabelas: pessoas físicas e pessoas jurídicas | 1 | [agente-fiduc-cad](datasets/agente-fiduc-cad.md) |
| `auditor-cad` | Cadastro dos auditores independentes registrados na CVM, em duas tabelas: pessoas físicas e pessoas jurídicas | 1 | [auditor-cad](datasets/auditor-cad.md) |
| `consultor-cad` | Cadastro dos consultores de valores mobiliários registrados na CVM: pessoas físicas e jurídicas, com diretores, responsáveis e sócios | 1 | [consultor-cad](datasets/consultor-cad.md) |
| `intermed-cad` | Cadastro dos participantes intermediários (corretoras, distribuidoras e demais intermediários financeiros) com o responsável por cada um | 1 | [intermed-cad](datasets/intermed-cad.md) |

## Companhias abertas

| Dataset | O que é | Arquivos no catálogo | Página |
|---|---|---|---|
| `cia-cad` | Cadastro vigente das companhias abertas registradas na CVM: situação do registro, setor, controle acionário, auditor e dados de contato | 1 | [cia-cad](datasets/cia-cad.md) |
| `cia-cgvn` | Informe do Código Brasileiro de Governança Corporativa (ICBGC, 'pratique ou explique'): a adoção, por cada companhia aberta, das práticas recomendadas | 9 | [cia-cgvn](datasets/cia-cgvn.md) |
| `cia-dfp` | Demonstrações Financeiras Padronizadas (DFP) das companhias abertas: balanço patrimonial, demonstrações do resultado, dos fluxos de caixa, das mutações do patrimônio líquido e do valor adicionado, em versões consolidada e individual | 17 | [cia-dfp](datasets/cia-dfp.md) |
| `cia-itr` | Informações Trimestrais (ITR) das companhias abertas: balanço patrimonial e demonstrações do trimestre, em versões consolidada e individual | 16 | [cia-itr](datasets/cia-itr.md) |
| `cia-fca` | Formulário Cadastral (FCA) das companhias abertas: dados gerais, endereços, auditor, escriturador, valores mobiliários, canais de divulgação e outros dados cadastrais, em tabelas separadas | 17 | [cia-fca](datasets/cia-fca.md) |
| `cia-fre` | Formulário de Referência (FRE) das companhias abertas: capital social, administração, remuneração, empregados, partes relacionadas e outros itens do formulário, em cerca de 50 tabelas | 17 | [cia-fre](datasets/cia-fre.md) |
| `cia-ipe` | Informações Periódicas e Eventuais (IPE): a lista dos documentos que as companhias abertas entregam (fatos relevantes, comunicados, atas, avisos), com assunto, categoria e link | 24 | [cia-ipe](datasets/cia-ipe.md) |

## Fundos de investimento

| Dataset | O que é | Arquivos no catálogo | Página |
|---|---|---|---|
| `fi-cad` | Cadastro dos fundos de investimento: o cadastro vigente (`cad_fi`), o histórico de alterações (`cad_fi_hist`) e o registro de fundos e classes sob a Resolução CVM 175 (`registro_fundo_classe`) | 3 | [fi-cad](datasets/fi-cad.md) |
| `fi-balancete` | Balancetes mensais dos fundos de investimento: o saldo de cada conta do plano contábil do fundo, no fim de cada mês | 143 | [fi-balancete](datasets/fi-balancete.md) |
| `fi-cda` | Composição e Diversificação das Aplicações (CDA) dos fundos: as posições de cada fundo por tipo de ativo (títulos públicos, ações, cotas de fundos, derivativos e outros), em tabelas separadas | 47 | [fi-cda](datasets/fi-cda.md) |
| `fi-entrega` | Registro das entregas de documentos pelos fundos de investimento: o documento, a competência, a data prevista e a data de entrega | 23 | [fi-entrega](datasets/fi-entrega.md) |
| `fi-extrato` | Extrato anual das informações dos fundos de investimento: dados cadastrais e de estrutura do fundo no ano de referência | 12 | [fi-extrato](datasets/fi-extrato.md) |
| `fi-inf-diario` | Informe diário dos fundos de investimento: o valor da cota, o patrimônio líquido, a captação, os resgates e o número de cotistas de cada fundo em cada dia útil | 71 | [fi-inf-diario](datasets/fi-inf-diario.md) |
| `fi-lamina` | Lâmina de informações essenciais dos fundos de investimento: perfil de risco, objetivos, política de investimento, taxas, rentabilidade histórica e cenários, em tabelas separadas | 95 | [fi-lamina](datasets/fi-lamina.md) |
| `fi-perfil` | Perfil mensal dos fundos de investimento: o número de cotistas por tipo de investidor e a política de investimento declarada, por fundo e mês | 95 | [fi-perfil](datasets/fi-perfil.md) |

## Fundos estruturados (FIAGRO, FIDC, FII e FIP)

| Dataset | O que é | Arquivos no catálogo | Página |
|---|---|---|---|
| `fiagro-inf-mensal` | Informe mensal dos Fundos de Investimento nas Cadeias Produtivas Agroindustriais (FIAGRO): ativos, passivos, cotistas e rentabilidade por fundo e subclasse | 19 | [fiagro-inf-mensal](datasets/fiagro-inf-mensal.md) |
| `fidc-inf-mensal` | Informe mensal dos Fundos de Investimento em Direitos Creditórios (FIDC): carteira, inadimplência, subordinação, cotistas e rentabilidade, em tabelas separadas por tema | 23 | [fidc-inf-mensal](datasets/fidc-inf-mensal.md) |
| `fii-dfin` | Demonstrações financeiras dos Fundos de Investimento Imobiliário (FII), anuais | 11 | [fii-dfin](datasets/fii-dfin.md) |
| `fii-inf-anual` | Informe anual estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, administração, ativos, cotistas e demais itens do informe, em tabelas separadas | 11 | [fii-inf-anual](datasets/fii-inf-anual.md) |
| `fii-inf-mensal` | Informe mensal estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, ativos, passivos e cotistas por fundo e mês, em três tabelas | 11 | [fii-inf-mensal](datasets/fii-inf-mensal.md) |
| `fii-inf-trim` | Informe trimestral estruturado dos Fundos de Investimento Imobiliário (FII): dados gerais, imóveis, ativos e outros itens do informe, em tabelas separadas | 11 | [fii-inf-trim](datasets/fii-inf-trim.md) |
| `fip-inf` | Informes dos Fundos de Investimento em Participações (FIP): trimestral de 2010 a 2023 e quadrimestral desde 2024 | 17 | [fip-inf](datasets/fip-inf.md) |

## Ofertas e securitização

| Dataset | O que é | Arquivos no catálogo | Página |
|---|---|---|---|
| `ofertas` | Ofertas públicas de distribuição de valores mobiliários registradas na CVM: o ofertante, o valor, o coordenador e as características da oferta, nos regimes anterior e posterior à Resolução CVM 160 (o ZIP da fonte estava vazio em 2026-11-16: sem conversão para o lake) | 1 | [ofertas](datasets/ofertas.md) |
| `securit-cra` | Securitização de Certificados de Recebíveis do Agronegócio (CRA): as demonstrações financeiras anuais das securitizadoras (`dfin_cra`) e o informe mensal de cada CRA (`inf_mensal_cra`), em tabelas separadas | 16 | [securit-cra](datasets/securit-cra.md) |
| `securit-cri` | Securitização de Certificados de Recebíveis Imobiliários (CRI): as demonstrações financeiras anuais das securitizadoras (`dfin_cri`) e o informe mensal de cada CRI (`inf_mensal_cri`), em tabelas separadas | 17 | [securit-cri](datasets/securit-cri.md) |

## Como a CVM publica

- A CVM mantém o Portal de Dados Abertos (https://dados.cvm.gov.br) e um espelho de arquivos em `https://dados.cvm.gov.br/dados/`, organizado por tema (`CIA_ABERTA`, `FI`, `FII`, `FIDC` e outros), com as pastas `DADOS` (arquivos) e `META` (dicionários de dados).
- Os arquivos são CSV com ponto e vírgula, avulsos ou dentro de ZIP (um CSV por tabela). Os conjuntos de documentos (`DOC`) têm um arquivo por ano ou por mês; os cadastros (`CAD`) têm um arquivo único reenviado todo dia.
- A CVM reenvia os arquivos do período corrente todos os dias; os de anos fechados mudam quando há reapresentações.
- Os dicionários de dados são arquivos de texto (ou ZIP de textos) no formato 'Campo, Descrição, Domínio, Tipo, Tamanho', um por tabela.
- A licença do portal é a Open Data Commons Open Database License (ODbL).
- O catálogo do fetcher lista os arquivos por contagem de períodos desde o primeiro ano publicado; arquivos do mês corrente ainda não publicados respondem 404 (por exemplo, `..._202611` em 2026-11-15).
- O conversor lê cada CSV com tipos inferidos e mantém os nomes de coluna como a CVM os publica (a caixa varia entre conjuntos: `CNPJ_CIA`, `CNPJ_Companhia`, `CNPJ_FUNDO`).

## Como os conjuntos se relacionam

- Companhias abertas ligam-se por `CD_CVM` e `CNPJ_CIA` (DFP, ITR) ou `CNPJ_Companhia` (FCA, FRE, IPE, CGVN) ao cadastro `cia-cad`.
- Fundos ligam-se por `CNPJ_FUNDO` (ou `CNPJ_FUNDO_CLASSE` nos arquivos a partir de 2023-11 ou 2023-12, conforme o conjunto: a adaptação à Resolução CVM 175 renomeou a coluna) ao cadastro `fi-cad`; confira o nome da coluna em cada conjunto e coalesça as duas ao ler vários meses.
- O formato do CNPJ varia: os informes, balancetes, extratos, lâminas, perfis, CDA e FIDC trazem a máscara (`00.000.000/0000-00`); `fi-entrega`, `fiagro-inf-mensal` e as tabelas `registro_*` de `fi-cad` trazem só os 14 dígitos; nos conjuntos de FII e de securitização o CNPJ do fundo ou da emissora tem máscara e o do administrador ou do cedente/devedor, não. Normalize antes de juntar.
- Os conjuntos mensais e trimestrais de FII e de securitização trazem cada reapresentação como uma linha com `Versao` maior: escolha a maior `Versao` por CNPJ e data de referência.
