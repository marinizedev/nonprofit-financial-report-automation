import pandas as pd
from services.simulador_igreja import gerar_lancamentos

frames = []

# Gera 12 meses de 2025
for mes in range(1, 13):
    df_mes = gerar_lancamentos(ano=2025, mes=mes)

    frames.append(df_mes)

df_total = pd.concat(frames, ignore_index=False)  # ← False preserva os IDs originais

# Garante formato de data correto
df_total["data"] = pd.to_datetime(df_total["data"]).dt.strftime("%Y-%m-%d")

# Salva planilha
df_total.to_excel("dados/lancamentos_ficticio.xlsx", index=False)

print(f"Planilha gerada: {len(df_total)} lançamentos")
print(df_total.groupby(["categoria"])["valor"].sum().round(2))