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

def generate_normas(elements, styles):
    # Ajustar estilos personalizados
    normal_style = ParagraphStyle(
        name='Normal',
        fontName='Helvetica',
        fontSize=12,
        leading=14,  # Espaçamento entre linhas
        alignment=4,  # Alinhamento justificado
    )
    bold_style = ParagraphStyle(
        name='Bold',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        alignment=4,
    )
    heading_style = ParagraphStyle(
        name='Heading1',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16,
        textColor=colors.black,
        spaceAfter=10
    )

    # Adicionar o título da seção "4 NORMAS"
    title = Paragraph("4  NORMAS", heading_style)
    elements.append(title)

    # Linha horizontal azul
    elements.append(Spacer(1, 2))
    line_style = ParagraphStyle(name="Line", fontSize=2, spaceAfter=10)
    elements.append(Paragraph("<hr width='100%' color='blue'/>", line_style))

    # Texto do conteúdo de "Normas"
    normas_text = """
    Norma é o instrumento que estabelece, em relação a processos existentes, prescrições destinadas à utilização com vistas à obtenção de um grau mínimo de aceitação de um produto ou serviço.<br/><br/>
    <b>NR 10</b> da Secretaria do Trabalho estabelece em seus parágrafos:<br/>
    <b>10.1.1</b> Esta Norma Regulamentadora – <b>NR</b> estabelece os requisitos e condições mínimas, objetivando a implantação de medidas de controle e sistemas preventivos, de forma a garantir a segurança e a saúde dos trabalhadores que, direta ou indiretamente, interajam em instalações elétricas e serviços com eletricidade.<br/>
    <b>10.1.2</b> Esta NR se aplica às fases de geração, transmissão, distribuição e consumo, incluindo as etapas de projeto, construção, montagem, operação, manutenção das instalações elétricas e quaisquer trabalhos realizados nas suas proximidades, observando-se as normas técnicas oficiais estabelecidas pelos órgãos competentes e, na ausência ou omissão destas, as normas internacionais cabíveis.<br/><br/>
    Entre elas estão as seguintes normas:<br/>
    a) NR 10 – Segurança em Instalações e Serviços em Eletricidade;<br/>
    b) NBR 5410 – Instalações elétricas de Baixa Tensão;<br/>
    c) NBR 14039 – Instalações elétricas de média tensão de 1,0 kV a 36,2 kV;<br/>
    d) NBR 61439-1 – Conjuntos de manobra e controle de baixa tensão – Regras Gerais;<br/>
    e) NBR 61439-3 – Conjuntos de manobra e controle de baixa tensão – Quadro de distribuição destinado a ser utilizado por pessoas comuns (DBO);<br/>
    f) NBR IEC 62271-200 – Conjunto de manobra e controle de alta tensão em invólucro metálico para tensões acima de 1 kV até e inclusive 52 kV;<br/>
    g) NBR 60079-14 – Atmosferas explosivas - Parte 14: Projeto, seleção e montagem de instalações elétricas;<br/>
    h) NFPA 70E - Standard for electrical safety in the workplace.
    """
    paragraph = Paragraph(normas_text, normal_style)
    elements.append(paragraph)

    # Espaçamento final
    elements.append(Spacer(1, 20))

