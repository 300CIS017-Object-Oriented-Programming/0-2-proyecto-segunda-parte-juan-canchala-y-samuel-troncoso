import streamlit as st
import sys
import os

st.set_page_config(page_title="Gestión de Eventos", page_icon="😂")

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from view.inicio import mostrar_pagina_inicio
from pages.Evento import mostrar_pagina_evento
from pages.Boleteria import mostrar_pagina_boleteria
from pages.Dashboard import mostrar_pagina_dashboard
from pages.Reportes import mostrar_pagina_reportes
from pages.Nosotros import mostrar_pagina_nosotros
from pages.Eventos import mostrar_pagina_eventos
from pages.Contacto import mostrar_pagina_contacto

with open('static/css/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if 'seleccion' not in st.session_state:
    st.session_state['seleccion'] = "Inicio"
if 'tipo_usuario' not in st.session_state:
    st.session_state['tipo_usuario'] = "usuario"

paginas_usuario = {
    "Inicio": mostrar_pagina_inicio,
    "Nosotros": mostrar_pagina_nosotros,
    "Eventos": mostrar_pagina_eventos,
    "Boletería": mostrar_pagina_boleteria,
    "Contacto": mostrar_pagina_contacto
}

paginas_admin = {
    "Inicio": mostrar_pagina_inicio,
    "Eventos": mostrar_pagina_evento,
    "Dashboard": mostrar_pagina_dashboard,
    "Reportes": mostrar_pagina_reportes
}

st.sidebar.image("static/img/logo.png", use_column_width=False, width=150)

def render_menu():
    if st.sidebar.button("Inicio"):
        st.session_state['seleccion'] = "Inicio"

    if st.session_state['tipo_usuario'] == "usuario":
        if st.sidebar.button("Nosotros"):
            st.session_state['seleccion'] = "Nosotros"
        if st.sidebar.button("Eventos"):
            st.session_state['seleccion'] = "Eventos"
        if st.sidebar.button("Boletería"):
            st.session_state['seleccion'] = "Boletería"
        if st.sidebar.button("Contacto"):
            st.session_state['seleccion'] = "Contacto"
    else:
        if st.sidebar.button("Eventos"):
            st.session_state['seleccion'] = "Eventos"
        if st.sidebar.button("Dashboard"):
            st.session_state['seleccion'] = "Dashboard"
        if st.sidebar.button("Reportes"):
            st.session_state['seleccion'] = "Reportes"

render_menu()

seleccion = st.session_state['seleccion']
if st.session_state['tipo_usuario'] == "usuario":
    if seleccion in paginas_usuario:
        paginas_usuario[seleccion]()
else:
    if seleccion in paginas_admin:
        paginas_admin[seleccion]()
