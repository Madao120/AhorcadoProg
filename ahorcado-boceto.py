import random, os, json
class Ahorcado:
    usuario: str
    contraseña : str
    LETRAS_USUARIO = [" ", "-"]
    letras_incorrectas : list
    letras_pokemon : list
    
    def __init__(self, json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            self.pokedex = json.load(file)

        self.letras_incorrectas = []
        self.letras_pokemon = []

    def clear_window(self): #Función para limpiar la ventana y que solo haya unas líneas limpias
        os.system('cls' if os.name == "nt" else "clear")

    def respuesta(self):
        res = ""
        while len(res) != 1:
            res = str(input("Introduce una letra\n"))
        return res

    def correct_word (self, pokemon): #Lista donde se guardarán las letras correctas, para que el programa sepa cuales son
        for i in pokemon:
            if i not in self.letras_pokemon:
                self.letras_pokemon.append(i)

    def print_letras_incorrectas(self): #Lista donde irán las letras incorrectas
        print("Letras incorrectas: ", ", ".join(self.letras_incorrectas))
            
    def print_word(self, pokemon): #Generador de palabra aleatoria, donde pondrá _ por cada letra de la palabra y sustituirá los mismos por las letras correctas en caso de que el usuario las responda
        for i in range(len(pokemon)):
            if pokemon[i] in Ahorcado.LETRAS_USUARIO:
                print(pokemon[i], " ", end="")
            else:
                print("_ ", end="")

    def play(self):
        pokemon_data = random.choice(self.pokedex)
        pokemon = pokemon_data["name"]
        self.correct_word(pokemon)
        intentos = 6

        while intentos >= 0:
            self.clear_window()
            if intentos == 6 or intentos == 5:
                print(f"Te quedan {intentos} intentos restantes.")
            if intentos == 4 or intentos == 3:
                print(f"Te quedan {intentos} intentos restantes.")
                print(f"Pista: Tipo principal del pokemon -> {pokemon_data["tipo"][0]}")
            elif intentos == 2:
                if len(pokemon_data["tipo"]) == 1:
                    print(f"Te quedan {intentos} intentos restantes.")
                    print(f"Pistas: \nTipo principal del pokemon -> {pokemon_data["tipo"][0]} \nSin tipo secundario")
                elif len(pokemon_data["tipo"]) > 1:
                    print(f"Te quedan {intentos} intentos restantes.")
                    print(f"Pistas: \nTipo principal del pokemon -> {pokemon_data["tipo"][0]} \nTipo secundario del pokemon -> {pokemon_data["tipo"][1]}")
            elif intentos == 1:
                if len(pokemon_data["tipo"]) == 1:
                    print(f"Te quedan {intentos} intento restante.")
                    print(f"Pistas: \nTipo principal del pokemon -> {pokemon_data["tipo"][0]} \nSin tipo secundario \nGeneración del Pokemon -> {pokemon_data["generacion"]}")
                elif len(pokemon_data["tipo"]) > 1:
                    print(f"Te quedan {intentos} intento restante.")
                    print(f"Pistas: \nTipo principal del pokemon -> {pokemon_data["tipo"][0]} \nTipo secundario del pokemon -> {pokemon_data["tipo"][1]} \nGeneración del Pokemon -> {pokemon_data["generacion"]}")
            elif intentos == 0:
                if len(pokemon_data["tipo"]) == 1:
                    print(f"Te quedan {intentos} intentos restantes.")
                    print(f"Pistas: \nTipo principal del pokemon -> {pokemon_data["tipo"][0]} \nSin tipo secundario \nGeneración del Pokemon -> {pokemon_data["generacion"]}")
                elif len(pokemon_data["tipo"]) > 1:
                    print(f"Te quedan {intentos} intentos restantes.")
                    print(f"Pistas: \nTipo principal del pokemon -> {pokemon_data["tipo"][0]} \nTipo secundario del pokemon -> {pokemon_data["tipo"][1]} \nGeneración del Pokemon -> {pokemon_data["generacion"]}")
            self.print_word(pokemon)
            self.print_letras_incorrectas()

            respuesta = self.respuesta()

            if respuesta in Ahorcado.LETRAS_USUARIO: #si la letra introducida ya está dentro de las respuestas previas no se contará el intento y permitirá otro intento
                print("Ya has ingresado esta letra.")
                input("Presiona Enter para continuar...")
                continue

            Ahorcado.LETRAS_USUARIO.append(respuesta)

            if respuesta in self.letras_pokemon:
                print("¡Correcto!")
            else:
                print("Incorrecto.")
                self.letras_incorrectas.append(respuesta)
                intentos -= 1

            if all(letra in Ahorcado.LETRAS_USUARIO for letra in pokemon):
                self.clear_window()
                print(f"¡Felicidades! Has capturado un {pokemon}")
                break
        else:
            self.clear_window()
            print(f"Vaya, perece que se ta ha escapado. El pokemon era: {pokemon}")

game = Ahorcado("data.json")
game.play()
# pokemon = random.choice(self.pokedex))

#separar el proyecto en; json, juego, vista, panel(palabra a adivinar(sin los _) y las pistas), usuario