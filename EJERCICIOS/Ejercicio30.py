"""
Elimina duplicados de una lista
"""

# Creamos una lista con elementos duplicados
lista1 = [1, 2, 3, 4, 5, 1, 2, 3]

# Eliminamos los duplicados utilizando set() y convertimos el resultado de nuevo a una lista
sinDuplicados = list(set(lista1))

# Imprimimos la lista sin duplicados
print(sinDuplicados)