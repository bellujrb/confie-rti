import streamlit as st
from fpdf import FPDF
from io import BytesIO
import plotly.graph_objects as go


def generate_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adicionar conteúdo ao PDF
    for line in content:
        pdf.cell(200, 10, txt=line, ln=True, align='L')

    # Salvar o PDF em um buffer de memória
    pdf_buffer = BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin1')  # Retorna o conteúdo como bytes
    pdf_buffer.write(pdf_output)
    pdf_buffer.seek(0)  # Reposiciona o buffer no início

    return pdf_buffer


def plot_conformity_chart(conformidades, nao_conformidades):
    # Preparar dados para o gráfico
    labels = ['Conforme', 'Não Conforme']
    sizes = [len(conformidades), len(nao_conformidades)]

    # Criar gráfico de barras usando Plotly
    fig = go.Figure(data=[
        go.Bar(name='Conformidades', x=labels, y=sizes, marker=dict(color=['#4CAF50', '#F44336']), text=sizes,
               textposition='auto')
    ])

    # Atualizar o layout do gráfico
    fig.update_layout(
        title='Gráfico de Conformidade',
        xaxis_title='Status',
        yaxis_title='Quantidade',
        xaxis=dict(tickmode='array', tickvals=labels),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='black')
    )

    # Mostrar gráfico no Streamlit
    st.plotly_chart(fig)

    # Mostrar detalhes das conformidades e não conformidades
    st.write("### Detalhes:")
    st.write("**Conforme:**")
    for item in conformidades:
        st.write(f"- {item}")
    st.write("**Não Conforme:**")
    for item in nao_conformidades:
        st.write(f"- {item}")


def run():
    st.title('Relatório')

    st.write("Clique no botão abaixo para gerar o relatório.")

    if st.button("Gerar Relatório"):
        content = [
            "Relatório de Não Conformidades",
            "",
            "Equipamento (TAG): QD Geral",
            "Descrição: -",
            "Conformetec (TAG): CONF-RTI-001",
            "",
            "Acessibilidade reduzida ao conjunto de manobra e controle.",
            "NC: 2.1 - Descrição: #NAME? - Infração: #NAME? - Nº Conformetec: #N/A - Local: #N/A - TAG: #VALUE! - Descrição: #N/A - Nº IMG: #N/A",
            "NC: 1.2 - D    escrição: #NAME? - Infração: #NAME? - Nº Conformetec: #N/A - Local: #N/A - TAG: #VALUE! - Descrição: #N/A - Nº IMG: #N/A",
            "NC: 1.3 - Descrição: #NAME? - Infração: #NAME? - Nº Conformetec: #N/A - Local: #N/A - TAG: #VALUE! - Descrição: #N/A - Nº IMG: #N/A",
        ]

        # Dados de conformidade (substitua pelos seus próprios dados)
        conformidades = ["Conformidade A", "Conformidade B"]
        nao_conformidades = ["Não Conformidade 1", "Não Conformidade 2", "Não Conformidade 3"]

        # Gerar o PDF
        pdf_buffer = generate_pdf(content)

        # Oferecer download do PDF
        st.download_button(
            label="Download do Relatório",
            data=pdf_buffer,
            file_name="relatorio.pdf",
            mime="application/pdf"
        )

        # Mostrar o gráfico de conformidade
        plot_conformity_chart(conformidades, nao_conformidades)


if __name__ == "__main__":
    run()
