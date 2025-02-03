import random

class Modo:
    def __init__(self, pokedex):
        self.pokedex = pokedex
        self.opcion = int

    def seleccionar_modo(self):
        print("\n📜 MODOS DE JUEGO 📜")
        print("1. Modo Clásico (Todos los Pokémon)")
        print("2. Modo por Tipo")
        print("3. Modo por Generación")
        print("4. Modo Doble Tipo")
        print("5. Populares")
        print("6. Modo Contrarreloj")
        print("7. Modo Expero (Sin Pistas)")

