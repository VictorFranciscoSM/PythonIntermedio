from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.largo * self.ancho

circulo = Circulo(5)
rectangulo = Rectangulo(4,5)

print(circulo.area())
print(rectangulo.area())
