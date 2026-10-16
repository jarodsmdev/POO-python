"""
Verifica si una palabra es un palindromo. Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando los espacios y las mayúsculas.
"""

palabra = "radar"

invertida = palabra[::-1]

esPalindromo = palabra == invertida

if esPalindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
