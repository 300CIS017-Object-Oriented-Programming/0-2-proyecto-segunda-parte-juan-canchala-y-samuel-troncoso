class EventoFilantropico:
    def __init__(self, artista, nombre, fecha, hora_apertura, hora_show, lugar_show, direccion, ciudad, estado, precioVentaRegular, precioPreVenta, estado_boleteria, aforoTotal, patrocinadores, codigo_cortesia):
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
        self.patrocinadores = patrocinadores
        self.codigo_cortesia = codigo_cortesia

    def calcular_ingresos(self):
        pass  