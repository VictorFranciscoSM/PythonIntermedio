class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mover(self):
        return "Vehiculo en movimiento"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)             #clase derivada
        self.tipo_motor = tipo_motor
    def mover(self):                                #modificacion de metodos
        return "Coche en movimiento"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    def mover(self):
        return "Bicicleta en movimiento"

vehiculo1 = Vehiculo("BYD", "Supra")
coche1 = Coche("Audi", "Corel", "deportivo")
Bicicleta1 = Bicicleta("Leon", "T1", "Montaña")

print(vehiculo1.mover())
print(coche1.mover())
print(Bicicleta1.mover())