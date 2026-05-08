from services.leitor import carregar_dados
from services.processador import calcular_totais
from services.gerador_excel import gerar_relatorio
from services.validador import validar
from utils.datas import ultimo_dia_do_mes
from services.gerador_pdf import converter_excel_para_pdf
from services.comprovantes_service import listar_comprovantes, gerar_comprovantes
from services.dossie_service import gerar_dossie
from services.capa_service import gerar_capa
from services.validador_comprovantes import validar_comprovantes
from services.gerador_comprovantes_fake import gerar_comprovantes_mes
import shutil
import os

df = carregar_dados("dados/lancamentos_ficticio.xlsx")

grupos = df.groupby(["ano", "mes"])

for (ano, mes), dados_mes in grupos:

    pasta_comprovantes = f"dados/{ano}/{mes:02d}/comprovantes"

    if os.path.exists(pasta_comprovantes):
        shutil.rmtree(pasta_comprovantes)

    gerar_comprovantes_mes(dados_mes, pasta_comprovantes, ano, mes)

    dados_mes = dados_mes.sort_values(by="data")

    totais = calcular_totais(dados_mes)

    data_final = ultimo_dia_do_mes(ano, mes)

    nome_arquivo = f"relatorio_{mes:02d}_{ano}.xlsx"

    print(f"Processando: {mes}/{ano}")

    gerar_relatorio(
        dados_mes,
        ano,
        mes,
        totais,
        data_final,
        "templates/template_relatorio.xlsx",
        nome_arquivo
    )

    validar(dados_mes, f"{mes}/{ano}")

    print(f"Gerado: {nome_arquivo}")

    pdf_relatorio = converter_excel_para_pdf(nome_arquivo)
    print(f"PDF gerado: {pdf_relatorio}")

    # ===== COMPROVANTES =====
    pdf_comprovantes = None
    
    if os.path.exists(pasta_comprovantes):
        comprovantes = listar_comprovantes(pasta_comprovantes)

        if comprovantes:
            pdf_comprovantes = f"comprovantes_{mes:02d}-{ano}.pdf"
            gerar_comprovantes(comprovantes, pdf_comprovantes)
            print(f"Comprovantes gerados: {pdf_comprovantes}")

            # VALIDAÇÃO
            faltantes = validar_comprovantes(dados_mes, pasta_comprovantes)

            if faltantes:
                print("\nCOMPROVANTES FALTANDO:")

                for item in faltantes:
                    print(f"{item['data']} - {item['categoria']} - R$ {item['valor']:.2f}")

            else:
                print("Todos os comprovantes estão OK")

        else:
            print("Nenhumn comprovante encontrado.")

    else:
        print("Pasta de comprovantes não encontrada.")

    capa_pdf = f"capa_{mes:02d}_{ano}.pdf"

    gerar_capa(capa_pdf, mes, ano)

    print(f"Capa gerada: {capa_pdf}")

    # ===== DOSSIÊ FINAL =====
    arquivos_para_unir = [capa_pdf, pdf_relatorio]

    if pdf_comprovantes:
        arquivos_para_unir.append(pdf_comprovantes)
        
    nome_dossie = f"dossie_{mes:02d}_{ano}.pdf"
    
    gerar_dossie(arquivos_para_unir, nome_dossie)

    print(f"Dossiê final gerado: {nome_dossie}")

    # Remove arquivos intermediários
    os.remove(capa_pdf)
    
    if pdf_comprovantes:
        os.remove(pdf_comprovantes)

    print("Arquivos intermediários removidos.")