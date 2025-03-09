class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este metodo debe ser implementado por las clases hijas")

class Coche(Vehiculo):
    def mover(self):    
        return "Coche en movimiento"

class Bicicleta(Vehiculo):
    def mover(self):
        return "Bicicleta en movimiento"

class Avion(Vehiculo):
    def mover(self):
        return "Avion volando"

def iniciar_movimiento(vehiculo):
    print(vehiculo.mover())

coche1 = Coche()
bicicleta1 = Bicicleta()
avion1 = Avion()

iniciar_movimiento(coche1)
iniciar_movimiento(bicicleta1)
iniciar_movimiento(avion1)
