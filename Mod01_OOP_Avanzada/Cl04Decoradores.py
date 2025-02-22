def decorador_1(func):
    def inner_1():
        print("Ejecutando decorador 1")
        return func()
    return inner_1

def decorador_2(func):
    def inner_2():
        print("Ejecutando decorador 2")
        return func()
    return inner_2

@decorador_1
@decorador_2
def mi_funcion():
    print("Ejecutando funcion original")

mi_funcion()