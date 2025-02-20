import os

class Ronda:
    def __init__(self, usuario, vista, pokemon, pistas, modo, tipo_modo=None):
        self.usuario = usuario
        self.vista = vista
        self.pokemon = pokemon
        self.pistas = pistas
        self.modo = modo
        self.tipo_modo = tipo_modo
        self.intentos = 5 if modo in [2, 3] else 6  # Modos 2 y 3 tienen menos intentos
        self.letras_usuario = [" ", "-"]            # Meto automáticamente el espacio y - ya que no quiero que el usuario tenga que meter estos caracteres ya que no son letras
        self.letras_incorrectas = []                # Letras incorrectas que ha introducido el usuario

    def ronda(self):
        while self.intentos >= 0:
            os.system('cls' if os.name == "nt" else "clear")        # Limpia la pantalla
            self.usuario.ranking_usuarios()                         # Mostrar el top 10 usuarios
            self.usuario.mostrar_puntuacion_actual()                # Mostrar la puntuación actual del usuario activo
            print(f"\nIntentos restantes: {self.intentos}")         # Muestra los intentos restantes

            self.vista.mostrar_palabra(self.pokemon, self.letras_usuario)   # Muestra la palabra oculta con _ para las letras no adivinadas, y si adivina la letra mostrará la misma

            if self.modo == 2:  
                self.vista.mostrar_pistas_tipo(self.intentos, self.pistas, self.modo, self.tipo_modo)   # Si el modo es el 2 deberé de cambiar el como se escojen las pistas haciendo que el tipo escojido por el usuario sea el que se muestre
            else:
                self.vista.mostrar_pistas(self.intentos, self.pistas, self.modo)    # Si el modo no es el segundo las istas procederán como normalmente

            print("Letras incorrectas:", " ".join(self.letras_incorrectas))         # Muestra las letras incorrectas que ha introducido el usuario

            while True:                                                             # Bucle para que el usuario introduzca únicamente una letra, que no sea un numero y que no haya introducido antes
                letra = input("Introduce una letra: ").lower()
                if len(letra) != 1:
                    print("Por favor, introduce solo una letra.")
                    continue
                if not letra.isalpha():
                    print("Solo se permiten letras.")
                    continue
                if letra in self.letras_usuario or letra in self.letras_incorrectas:
                    print("Ya has ingresado esta letra.")
                    continue
                break

            if letra in self.pokemon:               # Si la letra introducida está en el nombre del pokemon se dará como correcto y aparecerá en mostrar_palabra
                print("¡Correcto!")
                self.letras_usuario.append(letra)
            else:                                   # Si la letra no está en el nombre del pokemon se dará como incorrecto y se añadirá a la lista de letras incorrectas para que no vuelva a cometer el mismo error
                print("Incorrecto.")
                self.letras_incorrectas.append(letra)
                self.intentos -= 1

            if all(letra in self.letras_usuario for letra in self.pokemon):         # Si todas las letras del nombre del pokemon están en la lista de letras introducidas por el usuario, se dará como que ha adivinado el pokemon
                print(f"¡Ya está! ¡{self.pokemon.capitalize()} atrapado! Has ganado {self.intentos * (10 if self.modo == 7 else 5)} puntos.")
                self.usuario.actualizar_puntuacion(self.intentos * (10 if self.modo == 7 else 5))
                break
        else:                                                                       # Si no se han adivinado todas las letras del nombre del pokemon se perderá la ronda
            print(f"¡Oh no!. ¡El {self.pokemon} ha escapado! Has perdido 10 puntos.")
            self.usuario.actualizar_puntuacion(-10)