class CuentaBancaria:
    """Clase que representa una cuenta bancaria con atributos privados y métodos para acceder a ellos."""
    def __init__(self, nombre, saldo):
        self.__nombre = nombre # Atributo privado
        self.__saldo = saldo  # Atributo privado

    def __str__(self):
        return f"Titular: {self.__nombre}, Saldo: {self.__saldo}"

    def get_nombre(self):
        """Método getter para el nombre."""
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        """Método setter para el nombre."""
        if len(nuevo_nombre) < 2:
            print("El nombre debe tener al menos 2 caracteres.")
        self.__nombre = nuevo_nombre

    def get_saldo(self):
        """Método getter para el saldo."""
        return self.__saldo

    def depositar(self, cantidad):
        """Método para depositar dinero en la cuenta."""
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se ha depositado ${cantidad}, su nuevo saldo es ${self.get_saldo()}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        """Método para retirar dinero de la cuenta."""
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")

        if cantidad <= self.get_saldo():
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad}, su nuevo saldo es ${self.get_saldo()}")
        else:
            print("Fondos insuficientes para realizar el retiro.")

# Movimientos
cuenta = CuentaBancaria("Ana", 1000)

print(cuenta)

print(cuenta.get_nombre())

cuenta.set_nombre("Bea")
cuenta.set_nombre("Yo") # Falla

cuenta.depositar(500)
cuenta.depositar(-500) # Falla

cuenta.retirar(200)
cuenta.retirar(10000) # Falla

print("Saldo final:", cuenta.get_saldo())

"""

🧪 Ejercicio: Sistema básico de Cuenta Bancaria con encapsulamiento

En este ejercicio trabajarás con una clase que simula una cuenta bancaria utilizando el concepto de encapsulamiento en programación orientada a objetos.

La clase CuentaBancaria permite representar una cuenta con un titular y un saldo, ambos protegidos mediante atributos privados.

🎯 Objetivo

Comprender cómo funcionan los getters, setters y métodos de control para proteger y manipular datos dentro de una clase.

📌 Instrucciones

A partir de la clase CuentaBancaria, realiza las siguientes tareas:

Crea una instancia de la clase con un nombre de titular y un saldo inicial.
Muestra la información de la cuenta usando el método __str__.
Obtén el nombre del titular utilizando el método get_nombre().
Cambia el nombre del titular usando set_nombre() con un valor válido.
Intenta cambiar el nombre con un valor inválido (menos de 2 caracteres) y observa qué ocurre.
Realiza un depósito usando el método depositar().
Intenta hacer un depósito con un valor negativo y observa el manejo del error.
Realiza un retiro válido usando retirar().
Intenta retirar más dinero del disponible para verificar la validación de saldo.
Consulta el saldo final usando get_saldo().
"""


