class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        pass
    def saludar(self):
        print(f"Hola soy {self.nombre} y mi edad es {self.edad}")

persona1 = Persona("Victor", 28)
persona1.saludar()


