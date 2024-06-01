# models/Persona.py
class Persona:
    def __init__(self, nombre, dni, email, celular, nombre_artistico=None):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.celular = celular
        self.nombre_artistico = nombre_artistico
        self.ingresos = 0.0

    def actualizar_ingresos(self, monto):
        self.ingresos += monto

    def __repr__(self):
        return f"Persona({self.nombre}, Ingresos: {self.ingresos:.2f})"
