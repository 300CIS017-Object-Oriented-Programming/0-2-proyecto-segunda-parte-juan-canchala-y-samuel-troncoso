
from models.Evento import Evento


class EventoTeatro(Evento):
    def __init__(self, artista, nombreEvento, fecha, horaApertura, horaShow, lugar, direccion, ciudad, estadoShow,precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal, alquiler):
        super().__init__(artista, nombreEvento, fecha, horaApertura, horaShow, lugar, direccion, ciudad, estadoShow, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal)
        self.alquiler = alquiler

