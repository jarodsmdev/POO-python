juegos={"Red dead redemption":37990,"Clair Obscur: Expedition 33":24990,"Hollow Knight":15990,"Baldurs gate":42990,"Nioh 3":39990}
canasta = []
totalCanasta = 0
while True:
    print("==BIENVENIDO A STEAM==")
    print("1.- Agregar Juegos \n2.- Ver carrito \n3.- Ver total \n4.- Salir")

    while True:
        try:
            opc= int(input("Elija la opción deseada: "))
            break
        except ValueError:
            print("Ingrese una opcion válida")

    match opc:
        case 1:
            while True:
                try:
                    print("1.- Red dead redemption $37990\n2.- Clair Obscur: Expedition 33 $24990\n3.- Hollow Knight $15990\n4.- Baldurs gate $42990\n5.- Nioh 3 $39990\n0.- Volver al menu principal")
                    choice=int(input("Ingrese el número del juego que desea agregar al carrito: "))
                    break
                except ValueError:
                    print("Ingrese una opción válida")
            match choice:
                case 0:
                    break
                case 1:
                    print("Usted ha agregado 'Red dead redemption' a su carrito")
                    canasta.append("Red dead redemption")
                    totalCanasta += juegos["Red dead redemption"]
                case 2:    
                    print("Usted ha agregado 'Clair Obscur: Expedition 33' a su carrito")
                    canasta.append("Clair Obscur: Expedition 33")
                    totalCanasta += juegos["Clair Obscur: Expedition 33"]
                case 3:
                    print("Usted ha agregado 'Hollow Knight' a su carrito")
                    canasta.append("Hollow Knight")
                    totalCanasta += juegos["Hollow Knight"]
                case 4:
                    print("Usted ha agregado 'Baldurs gate' a su carrito")
                    canasta.append("Baldurs gate")
                    totalCanasta += juegos["Baldurs gate"]
                case 5:
                    print("Usted ha agregado 'Nioh 3' a su carrito")
                    canasta.append("Nioh 3")
                    totalCanasta += juegos["Nioh 3"]
                case _:
                    print("Ingrese una opción válida")
        case 2:
            print(f"Mostrando sus juegos en el carrito: \n{canasta}")
        case 3:
            print(f"Su total a pagar es de ${totalCanasta}")
        case 4:
            print("Gracias por comprar con nosotros")
            break
        case _:
            print("Ingrese una opción válida")