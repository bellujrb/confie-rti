import streamlit as st


def run():
    st.title('Registrar Setor')

    # Número CONF do projeto com o qual o usuário está interagindo
    numero_conf = "12345"  # Este valor pode ser dinamicamente ajustado conforme a necessidade

    st.header(f"Número CONF: {numero_conf})")

    with st.form(key='sector_form'):
        # Campo de texto para o nome do setor
        nome_do_setor = st.text_input("Nome do Setor")

        # Uploader para múltiplas imagens
        imagens_do_setor = st.file_uploader("Imagens do Setor", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        # Botão de envio do formulário
        submit_button = st.form_submit_button("Registrar Setor")

        if submit_button:
            st.success("Setor registrado com sucesso!")
            st.write("Nome do Setor:", nome_do_setor)

            if imagens_do_setor:
                st.write("Imagens carregadas:")
                # Define a quantidade de colunas que deseja
                num_cols = 3
                # Cria iterador para as colunas
                cols = st.columns(num_cols)
                # Itera sobre as imagens e as colunas
                for index, imagem in enumerate(imagens_do_setor):
                    with cols[index % num_cols]:
                        st.image(imagem, caption=imagem.name, use_column_width=True)


if __name__ == "__main__":
    run()
