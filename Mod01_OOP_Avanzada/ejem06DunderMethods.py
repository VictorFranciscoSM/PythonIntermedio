class Libro:
    def __init__(self, titulo, autor, año_publicacion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.paginas = paginas

    def __str__(self):
        return f"Libro {self.titulo} Autor {self.autor}, Año de publicacion {self.año_publicacion}, paginas {self.paginas}"
    
    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor}, {self.año_publicacion}, {self.paginas})"
    
l = Libro("hola", "Victor", 2015, 45)

print(str(l))
print(l)
print(repr(l))
