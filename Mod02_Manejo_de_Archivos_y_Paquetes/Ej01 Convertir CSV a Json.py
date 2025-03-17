import csv
import json

empleados_leidos = []

with open('Mod02_Manejo_de_Archivos_y_Paquetes\empelados.csv', mode= 'r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        fila['ID'] = int(fila['ID'])
        fila['Edad'] = int(fila['Edad'])
        empleados_leidos.append(fila)

with open('Mod02_Manejo_de_Archivos_y_Paquetes\empelados.json', mode = 'w') as archivo_json:
    json.dump(empleados_leidos, archivo_json, indent=4)
    print("Datos convertidos con exito")