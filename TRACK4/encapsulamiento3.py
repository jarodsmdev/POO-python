class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    def get_nombre(self):
        """Método getter para el nombre."""
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        """Método setter para el nombre."""
        if len(nuevo_nombre) < 2:
            print("[!] El nombre debe tener al menos 2 caracteres.")
            return
        self.__nombre = nuevo_nombre

    def get_edad(self):
        """Método getter para la edad."""
        return self.__edad

    def set_edad(self, nueva_edad):
        """Método setter para la edad."""
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa.")

# Creamos una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Imprimimos la información de la persona
print(persona1)  # Devuelve: "Nombre: Juan, Edad: 30"

# Modificamos el nombre utilizando el método setter
persona1.set_nombre("a")

# Imprimimos la información de la persona después de modificar el nombre
print(persona1)  # Devuelve: "Nombre: Carlos, Edad: 30"

# Modificamos la edad utilizando el método setter
persona1.set_edad(35)

# Imprimimos la información de la persona después de modificar la edad
print(persona1)  # Devuelve: "Nombre: Carlos, Edad: 35"