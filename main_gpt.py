import random
import os

class Ahorcado:
    def __init__(self) -> None:
        self.pokedex = {
            "bulbasaur": {
                "name": "bulbasaur",
                "tipo": ["planta", "veneno"],
                "generacion": "kanto"
            }
        }
        self.letras_usuario = []
        self.letras_incorrectas = []  # Para guardar letras incorrectas
        self.letras_pokemon = []

    def clear_window(self):
        os.system('cls' if os.name == "nt" else "clear")

    def respuesta(self):
        res = ""
        while len(res) != 1:
            res = input("Introduce una letra\n").lower()
        return res

    def correct_word(self, pokemon):
        for letra in pokemon:
            if letra not in self.letras_pokemon:
                self.letras_pokemon.append(letra)

    def print_word(self, pokemon):
        """Muestra la palabra con las letras adivinadas y guiones bajos para las faltantes."""
        for letra in pokemon:
            if letra in self.letras_usuario:
                print(letra, " ", end="")
            else:
                print("_ ", end="")
        print()  # Salto de línea al final

    def print_incorrect_letters(self):
        """Muestra las letras incorrectas ingresadas por el usuario."""
        print("Letras incorrectas: ", ", ".join(self.letras_incorrectas))

    def play(self):
        pokemon = self.pokedex["bulbasaur"]["name"]
        self.correct_word(pokemon)
        intentos = 6

        while intentos > 0:
            self.clear_window()
            print(f"Te quedan {intentos} intentos.")
            self.print_word(pokemon)
            self.print_incorrect_letters()

            respuesta = self.respuesta()

            if respuesta in self.letras_usuario:
                print("Ya ingresaste esa letra.")
                input("Presiona Enter para continuar...")
                continue

            self.letras_usuario.append(respuesta)

            if respuesta in self.letras_pokemon:
                print("¡Correcto!")
            else:
                print("Incorrecto.")
                self.letras_incorrectas.append(respuesta)
                intentos -= 1

            if all(letra in self.letras_usuario for letra in pokemon):
                self.clear_window()
                print(f"¡Felicidades! Adivinaste la palabra: {pokemon}")
                break
        else:
            self.clear_window()
            print(f"Perdiste. La palabra era: {pokemon}")

game = Ahorcado()
game.play()