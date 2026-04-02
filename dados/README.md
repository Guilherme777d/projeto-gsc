# Análise de Dados

## 2.1 Coleta e Tratamento de Dados (ETL)

Para análise do projeto, foram utilizados dados simulados representando projetos de tecnologia.

```python
import pandas as pd

# Criando dados simulados
dados = {
    'Projeto': ['A', 'B', 'C', 'D', 'E'],
    'Faturamento': [10000, 15000, 8000, 20000, 12000],
    'Horas_Gastas': [100, 150, 80, 200, 120],
    'Status': ['Entregue', 'Atrasado', 'Entregue', 'Entregue', 'Atrasado']
}

df = pd.DataFrame(dados)

# Tratamento
df['Custo_Hora'] = 150
