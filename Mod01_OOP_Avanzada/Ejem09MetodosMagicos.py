class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __repr__(self):
        return f"Producto({self.nombre}), Precio: {self.precio}, Cantidad: {self.cantidad}"
    
    def __eq__(self, other):
        return self.nombre == other.nombre
    
    def __lt__(self, other):
        return self.precio < other.value
    
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def __getitem__(self, nombre):
        return self.productos.get(nombre, "Producto no encontrado")
    
    def __setitem__(self, nombre, producto):
        self.productos[nombre] = producto
    
    def __delitem__(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
        else:
            print("Producto no encontrado para eliminar")
    
    def __iter__(self):
        self._productos_iter = iter(self.productos.values())
        return self
    
    def __next__(self):
        return next(self._productos_iter)
    
    def __call__(self, nombre):
        return self.__getitem__(nombre)
    
    def valor_total(self):
        return sum(p.precio * p.cantidad for p in self.productos.values())

p1 = Producto("Laptop", 6000, 5)
p2 = Producto("Teclado", 600, 2)
p3 = Producto("Mouse", 300, 4)

inventario = Inventario()
inventario["Laptop"] = p1
inventario["Teclado"] = p2
inventario["Mouse"] = p3

print(inventario["Laptop"])

inventario["Laptop"] = Producto("Laptop", 140, 1)

for producto in inventario:
    print(producto)

print(inventario["Laptop"])

del inventario["Mouse"]
for producto in inventario:
    print(producto)

print(inventario("Teclado"))

print("Valor total: ", inventario.valor_total())