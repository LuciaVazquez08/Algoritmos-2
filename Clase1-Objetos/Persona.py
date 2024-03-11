class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def cumpleaños(self) -> None:
        self.edad += 1
        