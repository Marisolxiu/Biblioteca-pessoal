import streamlit as st
from google.cloud import firestore


st.title("Firebase, formulário")

baseDados = firestore.Client.from_service_account_json("firebase.json")

#formulario de cadastro
with st.form("formfirebase"):
    nome= st.text_input("Nome:", placeholder="Informe seu nome...")
    apelido= st.text_input("Apelido:", placeholder="Informe seu apelido...")
    idade= st.number_input("idade:", step=1, min_value=12, max_value=30)
    senha= st.text_input("senha:", placeholder="Informe sua senha...", type="password")

    btnSalvarUsuario= st.form_submit_button("Salvar", use_container_width= True)
if btnSalvarUsuario:
    if nome and idade and senha and apelido:
    #Salvar no banco
        novoUsuario = baseDados.collection("usuarios").document(apelido)
        novoUsuario.set(
            {
            "nome": nome,
            "apelido": apelido,
            "idade": idade,
            "senha": senha
            }
        )
        st.success("Usuario Criado!")
    else:
        st.error("Informe seu nome, apelido, idade e senha por favor")