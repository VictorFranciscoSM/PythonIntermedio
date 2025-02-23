class CuentaBancaria:
    cuentas = 0
    def __init__(self, nombre, saldo = 0):
        self.nombre = nombre
        self.saldo = saldo
        CuentaBancaria.cuentas += 1

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Deposito {cantidad}, saldo actual {self.saldo}")

    def retirar(self, cantidad):
        if CuentaBancaria.validar_transaccion(self.saldo, cantidad):
            self.saldo -= cantidad
            print(f"Retirado: {cantidad}, saldo actual {self.saldo}")

    @classmethod
    def cuentas_abiertas(cls):
        return cls.cuentas
    
    @staticmethod
    def validar_transaccion(saldo, cantidad):
        if cantidad > saldo:
            return False
        else:
            return True
        
cliente1 = CuentaBancaria("Victor", 4500)
cliente1.depositar(120)
