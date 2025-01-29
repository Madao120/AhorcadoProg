import json
import random

class Panel:
    def __init__(self, json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            self.pokedex = json.load(file)

    def obtener_pokemon_aleatorio(self):
        return random.choice(self.pokedex)