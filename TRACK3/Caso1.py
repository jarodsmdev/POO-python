class Persona:
    def __init__(self, rut, nombre, apellido, edad):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido}, RUT: {self.rut}, Edad: {self.edad}"

persona1 = Persona("12345678-9", "Juan", "Perez", 30)
persona2 = Persona("98765432-1", "Ana", "Gómez", 25)

print(f"Nombre: {persona1.nombre} {persona1.apellido}, RUT: {persona1.rut}, Edad: {persona1.edad}")
print(f"Nombre: {persona2.nombre} {persona2.apellido}, RUT: {persona2.rut}, Edad: {persona2.edad}")

# Modificar atributos
persona1.nombre = "Eduardo"
print(persona1)

# Mostrar el cambio
print(f"Nombre modificado: {persona1.nombre} {persona1.apellido}, RUT: {persona1.rut}, Edad: {persona1.edad}")