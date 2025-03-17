import xml.etree.ElementTree as ET
import json

with open(r'Mod02_Manejo_de_Archivos_y_Paquetes\empleados.json', mode = 'r') as archivo_json:
    empleados_json = json.load(archivo_json)


raiz = ET.Element("Empleados")

for empleado in empleados_json:
    elemento_empleado = ET.SubElement(raiz,'empleado', id=str(empleado['ID']))
    nombre = ET.SubElement(elemento_empleado, 'Nombre')
    nombre.text = empleado['Nombre']
    edad = ET.SubElement(elemento_empleado, 'Edad')
    edad.text = str(empleado['Edad'])
    departamento = ET.SubElement(elemento_empleado, 'Departamento')
    departamento.text = empleado['Departamento']


arbol = ET.ElementTree(raiz)
arbol.write(r'Mod02_Manejo_de_Archivos_y_Paquetes/empleados.xml', encoding='utf-8', xml_declaration=True)
