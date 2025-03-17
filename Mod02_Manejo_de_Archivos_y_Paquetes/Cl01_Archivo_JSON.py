import json

datos = {"nombre": "Victor", "edad": 30, "ciudad": "Mexico"}

with open("Mod02_Manejo_de_Archivos_y_Paquetes\datos1.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)
try:    
    with open("Mod02_Manejo_de_Archivos_y_Paquetes\datos1.json", "r") as archivo:
        datos = json.load(archivo)
        print(datos)
except json.JSONDecodeError:
    print("Error el archivo no contiene datos json validos")