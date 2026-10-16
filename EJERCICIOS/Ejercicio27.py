"""
Realiza operaciones básicas con conjuntos union e intersección
"""

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión
union = conjunto1.union(conjunto2) # o conjunto1 | conjunto2
print("Unión:", union)

# Intersección
interseccion = conjunto1.intersection(conjunto2) # o conjunto1 & conjunto2
print("Intersección:", interseccion)