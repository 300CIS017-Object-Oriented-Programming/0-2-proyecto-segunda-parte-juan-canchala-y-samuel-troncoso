import streamlit as st
import json
from datetime import date
from fpdf import FPDF
import os
from static.mensajes import EXCEPCION_NO_EVENTOS

def mostrar_pagina_boleteria():
    st.title("Página de Boletería")

    def cargar_eventos():
        eventos = []
        try:
            with open('eventos.json', 'r') as f:
                for line in f:
                    eventos.append(json.loads(line))
        except FileNotFoundError:
            st.error(EXCEPCION_NO_EVENTOS)
        return eventos

    def guardar_boleto(boleto):
        with open('boletos.json', 'a') as f:
            json.dump(boleto, f)
            f.write('\n')

    def generar_pdf(boleto):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Recibo de Compra de Boleto", ln=True, align="C")
        pdf.cell(200, 10, txt=f"Evento: {boleto['evento']}", ln=True)
        pdf.cell(200, 10, txt=f"Comprador: {boleto['comprador']['nombre']}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {boleto['comprador']['email']}", ln=True)
        pdf.cell(200, 10, txt=f"Celular: {boleto['comprador']['celular']}", ln=True)
        pdf.cell(200, 10, txt=f"Cómo se enteró: {boleto['como_se_entero']}", ln=True)
        pdf.cell(200, 10, txt=f"Fase de Venta: {boleto['fase_venta']}", ln=True)
        pdf.cell(200, 10, txt=f"Descuento: {boleto['descuento']}%", ln=True)
        pdf.cell(200, 10, txt=f"Precio Final: ${boleto['precio_final']:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Cantidad de Boletos: {boleto['cantidad']}", ln=True)
        pdf.cell(200, 10, txt=f"Fecha de Compra: {boleto['fecha_compra']}", ln=True)

        if not os.path.exists('pdfs'):
            os.makedirs('pdfs')

        pdf_path = os.path.join('pdfs', f"recibo_{boleto['comprador']['nombre']}_{boleto['evento']}.pdf")
        pdf.output(pdf_path)
        return pdf_path

    def actualizar_ingresos_artista(artista, ingreso):
        try:
            with open('artistas.json', 'r') as f:
                artistas = json.load(f)
        except FileNotFoundError:
            artistas = {}

        if artista in artistas:
            artistas[artista] += ingreso
        else:
            artistas[artista] = ingreso

        with open('artistas.json', 'w') as f:
            json.dump(artistas, f)

    eventos = cargar_eventos()

    st.title("Boletería")
    st.header("Eventos Disponibles")

    if eventos:

        nombres_eventos = [evento["nombre"] for evento in eventos]
        nombre_evento_seleccionado = st.selectbox("Selecciona un evento", nombres_eventos)
        
        evento_seleccionado = next((evento for evento in eventos if evento["nombre"] == nombre_evento_seleccionado), None)

        if evento_seleccionado:
            st.subheader(evento_seleccionado["nombre"])
            st.text(f"Tipo: {evento_seleccionado['tipo']}")
            st.text(f"Fecha: {evento_seleccionado['fecha']}")
            st.text(f"Hora de apertura: {evento_seleccionado['hora_apertura']}")
            st.text(f"Hora del show: {evento_seleccionado['hora_show']}")
            st.text(f"Lugar: {evento_seleccionado['lugar_show']}")
            st.text(f"Dirección: {evento_seleccionado['direccion']}")
            st.text(f"Ciudad: {evento_seleccionado['ciudad']}")
            st.text(f"Estado: {evento_seleccionado['estado']}")
            st.text(f"Precio Regular: {evento_seleccionado['precio_regular']}")
            st.text(f"Precio Pre-venta: {evento_seleccionado['precio_preventa']}")
            st.text(f"Aforo Total: {evento_seleccionado['aforo_total']}")
            st.text("Artistas:")
            for artista in evento_seleccionado["artistas"]:
                st.text(f" - {artista['nombre_artistico']} ({artista['nombre']})")

            st.header("Comprar Boletos")
            nombre_comprador = st.text_input("Nombre del Comprador")
            email_comprador = st.text_input("Email del Comprador")
            celular_comprador = st.text_input("Celular del Comprador")
            como_se_entero = st.selectbox("¿Cómo se enteró del evento?", ["Redes Sociales", "Amigos/Familia", "Publicidad", "Otros"])
            fase_venta = st.selectbox("Fase de Venta", ["Pre-venta", "Venta Regular"])
            descuento = st.number_input("Descuento Aplicable (%)", 0, 100, 0)
            cantidad_boletos = st.number_input("Cantidad de Boletos", min_value=1, step=1)
            codigo_cortesia_ingresado = st.text_input("Código de Cortesía (si aplica)", "")
            
            precio = evento_seleccionado['precio_regular'] if fase_venta == "Venta Regular" else evento_seleccionado['precio_preventa']
            if codigo_cortesia_ingresado == evento_seleccionado.get('codigo_cortesia', ''):
                precio_final = 0.0
                st.success("Código de cortesía aplicado. Los boletos son gratis.")
            else:
                precio_final = precio * (1 - descuento / 100)
                st.warning("Código de cortesía incorrecto. Se aplicará el precio normal.")

            st.text(f"Precio Final por Boleto: {precio_final:.2f}")
            st.text(f"Precio Total: {precio_final * cantidad_boletos:.2f}")

            if st.button("Comprar Boletos"):

                aforo_total = evento_seleccionado["aforo_total"]
                boletos_vendidos = 0
                try:
                    with open('boletos.json', 'r') as f:
                        for line in f:
                            boleto = json.loads(line)
                            if boleto["evento"] == evento_seleccionado["nombre"]:
                                boletos_vendidos += boleto["cantidad"]
                except FileNotFoundError:
                    boletos_vendidos = 0

                if boletos_vendidos + cantidad_boletos <= aforo_total:
                    boleto = {
                        "evento": evento_seleccionado["nombre"],
                        "comprador": {
                            "nombre": nombre_comprador,
                            "email": email_comprador,
                            "celular": celular_comprador
                        },
                        "como_se_entero": como_se_entero,
                        "fase_venta": fase_venta,
                        "descuento": descuento,
                        "precio_final": precio_final * cantidad_boletos,
                        "cantidad": cantidad_boletos,
                        "fecha_compra": str(date.today())
                    }
                    guardar_boleto(boleto)
                    pdf_path = generar_pdf(boleto)
                    st.success(f"Boletos comprados exitosamente! Recibo guardado en {pdf_path}")
                    st.download_button(
                        label="Descargar Recibo",
                        data=open(pdf_path, "rb"),
                        file_name=pdf_path,
                        mime="application/octet-stream"
                    )

                    if evento_seleccionado['tipo'] == 'Bar':
                        ingreso_bar = 0.2 * precio_final * cantidad_boletos
                        ingreso_artista = 0.8 * precio_final * cantidad_boletos
                        st.text(f"Ingreso del Bar: {ingreso_bar:.2f}")
                        st.text(f"Ingreso del Artista: {ingreso_artista:.2f}")
                    elif evento_seleccionado['tipo'] == 'Teatro':
                        alquiler = evento_seleccionado.get('alquiler', 0) 
                        ingreso_tiquetera = 0.07 * precio_final * cantidad_boletos
                        ingreso_artista = 0.93 * precio_final * cantidad_boletos - alquiler
                        st.text(f"Ingreso de la Tiquetera: {ingreso_tiquetera:.2f}")
                        st.text(f"Ingreso del Artista después del alquiler: {ingreso_artista:.2f}")
                    elif evento_seleccionado['tipo'] == 'Filantrópico':
                        st.text(f"Ingreso del Artista: 0 (Evento Filantrópico)")
                    
                    for artista in evento_seleccionado["artistas"]:
                        actualizar_ingresos_artista(artista['nombre'], ingreso_artista / len(evento_seleccionado["artistas"]))
                else:
                    st.error("No hay más disponibilidad de aforo para este evento.")
    else:
        st.warning("No hay eventos disponibles en este momento.")
