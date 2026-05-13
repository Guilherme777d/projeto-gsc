"""
SecureTech Solutions - Pesquisa Operacional (Otimização)
"""

from pulp import LpProblem, LpMaximize, LpMinimize, LpVariable, LpStatus, value

def divisoria(texto):
    print(f"\n{'='*50}")
    print(f"{texto:^50}")
    print(f"{'='*50}")

# =====================================================================
# PROBLEMA 1: MAXIMIZAÇÃO DE LUCRO (MIX DE SERVIÇOS)
# =====================================================================
divisoria("PROBLEMA 1: MAXIMIZAÇÃO DE LUCRO")

# CENÁRIO BASE
print(">>> CENÁRIO BASE (100h Técnicas Disponíveis)")
modelo1 = LpProblem("Maximizacao_Lucro_SecureTech", LpMaximize)

# Variáveis (Inteiras)
x1 = LpVariable("Monitoramento_SOC", lowBound=0, cat="Integer")
x2 = LpVariable("Consultoria_LGPD", lowBound=0, cat="Integer")

# Função Objetivo
modelo1 += 5000 * x1 + 8000 * x2, "Lucro Total"

# Restrições Base
modelo1 += 2 * x1 + 4 * x2 <= 100, "Horas_Equipe"
modelo1 += x1 + 2 * x2 <= 40, "Capacidade_Infra"

modelo1.solve()

print(f"Status da Solução: {LpStatus[modelo1.status]}")
print(f"Qtd Contratos Monitoramento SOC: {value(x1)}")
print(f"Qtd Contratos Consultoria LGPD: {value(x2)}")
print(f"Lucro Máximo Esperado: R$ {value(modelo1.objective):,.2f}\n")

# CENÁRIO WHAT-IF (Queda de produtividade para 60h)
print(">>> CENÁRIO WHAT-IF (Capacidade de Horas cai para 60h)")
modelo1_whatif = LpProblem("Maximizacao_Lucro_WhatIf", LpMaximize)

x1_w = LpVariable("Monitoramento_SOC_W", lowBound=0, cat="Integer")
x2_w = LpVariable("Consultoria_LGPD_W", lowBound=0, cat="Integer")

modelo1_whatif += 5000 * x1_w + 8000 * x2_w
modelo1_whatif += 2 * x1_w + 4 * x2_w <= 60  # <- Mudança de parâmetro aqui!
modelo1_whatif += x1_w + 2 * x2_w <= 40

modelo1_whatif.solve()

print(f"Nova Qtd Monitoramento SOC: {value(x1_w)}")
print(f"Nova Qtd Consultoria LGPD: {value(x2_w)}")
print(f"Novo Lucro Máximo: R$ {value(modelo1_whatif.objective):,.2f}")
print(f"-> Impacto Financeiro: Perda de R$ {value(modelo1.objective) - value(modelo1_whatif.objective):,.2f}")


# =====================================================================
# PROBLEMA 2: MINIMIZAÇÃO DE CUSTOS (ALOCAÇÃO DE EQUIPE)
# =====================================================================
divisoria("PROBLEMA 2: MINIMIZAÇÃO DE CUSTO (RH)")

# CENÁRIO BASE
print(">>> CENÁRIO BASE (Salário Sênior R$ 7.500)")
modelo2 = LpProblem("Minimizacao_Custos_Equipe", LpMinimize)

# Variáveis (Inteiras)
y1 = LpVariable("Analista_Junior", lowBound=0, cat="Integer")
y2 = LpVariable("Analista_Senior", lowBound=0, cat="Integer")

# Função Objetivo
modelo2 += 3500 * y1 + 7500 * y2, "Custo Total RH"

# Restrições Base
modelo2 += 20 * y1 + 50 * y2 >= 160, "Demanda_Mensal"
modelo2 += y2 >= 2, "Supervisao_Minima_Senior"

modelo2.solve()

print(f"Status da Solução: {LpStatus[modelo2.status]}")
print(f"Analistas Juniores a contratar: {value(y1)}")
print(f"Analistas Seniores a contratar: {value(y2)}")
print(f"Custo Operacional Mínimo: R$ {value(modelo2.objective):,.2f}\n")

# CENÁRIO WHAT-IF (Salário do Sênior aumenta para R$ 9.000)
print(">>> CENÁRIO WHAT-IF (Salário Sênior aumenta para R$ 9.000)")
modelo2_whatif = LpProblem("Minimizacao_Custos_WhatIf", LpMinimize)

y1_w = LpVariable("Analista_Junior_W", lowBound=0, cat="Integer")
y2_w = LpVariable("Analista_Senior_W", lowBound=0, cat="Integer")

modelo2_whatif += 3500 * y1_w + 9000 * y2_w  # <- Mudança de parâmetro de custo aqui!
modelo2_whatif += 20 * y1_w + 50 * y2_w >= 160
modelo2_whatif += y2_w >= 2

modelo2_whatif.solve()

print(f"Nova composição - Juniores: {value(y1_w)}")
print(f"Nova composição - Seniores: {value(y2_w)}")
print(f"Novo Custo Operacional: R$ {value(modelo2_whatif.objective):,.2f}")
print(f"-> Impacto Financeiro: Aumento de R$ {value(modelo2_whatif.objective) - value(modelo2.objective):,.2f} na folha.")