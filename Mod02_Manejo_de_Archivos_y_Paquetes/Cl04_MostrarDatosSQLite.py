import sqlite3

conexion = sqlite3.connect("Mod02_Manejo_de_Archivos_y_Paquetes/Cl04_mi_base_de_datos.db")
print("Conexion a base de datos exitosa")

cursor = conexion.cursor()

""" agrega un nuevo empleado
cursor.execute('''
INSERT INTO empleados(nombre, edad, departamento)
VALUES("Maria", 20, "IT")
''')
conexion.commit()
"""

#muestra los datos almacenados en el data base
cursor.execute("SELECT * FROM empleados")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

#muestra los datos indicados de la data base
cursor.execute("SELECT nombre, edad FROM empleados")
empleados = cursor.fetchall()
for empleado in empleados:
    print(empleado)

cursor.execute("SELECT * FROM empleados WHERE edad > 25")
empleados_mayores = cursor.fetchall()
for empleado in empleados_mayores:
    print(empleado)
conexion.commit()

conexion.close()