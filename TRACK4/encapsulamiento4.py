class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    @property
    def nombre(self):
        """Método getter para el nombre."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Método setter para el nombre."""
        if len(nuevo_nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        """Método getter para la edad."""
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
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
persona1.nombre = "Carlos"
