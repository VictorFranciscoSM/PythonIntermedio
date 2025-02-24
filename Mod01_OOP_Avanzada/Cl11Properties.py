class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        return self._radio
    @radio.setter
    def radio(self, radio):
        if radio < 0:
            print("Valor incorrecto")
        else:
            self._radio = radio
    @property
    def area(self):
        return 3.1416 * self._radio ** 2
    
circulo = Circulo(4)
print(circulo.area)
circulo.radio = -3
circulo.radio =  7
print(circulo.area)