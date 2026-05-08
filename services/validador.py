def validar(dados_mes, mes_formatado):

    if (dados_mes["valor"] < 0).any():
        print(f"Atenção: valores negativos em {mes_formatado}")

    if dados_mes["historico"].isnull().any():
        print(f"Atenção: descricao faltando em {mes_formatado}")

    if not dados_mes["tipo"].isin(["entrada", "saida", "doador"]).all():
        print(f"Atenção: tipo inválido em {mes_formatado}")