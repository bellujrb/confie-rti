import streamlit as st
from PIL import Image
import io


def run():
    st.title('Registro de Projeto')

    # Entrada para o número do projeto
    numero_projeto = st.text_input("Número do Projeto")

    # Botão para começar a RIT
    start_rit = st.button("Começar a RIT")

    if start_rit:
        # Se o botão for pressionado, exibir os campos adicionais
        st.subheader("Configurações RTI")

        # Seletor de setor
        setor = st.selectbox("Escolha o Setor", ["Setor A", "Setor B", "Setor C"])

        # Uploader de imagem com base no setor escolhido
        imagens_do_setor = st.file_uploader("Imagens do Setor", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        # Visualizar imagens carregadas
        if imagens_do_setor:
            for imagem in imagens_do_setor:
                # Nome da imagem
                st.write(f"Nome da imagem: {imagem.name}")
                # Botão para visualizar a imagem
                if st.button(f"Visualizar {imagem.name}"):
                    img = Image.open(imagem)
                    st.image(img, caption=imagem.name, use_column_width=True)

        tag_conformetec = st.text_input("Tag Conformetec")
        local = st.text_input("Local")
        tag_equip = st.text_input("Tag Equip")
        desc_equip = st.text_input("Desc Equip")

        st.subheader("Questões RTI Tabela")

        # Lista de perguntas
        perguntas = [
            "O painel está acessível para inspeção, manutenção e operação?",
            "Os dispositivos de proteção estão funcionais?",
            "A sinalização é adequada e legível?"
        ]
        resposta_opcoes = ["Sim", "Não", "N/A"]
        titulo_nc_options = [
            "Conjunto de manobra e controle com acessibilidade reduzida pela maneira de instalação",
            "Proteção inadequada contra contatos indiretos",
            "Sinalização obsoleta ou danificada"
        ]

        # Inicializando a tabela
        for i, pergunta in enumerate(perguntas):
            st.write(f"{i + 1}- {pergunta}")
            cols = st.columns([1, 1, 1, 3])
            with cols[0]:
                resposta = st.radio("", resposta_opcoes, key=f"resposta_{i}")
            with cols[1]:
                st.write("")  # Espaço reservado para manter o layout da tabela consistente
            with cols[2]:
                st.write("")  # Espaço reservado para manter o layout da tabela consistente
            with cols[3]:
                titulo_nc = st.selectbox("Título da NC", options=titulo_nc_options, index=i % len(titulo_nc_options),
                                         key=f"titulo_{i}")
                descricao_nc = st.text_area("Descrição da NC", key=f"desc_{i}")
                recomendacao = st.text_area("Recomendação", key=f"rec_{i}")


if __name__ == "__main__":
    run()
