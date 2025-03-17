import pickle
import os
datos = {'nombre': 'Ana', 'edad': 24, 'ciudad': 'Morelos'}

# Crear carpeta si no existe
os.makedirs(r'Mod02_Manejo_de_Archivos_y_Paquetes', exist_ok=True)

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\pickle','wb') as archivo:
    pickle.dump(datos, archivo)
    