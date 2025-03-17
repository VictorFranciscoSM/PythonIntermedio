import json

with open('Mod02_Manejo_de_Archivos_y_Paquetes\empleados.json', mode = 'r') as archivo_json:
    datos_json = json.load(archivo_json)

nuevo_empleado = {'ID':6, 'Nombre':'David', 'Edad': 32, 'Departamento': 'Logistica'}
datos_json.append(nuevo_empleado)

with open('Mod02_Manejo_de_Archivos_y_Paquetes\empleados.json', mode = 'w') as archivo_json:
    json.dump(datos_json,archivo_json, indent=4)
