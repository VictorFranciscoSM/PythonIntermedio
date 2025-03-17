import xml.etree.ElementTree as ET

raiz = ET.Element("personas")
persona1 = ET.SubElement(raiz, "persona", nombre = "Victor")
persona1.text = "27 años, Mexico"
persona2 = ET.SubElement(raiz, "persona", nombre = "Francisco")
persona2.text = "28 años, Edo"

arbol = ET.ElementTree(raiz)
arbol.write("Mod02_Manejo_de_Archivos_y_Paquetes\datos2.xml")

tree = ET.parse("Mod02_Manejo_de_Archivos_y_Paquetes\datos2.xml")
raiz = tree.getroot()

for elemento in raiz:
    print(elemento.tag, elemento.attrib)