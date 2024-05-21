import streamlit as st
import json
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="Dashboard", page_icon="📊")

def cargar_datos(filename):
    datos = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                datos.append(json.loads(line))
    except FileNotFoundError:
        st.error(f"No se encontraron datos en {filename}.")
    return datos

eventos = cargar_datos('eventos.json')
boletos = cargar_datos('boletos.json')

df_eventos = pd.DataFrame(eventos)
df_boletos = pd.DataFrame(boletos)

st.title("Tablero de Control")
st.header("Filtrar por rango de fechas")

start_date = st.date_input("Fecha de inicio", value=date.today() - timedelta(days=30))
end_date = st.date_input("Fecha de fin", value=date.today())

df_eventos['fecha'] = pd.to_datetime(df_eventos['fecha'])
df_eventos_filtrado = df_eventos[(df_eventos['fecha'] >= pd.to_datetime(start_date)) & (df_eventos['fecha'] <= pd.to_datetime(end_date))]

df_boletos['fecha_compra'] = pd.to_datetime(df_boletos['fecha_compra'])
df_boletos_filtrado = df_boletos[(df_boletos['fecha_compra'] >= pd.to_datetime(start_date)) & (df_boletos['fecha_compra'] <= pd.to_datetime(end_date))]

st.subheader("Cantidad de Eventos por Tipo")
eventos_por_tipo = df_eventos_filtrado['tipo'].value_counts().reset_index()
eventos_por_tipo.columns = ['tipo', 'cantidad']
fig1 = px.bar(eventos_por_tipo, x='tipo', y='cantidad', title="Cantidad de Eventos por Tipo")
st.plotly_chart(fig1)

st.subheader("Ingresos Totales por Evento")
ingresos_por_evento = df_boletos_filtrado.groupby('evento')['precio_final'].sum().reset_index()
fig2 = px.bar(ingresos_por_evento, x='evento', y='precio_final', title="Ingresos Totales por Evento")
st.plotly_chart(fig2)


st.subheader("Ingresos Totales por Fecha")
ingresos_por_fecha = df_boletos_filtrado.groupby('fecha_compra')['precio_final'].sum().reset_index()
fig3 = px.line(ingresos_por_fecha, x='fecha_compra', y='precio_final', title="Ingresos Totales por Fecha")
st.plotly_chart(fig3)

st.header("Gestión de Ingreso al Evento")

def buscar_boletos(criterio, valor):
    return df_boletos_filtrado[df_boletos_filtrado[criterio].str.contains(valor, case=False, na=False)]

criterio_busqueda = st.selectbox("Buscar por", ["comprador.nombre", "evento"])
valor_busqueda = st.text_input("Valor de búsqueda")

if valor_busqueda:
    resultados_busqueda = buscar_boletos(criterio_busqueda, valor_busqueda)
    st.write(resultados_busqueda)

    if not resultados_busqueda.empty:
        boleto_seleccionado = st.selectbox("Selecciona un boleto", resultados_busqueda['evento'])
        if st.button("Registrar Asistencia"):
            st.success(f"Asistencia registrada para el boleto: {boleto_seleccionado}")

st.subheader("Cantidad de Boletos Vendidos por Evento")
boletos_vendidos_por_evento = df_boletos_filtrado.groupby('evento')['cantidad'].sum().reset_index()
fig4 = px.bar(boletos_vendidos_por_evento, x='evento', y='cantidad', title="Cantidad de Boletos Vendidos por Evento")
st.plotly_chart(fig4)
