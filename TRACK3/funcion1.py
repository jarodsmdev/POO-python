"""Ejemplo de funciones en Python."""
def saludar():
    """Función que imprime un saludo genérico."""
    print("Hola")

saludar() # Hola
saludar() # Hola

def obtener_numero():
    """Función que devuelve un número."""
    return 10

def sumar(a, b):
    """Función que suma dos números y devuelve el resultado."""
    return a + b

def saludo(nombre="invitado"):
    """Función que saluda a una persona por su nombre, con un valor por defecto."""
    print("Hola", nombre)
