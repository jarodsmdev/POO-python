# Ejemplo de una clase en Python
class Persona:
    """Clase que representa a una persona con un nombre y una edad."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar_a(self, otra_persona):
        """Método que devuelve un saludo dirigido a otra persona."""
        return f"Hola {otra_persona.nombre}, soy {self.nombre}."

    def saludar(self):
        """Método que devuelve un saludo con el nombre y la edad de la persona."""
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
# Ejemplo de uso
persona1 = Persona("Ana", 25)
saludo = persona1.saludar()
print(saludo)  # Devuelve: "Hola, mi nombre es Ana y tengo 25 años."
persona1.saludar_a("Carlos")  # Devuelve: "Hola Carlos, soy Ana."