import streamlit as st
import json
import pandas as pd
import plotly.express as px
from datetime import date
from io import BytesIO

st.set_page_config(page_title="Reportes", page_icon="📊")

# Función para cargar datos desde archivos JSON
def cargar_datos(filename):
    datos = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                datos.append(json.loads(line))
    except FileNotFoundError:
        st.error(f"No se encontraron datos en {filename}.")
    return datos

# Cargar datos de eventos y boletos
eventos = cargar_datos('eventos.json')
boletos = cargar_datos('boletos.json')

# Convertir datos a DataFrames
df_eventos = pd.DataFrame(eventos)
df_boletos = pd.DataFrame(boletos)

# Reporte de Ventas de Boletas
st.header("Reporte de Ventas de Boletas")

if not df_boletos.empty:
    df_boletos['tipo'] = df_boletos.apply(lambda x: 'Cortesía' if x['precio_final'] == 0 else 'Pagado', axis=1)
    ventas_por_tipo = df_boletos.groupby('tipo')['cantidad'].sum().reset_index()
    ingresos_totales = df_boletos.groupby(['fase_venta'])['precio_final'].sum().reset_index()
    
    st.subheader("Cantidad de Boletas Vendidas por Tipo")
    st.write(ventas_por_tipo)
    
    st.subheader("Ingresos Totales por Preventa y Venta Regular")
    st.write(ingresos_totales)
else:
    st.warning("No hay datos de ventas de boletos disponibles.")

# Reporte Financiero
st.header("Reporte Financiero")

if not df_boletos.empty:
    ingresos_por_tipo = df_boletos.groupby('tipo')['precio_final'].sum().reset_index()
    ingresos_por_fase = df_boletos.groupby('fase_venta')['precio_final'].sum().reset_index()
    
    st.subheader("Ingresos por Tipo de Pago")
    st.write(ingresos_por_tipo)
    
    st.subheader("Ingresos por Tipo de Boletería")
    st.write(ingresos_por_fase)
else:
    st.warning("No hay datos financieros disponibles.")

# Reporte de Datos de los Compradores
st.header("Reporte de Datos de los Compradores")

if not df_boletos.empty:
    # Normalizar datos de compradores y agregar las columnas necesarias
    df_compradores = df_boletos[['comprador', 'cantidad', 'precio_final']].explode('comprador').reset_index(drop=True)
    df_compradores = pd.json_normalize(df_compradores['comprador'])
    df_compradores['cantidad'] = df_boletos.explode('comprador')['cantidad'].values
    df_compradores['precio_final'] = df_boletos.explode('comprador')['precio_final'].values
    
    st.subheader("Datos de los Compradores")
    st.write(df_compradores)
    
    # Verificar columnas del DataFrame
    st.write("Columnas disponibles en df_compradores:", df_compradores.columns)

    # Gráfica de cantidad de boletos por comprador
    fig1 = px.bar(df_compradores, x='nombre', y='cantidad', title="Cantidad de Boletos por Comprador")
    st.plotly_chart(fig1)
    
    # Gráfica de ingresos por comprador
    fig2 = px.bar(df_compradores, x='nombre', y='precio_final', title="Ingresos por Comprador")
    st.plotly_chart(fig2)
    
    # Descargar datos en formato Excel
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Compradores')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    df_xlsx = to_excel(df_compradores)
    st.download_button(label='📥 Descargar Datos de Compradores',
                       data=df_xlsx,
                       file_name='datos_compradores.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
else:
    st.warning("No hay datos de compradores disponibles.")

# Reporte de Datos por Artista
st.header("Reporte de Datos por Artista")

if not df_eventos.empty:
    # Extraer los nombres de los artistas de manera segura
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
else:
    st.warning("No hay datos de eventos disponibles.")
