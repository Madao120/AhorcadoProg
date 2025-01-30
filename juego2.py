import os
import random
from usuario import Usuario
from vista import Vista
from panel import Panel
from modo import ModosDeJuego

class Juego:
    def __init__(self, archivo_pokemon, archivo_usuarios):
        self.usuario = Usuario(archivo_usuarios)
        self.panel = Panel(archivo_pokemon)
        self.vista = Vista()
        self.modos = ModosDeJuego(self.panel.pokedex)
        self.letras_usuario = [" ", "-"]
        self.letras_incorrectas = []

    def jugar(self):
        if not self.autenticar_usuario():
            return

        # Seleccionar el modo de juego
        modo = self.modos.seleccionar_modo()
        pokemones_filtrados = self.modos.aplicar_filtro(modo)

        if not pokemones_filtrados:
            print("No hay Pokémon disponibles para este modo. Intenta otra opción.")
            return

        pokemon_data = random.choice(pokemones_filtrados)
        pokemon = pokemon_data["name"]
        intentos = 6

        while intentos > 0:
            os.system('cls' if os.name == "nt" else "clear")
            print(f"Intentos restantes: {intentos}")
            self.vista.mostrar_palabra(pokemon, self.letras_usuario)
            if modo != "5":  # En modo experto no hay pistas
                self.vista.mostrar_pistas(intentos, pokemon_data)
            self.vista.mostrar_letras_incorrectas(self.letras_incorrectas)

            letra = input("Introduce una letra: ").lower()
            if letra in self.letras_usuario or letra in self.letras_incorrectas:
                print("Ya has ingresado esta letra.")
                continue

            if letra in pokemon:
                print("¡Correcto!")
                self.letras_usuario.append(letra)
            else:
                print("Incorrecto.")
                self.letras_incorrectas.append(letra)
                intentos -= 1

            if all(letra in self.letras_usuario for letra in pokemon):
                print(f"¡Felicidades! Has capturado un {pokemon}")
                self.usuario.actualizar_puntuacion(intentos * 5)
                break
        else:
            print(f"Vaya, parece que se te ha escapado. El Pokémon era: {pokemon}")
            self.usuario.actualizar_puntuacion(-10)
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