# Declaracion de una lista
notas = []
is_running = True

while is_running:

    while True:
        opcion = input("[+] Ingresa una nota: \n'salir' para escapar: ")
        try:
            if opcion.lower() == 'salir':
                print("Has salido con exito")
                is_running = False
                break

            # Intenta hacer la conversion
            opcion = int(opcion)

            if opcion < 0:
                raise ValueError
            # Agregar nota valida a la lista
            print("Has ingresado el numero", opcion)
            notas.append(opcion)
            #break
        except ValueError:
            print("Ha ocurrido un error, Pusiste un valor invalido")
        except Exception:
            print("Ha ocurrido un error")

for i in notas:
    print(f"Nota : {i}")


print("Suma:", sum(notas))
print("Promedio: ", sum(notas)/len(notas))

notasSort = []
notasSort = notas.copy() # Copia el contenido de la lista, sin el 'enlace' a la referencia de memoria
notasSort.sort()
print("Lista Ordenada: ", notasSort)

notasReverse = []
notasReverse = notas.copy() # Copia el contenido de la lista, sin el 'enlace' a la referencia de memoria
notasReverse.reverse()

print("Lista Invertida: ", notasReverse)
print(int(8.5))
print(notas)