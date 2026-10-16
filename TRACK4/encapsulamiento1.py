class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Creamos una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Imprimimos la información de la persona
print(persona1)  # Devuelve: "Nombre: Juan, Edad: 30"


# Modificamos el atributo 'nombre' directamente
persona1.nombre = "Carlos"

# Imprimimos la información de la persona después de modificar el nombre
print(persona1)  # Devuelve: "Nombre: Carlos, Edad: 30"