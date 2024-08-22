import streamlit as st
from PIL import Image
import time

# Função para formatar o tempo em horas, minutos e segundos
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def run():
    st.title('Registro de Projeto')

    # Entrada para o número do projeto
    numero_projeto = st.text_input("Número do Projeto")

    # Inicializando variáveis de sessão
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "elapsed_time" not in st.session_state:
        st.session_state.elapsed_time = 0
    if "temporizador_iniciado" not in st.session_state:
        st.session_state.temporizador_iniciado = False

    # Se o temporizador já foi iniciado, calcular o tempo decorrido
    if st.session_state.temporizador_iniciado:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time

    # Botão para começar a RIT
    if not st.session_state.temporizador_iniciado:
        start_rit = st.button("Começar a RIT")
        if start_rit:
            # Inicia o temporizador e marca como iniciado
            st.session_state.start_time = time.time()
            st.session_state.temporizador_iniciado = True

    # Exibir os campos adicionais após a RIT ser iniciada
    if st.session_state.temporizador_iniciado:
        st.subheader("Configurações RTI")

        # Seletor de setor
        setor = st.selectbox("Escolha o Setor", ["Setor A", "Setor B", "Setor C"])

        # Uploader de imagem com base no setor escolhido
        imagens_do_setor = st.file_uploader("Imagens do Setor", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        # Visualizar imagens carregadas
        if imagens_do_setor:
            for imagem in imagens_do_setor:
                # Nome da imagem
                st.write(f"Nome da imagem: {imagem.name}")
                # Botão para visualizar a imagem
                if st.button(f"Visualizar {imagem.name}"):
                    img = Image.open(imagem)
                    st.image(img, caption=imagem.name, use_column_width=True)

        tag_conformetec = st.text_input("Tag Conformetec")
        local = st.text_input("Local")
        tag_equip = st.text_input("Tag Equip")
        desc_equip = st.text_input("Desc Equip")

        st.subheader("Questões RTI Tabela")

        # Lista de perguntas
        perguntas = [
            "O painel está acessível para inspeção, manutenção e operação?",
            "Os dispositivos de proteção estão funcionais?",
            "A sinalização é adequada e legível?"
        ]
        resposta_opcoes = ["Sim", "Não", "N/A"]
        titulo_nc_options = [
            "Conjunto de manobra e controle com acessibilidade reduzida pela maneira de instalação",
            "Proteção inadequada contra contatos indiretos",
            "Sinalização obsoleta ou danificada"
        ]

        # Organizando as perguntas em expansores para melhorar a interface
        with st.form("form_rti"):
            for i, pergunta in enumerate(perguntas):
                with st.expander(f"{i + 1}- {pergunta}"):
                    cols = st.columns([1, 3])
                    with cols[0]:
                        resposta = st.radio("Resposta", resposta_opcoes, key=f"resposta_{i}")
                    with cols[1]:
                        titulo_nc = st.selectbox("Título da NC", options=titulo_nc_options, index=i % len(titulo_nc_options),
                                                 key=f"titulo_{i}")
                        descricao_nc = st.text_area("Descrição da NC", key=f"desc_{i}")
                        recomendacao = st.text_area("Recomendação", key=f"rec_{i}")
            # Botão para submeter o formulário
            submit = st.form_submit_button("Salvar Respostas")

        if submit:
            st.success("Respostas salvas com sucesso!")

        # Botão para criar a RTI
        criar_rti = st.button("Criar RTI")

        if criar_rti:
            # Salvando o tempo decorrido
            st.success(f"RTI criada! Tempo total: {format_time(st.session_state.elapsed_time)}")
            # Resetando o tempo para o próximo registro
            st.session_state.start_time = None
            st.session_state.elapsed_time = 0
            st.session_state.temporizador_iniciado = False

run()
