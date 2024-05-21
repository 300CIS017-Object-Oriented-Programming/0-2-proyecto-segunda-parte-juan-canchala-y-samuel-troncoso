from fpdf import FPDF

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
