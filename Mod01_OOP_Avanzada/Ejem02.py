def decorador(funcion_original):
    def nueva_funcion(*args, **kwargs):
        print("Antes de ejecutar la funcion")
        resultado = funcion_original(*args, **kwargs) #ejecucion de funcion original
        print("Despues de ejecutar la funcion")
        return resultado
    return nueva_funcion

@decorador
def sumar(a, b):
    return a + b 

print(sumar(5,5))
