class CuentaBancaria:
    def __init__(self, saldo = 0):
        self.__saldo = saldo        #modelo privado
    def deposito(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad invalida")
    def get_saldo(self):
        return self.__saldo
    
cuenta1 = CuentaBancaria(2000)
cuenta1.deposito(200)
print(cuenta1.get_saldo())