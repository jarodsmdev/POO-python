class Videojuego:
    def __init__(self, nombre, plataforma, anio):
        self.nombre = nombre
        self.plataforma = plataforma
        self.anio = anio
        self.horas_jugadas = 0

# Crear videojuegos
juego1 = Videojuego("Minecraft", "PC", 2011)
juego2 = Videojuego("The Legend of Zelda", "Nintendo", 2017)
juego3 = Videojuego("FIFA 24", "PlayStation", 2023)

# Mostrar datos iniciales
print("=== DATOS INICIALES ===")
print(f"{juego1.nombre} - {juego1.plataforma} - {juego1.anio} - {juego1.horas_jugadas} horas")
print(f"{juego2.nombre} - {juego2.plataforma} - {juego2.anio} - {juego2.horas_jugadas} horas")
print(f"{juego3.nombre} - {juego3.plataforma} - {juego3.anio} - {juego3.horas_jugadas} horas")

# Modificar horas jugadas del juego1
juego1.horas_jugadas = 120

print("\n=== DESPUÉS DE JUGAR ===")
print(f"{juego1.nombre} ahora tiene {juego1.horas_jugadas} horas jugadas")