import streamlit as st
import datetime
import json
from fpdf import FPDF
from models.EventoBar import EventoBar
from models.EventoFilantropico import EventoFilantropico
from models.EventoTeatro import EventoTeatro
from models.Patrocinador import Patrocinador
from models.Artista import Artista

# Configuración de la página
st.set_page_config(
    page_title="Evento",
    page_icon="😂"
)

# Listas para almacenar eventos y artistas
artistas_list = []

# Función para crear artista
def crear_artista(nombre, dni, email, celular, nombre_artistico, evento_nombre):
    return Artista(nombre, dni, email, celular, nombre_artistico, evento_nombre)

# Función para crear evento bar
def crear_evento_bar(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, num_presentaciones, codigo_cortesia):
    return EventoBar(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, num_presentaciones, codigo_cortesia)

# Función para crear evento teatro
def crear_evento_teatro(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, alquiler, codigo_cortesia):
    return EventoTeatro(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, alquiler, codigo_cortesia)

# Función para crear evento filantrópico
def crear_evento_filantropico(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, patrocinadores, codigo_cortesia):
    return EventoFilantropico(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, patrocinadores, codigo_cortesia)

# Función para generar un PDF de ticket
def generar_pdf(evento, tipo_evento):
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Ticket de Evento - {tipo_evento}", ln=True, align='C')
    
    # Información del evento
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nombre del Evento: {evento.nombre}", ln=True)
    pdf.cell(200, 10, txt=f"Fecha: {evento.fecha}", ln=True)
    pdf.cell(200, 10, txt=f"Hora de Apertura: {evento.hora_apertura}", ln=True)
    pdf.cell(200, 10, txt=f"Hora del Show: {evento.hora_show}", ln=True)
    pdf.cell(200, 10, txt=f"Lugar: {evento.lugar_show}", ln=True)
    pdf.cell(200, 10, txt=f"Dirección: {evento.direccion}", ln=True)
    pdf.cell(200, 10, txt=f"Ciudad: {evento.ciudad}", ln=True)
    pdf.cell(200, 10, txt=f"Estado: {evento.estado}", ln=True)
    pdf.cell(200, 10, txt=f"Precio Regular: {evento.precioVentaRegular}", ln=True)
    pdf.cell(200, 10, txt=f"Precio Pre-venta: {evento.precioPreVenta}", ln=True)
    pdf.cell(200, 10, txt=f"Aforo Total: {evento.aforoTotal}", ln=True)
    
    # Información del artista
    if isinstance(evento.artista, list):
        for art in evento.artista:
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"Artista: {art.nombre_artistico} ({art.nombre})", ln=True)
            pdf.cell(200, 10, txt=f"Email: {art.email}", ln=True)
            pdf.cell(200, 10, txt=f"Celular: {art.celular}", ln=True)
    else:
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Artista: {evento.artista.nombre_artistico} ({evento.artista.nombre})", ln=True)
        pdf.cell(200, 10, txt=f"Email: {evento.artista.email}", ln=True)
        pdf.cell(200, 10, txt=f"Celular: {evento.artista.celular}", ln=True)
    
    # Guardar PDF
    pdf.output(f"{evento.nombre}.pdf")
    return f"{evento.nombre}.pdf"

# Función para guardar eventos en un archivo JSON
def guardar_evento(evento, tipo_evento):
    evento_dict = {
        "tipo": tipo_evento,
        "nombre": evento.nombre,
        "fecha": str(evento.fecha),
        "hora_apertura": str(evento.hora_apertura),
        "hora_show": str(evento.hora_show),
        "lugar_show": evento.lugar_show,
        "direccion": evento.direccion,
        "ciudad": evento.ciudad,
        "estado": evento.estado,
        "precio_regular": evento.precioVentaRegular,
        "precio_preventa": evento.precioPreVenta,
        "aforo_total": evento.aforoTotal,
        "codigo_cortesia": evento.codigo_cortesia,
        "artistas": [{"nombre": art.nombre, "nombre_artistico": art.nombre_artistico} for art in evento.artista] if isinstance(evento.artista, list) else [{"nombre": evento.artista.nombre, "nombre_artistico": evento.artista.nombre_artistico}]
    }
    with open('eventos.json', 'a') as f:
        json.dump(evento_dict, f)
        f.write('\n')

# Título e imágenes
st.title("Aquí están nuestros eventos")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(r"static\img1.png", caption="Evento Bar", use_column_width="auto")
with col2:
    st.image(r"static\img2.png", caption="Evento Teatro", use_column_width="auto")
with col3:
    st.image(r"static\img3.png", caption="Evento Filantrópico", use_column_width="auto")

# Sección para crear eventos
st.header("Crear evento")
st.subheader("¿Qué se hace acá?")
st.markdown("Como su nombre indica, esta sección está destinada a la creación de eventos de tres tipos, cada uno con sus características distintas.")

# Selección del tipo de evento
option = st.selectbox("Selecciona el tipo de evento", ("Bar", "Teatro", "Filantrópico"))

# Datos del evento
st.title("Datos del evento")
col5, col6 = st.columns(2)
with col5:
    nombre = st.text_input("Nombre del show", "Ingrese nombre del show")
with col6:
    fecha = st.date_input("Fecha del show", datetime.date(2006, 9, 16))

col7, col8, col9 = st.columns(3)
with col7:
    hora_apertura = st.time_input("Hora de apertura de puertas", value=None)
with col8:
    hora_show = st.time_input("Hora del show", value=None)
with col9:
    lugar_show = st.text_input("Nombre del lugar del evento", "Javeriana Cali")

col10, col11 = st.columns(2)
with col10:
    direccion = st.text_input("Dirección del evento", "Calle 20 # 11-30")
with col11:
    ciudad = st.text_input("Ciudad del evento", "Yumbo")

estado = st.selectbox("Selecciona el estado del evento", ("realizado", "por realizar", "cancelado", "aplazado", "cerrado"))

col13, col14, col15 = st.columns(3)
with col13:
    precio_regular = st.number_input("Precio regular", value=None)
with col14:
    precio_preventa = st.number_input("Precio de preventa", value=None)
with col15:
    aforo_total = st.number_input("Aforo total", value=None)

estado_boleteria = "vacio"
codigo_cortesia = st.text_input("Código de Cortesía", "")

# Datos del artista
st.title("Datos del artista")
col31, col32, col33 = st.columns(3)
with col31:
    nombre_artista = st.text_input("Nombre Artista", "Daniel")
with col32:
    dni_artista = st.text_input("Documento de identidad", "1001316869")
with col33:
    email_artista = st.text_input("Email", "ejemplo@gmail.com")

col34, col35 = st.columns(2)
with col34:
    celular_artista = st.text_input("Celular", "301257069")
with col35:
    nombre_artistico = st.text_input("Nombre artístico", "Rels B")

if st.button("Añadir artista al evento"):
    artistas_list.append(crear_artista(nombre_artista, dni_artista, email_artista, celular_artista, nombre_artistico, nombre))

# Creación del evento según el tipo seleccionado
if option == "Bar":
    num_presentaciones = st.number_input("Número de presentaciones del artista", value=None)
    if st.button("Crear Evento Bar"):
        evento = crear_evento_bar(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo_total, num_presentaciones, codigo_cortesia)
        guardar_evento(evento, "Bar")
        artistas_list.clear()
        pdf_path = generar_pdf(evento, "Bar")
        st.success(f"Evento Bar creado y guardado en {pdf_path}")

elif option == "Teatro":
    alquiler = st.number_input("Alquiler del lugar", value=None)
    if st.button("Crear Evento Teatro"):
        evento = crear_evento_teatro(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo_total, alquiler, codigo_cortesia)
        guardar_evento(evento, "Teatro")
        artistas_list.clear()
        pdf_path = generar_pdf(evento, "Teatro")
        st.success(f"Evento Teatro creado y guardado en {pdf_path}")

elif option == "Filantrópico":
    patrocinador_list = []
    st.title("Datos patrocinador del evento")
    col16, col17 = st.columns(2)
    with col16:
        nombre_patrocinador = st.text_input("Nombre del patrocinador", "Olive Biscuit")
    with col17:
        dni_patrocinador = st.text_input("Documento de identidad", "1034304796")

    col18, col19, col20 = st.columns(3)
    with col18:
        email_patrocinador = st.text_input("Email", "mafalda_0_qgmail.com")
    with col19:
        celular_patrocinador = st.text_input("celular", "321968481")
    with col20:
        valor_aportado = st.number_input("Aporte del patrocinador", value=None)

    if st.button("Añadir Patrocinador"):
        patrocinador = Patrocinador(nombre_patrocinador, dni_patrocinador, email_patrocinador, celular_patrocinador, valor_aportado)
        patrocinador_list.append(patrocinador)
        st.success(f"Patrocinador {patrocinador.nombre} añadido")

    if st.button("Crear evento Filantrópico"):
        evento = crear_evento_filantropico(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo_total, patrocinador_list, codigo_cortesia)
        guardar_evento(evento, "Filantrópico")
        patrocinador_list.clear()
        artistas_list.clear()
        pdf_path = generar_pdf(evento, "Filantrópico")
        st.success(f"Evento Filantrópico creado y guardado en {pdf_path}")
