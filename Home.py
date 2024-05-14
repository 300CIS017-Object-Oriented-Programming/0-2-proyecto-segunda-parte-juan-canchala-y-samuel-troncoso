import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="😂"
)

st.title("Bienvenido al Sistema de Gestión de Eventos de Comedia")

st.write("Este sistema está diseñado para gestionar eventos de comedia, permitiendo a los administradores crear, editar y eliminar eventos, gestionar la boletería y generar reportes.")

st.header("Tipos de Eventos")
st.write("El sistema maneja tres tipos de eventos con características propias:")
st.markdown("- **Evento en Bar:** Los comediantes son pagados por presentarse.")
st.markdown("- **Evento en Teatro:** Se alquila el teatro y se retiene un porcentaje de la boletería.")
st.markdown("- **Evento Filantrópico:** Boletas gratuitas financiadas por patrocinadores.")

st.header("Criterios de Aceptación")
st.write("El sistema cumple con los siguientes criterios:")
st.markdown("- Gestión de tres tipos de eventos: Bar, Teatro y Filantrópico.")
st.markdown("- Definición de detalles del evento, estado y precios de boletas.")
st.markdown("- Gestión de boletería con verificación de disponibilidad y generación de boletas en PDF.")
st.markdown("---")
st.write("© 2024 Juan Canchala y Samuel Troncoso. All Rights Reserved.")


