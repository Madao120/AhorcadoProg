import random

class ModosDeJuego:
    def __init__(self, pokedex):
        self.pokedex = pokedex

    def seleccionar_modo(self):
        print("\n📜 MODOS DE JUEGO 📜")
        print("1. Modo Clásico (Todos los Pokémon)")
        print("2. Modo por Tipo")
        print("3. Modo por Generación")
        print("4. Modo Doble Tipo")
        print("5. Modo Experto (Sin Pistas)")
        print("6. Modo Contrarreloj")
        print("7. Modo Aleatorio con Dificultad")

        opcion = input("Selecciona un modo de juego (1-7): ")
        return opcion

    def aplicar_filtro(self, modo):
        if modo == "2":
            tipo = input("Elige un tipo de Pokémon: ").capitalize()
            return [p for p in self.pokedex if tipo in p["tipo"]]
        elif modo == "3":
            generacion = input("Elige una generación (Ej: Kanto, Johto, Hoenn): ").lower()
            return [p for p in self.pokedex if p["generacion"].lower() == generacion]
        elif modo == "4":
            return [p for p in self.pokedex if len(p["tipo"]) > 1]
        elif modo == "5":
            return self.pokedex  # Se desactivarán pistas en `Juego`
        elif modo == "6":
            return self.pokedex  # Se agregará un temporizador en `Juego`
        elif modo == "7":
            dificultad = input("Elige una dificultad (fácil/normal/difícil): ").lower()
            if dificultad == "fácil":
                return [p for p in self.pokedex if p["numero"] < 151]  # Solo Kanto
            elif dificultad == "difícil":
                return [p for p in self.pokedex if p["numero"] > 500]  # Pokémon menos conocidos
            else:
                return self.pokedex
        else:
            return self.pokedex  # Modo Clásico (todos los Pokémon)