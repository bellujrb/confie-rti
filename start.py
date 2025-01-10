import streamlit as st

def run():
    st.title("Bem-vindo ao Sistema de Criação de RTI da Conformetec")
    
    st.subheader("O que é o RTI?")
    st.write("""
    O RTI (Relatório Técnico de Inspeção) é um documento essencial para o acompanhamento e verificação de projetos de engenharia. 
    Ele serve para registrar não conformidades, ações corretivas, e garantir que todos os processos atendam aos requisitos e normas estabelecidas.
    """)
    
    st.subheader("Como usar o sistema?")
    st.write("""
    Este sistema foi projetado para ser uma ferramenta intuitiva e eficiente para engenheiros da Conformetec. 
    Siga as etapas abaixo para utilizar o sistema:
    
    1. **Cadastro do Projeto**: Registre as informações iniciais do projeto, incluindo número do projeto, nome, CNPJ, endereço e outras informações necessárias.
    2. **Cadastro de Setor**: Adicione setores relacionados ao projeto, especificando as áreas de atuação e responsáveis.
    3. **Formatação RTI**: Formate e organize o relatório técnico de inspeção de acordo com os padrões da Conformetec.
    4. **Inserção de NCS**: Registre as Não Conformidades (NCS) encontradas durante as inspeções.
    5. **Visualização de NCS Cadastradas**: Consulte todas as NCS registradas e verifique o status de cada uma.
    6. **Relatório Final**: Gere o relatório final do RTI para revisão e aprovação.
    """)

    st.info("Este sistema é de uso exclusivo da Conformetec e foi desenvolvido para otimizar o processo de criação e gestão de RTIs.")