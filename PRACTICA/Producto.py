class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}"
        

producto = Producto(1, "Manjar", 5000)

print(producto)
print(producto.nombre)
print(producto.codigo)
print(producto.precio)