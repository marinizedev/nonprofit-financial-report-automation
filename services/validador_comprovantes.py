import os

def validar_comprovantes(dados_mes, pasta_comprovantes):
    arquivos = os.listdir(pasta_comprovantes)
    arquivos_ids = set()

    for a in arquivos:
        nome_sem_ext = a.replace(".png", "")
        id_arquivo = nome_sem_ext.split("_")[-1]
        arquivos_ids.add(id_arquivo)

    faltando = []

    for _, row in dados_mes.iterrows():
        id_lanc = str(int(row["id"]))

        if id_lanc not in arquivos_ids:
            faltando.append({
                "id": id_lanc,
                "data": row["data"].strftime("%Y-%m-%d"),
                "categoria": row["categoria"],
                "valor": row["valor"]
            })

    return faltando