import streamlit as st
import pandas as pd

def initialize_session_state():
    if 'registered_sectors' not in st.session_state:
        st.session_state['registered_sectors'] = []

def run():
    st.title('Gerenciar Setores')

    initialize_session_state()

    with st.form(key='new_sector_form'):
        nome_do_setor = st.text_input("Nome do Novo Setor")

        imagens_do_setor = st.file_uploader("Imagens do Setor", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        submit_button = st.form_submit_button("Registrar Setor")

        if submit_button:
            if nome_do_setor and imagens_do_setor:
                st.session_state.registered_sectors.append({
                    'nome': nome_do_setor,
                    'imagens': list(imagens_do_setor)  
                })
                st.success("Setor registrado com sucesso!")
            else:
                st.error("Por favor, preencha o nome do setor e selecione ao menos uma imagem.")

    if st.session_state['registered_sectors']:
        st.subheader("Setores Registrados")

        df = pd.DataFrame({
            "Nome do Setor": [setor['nome'] for setor in st.session_state['registered_sectors']],
            "Número de Imagens": [len(setor['imagens']) for setor in st.session_state['registered_sectors']]
        })

        st.dataframe(df)

        setor_selecionado = st.selectbox("Selecione um Setor para gerenciar:", df['Nome do Setor'])

        setor = next(item for item in st.session_state['registered_sectors'] if item["nome"] == setor_selecionado)

        st.subheader(f"Imagens do Setor: {setor_selecionado}")
        num_cols = 3  
        cols = st.columns(num_cols)

        for index, imagem in enumerate(setor['imagens']):
            with cols[index % num_cols]:
                st.image(imagem, caption=imagem.name, use_column_width=True)
                if st.button(f"Excluir {imagem.name}", key=f"delete_{setor_selecionado}_{index}"):
                    setor['imagens'].remove(imagem)
                    st.success(f"Imagem {imagem.name} excluída com sucesso!")
                    st.experimental_rerun()

        with st.expander(f"Adicionar novas imagens ao setor: {setor_selecionado}"):
            novas_imagens = st.file_uploader("Novas imagens do Setor", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'], key=f'new_images_{setor_selecionado}')
            if novas_imagens:
                setor['imagens'].extend(novas_imagens)
                st.success("Novas imagens adicionadas com sucesso!")
                st.experimental_rerun()

        with st.expander(f"Editar nome do setor: {setor_selecionado}"):
            novo_nome = st.text_input("Editar nome do setor", value=setor['nome'], key=f"edit_nome_{setor_selecionado}")
            if st.button("Salvar nome editado", key=f"save_name_{setor_selecionado}"):
                setor['nome'] = novo_nome
                st.success("Nome do setor atualizado com sucesso!")
                st.experimental_rerun()

if __name__ == "__main__":
    run()
