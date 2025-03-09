class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
    
punto1 = Punto(2,3)
punto2 = Punto(2,3)
punto3 = Punto(1,3)

print( punto1 == punto2)
print( punto1 < punto2)