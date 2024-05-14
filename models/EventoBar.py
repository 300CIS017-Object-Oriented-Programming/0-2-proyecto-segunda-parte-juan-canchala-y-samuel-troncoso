
from models.Evento import Evento


class EventoBar(Evento):
    def __init__(self, artista, nombreEvento, fecha, horaApertura, horaShow, lugar,direccion, ciudad, estadoShow, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal, numPresentaciones):
        super().__init__(artista, nombreEvento, fecha, horaApertura, horaShow, lugar, direccion, ciudad, estadoShow, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal)
        self.numPresentaciones = numPresentaciones

