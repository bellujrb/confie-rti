from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib import colors

def add_header_and_footer(canvas, doc):
    canvas.setFont("Helvetica-Bold", 10)
    canvas.setFillColor(colors.green)
    canvas.drawString(20, 800, "CONF0323498 – PROJETO TESLA")  # Cabeçalho à esquerda
    canvas.drawRightString(550, 800, f"{doc.page}")  # Número da página à direita

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

def generate_metodologia(elements, styles):
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

    # Adicionar o título da seção "3 METODOLOGIA"
    title = Paragraph("3  METODOLOGIA", heading_style)
    elements.append(title)

    # Linha horizontal azul
    elements.append(Spacer(1, 2))
    line_style = ParagraphStyle(name="Line", fontSize=2, spaceAfter=10)
    elements.append(Paragraph("<hr width='100%' color='blue'/>", line_style))

    # Texto do conteúdo de "Metodologia"
    metodologia_text = """
    A nossa metodologia consiste em uma verificação minuciosa da documentação existente e dos meios de gestão das instalações elétricas voltada para a segurança. Para a inspeção visual utilizamos as prescrições da NBR 5410, seção 7 - Verificação Final (sem ensaios), item <b>7.2 Inspeção visual.</b><br/><br/>
    <b>7.2.1</b> A inspeção visual deve preceder os ensaios e ser efetuada normalmente com a instalação desenergizada.<br/><br/>
    <b>7.2.2</b> A inspeção visual é destinada a verificar se os componentes que constituem a instalação fixa permanente:<br/>
    a) são conformes às normas aplicáveis;<br/>
    <b>NOTA:</b> Isto pode ser verificado por marca de conformidade, certificação ou informação declarada pelo fornecedor.<br/>
    b) foram corretamente selecionados e instalados de acordo com esta Norma;<br/>
    c) não apresentam danos aparentes que possam comprometer seu funcionamento adequado e a segurança.<br/><br/>
    <b>7.2.3</b> A inspeção visual deve incluir no mínimo a verificação dos seguintes pontos:<br/>
    a) medidas de proteção contra choques elétricos, conforme 5.1;<br/>
    b) medidas de proteção contra efeitos térmicos, conforme 5.2;<br/>
    c) seleção e instalação das linhas elétricas, conforme 6.2;<br/>
    d) seleção, ajuste e localização dos dispositivos de proteção, conforme 6.3;<br/>
    e) presença dos dispositivos de seccionamento e comando, sua adequação e localização, conforme 5.6 e 6.3;<br/>
    f) adequação dos componentes e das medidas de proteção às condições de influências externas<br/>
    g) existentes, conforme 5.2.2, 6.1.3.2, 6.2.4, seção 9 e anexo C;<br/>
    h) identificação dos componentes, conforme 6.7;<br/>
    i) presença das instruções, sinalizações e advertências requeridas;<br/>
    j) adequação das conexões, conforme 6.2.8;<br/>
    k) acessibilidade, conforme 4.1.10 e 6.1.4.
    """
    paragraph = Paragraph(metodologia_text, normal_style)
    elements.append(paragraph)

    # Espaçamento final
    elements.append(Spacer(1, 20))

