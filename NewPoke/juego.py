import os
from usuario import Usuario
from vista import Vista
from modo import Modo
import os

class Juego:
    def __init__(self, archivo_pokemon, archivo_usuarios):
        self.usuario = Usuario(archivo_usuarios)
        self.modo = Modo(archivo_pokemon)
        self.vista = Vista()
        self.pokemon = str
        self.letras_usuario = [" ", "-"]
        self.letras_incorrectas = []
        self.pistas = list
        self.pistas_mostrar = list
        self.intentos = int
        self.multiplicador = float
        self.puntuacion = float

    def jugar(self):
        if not self.autenticar_usuario():
            return
        
        jugar = True
        while jugar:
            os.system('cls' if os.name == "nt" else "clear")
            self.usuario.ranking_usuarios()
            self.usuario.mostrar_puntuacion_actual()

            intentos = 6
            letras_usuario = [" ", "-"]
            letras_incorrectas = []

            self.vista.mostrar_modos()
            modo = self.modo.seleccionar_modo()
            motor_juego = self.modo.aplicar_modo(modo)
            pokemon_info = motor_juego[0] # Recibimos el diccionario
            tipo_modo = motor_juego[1] # Recibimos el tipo de modo

            pokemon = pokemon_info["name"]  # Extraemos solo el nombre
            pistas = self.modo.escoger_pistas(pokemon_info, modo)
            
            if modo == 2 or modo == 3:
                intentos = 5
            else:
                pass

            while intentos >= 0:
                os.system('cls' if os.name == "nt" else "clear")
                print(f"\nIntentos restantes: {intentos}")

                #pistas_mostradas = self.modo.aplicar_pistas(modo, intentos, pistas_mostradas, pistas)

                self.vista.mostrar_palabra(pokemon, letras_usuario)
                self.vista.mostrar_pistas(intentos, pistas, modo, tipo_modo)
                print("Letras incorrectas:", " ".join(letras_incorrectas))

                while True:
                    letra = input("Introduce una letra: ").lower()

                    if len(letra) != 1:
                        print("Por favor, introduce solo una letra.")
                        continue
                    if not letra.isalpha():
                        print("Solo se permiten letras.")
                        continue
                    if letra in letras_usuario or letra in letras_incorrectas:
                        print("Ya has ingresado esta letra.")
                        continue
                    break
                
                if letra in pokemon:
                    print("¡Correcto!")
                    letras_usuario.append(letra)
                else:
                    print("Incorrecto.")
                    letras_incorrectas.append(letra)
                    intentos -= 1

                if all(letra in letras_usuario for letra in pokemon):
                    print(f"¡Felicidades! Has capturado un {pokemon}")
                    self.usuario.actualizar_puntuacion(intentos * (10 if modo == 7 else 5))
                    break
            else:
                print(f"Vaya, el Pokémon era: {pokemon}")
                self.usuario.actualizar_puntuacion(-10)

            opcion = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if opcion != "s":
                print("Gracias por jugar. ¡Hasta la próxima!")
                jugar = False

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
                    