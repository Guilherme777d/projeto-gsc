import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Projeto": ["Firewall", "Backup", "Monitoramento", "Treinamento", "Auditoria"],
    "Horas": [120, 80, 150, 60, 90],
    "Faturamento": [12000, 9000, 18000, 5000, 10000],
    "Tempo_Resposta": [4.5, 3.2, 5.1, 2.8, 3.6]
}

df = pd.DataFrame(dados)

print("Base de dados:")
print(df)

print("\nIndicadores:")
print("Faturamento total:", df["Faturamento"].sum())
print("Horas totais:", df["Horas"].sum())
print("Tempo médio de resposta:", round(df["Tempo_Resposta"].mean(), 2))

plt.figure(figsize=(8, 5))
plt.bar(df["Projeto"], df["Faturamento"])
plt.title("Faturamento por Projeto")
plt.xlabel("Projeto")
plt.ylabel("Faturamento")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("grafico_faturamento.png")  # corrigido aqui
plt.show()
