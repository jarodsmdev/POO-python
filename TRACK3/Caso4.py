class Perro:
    """Clase que representa un perro con su nombre."""
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        """Método que devuelve una representación en cadena del perro."""
        return f"Perro: {self.nombre}"
    
    def ladrar(self):
        """Método que devuelve el sonido del ladrido del perro."""
        return "¡Guau!"

    def comer(self, comida):
        """Método que devuelve una frase indicando que el perro está comiendo."""
        return f"{self.nombre} está comiendo {comida}."
    
perro1 = Perro("Rex")
print(perro1)  # Devuelve: "Perro: Rex"
print(perro1.ladrar())  # Devuelve: "¡Guau!"
print(perro1.comer("croquetas"))  # Devuelve: "Rex está comiendo croquetas."

perro2 = Perro("Luna")
print(perro2)  # Devuelve: "Perro: Luna"
print(perro2.ladrar())  # Devuelve: "¡Guau!"
print(perro2.comer("huesos"))  # Devuelve: "Luna está comiendo huesos."