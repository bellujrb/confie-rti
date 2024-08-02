import streamlit as st
import pandas as pd

def run():
    st.title('NCS Inseridas')

    # Criando um DataFrame com dados de exemplo
    if 'ncs_data' not in st.session_state:
        st.session_state.ncs_data = pd.DataFrame({
            'Numero CONF': [101, 102, 103],
            'Imagem': ['https://via.placeholder.com/150', 'https://via.placeholder.com/150', 'https://via.placeholder.com/150'],
            'Local': ['Local A', 'Local B', 'Local C'],
            'Tag Equipamento': ['Tag 1', 'Tag 2', 'Tag 3'],
            'Descricao Equipamento': ['Desc 1', 'Desc 2', 'Desc 3'],
            'Titulo NC': ['Título NC1', 'Título NC2', 'Título NC3'],
            'Descricao NC': ['Descrição NC1', 'Descrição NC2', 'Descrição NC3'],
            'Base Tecnica': ['Base Técnica 1', 'Base Técnica 2', 'Base Técnica 3'],
            'Base Legal': ['Lei X', 'Lei Y', 'Lei Z'],
            'Infracao': ['Infração 1', 'Infração 2', 'Infração 3'],
            'Recomendacao': ['Recomendação 1', 'Recomendação 2', 'Recomendação 3'],
            'N° NC': [1, 2, 3]
        })

    st.dataframe(st.session_state.ncs_data.style.set_properties(**{
        'text-align': 'left',
        'white-space': 'normal'
    }))

if __name__ == "__main__":
    run()
