class Coche:
    cantidad_de_coches = 0
    def __init__(self, marca):
        self.marca = marca
        Coche.incrementar_coches()

    @classmethod
    def incrementar_coches(cls):
        cls.cantidad_de_coches += 1
        print(f"Cantidad de coches {cls.cantidad_de_coches}")
    
coche1 = Coche("Ford")
coche2 = Coche("BYD")
coche3 = Coche("BMW")