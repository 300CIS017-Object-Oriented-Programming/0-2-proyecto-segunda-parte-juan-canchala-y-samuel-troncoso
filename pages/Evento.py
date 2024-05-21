import streamlit as st
import datetime
import json
from fpdf import FPDF
from models.EventoBar import EventoBar
from models.EventoFilantropico import EventoFilantropico
from models.EventoTeatro import EventoTeatro
from models.Patrocinador import Patrocinador
from models.Artista import Artista

st.set_page_config(
    page_title="Evento",
    page_icon="😂"
)

def cargar_eventos():
    eventos = []
    try:
        with open('eventos.json', 'r') as f:
            for line in f:
                eventos.append(json.loads(line))
    except FileNotFoundError:
        st.error("No se encontraron eventos. Por favor, cree algunos eventos primero.")
    return eventos

artistas_list = []
eventos = cargar_eventos()

# Función para crear artista
def crear_artista(nombre, dni, email, celular, nombre_artistico, evento_nombre):
    return Artista(nombre, dni, email, celular, nombre_artistico, evento_nombre)

def crear_evento_bar(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, num_presentaciones, codigo_cortesia):
    return EventoBar(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, num_presentaciones, codigo_cortesia)

def crear_evento_teatro(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, alquiler, codigo_cortesia):
    return EventoTeatro(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, alquiler, codigo_cortesia)

def crear_evento_filantropico(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, patrocinadores, codigo_cortesia):
    return EventoFilantropico(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, patrocinadores, codigo_cortesia)

def generar_pdf(evento, tipo_evento):
    pdf = FPDF()
    pdf.add_page()
    

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Ticket de Evento - {tipo_evento}", ln=True, align='C')

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
    
    pdf.output(f"{evento.nombre}.pdf")
    return f"{evento.nombre}.pdf"

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

def actualizar_evento(eventos, evento_actualizado):
    for i, evento in enumerate(eventos):
        if evento['nombre'] == evento_actualizado['nombre']:
            eventos[i] = evento_actualizado
            break
    with open('eventos.json', 'w') as f:
        for evento in eventos:
            json.dump(evento, f)
            f.write('\n')

st.title("Aquí están nuestros eventos")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(r"static\img1.png", caption="Evento Bar", use_column_width="auto")
with col2:
    st.image(r"static\img2.png", caption="Evento Teatro", use_column_width="auto")
with col3:
    st.image(r"static\img3.png", caption="Evento Filantrópico", use_column_width="auto")

st.header("Crear evento")
st.subheader("¿Qué se hace acá?")
st.markdown("Como su nombre indica, esta sección está destinada a la creación de eventos de tres tipos, cada uno con sus características distintas.")

option = st.selectbox("Selecciona el tipo de evento", ("Bar", "Teatro", "Filantrópico"))

st.title("Datos del evento")
col5, col6 = st.columns(2)
with col5:
    nombre = st.text_input("Nombre del show", "Ingrese nombre del show", key="crear_nombre")
with col6:
    fecha = st.date_input("Fecha del show", datetime.date(2006, 9, 16), key="crear_fecha")

col7, col8, col9 = st.columns(3)
with col7:
    hora_apertura = st.time_input("Hora de apertura de puertas", value=None, key="crear_hora_apertura")
with col8:
    hora_show = st.time_input("Hora del show", value=None, key="crear_hora_show")
with col9:
    lugar_show = st.text_input("Nombre del lugar del evento", "Javeriana Cali", key="crear_lugar_show")

col10, col11 = st.columns(2)
with col10:
    direccion = st.text_input("Dirección del evento", "Calle 20 # 11-30", key="crear_direccion")
with col11:
    ciudad = st.text_input("Ciudad del evento", "Yumbo", key="crear_ciudad")

estado = st.selectbox("Selecciona el estado del evento", ("realizado", "por realizar", "cancelado", "aplazado", "cerrado"), key="crear_estado")

col13, col14, col15 = st.columns(3)
with col13:
    precio_regular = st.number_input("Precio regular", value=None, key="crear_precio_regular")
with col14:
    precio_preventa = st.number_input("Precio de preventa", value=None, key="crear_precio_preventa")
with col15:
    aforo_total = st.number_input("Aforo total", value=None, key="crear_aforo_total")

estado_boleteria = "vacio"
codigo_cortesia = st.text_input("Código de Cortesía", "", key="crear_codigo_cortesia")

st.title("Datos del artista")
col31, col32, col33 = st.columns(3)
with col31:
    nombre_artista = st.text_input("Nombre Artista", "Daniel", key="crear_nombre_artista")
with col32:
    dni_artista = st.text_input("Documento de identidad", "1001316869", key="crear_dni_artista")
with col33:
    email_artista = st.text_input("Email", "ejemplo@gmail.com", key="crear_email_artista")

col34, col35 = st.columns(2)
with col34:
    celular_artista = st.text_input("Celular", "301257069", key="crear_celular_artista")
with col35:
    nombre_artistico = st.text_input("Nombre artístico", "Rels B", key="crear_nombre_artistico")

if st.button("Añadir artista al evento", key="crear_añadir_artista"):
    artistas_list.append(crear_artista(nombre_artista, dni_artista, email_artista, celular_artista, nombre_artistico, nombre))

if option == "Bar":
    num_presentaciones = st.number_input("Número de presentaciones del artista", value=None, key="crear_num_presentaciones")
    if st.button("Crear Evento Bar", key="crear_evento_bar"):
        evento = crear_evento_bar(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo_total, num_presentaciones, codigo_cortesia)
        guardar_evento(evento, "Bar")
        artistas_list.clear()
        pdf_path = generar_pdf(evento, "Bar")
        st.success(f"Evento Bar creado y guardado en {pdf_path}")

elif option == "Teatro":
    alquiler = st.number_input("Alquiler del lugar", value=None, key="crear_alquiler")
    if st.button("Crear Evento Teatro", key="crear_evento_teatro"):
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
        nombre_patrocinador = st.text_input("Nombre del patrocinador", "Olive Biscuit", key="crear_nombre_patrocinador")
    with col17:
        dni_patrocinador = st.text_input("Documento de identidad", "1034304796", key="crear_dni_patrocinador")

    col18, col19, col20 = st.columns(3)
    with col18:
        email_patrocinador = st.text_input("Email", "mafalda_0_qgmail.com", key="crear_email_patrocinador")
    with col19:
        celular_patrocinador = st.text_input("celular", "321968481", key="crear_celular_patrocinador")
    with col20:
        valor_aportado = st.number_input("Aporte del patrocinador", value=None, key="crear_valor_aportado")

    if st.button("Añadir Patrocinador", key="crear_añadir_patrocinador"):
        patrocinador = Patrocinador(nombre_patrocinador, dni_patrocinador, email_patrocinador, celular_patrocinador, valor_aportado)
        patrocinador_list.append(patrocinador)
        st.success(f"Patrocinador {patrocinador.nombre} añadido")

    if st.button("Crear evento Filantrópico", key="crear_evento_filantrópico"):
        evento = crear_evento_filantropico(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo_total, patrocinador_list, codigo_cortesia)
        guardar_evento(evento, "Filantrópico")
        patrocinador_list.clear()
        artistas_list.clear()
        pdf_path = generar_pdf(evento, "Filantrópico")
        st.success(f"Evento Filantrópico creado y guardado en {pdf_path}")

st.header("Modificar evento")
st.subheader("Seleccione un evento para modificar")

nombres_eventos = [evento["nombre"] for evento in eventos]
nombre_evento_seleccionado = st.selectbox("Selecciona un evento", nombres_eventos, key="modificar_nombre_evento")

evento_seleccionado = next((evento for evento in eventos if evento["nombre"] == nombre_evento_seleccionado), None)

if evento_seleccionado:
    st.title("Modificar Datos del Evento")
    col5, col6 = st.columns(2)
    with col5:
        nombre_modificado = st.text_input("Nombre del show", evento_seleccionado["nombre"], key="modificar_nombre")
    with col6:
        fecha_modificada = st.date_input("Fecha del show", datetime.datetime.strptime(evento_seleccionado["fecha"], '%Y-%m-%d').date(), key="modificar_fecha")

    col7, col8, col9 = st.columns(3)
    with col7:
        hora_apertura_str = evento_seleccionado.get("hora_apertura", "00:00:00")
        hora_apertura_time = datetime.datetime.strptime(hora_apertura_str, '%H:%M:%S').time() if hora_apertura_str else datetime.time(0, 0)
        hora_apertura_modificada = st.time_input("Hora de apertura de puertas", hora_apertura_time, key="modificar_hora_apertura")
    with col8:
        hora_show_str = evento_seleccionado.get("hora_show", "00:00:00")
        hora_show_time = datetime.datetime.strptime(hora_show_str, '%H:%M:%S').time() if hora_show_str else datetime.time(0, 0)
        hora_show_modificada = st.time_input("Hora del show", hora_show_time, key="modificar_hora_show")
    with col9:
        lugar_show_modificado = st.text_input("Nombre del lugar del evento", evento_seleccionado["lugar_show"], key="modificar_lugar_show")

    col10, col11 = st.columns(2)
    with col10:
        direccion_modificada = st.text_input("Dirección del evento", evento_seleccionado["direccion"], key="modificar_direccion")
    with col11:
        ciudad_modificada = st.text_input("Ciudad del evento", evento_seleccionado["ciudad"], key="modificar_ciudad")

    estado_modificado = st.selectbox("Selecciona el estado del evento", ("realizado", "por realizar", "cancelado", "aplazado", "cerrado"), index=["realizado", "por realizar", "cancelado", "aplazado", "cerrado"].index(evento_seleccionado["estado"]), key="modificar_estado")

    col13, col14, col15 = st.columns(3)
    with col13:
        precio_regular_modificado = st.number_input("Precio regular", value=evento_seleccionado["precio_regular"], key="modificar_precio_regular")
    with col14:
        precio_preventa_modificado = st.number_input("Precio de preventa", value=evento_seleccionado["precio_preventa"], key="modificar_precio_preventa")
    with col15:
        aforo_total_modificado = st.number_input("Aforo total", value=evento_seleccionado["aforo_total"], key="modificar_aforo_total")

    codigo_cortesia_modificado = st.text_input("Código de Cortesía", evento_seleccionado.get("codigo_cortesia", ""), key="modificar_codigo_cortesia")

    if st.button("Guardar Cambios", key="modificar_guardar_cambios"):
        evento_modificado = {
            "tipo": evento_seleccionado["tipo"],
            "nombre": nombre_modificado,
            "fecha": str(fecha_modificada),
            "hora_apertura": str(hora_apertura_modificada),
            "hora_show": str(hora_show_modificada),
            "lugar_show": lugar_show_modificado,
            "direccion": direccion_modificada,
            "ciudad": ciudad_modificada,
            "estado": estado_modificado,
            "precio_regular": precio_regular_modificado,
            "precio_preventa": precio_preventa_modificado,
            "aforo_total": aforo_total_modificado,
            "codigo_cortesia": codigo_cortesia_modificado,
            "artistas": evento_seleccionado["artistas"]
        }
        actualizar_evento(eventos, evento_modificado)
        st.success("Evento modificado exitosamente")
