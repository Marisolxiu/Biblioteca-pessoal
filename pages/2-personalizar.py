import streamlit as st

html_code="""
<h1 style='color: purple'>BIBLIOTECA</h1>
"""

st.markdown(html_code, unsafe_allow_html=True)

#PARA ADICIONAR UNA IMAGEN
st.image("imagens/books.png")
#COLOCAR 3 IMAGENS NA MESMA COLUNA
st.write("## Adicione...")
colunas = st.columns(4)

colunas[0].image("imagens/Título.png")
colunas[1].image("imagens/Capa.png")
colunas[2].image("imagens/Comentarios.png")
colunas[3].image("imagens/Puntuação.png")
#USUARIO CONSIGA CARREGAR UMA IMAGEN
imagem = st.file_uploader(
"Adiciona uma portada bonita", type= ["jpg", "jpeg", "gif" , "png"])
                        
if imagem:
    st.image(imagem)