import os
from usuarios import Usuarios
from vista import Vista
from modo import Modo
import os

class Juego:
    def __init__(self, archivo_pokemon, archivo_usuarios):
        self.usuario = Usuarios(archivo_usuarios)
        self.modo = Modo(archivo_pokemon)
        self.vista = Vista()
        self.pokemon = str
        self.letras_usuario = [" ", "-"]
        self.letras_incorrectas = []
        self.pistas = list
        self.pistas_mostrar = list
        self.intentos = int

    def jugar(self):
        print("¡Bienvenido a la Zona Safari!")  
        if not self.usuario.autenticar_usuario():
            return
        
        jugar = True                                                                                                                    #Inicio del bucle para repetir partida
        while jugar:
            os.system('cls' if os.name == "nt" else "clear")                                                                            # Limpiar pantalla

            intentos = 6                                                                                                                # Número de intentos
            letras_usuario = [" ", "-"]                                                                                                 # Letras introducidas por el usuario
            letras_incorrectas = []                                                                                                     # Letras falladas por el usuario

            self.vista.mostrar_modos()                                                                                                  # Mostrar los modos de juego disponibles
            modo = self.modo.seleccionar_modo()                                                                                         # Seleccionar el modo de juego (que son numeros del 1 al 7)
            motor_juego = self.modo.aplicar_modo(modo)                                                                                  # Aplicar el modo de juego seleccionado y devolverá el pokemon filtrado
            pokemon_info = motor_juego[0]                                                                                               # Recibimos el diccionario que tiene la información del pokemon
            tipo_modo = motor_juego[1] if modo == 2 else None                                                                                            # Recibimos el tipo de modo introducido por el usuario

            pokemon = pokemon_info["name"]                                                                                              # Extraemos solo el nombre
            pistas = self.modo.escoger_pistas(pokemon_info, modo)                                                                       # En base a los datos del pokemon se escogerán unas pistasautomáticamente
            
            if modo == 2 or modo == 3:                                                                                                  # Si el modo es 2 o 3, se tendrán menos intentos para que esté más balanceado
                intentos = 5

            while intentos >= 0:                                                                                                        # Bucle para iniciar una ronda
                os.system('cls' if os.name == "nt" else "clear")
                self.usuario.ranking_usuarios()                                                                                         # Mostrar el top 10 usuarios
                self.usuario.mostrar_puntuacion_actual()                                                                                # Mostrar la puntuación actual del usuario
                print(f"\nIntentos restantes: {intentos}")                                                                              # Mostrar los intentos restantes para que el usuario sepa cuántos le quedan, contanto el intento 0

                self.vista.mostrar_palabra(pokemon, letras_usuario)                                                                     # Mostrar la palabra oculta en forma de _ hasta que se hacierte alguna letra
                if modo == 2:   
                    self.vista.mostrar_pistas_tipo(intentos, pistas, modo, tipo_modo)                                                   # Si el modo es 2, aplicaremos las pistas con la variable tipo_modo que es la introducida por el usuario, las mostrará según los intentos que queden
                else:
                    self.vista.mostrar_pistas(intentos, pistas, modo)                                                                   # Mostrar las pistas segun cuantos intentos queden
                print("Letras incorrectas:", " ".join(letras_incorrectas))                                                              # Mostrar las letras incorrectas que ha introducido el usuario separadas por un espacio

                while True:                                                                                                             # Bucle para que el usuario introduzca únicamente una letra, que no sea un numero y que no haya introducido antes
                    letra = input("Introduce una letra: ").lower()

                    if len(letra) != 1:                                                                                                 # Si la longitud de la letra introducida no es 1 reiniciará el bucle
                        print("Por favor, introduce solo una letra.")
                        continue
                    if not letra.isalpha():                                                                                             # Si la letra introducida no es una letra reiniciará el bucle
                        print("Solo se permiten letras.")
                        continue
                    if letra in letras_usuario or letra in letras_incorrectas:                                                          # Si la letra introducida ya ha sido introducida antes reiniciará el bucle
                        print("Ya has ingresado esta letra.")
                        continue
                    break
                
                if letra in pokemon:                                                                                                    # Si la letra introducida está en el nombre del pokemon se dará como correcto, esta letra se añadirá a la lista de letras introducidas por el usuario y por lo tanto aparecerá en la palabra oculta
                    print("¡Correcto!")
                    letras_usuario.append(letra)
                else:
                    print("Incorrecto.")                                                                                                # Si la letra introducida no está en el nombre del pokemon se dará como incorrecto, esta letra se añadirá a la lista de letras incorrectas y por lo tanto se mostrará en la lista de letras incorrectas
                    letras_incorrectas.append(letra)
                    intentos -= 1

                if all(letra in letras_usuario for letra in pokemon):                                                                   # Si todas las letras del nombre del pokemon están en la lista de letras introducidas por el usuario se dará como completado y ganará la ronda.
                    print(f"¡Ya está! ¡{pokemon.capitalize()} atrapado! Has ganado {intentos * (10 if modo == 7 else 5)} puntos.")
                    self.usuario.actualizar_puntuacion(intentos * (10 if modo == 7 else 5))                                             #Dependiendo de cuantos intentos queden se llevará una puntuación u otra.
                    break
            else:                                                                                                                       # Si fallamos todos los intentos se perderá la ronda.
                print(f"¡Oh no!. ¡El {pokemon} ha escapado! Has perdido 10 puntos.") 
                self.usuario.actualizar_puntuacion(-10)                                                                                 # Si se fallan todos los intentos se perderán 10 puntos

            opcion = input("\n¿Quieres volver a entrar a la Zona Safari? (s/n): ").lower()                                              # Bucle para volver a jugar
            if opcion != "s":
                print("La partida ha sido guardada.")
                jugar = False