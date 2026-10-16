class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def __str__(self):
        return f"Persona: {self.__nombre}, Edad: {self.__edad}"

# Crear una instancia de Persona
persona1 = Persona("Juan", 30)

# Mostrar pon terminal
print(persona1)

# Intentar modificar nombre
persona1.__nombre = "Carlos"

print(persona1)