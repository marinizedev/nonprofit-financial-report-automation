from PyPDF2 import PdfMerger

def gerar_dossie(caminhos_pdf, destino_final):
    merger = PdfMerger()

    for caminho in caminhos_pdf:
        merger.append(caminho)

    merger.write(destino_final)
    merger.close()