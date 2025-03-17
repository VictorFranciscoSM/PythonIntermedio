import csv
empleados = [{'ID': 1, 'Nombre': 'Victor', 'Edad': 27, 'Departamento':'Ventas'},
            {'ID': 2, 'Nombre': 'Frank', 'Edad': 25, 'Departamento':'Ventas'},
            {'ID': 3, 'Nombre': 'diego', 'Edad': 25, 'Departamento':'Ventas'},
            {'ID': 4, 'Nombre': 'Jose', 'Edad': 25, 'Departamento':'Ventas'},
            {'ID': 5, 'Nombre': 'Oman', 'Edad': 25, 'Departamento':'Ventas'}]

with open('Mod02_Manejo_de_Archivos_y_Paquetes\empelados.csv', mode = 'w', newline='') as archivo_csv:
    campos = ['ID', 'Nombre', 'Edad', 'Departamento']
    escritor = csv.DictWriter(archivo_csv, fieldnames= campos)
    escritor.writeheader()
    escritor.writerows(empleados)
    