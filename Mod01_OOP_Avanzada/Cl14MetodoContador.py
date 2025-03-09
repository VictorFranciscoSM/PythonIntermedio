class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.numero = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.numero >= self.limite:
            raise StopIteration
        self.numero += 1
        return self.numero
contador = Contador(5)
for num in contador:
    print(num)