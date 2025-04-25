import sqlite3

#busca el archivo .db ara hacar la conexion en caso de que no lo encuentre lo crea
conexion = sqlite3.connect("Mod02_Manejo_de_Archivos_y_Paquetes/Cl04_mi_base_de_datos.db")
print("Conexion de base de datos exitosa")

#se usa para interactuar con la base de datos 
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
               empleados(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER,
               departamento TEXT)
''' )

print("Tabla 'empleados' creada")

#se cierra la conexion con la base de datos para que no consuma memoria despues de no usarse
conexion.close()