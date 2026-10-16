listaContacto = []

while True:
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese Teléfono: ")

    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }

    # Validar que el nombre no está repetido
    repetido = False
    for i in listaContacto:
        if i["nombre"] == nombre:
            print(f"Nombre: '{nombre}' ya existe")
            repetido = True
            break

    if repetido is False:
        listaContacto.append(contacto)

    print(listaContacto)

    # Cambiar nombre de un contacto
    nombreBuscado = input("Ingrese el nombre a cambiar: ")

    for i in listaContacto:
        if i["nombre"] == nombreBuscado:
            nombreNuevo = input("Ingrese el nombre nuevo: ")
            #Actualizar el nombre
            i["nombre"] = nombreNuevo
            print("Se ha actualizado el nombre corretamente")

    r = input("¿Desea seguir ingresando contactos? s/n").lower()

    if r == "n":
        break