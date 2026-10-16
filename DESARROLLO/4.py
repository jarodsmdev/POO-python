class Producto:
    codigo = 1
    nombre = "Producto 1"
    precio = 0

producto = Producto()

print(type(producto))
print(producto.codigo)
print(producto.nombre)
print(producto.precio)

print("Modificando los atributos de la instancia producto...")
# Modificando los atributos de la instancia producto

producto.nombre = "Producto 2"
producto.precio = 200

print(type(producto))
print(producto.codigo)
print(producto.nombre)
print(producto.precio)