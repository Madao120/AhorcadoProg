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

        self.opcion = input("Selecciona un modo de juego (1-7): ")
        return self.opcion

    def aplicar_filtro(self, modo):
        if modo == "2":
            tipo = input("Elige un tipo de Pokémon: ").lower()
            return [p for p in self.pokedex if tipo in p["tipo"]]
        elif modo == "3":
            generacion = input("Elige una generación (Ej: Kanto, Johto, Hoenn): ").lower()
            return [p for p in self.pokedex if p["generacion"].lower() == generacion]
        elif modo == "4":
            return [p for p in self.pokedex if len(p["tipo"]) > 1]
        elif modo == "5":
            return [p for p in self.pokedex if p["numero"] < 650]  # Dará solo Pokemon de la 5º Gen para abajo
        elif modo == "6":
            return self.pokedex  # Se agregará un temporizador en `Juego(falta por incorporar)`
        elif modo == "7": # Modo sin pistas
            return self.pokedex 
        else:
            return self.pokedex  # Modo Clásico (todos los Pokémon)
# Activar las pistas según true and false, pista1 = True, pero si escojemos solo tipo fuego ej pista1 y 3 False, pero la 2 (generación) = True