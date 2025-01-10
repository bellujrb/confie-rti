import streamlit as st
import os
import time

import ncs_inserted
import ncs_totals
import register_project
import register_rti
import register_sector
import report
import start

def login():
    st.title("Login")
    
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state['logged_in'] = True
            st.success("Login realizado com sucesso!")
            time.sleep(1)
            st.rerun()  
        else:
            st.error("Usuário ou senha incorretos.")

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login()
        return

    st.title('Conformetec RTI')

    if 'step' not in st.session_state:
        st.session_state['step'] = 0  

    PAGES_TUTORIAL = [
        {"label": "Início", "page": start},
        {"label": "Cadastro do Projeto", "page": register_project},
        {"label": "Gerenciar Setores", "page": register_sector},
        {"label": "Formatação RTI", "page": register_rti},
        {"label": "NCS Inseridas", "page": ncs_inserted},
        {"label": "Banco de Dados NC", "page": ncs_totals},
        {"label": "Relatório", "page": report}
    ]

    current_step = st.session_state['step']

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if current_step > 0:
            if st.button("← Voltar", key="voltar"):
                st.session_state['step'] -= 1
                st.rerun()

    with col2:
        if current_step < len(PAGES_TUTORIAL) - 1:
            if st.button("Próximo →", key="proximo"):
                st.session_state['step'] += 1
                st.rerun()

    with col3:
        if st.button("Banco de Dados NC", key="banco_dados_nc"):
            st.session_state['step'] = 5  
            st.rerun()

    st.progress((current_step + 1) / len(PAGES_TUTORIAL))

    page_info = PAGES_TUTORIAL[current_step]
    page_info['page'].run()

    st.markdown("---")  

    if current_step == len(PAGES_TUTORIAL) - 1:
        st.success("Você concluiu todos os passos ;)")

if __name__ == "__main__":
    main()
