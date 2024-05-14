class Evento:
    def __init__(self, artista, nombreEvento, fecha, horaApertura, horaShow, lugar, direccion, ciudad, estadoShow, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal):
        self.artista = artista
        self.nombreEvento = nombreEvento
        self.fecha = fecha
        self.horaApertura = horaApertura
        self.horaShow = horaShow
        self.lugar = lugar
        self.direccion = direccion
        self.ciudad = ciudad
        self.estadoShow = estadoShow
        self.precioVentaRegular = precioVentaRegular
        self.precioPreVenta = precioPreVenta
        self.estadoBoleteria = estadoBoleteria
        self.aforoTotal = aforoTotal

    def cambiarEstado(self, nuevo_estado):
        self.estadoShow = nuevo_estado

    def calcularIngresos(self, cantidad_boletas_vendidas):
        return cantidad_boletas_vendidas * self.precioVentaRegular