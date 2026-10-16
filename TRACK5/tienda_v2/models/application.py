"""Módulo principal de la aplicación de la tienda."""

from TRACK5.tienda_v2.models.producto import Producto
from TRACK5.tienda_v2.models.carrito import Carrito

class Application:
    """Clase principal para ejecutar la aplicación de la tienda."""

    def mostrar_menu(self):
        """Muestra el menú de opciones al usuario."""
        print("\n--- MENÚ ---")
        print("1. Ver productos")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Ver carrito")
        print("5. Ver total")
        print("0. Salir")
        print("---------------------------------")

    def main(self):
        """Función principal que ejecuta la lógica de la aplicación."""
        producto1 = Producto(1, "Pan", 1000, 5)
        producto2 = Producto(2, "Leche", 1500, 3)
        producto3 = Producto(3, "Huevos", 3000, 2)

        lista_productos = [producto1, producto2, producto3]
        carrito = Carrito()

        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                for p in lista_productos:
                    print(f"ID: {p.id} - {p}")

            elif opcion == "2":
                id_buscar = int(input("ID: "))
                producto_encontrado = None

                for p in lista_productos:
                    if p.id == id_buscar:
                        producto_encontrado = p

                if producto_encontrado:
                    carrito.agregar_producto(producto_encontrado)
                else:
                    print("No encontrado")

            elif opcion == "0":
                break
