class MiPrimeraClase:
    miPrimerAtributo = 0
    miSegundoAtributo = "Hola Mundo"
    miTercerAtributo = True

class Libro:
    isbn = 1222222
    cantHojas = 1000
    autor = "Default"
    tipoTapa = "Dura"
    agotado = True

class Usuario:
    """Esta es la clase Usuario y 
    me permite representar usuarios de la vida real"""
    rut = 1231131132
    dv = 'K'
    nombre = ""
    segNombre = ""
    apellido = ""



usuario1 = Usuario()
print(type(usuario1))
print("RUT:", usuario1.rut, "-", usuario1.dv)

libro = Libro()
print(type(libro))
