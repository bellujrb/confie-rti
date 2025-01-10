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

def generate_documentacao(elements, styles):
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

    # Adicionar o título da seção "5 DOCUMENTAÇÃO DAS INSTALAÇÕES ELÉTRICAS"
    title = Paragraph("5  DOCUMENTAÇÃO DAS INSTALAÇÕES ELÉTRICAS", heading_style)
    elements.append(title)

    # Linha horizontal azul
    elements.append(Spacer(1, 2))
    line_style = ParagraphStyle(name="Line", fontSize=2, spaceAfter=10)
    elements.append(Paragraph("<hr width='100%' color='blue'/>", line_style))

    # Texto do conteúdo de "Documentação das Instalações Elétricas"
    documentacao_text = """
    Os estabelecimentos com carga instalada superior a 75 kW devem constituir e manter o <b>Prontuário de instalações elétricas (PIE)</b>, contendo, além do disposto nos subitens:<br/><br/>
    <b>10.2.3</b> “Os estabelecimentos são obrigados a manter esquemas unifilares atualizados das instalações elétricas dos seus estabelecimentos, com as especificações do sistema de aterramento e demais equipamentos e dispositivos de proteção”, no mínimo o disposto no subitem 10.2.4 e quando aplicável 10.2.5.<br/>
    a) conjunto de procedimentos e instruções técnicas e administrativas de segurança e saúde, implantadas e relacionadas a esta NR e descrição das medidas de controle existentes;<br/>
    b) documentação das inspeções e medições do sistema de proteção contra descargas atmosféricas e aterramentos elétricos;<br/>
    c) especificação dos equipamentos de proteção coletiva e individual e o ferramental, aplicáveis conforme determina esta NR;<br/>
    d) documentação comprobatória da qualificação, habilitação, capacitação, autorização dos trabalhadores e dos treinamentos realizados;<br/>
    e) resultados dos testes de isolação elétrica realizados em equipamentos de proteção individual e coletiva;<br/>
    f) certificações dos equipamentos e materiais elétricos em áreas classificadas;<br/>
    g) relatório técnico das inspeções atualizadas com recomendações, cronogramas de adequações, contemplando as alíneas de “a” a “f”.<br/><br/>
    <b>10.2.5</b> As empresas que operam em instalações ou equipamentos integrantes do sistema elétrico de potência devem constituir prontuário com o conteúdo do item 10.2.4 e acrescentar ao prontuário dos documentos a seguir listados:<br/>
    a) descrição dos procedimentos para emergências;<br/>
    b) certificações dos equipamentos de proteção coletiva e individual.<br/>
    Para o atendimento destas premissas há muitos outros documentos que são necessários e que estão implícitos neste item, e que para atendê-lo faz-se necessário recorrer às normas técnicas.
    """
    paragraph = Paragraph(documentacao_text, normal_style)
    elements.append(paragraph)

    # Espaçamento final
    elements.append(Spacer(1, 20))

