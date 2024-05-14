class Cliente(Persona):
    def __init__(self, nombre, ID, email, celular, comoseEntero):
        super().__init__(nombre, ID, email, celular)
        self.comoseEntero = comoseEntero