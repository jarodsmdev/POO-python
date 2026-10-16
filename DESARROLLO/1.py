"""
En la programación estructurada vs POO

En la programación estructurada, para representar un producto, se podrían usar variables suueltas, que si bien, pueden funcionar, no son tan eficientes ni organizadas como una clase en POO. Por ejemplo, para representar un producto, se podrían usar variables como:

# Programación estructurada

"""

producto1_codigo = 1
producto1_nombre = "Producto 1"
producto1_precio = 100

producto2_codigo = 2
producto2_nombre = "Producto 2"
producto2_precio = 200

"""
Luego para calcular el total, se tendría que escribir una función que reciba el precio y la cantidad, lo cual puede ser propenso a errores si no se manejan correctamente los datos.

"""

def calcular_total(precio, cantidad):
    return precio * cantidad

total1 = calcular_total(producto1_precio, 5)
total2 = calcular_total(producto2_precio, 10)

print("Total Producto 1:", total1)
print("Total Producto 2:", total2)

"""
Esto puede volverse complicado y difícil de mantener a medida que se agregan más productos o atributos. En cambio, con la programación orientada a objetos (POO), se puede crear una clase Producto que encapsule todos los atributos y métodos relacionados con un producto, lo que hace el código más organizado, reutilizable y fácil de mantener.
"""

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def calcular_total(self, cantidad):
        return self.precio * cantidad
    
p1 = Producto(1, "Producto 1", 100)
p2 = Producto(2, "Producto 2", 200)
p3 = Producto(3, "Producto 3", 300)
p4 = Producto(4, "Producto 4", 400)
p5 = Producto(5, "Producto 5", 500)

total1 = p1.calcular_total(5)
total2 = p2.calcular_total(10)
total3 = p3.calcular_total(15)
total4 = p4.calcular_total(20)
total5 = p5.calcular_total(25)
