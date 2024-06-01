import streamlit as st
import pandas as pd
import plotly.express as px
from controllers.event_controller import cargar_datos

def mostrar_pagina_dashboard():
    st.header("Dashboard de Gestión de Eventos")

    def cargar_eventos():
        return cargar_datos('eventos.json')

    eventos = cargar_eventos()

    df_eventos = pd.DataFrame(eventos)

    if not df_eventos.empty and 'fecha' in df_eventos.columns:
        df_eventos['fecha'] = pd.to_datetime(df_eventos['fecha'])

        st.subheader("Seleccionar rango de fechas")
        fecha_inicio = st.date_input("Fecha de inicio", value=pd.to_datetime("2005-01-01").date())
        fecha_fin = st.date_input("Fecha de fin", value=pd.to_datetime("2024-12-31").date())

        fecha_inicio = pd.to_datetime(fecha_inicio)
        fecha_fin = pd.to_datetime(fecha_fin)

        df_eventos_filtrados = df_eventos[(df_eventos['fecha'] >= fecha_inicio) & (df_eventos['fecha'] <= fecha_fin)]

        st.subheader("Cantidad de eventos por tipo")
        if not df_eventos_filtrados.empty:
            eventos_por_tipo = df_eventos_filtrados['tipo'].value_counts().reset_index()
            eventos_por_tipo.columns = ['tipo', 'cantidad']
        else:
            eventos_por_tipo = pd.DataFrame(columns=['tipo', 'cantidad'])
        fig1 = px.bar(eventos_por_tipo, x='tipo', y='cantidad', title="Cantidad de Eventos por Tipo")
        st.plotly_chart(fig1)

        st.subheader("Ingresos totales por eventos")
        if not df_eventos_filtrados.empty:
            if 'precio_regular' in df_eventos_filtrados.columns:
                df_eventos_filtrados['precio_regular'] = df_eventos_filtrados['precio_regular'].fillna(0)
                ingresos_por_evento = df_eventos_filtrados.groupby('nombre')['precio_regular'].sum().reset_index()
                ingresos_por_evento.columns = ['nombre', 'ingresos']
            else:
                ingresos_por_evento = pd.DataFrame(columns=['nombre', 'ingresos'])
        else:
            ingresos_por_evento = pd.DataFrame(columns=['nombre', 'ingresos'])
        fig2 = px.bar(ingresos_por_evento, x='nombre', y='ingresos', title="Ingresos Totales por Eventos")
        st.plotly_chart(fig2)

        ingresos_casa = 0
        ingresos_artistas = 0

        for evento in df_eventos_filtrados.itertuples():
            if evento.tipo == 'Bar':
                ingresos_casa += 0.2 * evento.precio_regular
                ingresos_artistas += 0.8 * evento.precio_regular
            elif evento.tipo == 'Teatro':
                if hasattr(evento, 'alquiler'):
                    ingresos_casa += 0.07 * evento.precio_regular
                    ingresos_artistas += (0.93 * evento.precio_regular) - evento.alquiler
                else:
                    ingresos_casa += 0.07 * evento.precio_regular
                    ingresos_artistas += 0.93 * evento.precio_regular

        ingresos = {
            'Casa': [ingresos_casa],
            'Artistas': [ingresos_artistas]
        }
        df_ingresos = pd.DataFrame(ingresos)

        st.subheader("Ingresos Totales")
        st.write(df_ingresos)
        fig3 = px.bar(df_ingresos, title="Ingresos Totales para Casa y Artistas")
        st.plotly_chart(fig3)

    else:
        st.warning("No hay eventos disponibles para mostrar en el dashboard.")
        st.subheader("Cantidad de eventos por tipo")
        fig1 = px.bar(pd.DataFrame(columns=['tipo', 'cantidad']), x='tipo', y='cantidad', title="Cantidad de Eventos por Tipo")
        st.plotly_chart(fig1)

        st.subheader("Ingresos totales por eventos")
        fig2 = px.bar(pd.DataFrame(columns=['nombre', 'ingresos']), x='nombre', y='ingresos', title="Ingresos Totales por Eventos")
        st.plotly_chart(fig2)

        st.subheader("Ingresos Totales")
        fig3 = px.bar(pd.DataFrame(columns=['Casa', 'Artistas']), title="Ingresos Totales para Casa y Artistas")
        st.plotly_chart(fig3)

mostrar_pagina_dashboard()
