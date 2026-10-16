
IS_RUNNING = True

MENU = '''
1. PEDIR CUANTOS PAQUETES A INGRESAR
2. REGISTRAR PAQUETES
3. SALIR
'''

while IS_RUNNING:
    print(MENU)
    OPCION = input("Ingrese su opción: ")

    if OPCION == "1":
        print("HAS SELECIONADO OPCION 1")

        while True:
            # VALIDO LA CANTIDAD SEA POSITIVA
            try:
                CANTIDAD_PAQUETES = int(input("INGRESE CANTIDAD DE PAQUETES: "))
                if CANTIDAD_PAQUETES < 0:
                    print("!CANTIDAD INVÁLIDA!")
                else:
                    print("VALOR VALIDO")
                    break
            except ValueError:
                print("¡INGRESA UN VALOR ENTERO POSITIVO!")
            except Exception:
                print("OCURRIÓ UN ERROR INESPERADO")

    elif OPCION == "2":
        print("HAS ELEGIDO LA OPCION 2")
        # PARA CADA PAQUETE DEBO PEDIR
        CODIGO = ""
        while True:
            CODIGO = input("INGRESE CODIGO: (DEBE COMENZAR CON CHI Y DEBE SER DE 8 CARACTERES)")

            if len(OPCION) == 8 and OPCION.upper().startswith("CHI"):
                print("codigo valido")




                
            else:
                print("ESCRIBE UN CODIGO VALIDO")
        

    elif OPCION == "3":
        print("GRACIAS POR VENIR!!")
        IS_RUNNING = False
    else:
        print("HAS PUESTO UNA OPCION NO VÁLIDA")