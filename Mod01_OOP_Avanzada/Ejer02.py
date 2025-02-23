import math
import json
"""
#Ejercicio 1
try:
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    sum = num1 / num2
    print(f"la division es: {num1 / num2}")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
"""

"""
#Ejercicio 2
def raiz(num):
    if num < 0:
        raise TypeError("NumeroNegativoError ")
    return math.sqrt(num)

try:
    num = int(input("Numero: "))
    
    print(f"la raiz es: {raiz(num)}")
except ValueError:
    print("Error de valor")
except TypeError as e:
    print(f"En negativo {e}")
"""

"""
#Ejercicio 3
try:
    nombre = input("Nombre del archivo a abrir: ")
    nombre = f"{nombre}.json"
    with open(nombre, "r", encoding="utf-8") as arhivo:
        datos = json.load(arhivo)
except FileNotFoundError:
    print("archivo no encontrado")
else:
    print("El archivo fue abierto")
"""
"""
#Ejercicio 4
try:
    archivo = open("nombre.txt", "r")
    datos = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    archivo.close()
"""
"""
#Ejercicio 5
lista = []
a = 0
try:
    if not lista:
        raise ValueError("Lista vacia")
    a = sum(lista)
    print(f"{a}")
except ValueError as e:
    print(f"{e}") 
"""

#Ejercicio 6
suma = 0
try:
    with open("numeros.json", "r") as archivo:
        datos = json.load(archivo)
        # Intenta obtener un valor numérico del JSON (por ejemplo, una clave "numero")
        if "numero" in datos:
            valor = datos["numero"]
            numero = int(valor)  # Intenta convertir el valor a entero
            print("El número leído del archivo JSON es:", numero)
        else:
            print("Error: El archivo JSON no contiene la clave 'numero'.")
except FileNotFoundError:
    print("archivo no encontrada")
except ValueError:
    print("No son numeros")
except Exception as e:
    print(f"A surgido el error: {e}")