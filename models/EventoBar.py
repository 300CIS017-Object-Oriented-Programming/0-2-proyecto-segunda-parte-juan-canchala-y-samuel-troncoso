class EventoBar:
    def __init__(self, artista, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precioVentaRegular, precioPreVenta, estado_boleteria, aforoTotal, num_presentaciones, codigo_cortesia):
        self.artista = artista
        self.nombre = nombre
        self.fecha = fecha
        self.hora_apertura = hora_apertura
        self.hora_show = hora_show
        self.lugar_show = lugar_show
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.precioVentaRegular = precioVentaRegular
        self.precioPreVenta = precioPreVenta
        self.estado_boleteria = estado_boleteria
        self.aforoTotal = aforoTotal
        self.num_presentaciones = num_presentaciones
        self.codigo_cortesia = codigo_cortesia
        self.ingreso_bar = 0.0
        self.ingreso_artista = 0.0

    def calcular_ingresos(self, precio_final, cantidad_boletos):
        self.ingreso_bar += 0.2 * precio_final * cantidad_boletos
        self.ingreso_artista += 0.8 * precio_final * cantidad_boletos
        for artista in self.artista:
            artista.actualizar_ingresos(self.ingreso_artista / len(self.artista))