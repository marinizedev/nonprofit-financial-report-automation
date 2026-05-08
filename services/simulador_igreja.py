import random
import pandas as pd
from datetime import date, timedelta
from faker import Faker
from config.regras_igreja import (
    DIAS_CULTO, SAZONALIDADE, FAIXA_DIZIMO,
    DESPESAS, ALUGUEL
)

fake = Faker("pt_BR")

DIAS_CULTO_INDICES = {1: "terca", 4: "sexta", 6: "domingo"}

def gerar_lancamentos(ano, mes, seed=42):
    random.seed(seed)

    lancamentos = []
    fator = SAZONALIDADE[mes]
    id_contador = 1  # ← contador global do mês

    data_atual = date(ano, mes, 1)
    while data_atual.month == mes:
        dia_semana = data_atual.weekday()
        nome_dia = DIAS_CULTO_INDICES.get(dia_semana)

        if nome_dia:
            regra = DIAS_CULTO[nome_dia]

            # OFERTA do culto
            valor_oferta = round(
                random.uniform(regra["oferta_min"], regra["oferta_max"]) * fator, 2
            )
            lancamentos.append({
                "id": id_contador,
                "data": data_atual,
                "historico": "Oferta",
                "tipo": "entrada",
                "categoria": "oferta",
                "valor": valor_oferta,
                "origem": "Culto",
                "observacao": nome_dia.capitalize(),
                "doador/benef.": ""
            })
            id_contador += 1

            # DÍZIMOS
            qtd_dizimos = random.randint(1, 3)
            for _ in range(qtd_dizimos):
                valor_dizimo = round(
                    random.uniform(
                        FAIXA_DIZIMO["min"],
                        FAIXA_DIZIMO["max"]
                    ) * fator, 2
                )
                lancamentos.append({
                    "id": id_contador,
                    "data": data_atual,
                    "historico": "Dízimo",
                    "tipo": "entrada",
                    "categoria": "dizimo",
                    "valor": valor_dizimo,
                    "origem": "Culto",
                    "observacao": "",
                    "doador/benef.": ""
                })
                id_contador += 1

        data_atual += timedelta(days=1)

    # ALUGUEL — dia 5 de cada mês
    lancamentos.append({
        "id": id_contador,
        "data": date(ano, mes, 5),
        "historico": ALUGUEL["historico"],
        "tipo": "saida",
        "categoria": "aluguel",
        "valor": ALUGUEL["valor"],
        "origem": "",
        "observacao": "",
        "doador/benef.": ""
    })
    id_contador += 1

    # DESPESAS
    qtd_despesas = random.randint(4, 8)
    despesas_escolhidas = random.choices(DESPESAS, k=qtd_despesas)

    for despesa in despesas_escolhidas:
        dia = random.randint(1, 28)
        valor = round(random.uniform(despesa["min"], despesa["max"]), 2)

        lancamentos.append({
            "id": id_contador,
            "data": date(ano, mes, dia),
            "historico": despesa["historico"],
            "tipo": "saida",
            "categoria": "despesa",
            "valor": valor,
            "origem": "",
            "observacao": "",
            "doador/benef.": ""
        })
        id_contador += 1

    # Ordena por data
    df = pd.DataFrame(lancamentos)
    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values(by="data").reset_index(drop=True)

    return df