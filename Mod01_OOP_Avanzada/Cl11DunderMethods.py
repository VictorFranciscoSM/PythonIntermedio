class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"
    
pers = Persona("Victor", 25)
print(Persona)
print(repr(pers))

class Milista:
    def __init__(self, elementos):
        self.elementos = elementos
    def __len__(self):
        return len(self.elementos)

lista = Milista([1,2,3,4])
print(len(lista))