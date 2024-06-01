import streamlit as st
import json
import pandas as pd
import plotly.express as px
from datetime import date
from io import BytesIO
from static.mensajes import EXCEPCION_NO_EVENTOS, EXCEPCION_NO_DATOS, EXCEPCION_NO_BOLETOS


def mostrar_pagina_reportes():
    st.header("Reporte de Ventas de Boletas")

    def cargar_datos(filename):
        datos = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    datos.append(json.loads(line))
        except FileNotFoundError:
            st.error(EXCEPCION_NO_EVENTOS)
        return datos

    eventos = cargar_datos('eventos.json')
    boletos = cargar_datos('boletos.json')

    df_eventos = pd.DataFrame(eventos)
    df_boletos = pd.DataFrame(boletos)

    def to_excel(df_dict):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        for sheet_name, df in df_dict.items():
            df.to_excel(writer, index=False, sheet_name=sheet_name)
        writer.close()
        processed_data = output.getvalue()
        return processed_data

    st.header("Reporte de Ventas de Boletas")

    if not df_boletos.empty:
        df_boletos['tipo'] = df_boletos.apply(lambda x: 'Cortesía' if x['precio_final'] == 0 else 'Pagado', axis=1)
        ventas_por_tipo = df_boletos.groupby('tipo')['cantidad'].sum().reset_index()
        ingresos_totales = df_boletos.groupby(['fase_venta'])['precio_final'].sum().reset_index()
    else:
        ventas_por_tipo = pd.DataFrame(columns=['tipo', 'cantidad'])
        ingresos_totales = pd.DataFrame(columns=['fase_venta', 'precio_final'])

    st.subheader("Cantidad de Boletas Vendidas por Tipo")
    st.write(ventas_por_tipo)
    fig1 = px.bar(ventas_por_tipo, x='tipo', y='cantidad', title="Cantidad de Boletas por Tipo")
    st.plotly_chart(fig1)

    st.subheader("Ingresos Totales por Preventa y Venta Regular")
    st.write(ingresos_totales)
    fig2 = px.bar(ingresos_totales, x='fase_venta', y='precio_final', title="Ingresos Totales por Preventa y Venta Regular")
    st.plotly_chart(fig2)

    st.header("Reporte Financiero")

    if not df_boletos.empty:
        ingresos_por_tipo = df_boletos.groupby('tipo')['precio_final'].sum().reset_index()
        ingresos_por_fase = df_boletos.groupby('fase_venta')['precio_final'].sum().reset_index()
        ingresos_por_evento = df_boletos.groupby('evento')['precio_final'].sum().reset_index()

        ingresos_casa = 0
        ingresos_artistas = 0

        for evento in df_eventos.itertuples():
            if evento.tipo == 'Bar':
                ingresos_casa += 0.2 * ingresos_por_evento.loc[ingresos_por_evento['evento'] == evento.nombre, 'precio_final'].sum()
                ingresos_artistas += 0.8 * ingresos_por_evento.loc[ingresos_por_evento['evento'] == evento.nombre, 'precio_final'].sum()
            elif evento.tipo == 'Teatro':
                if hasattr(evento, 'alquiler'):
                    ingresos_casa += 0.07 * ingresos_por_evento.loc[ingresos_por_evento['evento'] == evento.nombre, 'precio_final'].sum()
                    ingresos_artistas += (0.93 * ingresos_por_evento.loc[ingresos_por_evento['evento'] == evento.nombre, 'precio_final'].sum()) - evento.alquiler
                else:
                    ingresos_casa += 0.07 * ingresos_por_evento.loc[ingresos_por_evento['evento'] == evento.nombre, 'precio_final'].sum()
                    ingresos_artistas += 0.93 * ingresos_por_evento.loc[ingresos_por_evento['evento'] == evento.nombre, 'precio_final'].sum()

        ingresos = {
            'Casa': [ingresos_casa],
            'Artistas': [ingresos_artistas]
        }
        df_ingresos = pd.DataFrame(ingresos)
    else:
        ingresos_por_tipo = pd.DataFrame(columns=['tipo', 'precio_final'])
        ingresos_por_fase = pd.DataFrame(columns=['fase_venta', 'precio_final'])
        df_ingresos = pd.DataFrame(columns=['Casa', 'Artistas'])

    st.subheader("Ingresos por Tipo de Pago")
    st.write(ingresos_por_tipo)
    fig3 = px.bar(ingresos_por_tipo, x='tipo', y='precio_final', title="Ingresos por Tipo de Pago")
    st.plotly_chart(fig3)

    st.subheader("Ingresos por Tipo de Boletería")
    st.write(ingresos_por_fase)
    fig4 = px.bar(ingresos_por_fase, x='fase_venta', y='precio_final', title="Ingresos por Tipo de Boletería")
    st.plotly_chart(fig4)

    st.subheader("Ingresos Totales")
    st.write(df_ingresos)
    fig5 = px.bar(df_ingresos, title="Ingresos Totales para Casa y Artistas")
    st.plotly_chart(fig5)

    st.header("Reporte de Datos de los Compradores")

    if not df_boletos.empty:
        df_compradores = df_boletos[['comprador', 'cantidad', 'precio_final']].explode('comprador').reset_index(drop=True)
        df_compradores = pd.json_normalize(df_compradores['comprador'])
        df_compradores['cantidad'] = df_boletos.explode('comprador')['cantidad'].values
        df_compradores['precio_final'] = df_boletos.explode('comprador')['precio_final'].values
    else:
        df_compradores = pd.DataFrame(columns=['nombre', 'email', 'celular', 'cantidad', 'precio_final'])

    st.subheader("Datos de los Compradores")
    st.write(df_compradores)

    if 'nombre' in df_compradores.columns:
        fig6 = px.bar(df_compradores, x='nombre', y='cantidad', title="Cantidad de Boletos por Comprador")
        st.plotly_chart(fig6)

        fig7 = px.bar(df_compradores, x='nombre', y='precio_final', title="Ingresos por Comprador")
        st.plotly_chart(fig7)
    else:
        st.warning("La columna 'nombre' no está presente en los datos de compradores.")
        fig6 = px.bar(pd.DataFrame(columns=['nombre', 'cantidad']), x='nombre', y='cantidad', title="Cantidad de Boletos por Comprador")
        st.plotly_chart(fig6)

        fig7 = px.bar(pd.DataFrame(columns=['nombre', 'precio_final']), x='nombre', y='precio_final', title="Ingresos por Comprador")
        st.plotly_chart(fig7)

    df_xlsx = to_excel({
        'Ventas por Tipo': ventas_por_tipo,
        'Ingresos Totales': ingresos_totales,
        'Ingresos por Tipo de Pago': ingresos_por_tipo,
        'Ingresos por Tipo de Boletería': ingresos_por_fase,
        'Datos de Compradores': df_compradores,
        'Ingresos Totales': df_ingresos
    })

    st.download_button(label='📥 Descargar Todos los Datos',
                       data=df_xlsx,
                       file_name='reporte_completo.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    st.header("Reporte de Datos por Artista")

    if not df_eventos.empty:
        artistas = df_eventos.explode('artistas')['artistas'].dropna().apply(lambda x: x['nombre_artistico'] if isinstance(x, dict) else None).drop_duplicates().reset_index(drop=True)
        artista_seleccionado = st.selectbox("Selecciona un Artista", artistas)

        if artista_seleccionado:
            eventos_artista = df_eventos[df_eventos['artistas'].apply(lambda x: any(d.get('nombre_artistico', '') == artista_seleccionado for d in x if isinstance(d, dict)))]
            boletos_eventos_artista = df_boletos[df_boletos['evento'].isin(eventos_artista['nombre'])]
            boletos_vendidos = boletos_eventos_artista.groupby('evento')['cantidad'].sum().reset_index()
            aforo_cubierto = boletos_vendidos.merge(eventos_artista[['nombre', 'aforo_total']], left_on='evento', right_on='nombre')
            aforo_cubierto['porcentaje_aforo'] = (aforo_cubierto['cantidad'] / aforo_cubierto['aforo_total']) * 100

            st.subheader(f"Datos de Eventos para {artista_seleccionado}")
            st.write(aforo_cubierto[['evento', 'cantidad', 'aforo_total', 'porcentaje_aforo']])
            
            df_artista_xlsx = to_excel({'Datos de Eventos por Artista': aforo_cubierto})
            st.download_button(label=f'📥 Descargar Datos de {artista_seleccionado}',
                               data=df_artista_xlsx,
                               file_name=f'reporte_{artista_seleccionado}.xlsx',
                               mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    else:
        st.warning("No hay datos de eventos disponibles.")
        fig8 = px.bar(pd.DataFrame(columns=['evento', 'cantidad', 'aforo_total', 'porcentaje_aforo']), x='evento', y='cantidad', title="Datos de Eventos para Artistas")
        st.plotly_chart(fig8)

mostrar_pagina_reportes()
