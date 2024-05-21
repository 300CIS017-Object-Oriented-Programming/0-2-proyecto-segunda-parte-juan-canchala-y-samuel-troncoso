import streamlit as st

def configurar_pagina(titulo, icono):
    st.set_page_config(page_title=titulo, page_icon=icono)

def mostrar_imagenes():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(r"static\img1.png", caption="Evento Bar", use_column_width="auto")
    with col2:
        st.image(r"static\img2.png", caption="Evento Teatro", use_column_width="auto")
    with col3:
        st.image(r"static\img3.png", caption="Evento Filantrópico", use_column_width="auto")
