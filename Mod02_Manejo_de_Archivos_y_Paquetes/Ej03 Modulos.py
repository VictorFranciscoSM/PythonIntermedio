import os
import shutil

"""
#Crea un nuevo directorio
os.mkdir("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3Directorio")
"""

"""
for i in range(1,4):
    #se abre un lector .txt para acrear varios achivos en el directorio indicado
    with open(f"Mod02_Manejo_de_Archivos_y_Paquetes/Ej3Directorio/Ej3Directorio{i}.txt", "w") as f:
        f.write(f"Este es el contenido del archivo {i}. \n")    #creacion de arvhivos dentro de la carpeta mi directorio
"""

"""
#se crea el directorio
os.mkdir("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3CopiaDirectorio")
"""

"""
#copia los arvhico del directorio 1 al directorio 2
for i in range(1,4):
    shutil.copy(f"Mod02_Manejo_de_Archivos_y_Paquetes/Ej3Directorio/Ej3Directorio{i}.txt", "Mod02_Manejo_de_Archivos_y_Paquetes/Ej3CopiaDirectorio")
"""

"""
#crea una carpeta y posterior mueve el arvhivo del direcctorio uno al directorio 2
os.mkdir("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3DirectorioMoved")
shutil.move("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3CopiaDirectorio/Ej3Directorio1.txt", "Mod02_Manejo_de_Archivos_y_Paquetes/Ej3DirectorioMoved/Ej3Directorio1.txt")"
"""

#Se elimina todo lo que este adentro del directorio
shutil.rmtree("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3Directorio")
shutil.rmtree("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3CopiaDirectorio")
shutil.rmtree("Mod02_Manejo_de_Archivos_y_Paquetes/Ej3DirectorioMoved")
