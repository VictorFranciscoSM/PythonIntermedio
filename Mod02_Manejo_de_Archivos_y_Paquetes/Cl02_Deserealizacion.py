import json

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\Serializacion.json', 'r') as archivo:
    datos_recuperados = json.load(archivo)
    print(datos_recuperados)
    