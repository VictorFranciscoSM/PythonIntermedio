class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b

result1 = Calculadora.sumar(5,3)
result2 = Calculadora.restar(5,3)
print("Sumar: ", result1)
print("Restar: ", result2)