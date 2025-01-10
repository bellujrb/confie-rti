import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import re

def init_db():
    return pd.DataFrame(columns=["Número do Projeto", "Nome do Cliente", "CNPJ", "Endereço", "Cidade/Estado", "Número ART",
                                 "E-mail do Cliente", "CEP", "Data"])

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14:
        return False
    
    multiplicadores_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def calcula_dv(multiplicadores, num):
        soma = sum(int(digito) * multiplicador for digito, multiplicador in zip(num, multiplicadores))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    dv1 = calcula_dv(multiplicadores_1, cnpj[:-2])
    dv2 = calcula_dv(multiplicadores_2, cnpj[:-2] + dv1)
    
    return cnpj[-2:] == dv1 + dv2

def validar_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def validar_numerico(valor):
    return valor.isdigit()

def buscar_endereco_cep(cep):
    cep = re.sub(r'\D', '', cep)
    if len(cep) != 8:
        return None
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def buscar_empresa_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14:
        return None
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def run():
    st.title('Registro de Projeto')

    db = init_db()

    if 'nome' not in st.session_state:
        st.session_state['nome'] = ''
    if 'endereco' not in st.session_state:
        st.session_state['endereco'] = ''
    if 'city' not in st.session_state:
        st.session_state['city'] = ''

    with st.form(key='project_form'):
        numero_conf = st.text_input("Número do Projeto")
        logo = st.file_uploader("Logo (Imagem)", type=['png', 'jpg', 'jpeg'])

        cnpj = st.text_input("CNPJ")
        verificar_cnpj = st.form_submit_button("Verificar CNPJ")
        
        if verificar_cnpj:
            empresa_data = buscar_empresa_cnpj(cnpj)
            if empresa_data and 'erro' not in empresa_data:
                st.session_state['nome'] = empresa_data['nome']
                st.success(f"Empresa encontrada: {st.session_state['nome']}")
            else:
                st.error("CNPJ inválido ou não encontrado.")

        nome = st.text_input("Nome da Empresa", value=st.session_state['nome'])

        cep = st.text_input("CEP")
        verificar_cep = st.form_submit_button("Verificar CEP")

        if verificar_cep:
            endereco_data = buscar_endereco_cep(cep)
            if endereco_data and 'erro' not in endereco_data:
                st.session_state['endereco'] = f"{endereco_data['logradouro']}, {endereco_data['bairro']}"
                st.session_state['city'] = f"{endereco_data['localidade']}/{endereco_data['uf']}"
                st.success(f"Endereço encontrado: {st.session_state['endereco']}, {st.session_state['city']}")
            else:
                st.error("CEP inválido ou não encontrado.")
        
        endereco = st.text_input("Endereço", value=st.session_state['endereco'])
        numero = st.text_input("Numero", value=st.session_state['city'], key="complemento_numero")
        complemento = st.text_input("Complemento", value=st.session_state['city'], key="complemento_extra")
        city = st.text_input("Cidade/Estado", value=st.session_state['city'])
        
        numero_art = st.text_input("Número ART")
        email_cliente = st.text_input("E-mail do cliente")

        data = st.date_input("Data", value=datetime.now(), help="Pode pegar da data atual, mas pode inputar manualmente")

        submit_button = st.form_submit_button("Registrar Projeto")

        if submit_button:
            if not numero_conf or not nome or not cnpj or not endereco or not city or not numero_art or not email_cliente or not data or not cep:
                st.error("Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
            elif not validar_numerico(numero_conf):
                st.error("O número do projeto deve conter apenas números.")
            elif not validar_cnpj(cnpj):
                st.error("CNPJ inválido. Por favor, insira um CNPJ válido.")
            elif not validar_email(email_cliente):
                st.error("E-mail inválido. Por favor, insira um e-mail válido.")
            else:
                new_entry = pd.DataFrame([[numero_conf, nome, cnpj, endereco, city, numero_art, email_cliente, cep, data]],
                                         columns=db.columns)
                db = pd.concat([db, new_entry], ignore_index=True)

                if logo is not None:
                    files = {'logo': logo}
                else:
                    files = {}

                data_payload = {
                    'project_number': numero_conf,
                    'name': nome,
                    'cnpj': cnpj,
                    'address': endereco,
                    'city_state': city,
                    'art_number': numero_art,
                    'client_email': email_cliente,
                    'cep': cep,
                    'date': data.strftime('%Y-%m-%d')
                }

                response = requests.post('http://18.219.73.187:8080/api/project', data=data_payload, files=files)

                if response.status_code == 200:
                    st.success("Projeto registrado com sucesso!")
                else:
                    st.error(f"Erro ao registrar projeto: {response.status_code}")

                st.dataframe(db)

if __name__ == "__main__":
    run()
