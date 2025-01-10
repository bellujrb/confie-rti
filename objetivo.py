from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib import colors

def add_header_and_footer(canvas, doc):
    # Adicionar cabeçalho
    canvas.setFont("Helvetica-Bold", 10)
    canvas.setFillColor(colors.green)
    canvas.drawString(20, 800, "CONF0323498 – PROJETO PEC")  # Cabeçalho à esquerda
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

def generate_objetivo(elements, styles):
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

    # Adicionar o título da seção "1 OBJETIVO"
    title = Paragraph("1  OBJETIVO", heading_style)
    elements.append(title)

    # Linha horizontal azul
    elements.append(Spacer(1, 2))
    line_style = ParagraphStyle(name="Line", fontSize=2, spaceAfter=10)
    elements.append(Paragraph("<hr width='100%' color='blue'/>", line_style))

    # Texto do conteúdo de "Objetivo"
    objective_text = """
    O objetivo técnico deste relatório é:<br/><br/>
    a) Apresentar um diagnóstico das instalações elétricas em relação ao atendimento da Norma Regulamentadora (NR) nº10 Ministério do Trabalho e Emprego (MTE) vigente na época da inspeção;<br/><br/>
    b) Fornecer um Plano de Ação com as não conformidades encontradas e recomendações, como orientação para a empresa adotar em seu programa de segurança, visando adequação para o atendimento da NR-10 e ainda apresentar recomendações de melhorias para seu programa;<br/><br/>
    c) Orientar sobre as principais normas vigentes no Brasil ou normas internacionais quando aplicável, com relação às instalações elétricas.
    """
    paragraph = Paragraph(objective_text, normal_style)
    elements.append(paragraph)

    # Espaçamento final
    elements.append(Spacer(1, 20))

