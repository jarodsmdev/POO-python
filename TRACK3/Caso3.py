class Auto:
    """Clase que representa un auto con su marca y modelo."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        """Método que devuelve una representación en cadena del auto."""
        return f"Auto: {self.marca} {self.modelo}"

    def mostrar_info(self):
        """Método que muestra la información del auto."""
        print("Auto:\nMarca:", self.marca, "\nModelo:", self.modelo)

c1 = Auto("Toyota", "Corolla")
c1.mostrar_info() # Devuelve: "Auto:\nMarca: Toyota \nModelo: Corolla"
print(c1) # Devuelve: "Auto: Toyota Corolla"
