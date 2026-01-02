import streamlit as st

#TITULO
st.title("Minha Biblioteca Pessoal")
#CABEÇARIO
st.header("Desenvolva a sua propria bliblioteca pessoal", divider=True)
#SUBCABEÇARIO
st.subheader("*Para apaixonados pela literatura* :open_book:")
#TEXTO
st.write("###### Bem-vindo à sua biblioteca digital personalizada. Esta plataforma foi desenvolvida para facilitar a organização, o registro e o acompanhamento dos seus livros de forma simples e intuitiva. Adicione seus títulos favoritos, personalize com capas, registre informações relevantes e construa uma biblioteca que reflita o seu gosto pela leitura e pela organização.")
st.markdown("""___""")
st.write("#### Passos para começar")
st.markdown("""
###### 1.- Cadastre-se na plataforma""")
if st.button("Formulario de registro 📝"):
    st.switch_page("pages/1-registro.py")

st.markdown("""        
###### 2.- Personalize sua biblioteca e aproveite a experiência""")
if st.button("Personalizar biblioteca 🎨🖌️🧩✨"):
    st.switch_page("pages/2-personalizar.py")
