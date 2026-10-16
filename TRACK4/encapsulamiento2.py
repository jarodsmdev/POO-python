class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

# Creamos una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Imprimimos la información de la persona
print(persona1)  # Devuelve: "Nombre: Juan, Edad: 30"

# Intentamos modificar el atributo 'nombre' directamente (esto no funcionará debido al encapsulamiento)
persona1.__nombre = "Carlos"

# Imprimimos la información de la persona después de intentar modificar el nombre
print(persona1)  # Devuelve: "Nombre: Juan, Edad: 30" (el nombre no ha cambiado debido al encapsulamiento)

persona1._Persona__nombre = "Pedro"

print(persona1)  # Devuelve: "Nombre: Pedro, Edad: 30" (el nombre ha cambiado utilizando el nombre mangled)