def decorador_multiplicacion(func):
    def inner(num):
        resultado = func(num)
        return resultado * 2
    return inner

@decorador_multiplicacion
def obtener_numero(numero):
    return numero

print(obtener_numero(5))

def log(func):
    def inner(*args, **kwargs):
        print(f"Llmada a la funcion {func.__name__} con los argumentos {args} y {kwargs}")
        return func(*args, **kwargs)
    return inner

@log
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("juan")