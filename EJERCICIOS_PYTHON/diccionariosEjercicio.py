juegos={
    "Red dead redemption":37990,
    "Clair Obscur: Expedition 33":24990,
    "Hollow Knight":15990,
    "Baldurs gate":42990,
    "Nioh 3":39990
    }


# Accedemos al valor atraves de la key
precio = juegos["Baldurs gate"]

print(precio)

# formaPago = input("Ingrese forma de pago")

# if formaPago == "tarjeta":
#     aumento = 0.4
#     aumentPrecio = precio * aumento
#     precioFinal = precio + aumentPrecio
#     print(precioFinal)
print("*"*10)

# for i in juegos:
#     print(i, juegos[i])

# Mostrar los elementos que sean mayor a 37990
# for i in juegos:
#     precio = juegos[i] # aca se obtiene el prcio del juego a traves de la llave
#     if  precio > 37990:
#         print(i, juegos[i])


# # Agregar valores
# juegos["GTA IV"] = 0

# # Editar valor
# juegos["GTA IV"] = 80000

# # Recorrer diccionarios por valor
# for valor in juegos.values():
#     print(valor)

# Recorrer diccionarios por key and values
for k,v in juegos.items():
    print(f"Key: {k} Value: {v}")

print(juegos)
