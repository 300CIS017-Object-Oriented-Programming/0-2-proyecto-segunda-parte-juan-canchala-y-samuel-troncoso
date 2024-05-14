from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(informacion, nombre_archivo):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(100, 750, informacion)
    c.save()

import streamlit as st

def generar_pdf(informacion, nombre_archivo):
    # Lógica para generar el PDF usando reportlab
    pass

# Contenido de la página
st.title("Generador de PDF")

# Información para el PDF
informacion = "Hola, este es un PDF generado desde Streamlit."

# Botón para generar y descargar el PDF
if st.button("Descargar PDF"):
    generar_pdf(informacion, "mi_pdf.pdf")
    st.success("PDF generado y descargado correctamente.")
    with open("mi_pdf.pdf", "rb") as file:
        pdf_bytes = file.read()
    st.download_button(label="Descargar PDF", data=pdf_bytes, file_name="mi_pdf.pdf", mime="application/pdf")
