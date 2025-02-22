def decorador(funcion_original):
    def nueva_funcion():
        print("Asted de ejecutar la funcion")
        funcion_original()
        print("Despues de ejecutar la funcion")
    return nueva_funcion

@decorador  #aplicamos el decorador
def hola():
    print("Hola")

hola()