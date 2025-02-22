try:
    archivo = input("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no fue encontrado")
finally:    #simpre se ejecuta sin importar si paso una expcion
    archivo.close()
    print("Arhivo se a cerrado")