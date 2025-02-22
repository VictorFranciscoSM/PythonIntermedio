#nultiples ecepciones
try:
    a = int(input("Nuemero a ser devidido: "))
    b = int(input("Nuemero divisor: "))
    re = a/b
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Se esperaba un numero entero")
except Exception as e:
    print(f"No se puede realizar a ocurrido in error: {e}")
else:       #se ejecuta solo si no a acurrido ninguna excepcion
    print(f"El resultado es: {re}")
#simpre se ejecuta sin importar si paso una expcion
