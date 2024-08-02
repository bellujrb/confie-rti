import streamlit as st
from datetime import datetime


def run():
    st.title('Registro de Projeto')

    with st.form(key='project_form'):
        # Upload de imagem para o logotipo
        numero_conf = st.text_input("Número do Projeto")
        logo = st.file_uploader("Logo (Imagem)", type=['png', 'jpg', 'jpeg'])

        # Campos de texto para as informações do projeto
        nome = st.text_input("Nome")
        cnpj = st.text_input("CNPJ")
        endereco = st.text_input("Endereço")
        city = st.text_input("Cidade/Estado")
        numero_art = st.text_input("Número ART")
        email_cliente = st.text_input("E-mail do cliente")

        # Campo de data
        data = st.date_input("Data", value=datetime.now(),
                             help="Pode pegar da data atual, mas pode inputar manualmente")

        submit_button = st.form_submit_button("Registrar Projeto")

        if submit_button:
            st.success("Projeto registrado com sucesso!")
            # Aqui você pode adicionar código para salvar os dados ou realizar outras ações
