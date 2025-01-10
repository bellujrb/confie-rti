import streamlit as st
import pandas as pd
import requests

# Função para buscar as NCs, com ou sem categoria
def fetch_nc_data(category):
    url = 'http://18.219.73.187:8080/api/non-compliances'
    headers = {
        'accept': 'application/json',
        'Category': category  # O cabeçalho 'Category' é obrigatório, então sempre passamos.
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()  # Retorna o conteúdo da resposta em JSON
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados: {e}")
        st.write(f"Detalhes do erro: {e}")
        return None

def run():
    st.title('NCs Cadastradas')

    # Parte 2: Filtro por Categoria
    st.subheader('Visualizar NCs por Categoria')

    # Seleciona uma categoria
    category_options = [ 
        'TODOS',
        'ACESSIBILIDADE', 
        'IDENTIFICAÇÃO_E_SINALIZAÇÃO', 
        'COMPONENTES_PORTA', 
        'INVOLUCRO', 
        'PARTES_ENERGIZADAS_EXPOSTAS', 
        'ATERRAMENTO', 
        'GRAU_DE_PROTEÇÃO_IP', 
        'LOCKOUT_E_TAGOUT', 
        'DISPOSITIVOS_DE_SECCIONAMENTO_E_PROTEÇÃO', 
        'ESTADO_DE_CONSERVAÇÃO_DOS_COMPONENTES', 
        'ARMAZENAMENTO_INADEQUADO', 
        'IDENTIFICAÇÃO_DOS_COMPONENTES', 
        'CONEXÕES', 
        'ILUMINAÇÃO' 
    ]

    selected_category = st.selectbox('Selecione uma categoria', category_options)

    # Se o usuário selecionar uma categoria, faz a requisição correspondente
    if selected_category:
        nc_category_data = fetch_nc_data(selected_category)
        if nc_category_data:
            # Converte para DataFrame e remove as colunas indesejadas
            df_category = pd.DataFrame(nc_category_data)
            
            # Verifica se há dados
            if df_category.empty:
                st.warning(f"Não foram encontrados dados para a categoria {selected_category}.")
            else:
                # Removendo colunas indesejadas, se existirem
                columns_to_drop = ['created_at', 'updated_at', 'deleted_at']
                df_category = df_category.drop(columns=columns_to_drop, errors='ignore')
                
                # Exibe o DataFrame no Streamlit
                st.dataframe(df_category.style.set_properties(**{'text-align': 'left', 'white-space': 'normal'}))
        else:
            st.error(f"Erro ao carregar os dados da categoria {selected_category}.")

if __name__ == "__main__":
    run()
