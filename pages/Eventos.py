import streamlit as st
import json
from static.mensajes import EXCEPCION_NO_EVENTOS, EXCEPCION_NO_DATOS, EXCEPCION_NO_BOLETOS

def mostrar_pagina_eventos():
    st.title("Eventos")

    def cargar_eventos():
        eventos = []
        try:
            with open('eventos.json', 'r') as f:
                for line in f:
                    eventos.append(json.loads(line))
        except FileNotFoundError:
            st.error(EXCEPCION_NO_EVENTOS)
        return eventos

    eventos = cargar_eventos()

    if eventos:
        for evento in eventos:
            st.subheader(evento["nombre"])
            st.text(f"Fecha: {evento['fecha']}")
            st.text(f"Hora: {evento['hora_show']}")
            st.text(f"Lugar: {evento['lugar_show']}")
            st.text(f"Dirección: {evento['direccion']}")
            st.text(f"Ciudad: {evento['ciudad']}")
            st.text(f"Estado: {evento['estado']}")
            st.text(f"Precio Regular: {evento['precio_regular']}")
            st.text(f"Precio Pre-venta: {evento['precio_preventa']}")
            st.text(f"Aforo Total: {evento['aforo_total']}")
            st.text("Artistas:")
            for artista in evento["artistas"]:
                st.text(f" - {artista['nombre_artistico']} ({artista['nombre']})")
    else:
        st.warning("No hay eventos disponibles.")
