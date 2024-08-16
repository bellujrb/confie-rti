import streamlit as st
import pandas as pd
from datetime import datetime


# Função para inicializar o banco de dados no cache
@st.cache_data
def init_db():
    return pd.DataFrame(columns=["Número do Projeto", "Logo", "Nome", "CNPJ", "Endereço", "Cidade/Estado", "Número ART",
                                 "E-mail do Cliente", "Data"])


def run():
    st.title('Registro de Projeto')

    # Inicializa o banco de dados
    db = init_db()

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
            # Adiciona os dados ao DataFrame
            new_entry = pd.DataFrame([[numero_conf, logo, nome, cnpj, endereco, city, numero_art, email_cliente, data]],
                                     columns=db.columns)
            db = pd.concat([db, new_entry], ignore_index=True)

            st.success("Projeto registrado com sucesso!")

            # Exibe a tabela atualizada
            st.dataframe(db)

            # Atualiza o banco de dados no cache
            st.cache_data.clear()
            st.cache_data(init_db)

