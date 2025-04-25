import sqlite3

conexion = sqlite3.connect("Mod02_Manejo_de_Archivos_y_Paquetes/Cl04_mi_base_de_datos.db")
print("Conexion a base datos exitosa")

cursor = conexion.cursor()
cursor.execute('''
UPDATE empleados
               SET edad = 31
               WHERE nombre = "Juan Perez"
''')

cursor.execute('''
    DELETE FROM empleados WHERE ID = 1           
''')

conexion.commit()

conexion.close()