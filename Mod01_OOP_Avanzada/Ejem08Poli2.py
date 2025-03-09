class Animal:
    def hacer_sonido(self):
        return NotImplementedError("metodo implementado por la clase hija")
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
def sonar_animales(animales):
    for animal in animales:
        print(animal.hacer_sonido())

perro = Perro() 
gato = Gato()

sonar_animales([perro, gato])