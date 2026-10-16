class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

p1 = Producto(1, "Producto 1", 100)
p2 = Producto(2, "Producto 2", 200)
print(type(p1))
print(p1.codigo)
print(p1.nombre)
print(p1.precio)

print(type(p2))
print(p2.codigo)
print(p2.nombre)
print(p2.precio)