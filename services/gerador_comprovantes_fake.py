import os
from PIL import Image, ImageDraw, ImageFont
import shutil

def criar_recibo(destino, data, historico, valor, numero):
    """Gera imagem simulando recibo de dízimo/oferta/aluguel"""
    
    img = Image.new("RGB", (600, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Borda
    draw.rectangle([10, 10, 590, 390], outline=(0, 0, 0), width=2)

    # Cabeçalho
    draw.rectangle([10, 10, 590, 70], fill=(230, 230, 230))
    draw.text((300, 40), "RECIBO DE PAGAMENTO", fill=(0, 0, 0), anchor="mm")

    # Número do recibo
    draw.text((500, 90), f"Nº {numero:04d}", fill=(100, 100, 100), anchor="mm")

    # Dados
    draw.text((50, 120), f"Data: {data.strftime('%d/%m/%Y')}", fill=(0, 0, 0))
    draw.text((50, 160), f"Referente a: {historico}", fill=(0, 0, 0))
    draw.text((50, 200), f"Valor: R$ {valor:.2f}", fill=(0, 0, 0))
    draw.text((50, 240), "Comunidade Esperança", fill=(0, 0, 0))
    draw.text((50, 280), "CNPJ: 12.345.678/0001-90", fill=(100, 100, 100))

    # Assinatura
    draw.line([50, 360, 280, 360], fill=(0, 0, 0), width=1)
    draw.text((165, 375), "Tesoureira", fill=(100, 100, 100), anchor="mm")

    draw.line([320, 360, 550, 360], fill=(0, 0, 0), width=1)
    draw.text((435, 375), "Responsável", fill=(100, 100, 100), anchor="mm")

    img.save(destino)


def criar_nota_fiscal(destino, data, historico, valor, numero):
    """Gera imagem simulando nota fiscal de despesa"""

    img = Image.new("RGB", (600, 500), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Borda
    draw.rectangle([10, 10, 590, 490], outline=(0, 0, 0), width=2)

    # Cabeçalho
    draw.rectangle([10, 10, 590, 80], fill=(200, 220, 200))
    draw.text((300, 30), "NOTA FISCAL", fill=(0, 0, 0), anchor="mm")
    draw.text((300, 60), "PRESTAÇÃO DE SERVIÇOS / PRODUTOS", fill=(50, 50, 50), anchor="mm")

    # Número e data
    draw.text((50, 100), f"NF Nº: {numero:06d}", fill=(0, 0, 0))
    draw.text((400, 100), f"Data: {data.strftime('%d/%m/%Y')}", fill=(0, 0, 0))

    # Linha divisória
    draw.line([10, 130, 590, 130], fill=(0, 0, 0), width=1)

    # Emitente fictício
    draw.text((50, 150), "Fornecedor Fictício Ltda", fill=(0, 0, 0))
    draw.text((50, 175), "CNPJ: 98.765.432/0001-10", fill=(100, 100, 100))

    # Linha divisória
    draw.line([10, 210, 590, 210], fill=(0, 0, 0), width=1)

    # Descrição
    draw.text((50, 230), "DESCRIÇÃO DOS SERVIÇOS/PRODUTOS", fill=(0, 0, 0))
    draw.text((50, 260), f"• {historico}", fill=(50, 50, 50))

    # Linha divisória
    draw.line([10, 310, 590, 310], fill=(0, 0, 0), width=1)

    # Valores
    draw.text((50, 330), "Subtotal:", fill=(0, 0, 0))
    draw.text((500, 330), f"R$ {valor:.2f}", fill=(0, 0, 0), anchor="rm")

    draw.rectangle([10, 370, 590, 420], fill=(230, 230, 230))
    draw.text((50, 393), "TOTAL:", fill=(0, 0, 0))
    draw.text((500, 393), f"R$ {valor:.2f}", fill=(0, 0, 0), anchor="rm")

    # Rodapé
    draw.text((300, 450), "Documento gerado para fins de controle interno", 
              fill=(150, 150, 150), anchor="mm")

    img.save(destino)


def gerar_comprovantes_mes(df_mes, pasta_destino, ano, mes):
    """Gera comprovante para cada lançamento do mês"""

    # Limpa pasta antes de gerar — evita arquivos antigos
    if os.path.exists(pasta_destino):
        shutil.rmtree(pasta_destino)

    os.makedirs(pasta_destino, exist_ok=True)

    for _, row in df_mes.iterrows():
        id_lanc = int(row["id"])
        data = row["data"].date()
        categoria = str(row["categoria"]).strip().lower()
        valor = round(float(row["valor"]), 2)
        historico = str(row["historico"])

        nome_base = f"{data.strftime('%Y-%m-%d')}_{categoria}_{id_lanc}.png"
        destino = os.path.join(pasta_destino, nome_base)

        if categoria == "despesa":
            criar_nota_fiscal(destino, data, historico, valor, id_lanc)
        else:
            criar_recibo(destino, data, historico, valor, id_lanc)

    print(f"Comprovantes gerados em: {pasta_destino}")