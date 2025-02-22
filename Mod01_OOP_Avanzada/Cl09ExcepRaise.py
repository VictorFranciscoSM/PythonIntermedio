def validar_edad(edad):
    if edad < 18:
        raise ValueError("Edad tiene que ser mayor a 18")
    else:
        print("Edad valida")

try:
    edad_u = int(input("Ingresa edad: "))
    validar_edad(edad_u)
except ValueError as e:
    print(f"Error {e}")