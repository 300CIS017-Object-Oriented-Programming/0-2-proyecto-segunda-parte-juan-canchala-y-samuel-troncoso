from models.Persona import Persona


class Patrocinador(Persona):
    def __init__(self, nombre, ID, email, celular, valorAportado):
        super().__init__(nombre, ID, email, celular)
        self.valorAportado = valorAportado
