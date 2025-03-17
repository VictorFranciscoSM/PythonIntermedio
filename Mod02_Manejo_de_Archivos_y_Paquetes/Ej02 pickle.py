import pickle
import json

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def __repr__(self):
        return f"{self.nombre}, {self.edad} años, {self.ciudad}"
    
personas = [Persona("victor", 27, "EDOMX"), Persona("Ale", 25, "MX")]

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\persona.pickle', 'wb') as archivo:
    pickle.dump(personas,archivo)

personas_json = [{'nombre': p.nombre, 'edad': p.edad, 'ciudad': p.ciudad} for p in personas]

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\persona.json', 'w') as archivo:
    json.dump(personas_json, archivo, indent= 4)

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\persona.pickle', 'rb') as archivo:
    personas_recuperar_pickle = pickle.load(archivo)
    print("Deseralizacion con pickle:", personas_recuperar_pickle)

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\persona.json', 'r') as archivo:
    personas_reperados_json = json.load(archivo)
    print("Deserealizacion con json: ", personas_reperados_json)
