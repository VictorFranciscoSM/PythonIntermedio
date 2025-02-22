#Decorador que convierte texto a mayuscula
def a_mayuscula(funcion_original):
    def funcion_nueva(*args, **kwargs):
        print("Palabra")
        mayuscula = funcion_original(*args, **kwargs)
        return mayuscula.upper()
    return funcion_nueva

@a_mayuscula
def convertir_texto(x):
    return x

print(convertir_texto("esto es una prueba"))

