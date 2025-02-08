import random
import json

class Modo:
    def __init__(self, json_file):
        self.opcion = int
        self.respuesta = int
        self.pokedex = list
        with open(json_file, "r", encoding="utf-8") as file:
            self.pokedex = json.load(file)

    def seleccionar_modo(self):
        while True:
            try:
                self.respuesta = int(input("Elige el modo de juego (1-7): "))
                if 1 <= self.respuesta <= 7:
                    return self.respuesta
                else:
                    print("Número fuera de rango. Debe estar entre 1 y 7.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def aplicar_modo(self, modo):        
        if modo == 1:  # Modo clásico
            return [random.choice(self.pokedex)]
        elif modo == 2:  # Modo por tipo
            tipo = input("Escoge un tipo de Pokémon: ").lower()
            return [random.choice([p for p in self.pokedex if tipo in p["tipo"]]), tipo]
        elif modo == 3:  # Modo por generación
            generacion = input("Escoge la generación del Pokémon: ").lower()
            return [random.choice([p for p in self.pokedex if generacion in p["generacion"]])]
        elif modo == 4:  # Modo doble tipo
            return [random.choice([p for p in self.pokedex if len(p["tipo"]) > 1])]
        elif modo == 5:  # Modo populares
            return [random.choice([p for p in self.pokedex if p["numero"] < 650])]
        elif modo == 6:  # Modo impopulares
            return [random.choice([p for p in self.pokedex if p["numero"] > 649])]
        elif modo == 7:  # Modo sin pistas
            return [random.choice(self.pokedex)]

    def escoger_pistas(self, pokemon_info, modo):
        pistas = []
        if modo in [1, 2, 4, 5, 6]:  # Modo clásico, por tipo, doble tipo, populares e impopulares
            pistas.append(pokemon_info['tipo'][0])
            pistas.append(pokemon_info['generacion'])
            pistas.append(pokemon_info['tipo'][1] if len(pokemon_info['tipo']) > 1 else "No tiene tipo secundario")
        elif modo == 3:  # Modo por generación, cambia el orden de las pistas
            pistas.append(pokemon_info['generacion'])
            pistas.append(pokemon_info['tipo'][0])
            pistas.append(pokemon_info['tipo'][1] if len(pokemon_info['tipo']) > 1 else "No tiene tipo secundario")
        return pistas

    # def aplicar_pistas(self, modo, intentos, pistas_mostradas, pistas_sin_mostrar):
    #     if modo in [1, 4, 5, 6]:  # Modo clásico, doble tipo, populares e impopulares
    #         if intentos == 4:
    #             pistas_mostradas.append(pistas_sin_mostrar[0])
    #         elif intentos == 2:
    #             pistas_mostradas.append(pistas_sin_mostrar[1])
    #         elif intentos == 1:
    #             pistas_mostradas.append(pistas_sin_mostrar[2])
    #     elif modo in [2, 3]:  # Modo por tipo y generación
    #         if intentos == 5:
    #             pistas_mostradas.append(pistas_sin_mostrar[0])
    #         elif intentos == 3:
    #             pistas_mostradas.append(pistas_sin_mostrar[1])
    #         elif intentos == 1:
    #             pistas_mostradas.append(pistas_sin_mostrar[2])
    #     return pistas_mostradas


