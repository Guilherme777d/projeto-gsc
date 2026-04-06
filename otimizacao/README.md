# 4. Pesquisa Operacional

## 4.1 Problema 1: Maximização de Lucro

### Contexto

A empresa SecureTech Solutions possui recursos limitados de desenvolvimento e suporte técnico. Assim, é necessário decidir quantos projetos do Tipo A e do Tipo B devem ser aceitos para maximizar o lucro mensal.

### Modelagem Matemática

**Variáveis de decisão:**

* x = quantidade de projetos do Tipo A
* y = quantidade de projetos do Tipo B

**Função objetivo:**
Maximizar:

Z = 5000x + 8000y

**Restrições:**

* 2x + 4y ≤ 100  (horas de desenvolvimento)
* x + 2y ≤ 40    (horas de suporte)
* x ≥ 0, y ≥ 0

### Código Python

```python
from pulp import LpMaximize, LpProblem, LpVariable, value

# Criando o modelo
modelo = LpProblem("Maximizacao_Lucro", LpMaximize)

# Variáveis de decisão
x = LpVariable("Projeto_A", lowBound=0, cat="Integer")
y = LpVariable("Projeto_B", lowBound=0, cat="Integer")

# Função objetivo
modelo += 5000 * x + 8000 * y

# Restrições
modelo += 2 * x + 4 * y <= 100
modelo += x + 2 * y <= 40

# Resolvendo
modelo.solve()

print("Quantidade Projeto A:", value(x))
print("Quantidade Projeto B:", value(y))
print("Lucro Máximo:", value(modelo.objective))
```

### Análise de Cenário (What-If)

Se a capacidade de desenvolvimento cair de 100 para 60 horas, a empresa precisará aceitar menos projetos, reduzindo o lucro máximo. Isso demonstra como a limitação de recursos afeta diretamente a tomada de decisão.

---

## 4.2 Problema 2: Minimização de Custos

### Contexto

A empresa precisa alocar técnicos entre diferentes clientes buscando minimizar os custos operacionais de atendimento.

### Modelagem Matemática

**Variáveis de decisão:**

* x1 = quantidade de atendimentos para Cliente 1
* x2 = quantidade de atendimentos para Cliente 2

**Função objetivo:**
Minimizar:

C = 200x1 + 300x2

**Restrições:**

* x1 + x2 ≥ 10   (quantidade mínima de atendimentos)
* x1 ≥ 0, x2 ≥ 0

### Código Python

```python
from pulp import LpMinimize, LpProblem, LpVariable, value

# Criando o modelo
modelo2 = LpProblem("Minimizacao_Custos", LpMinimize)

# Variáveis de decisão
x1 = LpVariable("Cliente_1", lowBound=0, cat="Integer")
x2 = LpVariable("Cliente_2", lowBound=0, cat="Integer")

# Função objetivo
modelo2 += 200 * x1 + 300 * x2

# Restrições
modelo2 += x1 + x2 >= 10

# Resolvendo
modelo2.solve()

print("Atendimentos Cliente 1:", value(x1))
print("Atendimentos Cliente 2:", value(x2))
print("Custo Mínimo:", value(modelo2.objective))
```

### Análise de Cenário (What-If)

Se a demanda mínima subir de 10 para 15 atendimentos, o custo total aumentará. Esse tipo de simulação ajuda a empresa a entender o impacto de mudanças operacionais antes de tomar decisões reais.

---

## Análise Crítica

Os modelos matemáticos apresentados ajudam a empresa a tomar decisões mais eficientes com base em restrições reais de recursos. A maximização de lucro permite identificar a melhor combinação de projetos para aumentar os ganhos, enquanto a minimização de custos ajuda a reduzir desperdícios e melhorar a eficiência operacional.

A análise de cenário (What-If) é fundamental para preparar a empresa para imprevistos, pois mostra como alterações em recursos, capacidade ou demanda impactam diretamente os resultados. Dessa forma, a Pesquisa Operacional se torna uma ferramenta estratégica para apoiar a gestão e tornar o projeto mais realista e completo.
