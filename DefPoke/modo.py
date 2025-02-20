import random
import json

class Modo:
    def __init__(self, json_file):
        self.opcion = int
        self.respuesta = int
        self.pokedex = list
        with open(json_file, "r", encoding="utf-8") as file:
            self.pokedex = json.load(file)

    def seleccionar_modo(self):                                                         # Selecciona el modo de juego que se muestran en vista y se responde del 1 al 7
        while True:
            try:
                self.respuesta = int(input("Elige el modo de juego (1-7): "))
                if 1 <= self.respuesta <= 7:
                    return self.respuesta
                else:
                    print("Número fuera de rango. Debe estar entre 1 y 7.")             # Si el número no está entre 1 y 7, se imprime el mensaje de error
            except ValueError:
                print("Por favor, introduce un número válido.")

    def aplicar_modo(self, modo):                                            # Aplica el modo de juego seleccionado, aquí es donde se escojerá el pokemon                               
        if modo == 1:  # Modo clásico
            return [random.choice(self.pokedex)]
        elif modo == 2:  # Modo por tipo
            tipo = input("Escoge un tipo de Pokémon: ").lower()
            return [random.choice([p for p in self.pokedex if tipo in p["tipo"]]), tipo]    # Se devuelve el pokemon según el tipo escogido y se deuvuelve el tipo para que posteriormente en las pistas no haya redundancias, ya que aquí se escoje el tipo independientemente de que sea le principal o no, por lo que en las pistas a mostrar es conveniente tener tipo como variable
        elif modo == 3:  # Modo por generación
            generacion = input("Escoge la generación del Pokémon: ").lower()                
            return [random.choice([p for p in self.pokedex if generacion in p["generacion"]])]  # Se devuelve el pokemon según la generación escogida
        elif modo == 4:  # Modo doble tipo
            return [random.choice([p for p in self.pokedex if len(p["tipo"]) > 1])]             # Se devuelve el pokemon que tenga más de un tipo
        elif modo == 5:  # Modo populares
            return [random.choice([p for p in self.pokedex if p["numero"] < 650])]              # Se devuelve el pokemon que tenga un número menor a 650
        elif modo == 6:  # Modo impopulares
            return [random.choice([p for p in self.pokedex if p["numero"] > 649])]              # Se devuelve el pokemon que tenga un número mayor a 649
        elif modo == 7:  # Modo sin pistas
            return [random.choice(self.pokedex)]  

    def escoger_pistas(self, pokemon_info, modo):
        pistas = []
        if modo in [1, 2, 4, 5, 6]: # Modo clásico, por tipo, doble tipo, populares e impopulares
            pistas.append(pokemon_info['tipo'][0])
            pistas.append(pokemon_info['generacion'])
            pistas.append(pokemon_info['tipo'][1] if len(pokemon_info['tipo']) > 1 else "No tiene tipo secundario")
        elif modo == 3: # Modo por generación, cambia el orden de las pistas
            pistas.append(pokemon_info['generacion'])
            pistas.append(pokemon_info['tipo'][0])
            pistas.append(pokemon_info['tipo'][1] if len(pokemon_info['tipo']) > 1 else "No tiene tipo secundario")
        return pistas


