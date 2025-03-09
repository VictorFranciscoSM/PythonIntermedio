class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def trabajar(self):
        raise NotImplementedError("Este metodo debe ser implementado por la clase hija")
    
class Gerente(Empleado):
    def trabajar(self):
        return f"{self.nombre} esta gestionando el equipo"
    
class Desarrollador(Empleado):
    def trabajar(self):
        return f"{self.nombre} esta escribiendo codigo"

def realizar_trabajo(empleado):
    print(empleado.trabajar())

gerente = Gerente("Victor")
desarrollador = Desarrollador("Francisco")

realizar_trabajo(gerente)
realizar_trabajo(desarrollador)