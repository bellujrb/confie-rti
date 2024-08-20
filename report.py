import streamlit as st
from fpdf import FPDF
from io import BytesIO
import matplotlib.pyplot as plt


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

    # Criar gráfico de barras
    fig, ax = plt.subplots(figsize=(6, 4))

    # Definir cores e barras com gradiente suave
    bar_colors = ['#4CAF50', '#F44336']
    bars = ax.bar(labels, sizes, color=bar_colors, edgecolor='black', linewidth=1.2)

    # Adicionar rótulos de valor nas barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, int(yval), ha='center', va='bottom', fontsize=12,
                fontweight='bold')

    # Adicionar título e rótulos
    ax.set_title('Gráfico de Conformidade', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Quantidade', fontsize=12)
    ax.set_xlabel('Status', fontsize=12)

    # Adicionar grade para melhorar a legibilidade
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Ajustar limites do eixo Y para dar espaço ao rótulo superior
    ax.set_ylim(0, max(sizes) + 1)

    # Estilo mais atraente
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12)

    # Mostrar gráfico
    st.pyplot(fig)

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
            "NC: 1.2 - Descrição: #NAME? - Infração: #NAME? - Nº Conformetec: #N/A - Local: #N/A - TAG: #VALUE! - Descrição: #N/A - Nº IMG: #N/A",
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
