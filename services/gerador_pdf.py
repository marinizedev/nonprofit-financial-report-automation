import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

def converter_excel_para_pdf(arquivo_excel):
    libreoffice = os.getenv("LIBREOFFICE_PATH")
    
    if not libreoffice:
        raise ValueError("LIBREOFFICE_PATH não configurado no .env")
    
    pasta_saida = os.path.dirname(os.path.abspath(arquivo_excel))

    subprocess.run([
        libreoffice,
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        pasta_saida,
        arquivo_excel
    ], check=True)

    return arquivo_excel.replace(".xlsx", ".pdf")