import json

datos = {'nombre': 'Victor', 'edad': 25, 'ciudad': 'EDOMX'}

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\Serializacion.json', mode = 'w') as archivo:
    json.dump(datos,archivo, indent=4)
    