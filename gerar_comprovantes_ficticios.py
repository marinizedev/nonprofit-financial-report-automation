import pandas as pd
from services.simulador_igreja import gerar_lancamentos
from services.gerador_comprovantes_fake import gerar_comprovantes_mes

for mes in range(1, 13):
    df_mes = gerar_lancamentos(ano=2025, mes=mes)
    
    pasta = f"dados/2025/{mes:02d}/comprovantes"
    
    gerar_comprovantes_mes(df_mes, pasta, ano=2025, mes=mes)
    
    print(f"Mês {mes:02d}/2025 — {len(df_mes)} comprovantes gerados")

    print(len(df_mes))

    df_resumo = df_mes.groupby(["data", "categoria"]).agg({"valor": "sum"}).reset_index()

    print(len(df_resumo))