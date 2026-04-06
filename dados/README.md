# 2. Análise de Dados (Python)

## 2.1 Coleta e Preparação de Dados (ETL)

Nesta etapa, foi criada uma base de dados simulada para representar o funcionamento da empresa SecureTech Solutions. Os dados incluem informações sobre clientes, faturamento, horas gastas, custo por hora, tempo de resposta e status dos projetos.

O objetivo do ETL é organizar, limpar e preparar os dados para análise, removendo valores nulos e preenchendo informações necessárias para o cálculo dos indicadores de desempenho.

### Código Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando base de dados simulada
dados = {
    'Cliente': ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Empresa E'],
    'Faturamento': [12000, 18000, 15000, 20000, 17000],
    'Horas_Gastas': [80, 120, 95, 140, 110],
    'Custo_Hora': [50, 50, np.nan, 50, 50],
    'Tempo_Resposta': [2.5, 3.0, 1.8, 4.2, 2.7],
    'Status': ['Concluído', 'Concluído', 'Em andamento', 'Concluído', 'Em andamento']
}

df = pd.DataFrame(dados)

# Limpeza de dados
df.dropna(subset=['Faturamento', 'Horas_Gastas'], inplace=True)
df['Custo_Hora'] = df['Custo_Hora'].fillna(50)

print("Base de dados tratada:")
print(df)
```

---

## 2.2 Cálculo de Indicadores (KPIs)

Foram definidos três indicadores principais para apoiar a tomada de decisão da empresa:

* **Faturamento Total:** soma de todo o faturamento dos projetos
* **Tempo Médio de Resposta:** média do tempo de resposta aos clientes
* **Custo Médio por Projeto:** média do custo estimado de execução dos projetos

### Código Python

```python
# KPIs
faturamento_total = df['Faturamento'].sum()
tempo_medio_resposta = df['Tempo_Resposta'].mean()
custo_medio_projeto = (df['Horas_Gastas'] * df['Custo_Hora']).mean()

print(f"Faturamento Total: R$ {faturamento_total:,.2f}")
print(f"Tempo Médio de Resposta: {tempo_medio_resposta:.2f} horas")
print(f"Custo Médio por Projeto: R$ {custo_medio_projeto:,.2f}")
```

---

## 2.3 Visualização de Dados

Os gráficos foram utilizados para mostrar a distribuição do faturamento e a relação entre horas gastas e faturamento.

### Código Python

```python
# Gráfico 1: Faturamento por cliente
plt.figure(figsize=(8, 5))
plt.bar(df['Cliente'], df['Faturamento'])
plt.title('Faturamento por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Faturamento')
plt.show()

# Gráfico 2: Horas Gastas x Faturamento
plt.figure(figsize=(8, 5))
plt.scatter(df['Horas_Gastas'], df['Faturamento'])
plt.title('Relação entre Horas Gastas e Faturamento')
plt.xlabel('Horas Gastas')
plt.ylabel('Faturamento')
plt.show()
```

---

## Análise Crítica

A análise dos dados mostra que a SecureTech Solutions possui variação relevante entre esforço operacional e retorno financeiro dos projetos. O faturamento total indica que a empresa possui boa capacidade de geração de receita, mas o tempo médio de resposta evidencia a necessidade de melhorar a agilidade no atendimento.

Além disso, a relação entre horas gastas e faturamento permite identificar que projetos mais demorados nem sempre representam proporcionalmente maior retorno, o que justifica a importância de acompanhar indicadores de desempenho e otimizar a alocação de recursos.

Esses dados reforçam a necessidade do projeto proposto, pois demonstram que a empresa precisa de melhor controle operacional, segurança e apoio analítico para tomar decisões mais estratégicas.
