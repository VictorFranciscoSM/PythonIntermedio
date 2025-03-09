class Multiplicador:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, numero):             #comportamiento de funcion en un objeto
        return numero * self.factor
    
multiplicar = Multiplicador(4)

print(multiplicar(10))