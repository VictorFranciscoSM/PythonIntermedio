import xml.etree.ElementTree as ET
import json
import os

#En Python, cuando usas una barra invertida (\) dentro de una cadena, Python la interpreta como el inicio de una secuencia de escape.
#Una secuencia de escape es una combinación especial de caracteres que Python usa para representar caracteres especiales como:
#\n → Nueva línea
#\t → Tabulación
#\\ → Barra invertida literal
#✅ Una cadena cruda (r"...")
#✅ Barras dobles (\\)
#✅ Barras normales (/)

# Crear carpeta si no existe
os.makedirs(r'Mod02_Manejo_de_Archivos_y_Paquetes', exist_ok=True)

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\empleados.json', mode = 'r') as archivo_json:
    empleados_json = json.load(archivo_json)


raiz = ET.Element("Empleados")

for empleado in empleados_json:
    #Si alguna clave (ID, Nombre, Edad, Departamento) no existe en el JSON o es None, lanzará un error al tratar de acceder al valor.
    #✅ Solución → Usa get() para evitar errores si la clave no existe:
    
    elemento_empleado = ET.SubElement(raiz,'empleado', id=str(empleado.get('ID','')))
    nombre = ET.SubElement(elemento_empleado, 'Nombre')
    nombre.text = empleado['Nombre']
    edad = ET.SubElement(elemento_empleado, 'Edad')
    edad.text = str(empleado['Edad'])
    departamento = ET.SubElement(elemento_empleado, 'Departamento')
    departamento.text = empleado['Departamento']


arbol = ET.ElementTree(raiz)
arbol.write(r'Mod02_Manejo_de_Archivos_y_Paquetes/empleados.xml', encoding='utf-8', xml_declaration=True)