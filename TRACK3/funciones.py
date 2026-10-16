def funcion_sin_parametros_sin_retorno():
    """Esta función no tiene parámetros y no devuelve ningún valor."""
    print("Esta función no tiene parámetros.")

def funcion_sin_parametros_con_retorno():
    """Esta función no tiene parámetros pero devuelve un valor."""
    return "Esta función no tiene parámetros pero sí tiene un valor de retorno."

def funcion_con_parametros_sin_retorno(nombre, edad):
    """Esta función tiene parámetros pero no devuelve ningún valor."""
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

def funcion_con_parametros_con_retorno(a, b):
    """Esta función tiene parámetros y devuelve un valor."""
    return a + b

def funcion_con_parametros_opcionales(nombre, edad=30):
    """Esta función tiene un parámetro opcional."""
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")