
from models.Evento import Evento


class EventoFilantropico(Evento):
    def __init__(self, artista, nombreEvento, fecha, horaApertura, horaShow, lugar, direccion, ciudad, estadoShow, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal, patrocinadores):
        super().__init__(artista, nombreEvento, fecha, horaApertura, horaShow, lugar, direccion, ciudad, estadoShow, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal)
        self.patrocinadores = patrocinadores

