import streamlit as st

import ncs_inserted
import ncs_totals
import register_project
import register_rti
import register_sector
import report


def check_credentials(username, password):
    return username == "admin" and password == "admin"


def main():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    # Tela de login
    if not st.session_state['authenticated']:
        st.title("Login")
        with st.form(key='login_form'):
            username = st.text_input("Nome de Usuário")
            password = st.text_input("Senha", type="password")
            login_button = st.form_submit_button("Login")
            if login_button:
                if check_credentials(username, password):
                    st.session_state['authenticated'] = True
                    st.rerun()
                else:
                    st.error("Credenciais incorretas, por favor tente novamente.")
        return

    # Adicionando logo no cabeçalho da sidebar com HTML e CSS
    st.sidebar.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem; margin-top: 1rem;">
            <img src="logo.png" alt="Logo" style="height: 60px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title('Navegação')
    PAGES_INDIVIDUAL = {
        "Cadastro do Projeto": register_project,
        "Cadastro de Setor": register_sector,
        "Formatação RTI": register_rti,
        "NCS Inseridas": ncs_inserted,
        "NCS Cadastradas": ncs_totals,
        "Relatório": report
    }

    selection = st.sidebar.radio("Ir para", list(PAGES_INDIVIDUAL.keys()), key='page')
    page = PAGES_INDIVIDUAL[selection]
    page.run()


if __name__ == "__main__":
    main()
