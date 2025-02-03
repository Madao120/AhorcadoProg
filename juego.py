import os
import random
from usuario import Usuario
from vista import Vista
from panel import Panel
from modo import Modo

class Juego:
    def __init__(self, archivo_pokemon, archivo_usuarios):
        self.usuario = Usuario(archivo_usuarios)
        self.panel = Panel(archivo_pokemon)
        self.vista = Vista()
        self.modos = Modo(self.panel.pokedex)
        self.letras_usuario = [" ", "-"]
        self.letras_incorrectas = []

    def jugar(self):
        if not self.autenticar_usuario():
            return

        while True:  # Bucle para jugar varias veces sin volver a autenticarse
            # Seleccionar el modo de juego
            modo = self.modos.seleccionar_modo()
            pokemones_filtrados = self.modos.aplicar_filtro(modo)

            if not pokemones_filtrados:
                print("No hay Pokémon disponibles para este modo. Intenta otra opción.")
                continue  # Volver a pedir otro modo en caso de error

            pokemon_data = random.choice(pokemones_filtrados)
            pokemon = pokemon_data["name"]
            intentos = 6
            letras_usuario = [" ", "-"]
            letras_incorrectas = []

            while intentos > 0:
                os.system('cls' if os.name == "nt" else "clear")
                self.usuario.ranking_usuarios()
                self.usuario.mostrar_puntuacion_actual()
                print(f"\n \n \n \n Intentos restantes: {intentos}")
                self.vista.mostrar_palabra(pokemon, letras_usuario)
                if modo != "7":  # En modo experto no hay pistas
                    self.vista.mostrar_pistas(intentos, pokemon_data, modo)
                self.vista.mostrar_letras_incorrectas(letras_incorrectas)

                letra = input("Introduce una letra: ").lower()
                if letra in letras_usuario or letra in letras_incorrectas:
                    print("Ya has ingresado esta letra.")
                    continue

                if letra in pokemon:
                    print("¡Correcto!")
                    letras_usuario.append(letra)
                else:
                    print("Incorrecto.")
                    letras_incorrectas.append(letra)
                    intentos -= 1

                if all(letra in letras_usuario for letra in pokemon):
                    print(f"¡Felicidades! Has capturado un {pokemon}")
                    self.usuario.actualizar_puntuacion(intentos * 5)
                    break
            else:
                print(f"Vaya, parece que se te ha escapado. El Pokémon era: {pokemon}")
                self.usuario.actualizar_puntuacion(-10)

            # Preguntar si quiere jugar otra vez o salir
            opcion = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if opcion != "s":
                print("Gracias por jugar. ¡Hasta la próxima!")
                break  # Salir del bucle y terminar el juego

    def autenticar_usuario(self):
        while True:
            opcion = input("¿Tienes cuenta? (s/n): ").lower()
            if opcion == "s":
                usuario = input("Usuario: ")
                contraseña = input("Contraseña: ")
                if self.usuario.iniciar_sesion(usuario, contraseña):
                    return True
            elif opcion == "n":
                usuario = input("Elige un nombre de usuario: ")
                contraseña = input("Elige una contraseña: ")
                if self.usuario.registrar_usuario(usuario, contraseña):
                    return True
            else:
                print("Opción no válida.")