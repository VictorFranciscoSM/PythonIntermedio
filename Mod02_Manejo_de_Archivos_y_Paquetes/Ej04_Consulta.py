import sqlite3

conexion = sqlite3.connect("Mod02_Manejo_de_Archivos_y_Paquetes/Ej04_Libros.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM libros WHERE ano_publicacion > 2000")
libros_recientes = cursor.fetchall()
for libro in libros_recientes:
    print(libro)

cursor.execute('''
UPDATE libros
               SET autor = "Jesuly"
               WHERE id = 3
''')

cursor.execute('''
DELETE FROM libros WHERE titulo = "1984"
''')
conexion.close()