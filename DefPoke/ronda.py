import os

class Ronda:
    def __init__(self, usuario, vista, modo, pokemon_info: dict, tipo_modo=None):
        self.usuario = usuario
        self.vista = vista
        self.pokemon = pokemon_info["name"]
        self.pistas = modo.escoger_pistas(pokemon_info, tipo_modo)
        self.tipo_modo = tipo_modo
        self.intentos = 5 if tipo_modo in [2, 3] else 6
        self.letras_usuario = [" ", "-"]
        self.letras_incorrectas = []

    def obtener_letra(self):
        while True:
            letra = input("Introduce una letra: ").lower()
            if len(letra) != 1:
                print("Introduce solo una letra.")
            elif not letra.isalpha():
                print("Solo se permiten letras.")
            elif letra in self.letras_usuario or letra in self.letras_incorrectas:
                print("Ya has ingresado esta letra.")
            else:
                return letra

    def jugar(self):
        while self.intentos >= 0:
            os.system('cls' if os.name == "nt" else "clear")
            self.usuario.ranking_usuarios()
            self.usuario.mostrar_puntuacion_actual()
            print(f"\nIntentos restantes: {self.intentos}")

            self.vista.mostrar_palabra(self.pokemon, self.letras_usuario)

            if self.tipo_modo == 2:
                self.vista.mostrar_pistas_tipo(self.intentos, self.pistas, self.tipo_modo)
            else:
                self.vista.mostrar_pistas(self.intentos, self.pistas, 1 if self.tipo_modo is None else self.tipo_modo)

            print("Letras incorrectas:", " ".join(self.letras_incorrectas))

            letra = self.obtener_letra()

            if letra in self.pokemon:
                print("¡Correcto!")
                self.letras_usuario.append(letra)
            else:
                print("Incorrecto.")
                self.letras_incorrectas.append(letra)
                self.intentos -= 1

            if all(letra in self.letras_usuario for letra in self.pokemon):
                puntos = self.intentos * (10 if self.tipo_modo == 7 else 5)
                print(f"¡{self.pokemon.capitalize()} atrapado! Ganaste {puntos} puntos.")
                self.usuario.actualizar_puntuacion(puntos)
                return True

        print(f"¡Oh no! ¡El {self.pokemon} ha escapado! Has perdido 10 puntos.") 
        self.usuario.actualizar_puntuacion(-10)
        return False