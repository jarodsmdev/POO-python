"""
Crear una clase llamada Producto con los siguientes atributos:
- codigo
- nombre
- precio
Crea su constructor y una función llamada calcular total que reciba la cantidad y devuelva el precio total.
"""

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return "Codigo: " + str(self.codigo) + ", Nombre: " + self.nombre + ", Precio: " + str(self.precio)

    def calcular_total(self, unidades):
        return self.precio * unidades

p1 = Producto(1, "Producto 1", 100)
p2 = Producto(2, "Producto 2", 200)
p3 = Producto(3, "Producto 3", 300)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(5))
print(p2.calcular_total(10))
print(p3.calcular_total(15))
