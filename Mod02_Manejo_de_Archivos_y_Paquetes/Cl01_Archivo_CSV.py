import csv

datos = [["Nombre", "Edad", "Ciudad"], ["Ana", 30, "Lima"], ["Carlos", 24, "Mexico"], ["Martha", 32, "Monterrey"]]

with open("Mod02_Manejo_de_Archivos_y_Paquetes\datos.csv", mode = "w", newline = "") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

with open("Mod02_Manejo_de_Archivos_y_Paquetes\datos.csv", newline = "") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
