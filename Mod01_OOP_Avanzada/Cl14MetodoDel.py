class MiClase:
    def __init__(self):
        print("Objeto creado")
    
    def __del__(self):
        print("Objeto destruido")

obj = MiClase()
del obj