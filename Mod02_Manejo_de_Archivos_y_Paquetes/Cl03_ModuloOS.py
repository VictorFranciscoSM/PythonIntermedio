import os
arcvhivo  = "Mod02_Manejo_de_Archivos_y_Paquetes/EjemploOS.txt"

if os.path.exists(arcvhivo):
    print(f"{arcvhivo} existe")
else:
    print(f"{arcvhivo} no existe")

tamano = os.path.getsize(arcvhivo)
print(f"El tamaño del {arcvhivo} es {tamano} bytes")

ruta_abs = os.path.abspath(arcvhivo)
print(f"la ruta absoluta del {arcvhivo} es {ruta_abs}")

"""
os.mkdir("nuevo_directorio")    #crea un nuevo derectorio desde donde se encuentre la termina que esta usnado python
print("Directorio 'nuevo_directorio' creado) #cabe menscionar que para este se creara en la carpeta cusopython
"""

os.chdir("nuevo_direcorio")             #cambia la ruta del directorio
print(f"El directorio actual es: {os.getcwd()}")        #

arcvhivos = os.listdir()            #en lista los arvhivos que se encuentran en el directorio actual
print(f"archivos en el directorio: {arcvhivos}")  

os.remove("EjemploOS.txt")          #elimina el archivo indicado
print(f"archivo 'EjemploOS.txt' fue eliminado")

os.rmdir("nuevo_directorio")        #elimina el directorio indicado, para poder eliminarse necesita  estar vacio el directorio, si no marcara error
print(f"directorio 'nuevo_directorio' eliminado")