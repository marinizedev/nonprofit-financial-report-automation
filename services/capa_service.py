from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def gerar_capa(destino, mes, ano):
    doc = SimpleDocTemplate(destino)

    styles = getSampleStyleSheet()

    estilo_central = ParagraphStyle(
        name="Centralizado",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        spaceAfter=10
    )

    estilo_titulo = ParagraphStyle(
        name="Titulo",
        parent=styles["Title"],
        alignment=TA_CENTER
    )

    elementos = []

    # LOGO
    try:
        logo = Image("assets/logo.png", width=120, height=120)
        logo.hAlign = "CENTER"
        elementos.append(logo)
        elementos.append(Spacer(1, 20))
    except:
        pass

    # TÍTULO
    elementos.append(Paragraph("RELATÓRIO FINANCEIRO", estilo_titulo))
    elementos.append(Spacer(1, 30))

    # MÊS
    elementos.append(Paragraph(f"Mês: {mes:02d}/{ano}", estilo_central))
    elementos.append(Spacer(1, 20))

    # RESPONSÁVEL
    elementos.append(Paragraph("Responsável: ____________________", estilo_central))
    elementos.append(Spacer(1, 15))

    # IGREJA
    elementos.append(Paragraph("Igreja: COMUNIDADE ESPERANÇA", estilo_central))
    elementos.append(Spacer(1, 30))

    doc.build(elementos)