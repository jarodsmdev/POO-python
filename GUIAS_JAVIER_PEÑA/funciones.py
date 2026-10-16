def suma(listaNumeros):
    """ESTA ES UNA FUNCION PARA SUMAR LISTAS"""
    acumulador = 0
    for i in listaNumeros:
        #acumulador = i + acumulador
        acumulador += i
    return acumulador

def sumar(num1, num2):
    return num1 + num2

def multiplicar(a, b):
    return a * b

def porcentajeDeAlgo(porcentaje, total):
    return (porcentaje/100) * total #0.5/100

def treinaPorCientoDe(total):
    print( (30/100) * total)

def cuentaRegresiva(numero):
    for i in range(numero, -1, -1):
        print(i)

def menu():
    print("---------------------------")
    print("MENU")
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    op = opcion = input("Ingrese una opcion")
    return op

# --------------programa principal-------------------------
numeros = [1, 2, 3, 4]

resultado = suma(numeros)
print(resultado)

print(sumar(100,8))
print(multiplicar(7,9))
porcentaje = porcentajeDeAlgo(30,100)# asi se va a usar
print( (sumar(4,5) + porcentaje))

treinaPorCientoDe(90) # sin retorno

cuentaRegresiva(90)

op = menu()
try:
    op = int(op) #'9'
    print(sumar(op, 9))
except Exception:
    print("VAlor no permitido")
