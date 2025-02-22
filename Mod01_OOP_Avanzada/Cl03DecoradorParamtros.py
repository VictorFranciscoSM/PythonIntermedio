def decorador_con_parametro(func):
    def funcion_decorada(a,b):
        print(f"Antes de ejecutar con parametros {a} y {b}")
        resultado = func(a,b)
        print(f"Despues de ejcutar la funcion conresultado: {resultado}")
        return resultado
    return funcion_decorada

@decorador_con_parametro
def sumar(a,b):
    return a+b

sumar(3,5)
