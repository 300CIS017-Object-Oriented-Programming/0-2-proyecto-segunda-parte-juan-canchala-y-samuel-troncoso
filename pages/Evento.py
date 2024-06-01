import streamlit as st
import datetime
import json
import os
from fpdf import FPDF
from models.EventoBar import EventoBar
from models.EventoFilantropico import EventoFilantropico
from models.EventoTeatro import EventoTeatro
from models.Patrocinador import Patrocinador
from models.Artista import Artista
from static.mensajes import EXCEPCION_NO_EVENTOS, EXCEPCION_NO_DATOS, EXCEPCION_NO_BOLETOS

if not os.path.exists('pdfs'):
    os.makedirs('pdfs')

def mostrar_pagina_evento():
    def cargar_eventos():
        eventos = []
        try:
            with open('eventos.json', 'r') as f:
                for line in f:
                    eventos.append(json.loads(line))
        except FileNotFoundError:
            st.error(EXCEPCION_NO_EVENTOS)
        return eventos

    def cargar_boletos():
        boletos = []
        try:
            with open('boletos.json', 'r') as f:
                for line in f:
                    boletos.append(json.loads(line))
        except FileNotFoundError:
            st.error(EXCEPCION_NO_BOLETOS)
        return boletos

    def eliminar_evento(eventos, nombre_evento):
        eventos = [evento for evento in eventos if evento["nombre"] != nombre_evento]
        with open('eventos.json', 'w') as f:
            for evento in eventos:
                json.dump(evento, f)
                f.write('\n')
        return eventos

    artistas_list = []
    eventos = cargar_eventos()
    boletos = cargar_boletos()

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
        
        logo_path = "static/img/logo.png"
        pdf.image(logo_path, x=10, y=8, w=30)

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Ticket de Evento - {tipo_evento}", ln=True, align='C')

        pdf.ln(10)
        pdf.cell(200, 10, txt=f" ", ln=True)
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
        
        output_path = os.path.join('pdfs', f"{evento.nombre}.pdf")
        pdf.output(output_path)
        return output_path

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
            "precio_regular": evento.precioVentaRegular if evento.precioVentaRegular is not None else 0,
            "precio_preventa": evento.precioPreVenta if evento.precioPreVenta is not None else 0,
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

    st.header("Crear evento")

    option = st.selectbox("Selecciona el tipo de evento", ("Bar", "Teatro", "Filantrópico"))

    st.title("Datos del evento")
    col5, col6 = st.columns(2)
    with col5:
        nombre = st.text_input("Nombre del show", " ", key="crear_nombre")
    with col6:
        fecha = st.date_input("Fecha del show", datetime.date(2024, 1, 1), key="crear_fecha")

    col7, col8, col9 = st.columns(3)
    with col7:
        hora_apertura = st.time_input("Hora de apertura de puertas", value=None, key="crear_hora_apertura")
    with col8:
        hora_show = st.time_input("Hora del show", value=None, key="crear_hora_show")
    with col9:
        lugar_show = st.text_input("Nombre del lugar del evento", " ", key="crear_lugar_show")

    col10, col11 = st.columns(2)
    with col10:
        direccion = st.text_input("Dirección del evento", " ", key="crear_direccion")
    with col11:
        ciudad = st.text_input("Ciudad del evento", " ", key="crear_ciudad")

    estado = st.selectbox("Selecciona el estado del evento", ("realizado", "por realizar", "cancelado", "aplazado", "cerrado"), key="crear_estado")

    if option != "Filantrópico":
        col13, col14, col15 = st.columns(3)
        with col13:
            precio_regular = st.number_input("Precio regular", value=0, key="crear_precio_regular")
        with col14:
            precio_preventa = st.number_input("Precio de preventa", value=0, key="crear_precio_preventa")
        with col15:
            codigo_cortesia = st.text_input("Código de Cortesía", "", key="crear_codigo_cortesia")

    aforo_total = st.number_input("Aforo total", value=0, key="crear_aforo_total")

    st.title("Datos del artista")
    col31, col32, col33 = st.columns(3)
    with col31:
        nombre_artista = st.text_input("Nombre Artista", " ", key="crear_nombre_artista")
    with col32:
        dni_artista = st.text_input("Documento de identidad", " ", key="crear_dni_artista")
    with col33:
        email_artista = st.text_input("Email", " ", key="crear_email_artista")

    col34, col35 = st.columns(2)
    with col34:
        celular_artista = st.text_input("Celular", " ", key="crear_celular_artista")
    with col35:
        nombre_artistico = st.text_input("Nombre artístico", " ", key="crear_nombre_artistico")

    if st.button("Añadir artista al evento", key="crear_añadir_artista"):
        artistas_list.append(crear_artista(nombre_artista, dni_artista, email_artista, celular_artista, nombre_artistico, nombre))

    if option == "Bar":
        num_presentaciones = st.number_input("Número de presentaciones del artista", value=0, key="crear_num_presentaciones")
        if st.button("Crear Evento Bar", key="crear_evento_bar"):
            evento = crear_evento_bar(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, "vacio", aforo_total, num_presentaciones, codigo_cortesia)
            guardar_evento(evento, "Bar")
            artistas_list.clear()
            pdf_path = generar_pdf(evento, "Bar")
            st.success(f"Evento Bar creado y guardado en {pdf_path}")

    elif option == "Teatro":
        alquiler = st.number_input("Alquiler del lugar", value=0, key="crear_alquiler")
        if st.button("Crear Evento Teatro", key="crear_evento_teatro"):
            evento = crear_evento_teatro(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precio_regular, precio_preventa, "vacio", aforo_total, alquiler, codigo_cortesia)
            guardar_evento(evento, "Teatro")
            artistas_list.clear()
            pdf_path = generar_pdf(evento, "Teatro")
            st.success(f"Evento Teatro creado y guardado en {pdf_path}")

    elif option == "Filantrópico":
        patrocinador_list = []
        st.title("Datos patrocinador del evento")
        col16, col17 = st.columns(2)
        with col16:
            nombre_patrocinador = st.text_input("Nombre del patrocinador", " ", key="crear_nombre_patrocinador")
        with col17:
            dni_patrocinador = st.text_input("Documento de identidad", " ", key="crear_dni_patrocinador")

        col18, col19, col20 = st.columns(3)
        with col18:
            email_patrocinador = st.text_input("Email", " ", key="crear_email_patrocinador")
        with col19:
            celular_patrocinador = st.text_input("celular", " ", key="crear_celular_patrocinador")
        with col20:
            valor_aportado = st.number_input("Aporte del patrocinador", value=0, key="crear_valor_aportado")

        if st.button("Añadir Patrocinador", key="crear_añadir_patrocinador"):
            patrocinador = Patrocinador(nombre_patrocinador, dni_patrocinador, email_patrocinador, celular_patrocinador, valor_aportado)
            patrocinador_list.append(patrocinador)
            st.success(f"Patrocinador {patrocinador.nombre} añadido")

        if st.button("Crear evento Filantrópico", key="crear_evento_filantrópico"):
            evento = crear_evento_filantropico(artistas_list, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, 0, 0, "vacio", aforo_total, patrocinador_list, "")
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
        if evento_seleccionado["estado"].lower() == "realizado":
            st.warning("No se pueden modificar eventos que ya han sido realizados.")
        else:
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

        if st.button("Eliminar Evento", key="eliminar_evento"):
            if any(boleto["evento"] == evento_seleccionado["nombre"] for boleto in boletos):
                st.warning("No se puede eliminar el evento porque ya se han vendido boletos para este evento.")
            else:
                eventos = eliminar_evento(eventos, evento_seleccionado["nombre"])
                st.success(f"Evento '{evento_seleccionado['nombre']}' eliminado exitosamente.")
                st.experimental_rerun()

mostrar_pagina_evento()
