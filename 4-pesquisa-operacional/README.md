# 🧮 4. Pesquisa Operacional

Nesta etapa, aplicamos a modelagem matemática para resolver gargalos operacionais da **SecureTech Solutions**, utilizando a programação linear para garantir a melhor aplicação de recursos limitados.

> 💻 **Acesso ao Código-Fonte:** Os modelos matemáticos foram resolvidos utilizando a biblioteca **PuLP**. O script completo com as resoluções e simulações está disponível no link abaixo.
> 👉 **[Clique aqui para visualizar o script `otimizacao_processos.py`](./otimizacao_processos.py)**

---

## 4.1 Problema 1: Mix de Serviços (Maximização de Lucro)

### Contexto de Negócio

A SecureTech Solutions oferece dois serviços principais: **Monitoramento SOC (S)** e **Consultoria LGPD (C)**. Como possuímos um limite de horas técnicas mensais da nossa equipe especializada, precisamos decidir a quantidade ideal de cada contrato para maximizar o lucro operacional.

### Modelagem Matemática

**Variáveis de Decisão:**

- $x_1$: Quantidade de contratos de Monitoramento SOC.
- $x_2$: Quantidade de contratos de Consultoria LGPD.

**Função Objetivo (Maximizar Lucro):**
$Z = 5000x_1 + 8000x_2$

**Restrições:**

1. **Horas de Implementação:** $2x_1 + 4x_2 \leq 100$ (Limite de horas da equipe técnica)
2. **Capacidade de Monitoramento:** $x_1 + 2x_2 \leq 40$ (Limite de infraestrutura)
3. **Não-negatividade:** $x_1, x_2 \geq 0$ (Valores inteiros)

### Análise de Cenário (What-If)

**Cenário:** Caso a disponibilidade da equipe técnica caia para 60h (ex: período de férias ou treinamentos), o modelo recalcula a prioridade para os contratos que trazem maior margem por hora trabalhada.

- **Impacto Original:** 40 contratos SOC e 0 LGPD (Lucro de R$ 200.000,00).
- **Novo Impacto:** 30 contratos SOC e 0 LGPD (Lucro de R$ 150.000,00).
- **Conclusão:** A redução de 40 horas na capacidade técnica resulta em uma perda financeira direta de R$ 50.000,00 no faturamento máximo, evidenciando a necessidade de automação de processos para depender menos de horas manuais.

---

## 4.2 Problema 2: Dimensionamento de Equipe (Minimização de Custo)

### Contexto de Negócio

Para atender a demanda mensal de no mínimo 160 chamados técnicos, a empresa pode utilizar **Analistas Juniores** e **Analistas Sêniores**. O objetivo é atingir a meta de atendimento com o menor custo de folha de pagamento possível.

### Modelagem Matemática

**Variáveis de Decisão:**

- $y_1$: Número de Analistas Juniores.
- $y_2$: Número de Analistas Sêniores.

**Função Objetivo (Minimizar Custos):**
$C = 3500y_1 + 7500y_2$

**Restrições:**

1. **Demanda de Chamados:** $20y_1 + 50y_2 \geq 160$ (Capacidade de resolução mensal)
2. **Supervisão Obrigatória:** $y_2 \geq 2$ (Mínimo de 2 sêniores para garantir a qualidade)
3. **Não-negatividade:** $y_1, y_2 \geq 0$

### Análise de Cenário (What-If)

**Cenário:** Se o custo de mercado de um Analista Sênior aumentar para R$ 9.000, o modelo avalia se a composição da equipe deve ser alterada.

- **Conclusão:** Mesmo com o aumento de custo, a restrição de qualidade (mínimo de 2 sêniores) mantém a estrutura base (3 juniores e 2 sêniores), mas acarreta um aumento de R$ 3.000,00 na folha salarial, forçando a empresa a buscar maior produtividade dos juniores.

---

## 🧠 Análise Crítica e Conclusão

A aplicação de Pesquisa Operacional permite que a **SecureTech Solutions** saia da tomada de decisão baseada em "intuição" e passe para uma gestão matemática.

1. **Eficiência Financeira:** Identificamos o ponto exato de equilíbrio entre custo de pessoal e entrega de serviço.
2. **Visão Estratégica:** As análises "What-If" funcionam como um simulador de riscos, permitindo prever o impacto financeiro de mudanças operacionais antes mesmo delas ocorrerem.
3. **Escalabilidade:** Com modelos prontos, a empresa pode ajustar parâmetros de custo e capacidade conforme cresce no mercado de cibersegurança.
