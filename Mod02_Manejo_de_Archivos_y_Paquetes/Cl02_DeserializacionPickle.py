import pickle
import os

# Crear carpeta si no existe
os.makedirs(r'Mod02_Manejo_de_Archivos_y_Paquetes', exist_ok=True)

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\pickle','rb') as archivo:
    datos_recuperados = pickle.load(archivo)
    print(datos_recuperados)
    