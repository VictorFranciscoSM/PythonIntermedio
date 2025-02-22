import time

def medir_tiempo(funcion_original):
    def nueva_funcion(*args, **kwargs):
        inicio = time.time()
        resultado = funcion_original(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return nueva_funcion

@medir_tiempo
def tarea_pesada():
    time.sleep(2)
    print("Tarea completada")

tarea_pesada()
