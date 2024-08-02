import streamlit as st
import pandas as pd

def run():
    st.title('Total de NCS Cadastradas')

    # Supondo que os dados já estão carregados em st.session_state.control_data
    if 'control_data' not in st.session_state:
        # Caso os dados ainda não estejam no estado da sessão, vamos criar alguns dados fictícios
        st.session_state.control_data = pd.DataFrame({
            'Titulo da NC': ["NC1", "NC2", "NC3"],
            'Descricao da NC': ["Descrição de NC1", "Descrição de NC2", "Descrição de NC3"],
            'Base Tecnica': ["Técnica 1", "Técnica 2", "Técnica 3"],
            'Base Legal': ["Lei A", "Lei B", "Lei C"],
            'Infracoes': ["Infração 1", "Infração 2", "Infração 3"],
            'Recomendações': ["Recomendação 1", "Recomendação 2", "Recomendação 3"],
            'Notas': ["Nota 1", "Nota 2", "Nota 3"],
        })

    # Renomeando as colunas do DataFrame
    st.session_state.control_data.rename(columns={
        'Titulo da NC': 'Título da NC',
        'Descricao da NC': 'Descrição da NC',
        'Base Tecnica': 'Base Técnica',
        'Base Legal': 'Base Legal',
        'Infracoes': 'Infrações',
        'Recomendações': 'Recomendações',
        'Antigo': 'Antigo',
        'Novo': 'Novo'
    }, inplace=True)

    # Exibindo a tabela
    st.dataframe(st.session_state.control_data.style.set_properties(**{'text-align': 'left', 'white-space': 'normal'}))

if __name__ == "__main__":
    run()
