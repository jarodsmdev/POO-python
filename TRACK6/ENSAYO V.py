def menu():
    menu = """
        MENÚ BODEGA
        1. Registrar producto
        2. Aumentar stock
        3. Vender producto
        4. Buscar producto por código
        5. Ver productos con bajo stock
        6. Mostrar valorización total de la bodega
        7. Salir
    """
    print(menu)

def validarCodigo(codigo):

    if len(codigo.strip()) >= 5:
        return True
    else:
        print("Código debe ser mayor de 4 caracteres")
        return False

def validarNombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    else:
        print("Nombre no puede estar vacío")
        return False

# def esNumero(valor: str):
#     valor.isnumeric()

def esNumero(valor):
    try:
        int(valor)
        return True
    except Exception:
        return False

def validarStock(stock):
    if esNumero(stock):
        if int(stock) >= 0:
            return True
    else:
        print("El stock debe ser número entero y debe ser positivo")
        return False
    
def validarPrecio(precio):
    if esNumero(precio) and precio > 0:
        return True
    else:
        print("El precio debe ser número entero y mayor a cero")
        return False

def registrarProducto(listaProductos):
    codigo = input("Ingrese codigo: ")
    nombre = input("Ingrese nombre: ")
    stock = input("Ingrese stock: ")
    precio = input("Ingrese precio: ")

    if validarCodigo(codigo) and validarNombre(nombre) and validarStock(stock) and validarPrecio(precio):

        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "stock": stock,
            "precio": precio
        }

        listaProductos.append(producto)


# ---------PROGRAMA PRINCIPAL --------
productos = []


while True:
    menu()
    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("Registrar producto: ")
            registrarProducto(productos)
            print(productos)
        elif opcion == 2:
            print("Aumentar stock")
        elif opcion == 3:
            print("Vender producto")
        elif opcion == 4:
            print("Buscar producto por codigo")
        elif opcion == 5:
            print("Ver productos con bajo stock")
        elif opcion == 6:
            print("Mostrar valorización total de la bodega")
        else:
            print("Salir")
            break
    except ValueError:
        print("Opción no válida")
    # except Exception:
    #     print("Ocurrió un error no controlado")


