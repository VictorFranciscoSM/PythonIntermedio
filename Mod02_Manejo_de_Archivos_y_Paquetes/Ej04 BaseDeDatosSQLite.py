import sqlite3

conexion = sqlite3.connect("Mod02_Manejo_de_Archivos_y_Paquetes/Ej04_Libros.db")
cursor = conexion.cursor()

"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS libros(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT, 
               autor TEXT NOT NULL,
               ano_publicacion INTEGER
               )
''')
"""

cursor.execute('''
INSERT INTO libros (titulo, autor, ano_publicacion)
               VALUES("El alquimista", "Paulo Coelho", 1988)
''')
cursor.execute('''
INSERT INTO libros (titulo, autor, ano_publicacion)
               VALUES("1984", "George", 1945)
''')
cursor.execute('''
INSERT INTO libros (titulo, autor, ano_publicacion)
               VALUES("El viento se llevo", "Adriana", 2012)
''')

conexion.commit()

conexion.close()