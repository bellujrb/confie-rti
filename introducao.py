from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib import colors

def add_header_and_footer(canvas, doc):
    # Adicionar cabeçalho
    canvas.setFont("Helvetica-Bold", 10)
    canvas.setFillColor(colors.green)
    canvas.drawString(20, 800, "CONF0323498 – PROJETO TESLA")  # Cabeçalho à esquerda
    canvas.drawRightString(550, 800, f"{doc.page}")  # Número da página à direita

    # Rodapé
    footer_text = (
        "Conformetec Assessoria Técnica para a Conformidade Elétrica\n"
        "Rua Coronel Francisco Schmidt 1400, Sala 33 – Sertãozinho/SP  CEP: 14160-710\n"
        "Telefone (16) 3524-8327"
    )
    text_object = canvas.beginText(105 * 1, 15 * 1)
    for line in footer_text.split("\n"):
        text_width = canvas.stringWidth(line, "Helvetica", 9)
        text_object.setTextOrigin((A4[0] - text_width) / 2, text_object.getY())  # Centralizar o texto
        text_object.textLine(line)
    canvas.drawText(text_object)

def generate_introducao(elements, styles):
    # Ajustar estilos personalizados
    normal_style = ParagraphStyle(
        name='Normal',
        fontName='Helvetica',
        fontSize=12,
        leading=14,  # Espaçamento entre linhas
        alignment=4,  # Alinhamento justificado
    )
    heading_style = ParagraphStyle(
        name='Heading1',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16,
        textColor=colors.black,
        spaceAfter=10
    )

    # Adicionar o título da seção "2 INTRODUÇÃO"
    title = Paragraph("2  INTRODUÇÃO", heading_style)
    elements.append(title)

    # Linha horizontal azul
    elements.append(Spacer(1, 2))
    line_style = ParagraphStyle(name="Line", fontSize=2, spaceAfter=10)
    elements.append(Paragraph("<hr width='100%' color='blue'/>", line_style))

    # Texto do conteúdo de "Introdução"
    introducao_text = """
    A <b>NR-10</b> estabelece os requisitos e condições mínimas objetivando a implantação de medidas de controle e sistemas preventivos, de forma a garantir a segurança e a saúde dos trabalhadores que, direta ou indiretamente, interajam em instalações elétricas e serviços com eletricidade.
    """
    paragraph = Paragraph(introducao_text, normal_style)
    elements.append(paragraph)

    # Espaçamento final
    elements.append(Spacer(1, 20))

