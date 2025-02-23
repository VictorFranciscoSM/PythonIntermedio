class Empleado:
    empleados = 0
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.empleados += 1

    def mostar_info(self):
        print(f"El empleado {self.nombre} su salario es: {self.salario}")

    def aumentar_salario(self, porcentaje):
        self.salario += porcentaje*self.salario

    @classmethod
    def contar_empleados(cls):
        return cls.empleados
    
    @classmethod
    def crear_empleado_desde_cadena(cls, cadena):
        nombre, salario = cadena.split(",")
        return cls(nombre, float(salario))
    
    @staticmethod
    def es_salario_alto(salario):
        return salario > 5000


string = "Victor 5000"
palabras = string.split()
