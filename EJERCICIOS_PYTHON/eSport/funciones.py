def saludar():
    print("Hola equipo")

def saludar2(mensaje):
    print(mensaje)

def saludar3(mensaje):
    return "Hola " + mensaje

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def division(a, b):
    # if b == 0:
    #     print("No puedes div por cero")
    # else:
    #     return a / b
    
    if b != 0:
        return a /b


# Ejecutar mi funcion
# saludar()
# saludar2("Bienvenidos equipo gracias por asistir")
# mensaje = saludar3("Bienvenidos todos y todas")

# lista = []
# lista.append(mensaje)

# print(lista)

# print(sumar(2,2))
# print(division(2,0))

def menu():
    opciones = """
    "1. opcion 1"
    "2. opcion 2"
    "3. opcion 3"
    "4. opcion 4"
    "5. opcion 5"
    """
    return opciones

def inputString(opcion):
    return input(opcion)

def inputInteger(opcion):
    try:
        valor = int(input(opcion))
        return valor
    except Exception as e:
        print(e)


# while True:
#     print(menu())
#     op = inputString("Ingrese una opcion")

#     if op == '0':
#         break

inputInteger("Ingrese un numero")