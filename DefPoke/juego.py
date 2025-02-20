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
        
        jugar = True  
        while jugar:
            os.system('cls' if os.name == "nt" else "clear")

            self.vista.mostrar_modos()  
            modo = self.modo.seleccionar_modo()  
            motor_juego = self.modo.aplicar_modo(modo)  
            pokemon_info = motor_juego[0]  

            tipo_modo = motor_juego[1] if modo == 2 else None  

            ronda = Ronda(self.usuario, self.vista, self.modo, pokemon_info, tipo_modo)
            ronda.jugar()

            opcion = input("\n¿Quieres volver a entrar a la Zona Safari? (s/n): ").lower()
            if opcion != "s":
                print("La partida ha sido guardada.")
                jugar = False