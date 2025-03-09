from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Ave(Volador):
    def volar(self):
        return "El ave esta volando"

class Avion(Volador):
    def volar(self):
        return "El avion vuela"

ave = Ave()
avion = Avion()

print(ave.volar())
print(avion.volar())