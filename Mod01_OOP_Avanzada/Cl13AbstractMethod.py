from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    @abstractmethod
    def descansar(self):
        pass
class Gerente(Empleado):
    def trabajar(self):
        return "Gestionando el equipo"
    def descansar(self):
        return "Descansando en la oficina"
class Desarrolador(Empleado):
    def trabajar(self):
        return "Escribiendo codigo"
    def descansar(self):
        return "Decanso de codigo"

gerente = Gerente()
desarrolador = Desarrolador()
print(gerente.trabajar())
print(gerente.descansar())
print(desarrolador.trabajar())
print(desarrolador.descansar())