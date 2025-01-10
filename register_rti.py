import streamlit as st
import requests

def initialize_session_state():
    if 'inputs' not in st.session_state:
        st.session_state.inputs = {
            "numero_projeto": "",
            "setor": "Setor A",  
            "tag_conformetec": "",
            "local": "",
            "tag_equip": "",
            "desc_equip": ""
        }

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    if 'selected_images' not in st.session_state:
        st.session_state.selected_images = []

    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    if 'responses' not in st.session_state:
        st.session_state.responses = []

    if 'resposta_atual' not in st.session_state:
        st.session_state.resposta_atual = ""

    if 'titulo_nc_atual' not in st.session_state:
        st.session_state.titulo_nc_atual = ""

    if 'descricao_nc_atual' not in st.session_state:
        st.session_state.descricao_nc_atual = ""

    if 'recomendacao_atual' not in st.session_state:
        st.session_state.recomendacao_atual = ""

    if 'api_images' not in st.session_state:
        st.session_state.api_images = []  

def fetch_sectors():
    url = "http://18.219.73.187:8080/api/sectors"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  
    else:
        st.error("Falha ao buscar os setores da API.")
        return []

def fetch_questions():
    url = "http://18.219.73.187:8080/api/questions"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Falha ao buscar perguntas da API")
        return []

def input_form():
    st.subheader("Informações do Projeto")

    st.session_state.inputs["numero_projeto"] = st.text_input("Número do Projeto", st.session_state.inputs["numero_projeto"])

    sectors_data = fetch_sectors()
    
    if sectors_data:
        sector_names = [sector['name'] for sector in sectors_data] 
        selected_sector = st.selectbox("Escolha o Setor", sector_names) 

        sector_selected_data = next(sector for sector in sectors_data if sector['name'] == selected_sector)
        image_urls = eval(sector_selected_data['images'])  

        st.session_state.api_images = image_urls

        st.write(f"Setor selecionado: {selected_sector}")
    else:
        st.error("Nenhum setor disponível.")

    st.session_state.inputs["tag_conformetec"] = st.text_input("Tag Conformetec", st.session_state.inputs["tag_conformetec"])
    st.session_state.inputs["local"] = st.text_input("Local", st.session_state.inputs["local"])
    st.session_state.inputs["tag_equip"] = st.text_input("Tag Equip", st.session_state.inputs["tag_equip"])
    st.session_state.inputs["desc_equip"] = st.text_input("Desc Equip", st.session_state.inputs["desc_equip"])

def run():
    initialize_session_state()

    st.title('Registro de Projeto')

    questions_data = fetch_questions()

    if not questions_data:
        st.error("Nenhuma pergunta disponível.")
        return

    input_form()

    perguntas = [q["question"] for q in questions_data]
    resposta_opcoes = ["Sim", "Não", "N/A"]

    current_question = questions_data[st.session_state.question_index]
    nc_options = [nc["nc_title"] for nc in current_question["ncs"]]

    pergunta_atual = perguntas[st.session_state.question_index]
    st.markdown(f"<h2>{pergunta_atual}</h2>", unsafe_allow_html=True)

    st.session_state.resposta_atual = st.radio("Resposta", resposta_opcoes, key=f"resposta_{st.session_state.question_index}")

    if st.session_state.resposta_atual == "Não":
        selected_nc = st.selectbox("Título da NC", options=nc_options, key=f"titulo_{st.session_state.question_index}")

        nc_selecionada = next(nc for nc in current_question["ncs"] if nc["nc_title"] == selected_nc)

        st.text_area("Descrição da NC", value=nc_selecionada["nc_description"], height=150, disabled=True)
        st.text_area("Recomendação", value=nc_selecionada["recommendation"], height=150, disabled=True)

        st.write("Escolha imagens associadas à resposta:")
        selected_images = []
        cols = st.columns(3)  

        for i, url in enumerate(st.session_state.api_images):
            with cols[i % 3]:
                st.image(url, use_column_width=True)
                if st.checkbox(f"Selecionar Imagem {i+1}", key=f"select_img_{i}"):
                    selected_images.append(url)

        st.write("Imagens selecionadas:")
        if selected_images:
            for img_url in selected_images:
                st.write(img_url)
        else:
            st.write("Nenhuma imagem selecionada.")
    else:
        st.info("Detalhes de não conformidade não necessários para esta resposta.")
        st.session_state.selected_images.clear()

    st.write("---")

    if st.button("Próxima Pergunta"):
        if st.session_state.question_index < len(perguntas) - 1:
            st.session_state.question_index += 1
        else:
            st.success("Você respondeu a todas as perguntas!")

if __name__ == "__main__":
    run()
