import streamlit as st


def run():
    st.title("Relatório Técnico de Inspeção das Instalações Elétricas (RTI)")

    st.header("Bem-vindo ao Sistema de RTI")

    st.write("""
    O Relatório Técnico de Inspeção das Instalações Elétricas (RTI) é uma ferramenta desenvolvida para facilitar a inspeção e o registro das condições das instalações elétricas de uma propriedade.

    A RTI é de grande importância para garantir a segurança e a conformidade com as normas técnicas, além de auxiliar na manutenção preventiva e corretiva das instalações elétricas.
    """)

    st.subheader("Funcionalidades do Sistema RTI:")

    st.write("""
    - **Visualização de RTI**: O cliente poderá visualizar os resultados das RTIs realizadas e acessar as informações detalhadas sobre o estado de cada componente inspecionado.
    - **Criação de RTI**: O engenheiro responsável terá a capacidade de gerar e preencher um relatório RTI com base nas inspeções realizadas nas instalações elétricas.
    """)

    st.subheader("Como Funciona a Criação de uma RTI?")

    st.write("""
    1. O engenheiro irá iniciar a criação de uma RTI, inserindo o número do projeto e escolhendo o setor a ser inspecionado.
    2. Durante a inspeção, serão coletadas imagens e informações detalhadas sobre as condições das instalações.
    3. O sistema permite ao engenheiro registrar as não conformidades (NC), suas descrições e recomendações para correção.
    4. Após concluir a inspeção, o relatório RTI é gerado e pode ser visualizado pelo cliente.
    """)

    st.subheader("Status Atual: Em Fase de Testes")

    st.write("""
    O sistema RTI ainda está em fase de testes e melhorias contínuas. Estamos trabalhando para garantir que todas as funcionalidades estejam completas e funcionando corretamente. Agradecemos a sua paciência enquanto refinamos o sistema.
    """)

    st.info("Caso tenha dúvidas ou sugestões, por favor entre em contato com o suporte técnico.")