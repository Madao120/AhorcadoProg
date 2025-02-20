import os
from usuarios import Usuarios
from vista import Vista
from modo import Modo
from ronda import Ronda

class Juego:
    def __init__(self, archivo_pokemon, archivo_usuarios):
        self.usuario = Usuarios(archivo_usuarios)
        self.modo = Modo(archivo_pokemon)
        self.vista = Vista()

    def jugar(self):
        print("¡Bienvenido a la Zona Safari!")  
        if not self.usuario.autenticar_usuario():
            return
        
        jugar = True    #Inicio del bucle para repetir partida
        while jugar:                                                                                
            os.system('cls' if os.name == "nt" else "clear")  # Limpiar pantalla

            self.vista.mostrar_modos()                          # Mostrar los modos de juego disponibles
            modo = self.modo.seleccionar_modo()                 # Seleccionar el modo de juego (que son numeros del 1 al 7)
            motor_juego = self.modo.aplicar_modo(modo)          # Aplicar el modo de juego seleccionado y devolverá el pokemon filtrado
            pokemon_info = motor_juego[0]                       # Recibimos el diccionario que tiene la información del pokemon
            tipo_modo = motor_juego[1] if modo == 2 else None   # Recibimos el tipo de modo introducido por el usuario

            pokemon = pokemon_info["name"]                          # Extraemos solo el nombre
            pistas = self.modo.escoger_pistas(pokemon_info, modo)   # En base a los datos del pokemon se escogerán unas pistasautomáticamente

            ronda = Ronda(self.usuario, self.vista, pokemon, pistas, modo, tipo_modo) # Creamos una instancia de la clase Ronda
            ronda.ronda()   # Iniciamos la ronda de juego 

            opcion = input("\n¿Quieres volver a entrar a la Zona Safari? (s/n): ").lower()  # Preguntamos si quiere volver a jugar para reiniciar el bucle principal
            if opcion != "s":
                print("La partida ha sido guardada.")   
                jugar = False                                                               # Si la respuesta no es "s" se mostrará un mensaje de que la partida ha sido guardada saliendo del bucle