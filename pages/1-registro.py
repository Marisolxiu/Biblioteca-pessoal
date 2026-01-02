import streamlit as st
import datetime as dt

if "registro_ok" not in st.session_state:
    st.session_state.registro_ok = False

st.title("Formulário de registro")

st.header("Prencha o formulário abaixo")
st.markdown("""___""")

with st.form("formulário"):
    
        nome = st.text_input("Informe seu nome:", placeholder="prencha o seu nome")
        idade = st.number_input("Informe sua idade:", min_value=12, max_value=30, step=1)
        dataNascimento = st.date_input("Data de Nascimento:",value=dt.date(2005, 1, 1), format= "DD/MM/YYYY")
        horaAtual = st.time_input("Selecione a hora:", step=60)
        corPerfil = st.color_picker("Selecione a cor do perfil")

        btnformulário = st.form_submit_button("Cadastrar")
        if btnformulário:
                if not nome:
                        st.error("Preencha o nome")
                elif len(nome) <=3:
                        st.error("O nome precisa ter pelo menos 4 letras")
                else:
                        st.write("Nome:", nome)
                        st.write("Idade:", idade)
                        st.write("Data de Nascimento:", dataNascimento)
                        st.write("Hora Atual:", horaAtual)
                        st.write("Cor do Perfil:", corPerfil)

                        html_code = """
                                <h1 style='color:{};'>Essa é cor que você escolheu</h1>
                        """.format(corPerfil)
                        st.markdown(html_code, unsafe_allow_html=True)
                        

                        #REGISTRO CORRETO
                        st.session_state.registro_ok = True
if st.session_state.registro_ok:                       
        if st.button("Personalizar biblioteca 🎨🖌️🧩✨"):
                st.switch_page("pages/2-personalizar.py")
