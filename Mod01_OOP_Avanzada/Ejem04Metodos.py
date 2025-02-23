class Empleado:
    cantidad_emplados = 0
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.incrementar_empleados()

    @classmethod
    def incrementar_empleados(cls):
        cls.cantidad_emplados += 1
    @staticmethod
    def calcular_bonificacion(salario):
        if salario < 3000:
            return salario * 0.15
        else:
            return salario * 0.1
    @classmethod
    def obtener_total_de_empleados(cls):
        return cls.cantidad_emplados
    
emplado1 = Empleado("Victor", 2000)
emplado2 = Empleado("Diego", 3000)
emplado3 = Empleado("Oman", 4000)

print(f"Total de empleados: {Empleado.obtener_total_de_empleados()}")
bonificacion = emplado1.calcular_bonificacion(emplado1.salario)
print(f"Bonificacion de {emplado1.nombre} es: {bonificacion}")