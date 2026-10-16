
def agregarProducto(lista):
    codigo = input("Ingrese codigo: ")
    nombre = input("Ingrese nombre: ")
    stock = input("Ingrese stock: ")
    precio = input("Ingrese precio: ")

    producto = {
            "codigo": codigo,
            "nombre": nombre,
            "stock": int(stock),
            "precio": int(precio),
            "estado": "NORMAL"
        }
    
    lista.append(producto)

def menu():
    menu = """
        --- MENÚ BODEGA ---
        
        1. Registrar producto
        2. Aumentar stock
        3. Vender producto
        4. Buscar producto por código
        5. Ver productos con bajo stock
        6. Mostrar valorización total de la bodega
        7. Salir
        """
    print(menu)

def buscarProducto(productos: list):
    encontrado = -1
    while True:
        codigo = input("Ingresa el código a buscar: ").strip()

        if codigo != "":

            # productos = [ {...}, {...}, {...}]
            for producto in productos:
                if producto["codigo"] == codigo:
                    encontrado =  productos.index(producto)
                    #TODO: BREAK

            if encontrado == -1:
                    print("El producto no se encuentra registrado")
            else:
                print(productos[encontrado])
            break
        else:
            print("Ingresa un valor distinto de vacío")

# ------------------programa principal --------

lista = []

while True:
    menu()
    opcion = input("Ingrese la opcion: ")

    if opcion == "1":
        print("--AGREGAR PRODUCTO--")
        agregarProducto(lista)
    elif opcion == "4":
        print("--BUSCAR PRODUCTO--")
        
        buscarProducto(lista)
        #TODO: LLAMAR A LA FUCNION PARA BUSCAR PRODUCTO
    elif opcion == "7":
        print("Programa finalizado")
        break
    else:
        print("Opción inválida")