import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo para deixar os gráficos mais "bonitos" e modernos
sns.set_theme(style="whitegrid")

# ==========================================
# 1. EXTRAÇÃO E GERAÇÃO DE DADOS 
# ==========================================
print("Iniciando processo de ETL...\n")
np.random.seed(42)

# Lista de serviços
servicos = ["Monitoramento SOC", "Backup Cloud", "Firewall", "Auditoria LGPD", "Treinamento Phishing"]

# PESOS REAIS DE MERCADO: 
# SOC (35% das vendas), Backup (25%), Firewall (20%), Auditoria (15%), Treinamento (5%)
pesos_servicos = [0.35, 0.25, 0.20, 0.15, 0.05]

status_opcoes = ["Entregue", "Em Andamento", "Atrasado", "Cancelado"]
pesos_status = [0.60, 0.25, 0.10, 0.05] 

dados_brutos = {
    "ID_Chamado": range(1, 201),
    # Aplicando os pesos aqui para forçar o SOC a ser o mais vendido!
    "Servico": np.random.choice(servicos, 200, p=pesos_servicos), 
    "Status": np.random.choice(status_opcoes, 200, p=pesos_status),
    "Horas_Trabalhadas": np.random.uniform(20, 300, 200).round(1),
    "Faturamento_R$": np.random.uniform(800, 12000, 200).round(2),
    "Tempo_Resposta_h": np.random.uniform(1, 24, 200).round(1),
    "Satisfacao_Cliente": np.random.choice([1, 2, 3, 4, 5, np.nan], 200)
}

df = pd.DataFrame(dados_brutos)

# Inserindo erros/nulos propositais
df.loc[10:25, 'Faturamento_R$'] = np.nan

# ==========================================
# 2. TRANSFORMAÇÃO E LIMPEZA (ETL)
# ==========================================
df['Faturamento_R$'] = df.groupby('Servico')['Faturamento_R$'].transform(lambda x: x.fillna(x.mean()))
df_limpo = df.dropna(subset=['Satisfacao_Cliente']).copy()
df_limpo['Satisfacao_Cliente'] = df_limpo['Satisfacao_Cliente'].astype(int)

# ==========================================
# 3. CÁLCULO DE KPIs
# ==========================================
faturamento_total = df_limpo["Faturamento_R$"].sum()
ticket_medio = df_limpo["Faturamento_R$"].mean()
taxa_atraso = (len(df_limpo[df_limpo['Status'] == 'Atrasado']) / len(df_limpo)) * 100

print("\n--- KPIs ESTRATÉGICOS ---")
print(f"1. Faturamento Total: R$ {faturamento_total:,.2f}")
print(f"2. Ticket Médio: R$ {ticket_medio:,.2f}")
print(f"3. Taxa de Projetos Atrasados: {taxa_atraso:.1f}%")

# ==========================================
# 4. DATA VIZ (Gráficos Profissionais)
# ==========================================
cores_status = {"Entregue": "#2ecc71", "Em Andamento": "#3498db", "Atrasado": "#f39c12", "Cancelado": "#e74c3c"}

# Gráfico 1: Distribuição de Status (Gráfico de Barras)
plt.figure(figsize=(8, 5))
sns.countplot(data=df_limpo, x="Status", palette=cores_status, order=status_opcoes)
plt.title("Gráfico 1: Distribuição de Status dos Projetos", fontsize=14, fontweight='bold', pad=15)
plt.ylabel("Nº de Projetos")
plt.xlabel("")
plt.tight_layout()
plt.savefig("grafico_status.png", dpi=300)
plt.close()

# Gráfico 2: Faturamento vs Esforço (Gráfico de Dispersão/Scatterplot)
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df_limpo, x="Horas_Trabalhadas", y="Faturamento_R$", hue="Status", 
                palette=cores_status, s=100, alpha=0.8)
plt.title("Gráfico 2: Faturamento vs Esforço (Horas)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Esforço (Horas Gastas)")
plt.ylabel("Faturamento (R$)")
plt.legend(title="Status do Projeto", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("grafico_dispersao.png", dpi=300)
plt.close()

# Gráfico 3: Faturamento por Serviço
plt.figure(figsize=(10, 6))
faturamento_servico = df_limpo.groupby("Servico")["Faturamento_R$"].sum().reset_index()
faturamento_servico = faturamento_servico.sort_values(by="Faturamento_R$", ascending=False)

ax = sns.barplot(data=faturamento_servico, x="Servico", y="Faturamento_R$", color="#34495e")
plt.title("Gráfico 3: Faturamento Total por Categoria de Serviço", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Tipo de Serviço")
plt.ylabel("Faturamento Total (R$)")
plt.xticks(rotation=15)

# Adicionando rótulos nas barras
for p in ax.patches:
    ax.annotate(f'R$ {p.get_height()/1000:.1f}k', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')

plt.tight_layout()
plt.savefig("grafico_faturamento_servico.png", dpi=300)
plt.close()

print("\nOs 3 gráficos foram gerados e salvos com sucesso!")