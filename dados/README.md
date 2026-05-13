# 📊 2. Análise de Dados

Nesta etapa, utilizámos **Python** e as bibliotecas **Pandas** e **Seaborn** para simular o comportamento de uma base de dados realista da **SecureTech Solutions**. O objetivo é transformar dados brutos em inteligência de negócio.

> 💻 **Acesso ao Código-Fonte:** O código completo de extração, limpeza e geração dos gráficos está disponível no script oficial da nossa análise.
> 👉 **[Clique aqui para visualizar ao script `analise_dados.py`](./analise_dados.py)**

---

## 2.1 Recolha e Preparação de Dados (Pipeline ETL)

Construímos um script que simula 200 chamados de contratos e implementações de segurança (com estado de entrega, horas trabalhadas e faturação), inserindo falhas propositadas e valores nulos (`NaN`) para testar o tratamento de dados.

O processo de **ETL (Extract, Transform, Load)** aplicado consistiu em:

- **Extract (Extração):** Geração de um _DataFrame_ a simular a prestação de serviços como "Monitorização SOC", "Backup Cloud" e "Auditoria LGPD".
- **Transform (Transformação e Limpeza):** \* **Tratamento de Nulos:** Valores financeiros ausentes foram preenchidos com a média ponderada do respetivo serviço.
  - **Remoção de Inconsistências:** Exclusão de linhas onde não houve resposta à pesquisa de satisfação do cliente (`dropna`).
  - **Formatação:** Conversão de tipos de dados numéricos para padronização analítica.
- **Load (Carga):** O _DataFrame_ limpo foi utilizado para gerar as métricas finais.

---

## 2.2 Indicadores Chave de Desempenho (KPIs)

A partir da base de dados tratada, o nosso algoritmo calculou as seguintes métricas estratégicas, refletindo a realidade de uma consultoria focada em PMEs (Pequenas e Médias Empresas):

1.  **Faturação Total Operacional:** `R$ 1.243.619,53`
2.  **Ticket Médio por Serviço:** `R$ 6.218,09`
3.  **Taxa de Projetos Atrasados:** `10.4%` (KPI Crítico de gestão de tempo).

---

## 2.3 Visualização de Dados (Data Viz)

Para responder a perguntas estratégicas da empresa, geramos painéis visuais focados na gestão de estado, eficiência operacional e receita.

### Visão Geral da Operação

Primeiro, avaliamos o volume e a saúde das entregas da empresa. O gráfico abaixo mostra como os 200 projetos simulados estão distribuídos:

![Gráfico de Distribuição de Estado](./grafico_status.png)

### Eficiência Operacional (Esforço vs Retorno)

O gráfico de dispersão ajuda-nos a entender a relação direta entre o esforço empregue (horas de trabalho da equipa) e o retorno financeiro gerado para a SecureTech, categorizando pelo estado do projeto. Projetos com muitas horas e baixa faturação exigem revisão de âmbito e otimização.

![Gráfico de Dispersão - Faturação vs Horas](./grafico_dispersao.png)

### Receita por Portefólio de Serviços

Abaixo, visualizamos qual a categoria de serviço de cibersegurança que traz o maior volume de capital, o que orienta as decisões estratégicas e os próximos investimentos de marketing.

![Gráfico de Faturação por Serviço](./grafico_faturamento_servico.png)

---

## 2.4 Análise Crítica dos Resultados

A análise exploratória dos dados revela _insights_ valiosos para a tomada de decisão da direção:

- **Posicionamento de Mercado:** Um ticket médio na casa dos R$ 6.000 confirma a forte atuação da SecureTech no mercado B2B de PMEs. Soluções escaláveis e contratos de menor valor, mas em maior volume, sustentam uma faturação anual superior a 1.2 milhões.
- **Gestão de Tempo e Otimização:** Com uma taxa de atraso na ordem dos 10%, a SecureTech possui uma operação maioritariamente saudável, mas o gráfico de dispersão mostra que alguns projetos "Em Andamento" ou "Atrasados" estão a consumir mais horas do que o planeado. É necessário utilizar técnicas de otimização para realocar a equipa técnica.
- **Carro-Chefe Financeiro:** A análise de receita indica claramente que a "Monitorização SOC" e o "Backup Cloud" são os serviços de maior valor acrescentado. Como as pequenas empresas são alvos frequentes de _ransomware_, estes serviços representam a maior faturação e devem ser o foco comercial da empresa.
- **Maturidade dos Dados:** A implementação do pipeline de ETL provou que a ausência de preenchimento de campos operacionais pode distorcer a realidade da empresa. A automação da limpeza de dados evitou relatórios imprecisos.
