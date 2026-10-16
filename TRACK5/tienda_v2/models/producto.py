"""Módulo para manejar los productos de la tienda."""

class Producto:
    def __init__(self, id:int, nombre:str, precio:float, stock:int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio}  (Stock: {self.stock})"

    def actualizar_stock(self, cantidad:int):
        """Actualiza el stock del producto. La cantidad puede ser positiva (para agregar stock) o negativa (para reducir stock)."""
        if self.stock + cantidad < 0:
            raise ValueError(f"No hay suficiente stock de {self.nombre} para esta operación.")
        self.stock += cantidad