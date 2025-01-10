import streamlit as st
import pandas as pd
import requests

def run():
    st.title('NCs Inseridas')

    # Função para fazer a requisição dos setores da API
    def fetch_sectors():
        url = 'http://18.219.73.187:8080/api/sectors'
        try:
            response = requests.get(url, headers={'accept': 'application/json'})
            if response.status_code == 200:
                return response.json()  # Retorna os dados no formato JSON
            else:
                st.error(f"Erro ao buscar setores: {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            st.error(f"Erro de conexão: {e}")
            return []

    # Verifica se os dados já estão carregados na sessão
    if 'ncs_data' not in st.session_state:
        # Dados fictícios de NCs
        st.session_state.ncs_data = pd.DataFrame({
            'Numero CONF': [101, 102, 103],
            'N° NC': [1, 2, 3],
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
        })

    # Buscar os setores da API e verificar se a coluna "Setor" está carregada
    setores_data = fetch_sectors()

    if setores_data:
        # Extrair os nomes dos setores da resposta da API (presumindo que a resposta contenha uma lista de dicionários)
        setores_nomes = [setor['name'] for setor in setores_data]  # Ajuste conforme a estrutura da resposta da API
    else:
        # Se não conseguir buscar os setores, usa valores genéricos
        setores_nomes = ['Setor A', 'Setor B', 'Setor C']

    # Adicionar a coluna "Setor" caso não exista
    if 'Setor' not in st.session_state.ncs_data.columns:
        # Cria a coluna "Setor" com base nos dados da API (ou valores genéricos)
        st.session_state.ncs_data['Setor'] = setores_nomes[:len(st.session_state.ncs_data)]

    # Selecionar setor para visualizar NCs daquele setor específico
    setor_selecionado = st.selectbox('Selecione o Setor para Visualizar NCs', setores_nomes)

    # Filtrar NCs pelo setor selecionado
    ncs_setor = st.session_state.ncs_data[st.session_state.ncs_data['Setor'] == setor_selecionado]

    st.subheader(f'NCs para o Setor: {setor_selecionado}')
    # Exibindo tabela com NCs do setor selecionado
    st.dataframe(ncs_setor.style.set_properties(**{
        'text-align': 'left',
        'white-space': 'normal'
    }))

    # Exibindo tabela com todas as NCs
    st.subheader('Todas as NCs')
    st.dataframe(st.session_state.ncs_data.style.set_properties(**{
        'text-align': 'left',
        'white-space': 'normal'
    }))

if __name__ == "__main__":
    run()
