inventario = [
    {'comida': 'Fideos', 'precio': 80000, 'is_cold': False},
    {'comida': 'Arroz', 'precio': 50000, 'is_cold': False},
    {'comida': 'Puré', 'precio': 40000, 'is_cold': True},
]

for diccionario in inventario:
    for llave, valor in diccionario.items():
        print(llave, valor)


# def buscar_precio_comida(nombre_comida):
#     """Función que permite buscar el precio de una comida"""
#     for diccionario in inventario:
#         if diccionario["comida"].lower() == nombre_comida.lower():
#             return diccionario["precio"]
#     return None

# def es_numero(valor):
#     """Función que comprueba si el valor ingresado se puede convertir en Entero"""
#     try:
#         int(valor)
#         return True
#     except ValueError:
#         return False


# # -------- CÓDIGO PRINCIPAL ----------
# while True:
#     print("")
#     print("---MENU---")
#     print("")
#     print("1. Ingrese nombre de la comida a buscar")
#     print("2. Validar si es un numero o no")
#     print("0. Salir")
#     opcion = input("Ingrese su opcion: ")
#     if opcion == '0':
#         print("-- PROGRAMA FINALIZADO ---")
#         break
#     elif opcion == '1':
#         comida = input("Ingrese nombre la comida a buscar: ")
#         precio = buscar_precio_comida(comida)
#         if precio is not None:
#             print(f"El precio de {comida} es {precio}")
#         else:
#             print(f"La comida {comida} no está registrada")
#     elif opcion == '2':

#         comparar = input("Ingrese el valor a validar: ")
#         if es_numero(comparar) == True:
#             print("Es un número")
#         else:
#             print("No es un numero")
#     else:
#         print("[!] Opción no válida, Reintente")