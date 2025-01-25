import random, os
class Ahorcado:
    def __init__(self) -> None:
        self.pokedex = {
            "bulbasaur": {
                "name": "bulbasaur",
                "tipo": ["planta", "veneno"],
                "generacion": "kanto"
            }
        }
        self.usuario = str
        self.contraseña = str
        self.letras_usuario = []
        self.letras_pokemon = []

    def clear_window(self):
        os.system('cls' if os.name == "nt" else "clear")

    def respuesta(self):
        res = ""
        while len(res) != 1:
            res = input("Introduce una letra\n")
        return res

    def correct_word (self, pokemon):
        for i in pokemon:
            if i not in self.letras_pokemon:
                self.letras_pokemon.append(i)
            
    def print_word(self, pokemon):
        for i in range(len(pokemon)):
            if pokemon[i] in self.letras_usuario:
                print(pokemon[i], " ", end="")
            else:
                print("_ ", end="")

    def play(self):
        self.correct_word(self.pokedex["bulbasaur"]["name"])
        while True:
            self.clear_window()
            self.print_word(self.pokedex["bulbasaur"]["name"])
            respuesta = self.respuesta()
            self.letras_usuario.append(respuesta)
            for i in self.letras_usuario:
                if i not in self.letras_pokemon:
                    print(i, end="")

game = Ahorcado()
Ahorcado.play(game)



# pokemon = random.choice(self.pokedex))

