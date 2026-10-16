"""
Combina dos listas en pares usando la función zip() y muestra el resultado.
"""

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

# Combinar las listas en pares usando zip()
pares = list(zip(lista1, lista2))

print("Pares combinados:", pares)