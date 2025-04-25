import shutil

"""
#Copia el archivo, puede ser en otro directorio se define en la sgunda parte
shutil.copy("Mod02_Manejo_de_Archivos_y_Paquetes/ShutilOrigen.txt", "Mod02_Manejo_de_Archivos_y_Paquetes/CopiaShutilOrigen.txt")
print("Archivo copiado con exito")
"""

"""
#copia el directorio indicado la primera poscion al segunda 
shutil.copytree("Mod02_Manejo_de_Archivos_y_Paquetes/HolaShutil", "Mod02_Manejo_de_Archivos_y_Paquetes/HolaShutil2")
print("Directorio copiado")
"""

"""
#mueve el arvico a otro nuevo directorio
shutil.move("Mod02_Manejo_de_Archivos_y_Paquetes/ShutilOrigen.txt", "Mod02_Manejo_de_Archivos_y_Paquetes/HolaShutil/ShutilOrigen.txt")
print("arcchivo movido al directorio indicado")
"""

"""
#mueve el arvico a otro nuevo directorio
shutil.move("Mod02_Manejo_de_Archivos_y_Paquetes/HolaShutil2", "Mod02_Manejo_de_Archivos_y_Paquetes/HolaShutil")
print("directorio movido al directorio indicado")
"""

#elinima el directorio indicado
shutil.rmtree("Mod02_Manejo_de_Archivos_y_Paquetes/HolaShutil")
print("Directorio eliminado")