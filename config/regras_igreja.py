from datetime import datetime

NOME_ORGANIZACAO = "Comunidade Esperança"
CNPJ_FICTICIO = "12.345.678/0001-90"

# Dias de culto e peso das ofertas
DIAS_CULTO = {
    "domingo": {"oferta_min": 150, "oferta_max": 800},
    "terca":   {"oferta_min": 50,  "oferta_max": 300},
    "sexta":   {"oferta_min": 120, "oferta_max": 600}
}

# Sazonalidade mensal — fator multiplicador de entradas
SAZONALIDADE = {
    1:  0.70,  # janeiro — início de ano fraco
    2:  0.75,
    3:  0.85,
    4:  0.90,
    5:  0.90,
    6:  0.95,
    7:  0.95,
    8:  1.00,
    9:  1.05,
    10: 1.10,
    11: 1.15,
    12: 1.30   # dezembro — final de ano forte
}

# Dízimos — perfis de dizimistas fictícios
FAIXA_DIZIMO = {
    "min": 50,
    "max": 2500
}

# Despesas com categorias reais
DESPESAS = [
    {"historico": "Produtos de limpeza",    "min": 40,   "max": 150},
    {"historico": "Combustível",            "min": 80,   "max": 300},
    {"historico": "Despesa Pregador",       "min": 100,  "max": 400},
    {"historico": "Talão de energia",       "min": 80,   "max": 180},
    {"historico": "Talão de água",          "min": 30,   "max": 80},
    {"historico": "Decoração",              "min": 50,   "max": 300},
    {"historico": "Material de escritório", "min": 30,   "max": 120},
    {"historico": "Reforma",                "min": 200,  "max": 1200},
]

# Aluguel fixo mensal
ALUGUEL = {
    "historico": "Aluguel da Igreja",
    "valor": 1000.00
}