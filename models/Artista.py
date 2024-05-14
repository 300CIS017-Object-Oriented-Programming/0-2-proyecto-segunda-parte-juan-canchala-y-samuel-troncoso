from models.Persona import Persona


class Artista(Persona):
    def __init__(self, nombre, ID, email, celular, nombreArtistico, evento):
        super().__init__(nombre, ID, email, celular)
        self.nombreArtistico = nombreArtistico
        self.evento = evento