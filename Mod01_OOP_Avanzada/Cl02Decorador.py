def decorador(func):
    def decorador_decorado():
        print("Algo se esta haceindo antes de ejecutar la funcion")
        func()
        print("Algo se esta haciendo despues de ejecutar la funcion")
    return decorador_decorado


@decorador          #mi_funcion = decorador(mi_funcion) es lo mismo que definirlo de esta forma
def mi_funcion():
    print("Ejecutando la funcion original")

#mi_funcion = decorador(mi_funcion)
mi_funcion()