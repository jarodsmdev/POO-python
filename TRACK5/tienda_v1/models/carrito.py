"""Módulo para manejar el carrito de compras."""

from models.producto import Producto

class Carrito:
    """Clase para manejar el carrito de compras."""
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        """Agrega un producto al carrito y actualiza el stock del producto."""
        try:
            if producto.stock <= 0:
                raise ValueError(f"No hay stock disponible de {producto.nombre}.")
            self.productos.append(producto)
            producto.actualizar_stock(-1)
        except ValueError as e:
            print(e)

    def eliminar_producto(self, producto: Producto):
        """Elimina un producto del carrito y actualiza el stock del producto."""
        if producto in self.productos:
            self.productos.remove(producto)
            producto.actualizar_stock(1)

    def calcular_total(self):
        """Calcula el total del carrito sumando el precio de cada producto."""
        total = 0

        for producto in self.productos:
            precio = producto.precio
            total = total + precio
        return total

    def mostrar_carrito(self):
        """Muestra los productos en el carrito."""
        if not self.productos:
            print("El carrito está vacío.")
            return

        for p in self.productos:
            print(p)
