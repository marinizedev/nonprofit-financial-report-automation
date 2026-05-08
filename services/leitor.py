import pandas as pd

def carregar_dados(caminho):
    df = pd.read_excel(caminho)

    df.columns = df.columns.str.strip().str.lower()

    df["tipo"] = (
        df["tipo"]
        .astype(str)
        .str.replace("'", "", regex=False)
        .str.strip()
        .str.lower()
    )

    df["categoria"] = (
        df["categoria"]
        .astype(str)
        .str.replace("'", "", regex=False)
        .str.strip()
        .str.lower()
    )
    
    df = df.dropna(subset=["data", "valor"])

    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    df = df.dropna(subset=["data"])

    df["ano"] = df["data"].dt.year
    df["mes"] = df["data"].dt.month

    validos = ["entrada", "saida"]

    df = df[df["tipo"].isin(validos)]

    return df