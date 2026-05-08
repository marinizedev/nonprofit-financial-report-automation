import os
from datetime import datetime
from PyPDF2 import PdfMerger
from PIL import Image
import tempfile

EXTENSOES_VALIDAS = (".png", ".jpg", ".jpeg", ".pdf")

def listar_comprovantes(pasta):
    comprovantes = []

    for nome in os.listdir(pasta):
        if nome.lower().endswith(EXTENSOES_VALIDAS):

            try:
                data_str = nome.split("_")[0]
                data = datetime.strptime(data_str, "%Y-%m-%d")

                comprovantes.append({
                    "nome": nome,
                    "caminho": os.path.join(pasta, nome),
                    "data": data
                })
            except:
                print(f"Arquivo ignorado (fora do padrão): {nome}")

    return sorted(comprovantes, key=lambda x: x["data"])

def gerar_comprovantes(lista, destino_pdf):
    merger= PdfMerger()
    temporarios = []

    for item in lista:
        caminho = item["caminho"]

        if caminho.lower().endswith(".pdf"):
            merger.append(caminho)

        else:
            img = Image.open(caminho).convert("RGB")

            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            img.save(temp.name, "PDF")

            temporarios.append(temp.name)
            merger.append(temp.name)

    merger.write(destino_pdf)
    merger.close()

    for temp in temporarios:
        os.remove(temp)