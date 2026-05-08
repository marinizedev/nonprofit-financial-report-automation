def calcular_totais(dados_mes):
    total_entradas = dados_mes[dados_mes["tipo"] == "entrada"]["valor"].sum()
    total_saidas = dados_mes[dados_mes["tipo"] == "saida"]["valor"].sum()
    saldo = total_entradas - total_saidas

    return total_entradas, total_saidas, saldo