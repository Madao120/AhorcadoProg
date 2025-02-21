import json
import os

class Usuarios:
    archivo_usuarios = {}
    usuario_actual = None
    puntuaciones = {}
    def __init__(self, archivo_usuarios):
        self.archivo_usuarios = archivo_usuarios
        self.usuario_actual = None
        self.puntuaciones = {}

        # Cargar datos de usuarios
        if not os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, "w") as file:
                json.dump({}, file)
        else:
            with open(self.archivo_usuarios, "r") as file:
                self.puntuaciones = json.load(file)

    def iniciar_sesion(self, usuario, contraseña):
        if usuario in self.puntuaciones and self.puntuaciones[usuario]["contraseña"] == contraseña:
            self.usuario_actual = usuario  # Asigna correctamente el usuario actual
            print(f"¡Bienvenido de nuevo, {usuario}!")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False

    def registrar_usuario(self, usuario, contraseña):
        if usuario in self.puntuaciones:
            print("Este usuario ya existe. Intenta con otro nombre.")
            return False
        else:
            self.puntuaciones[usuario] = {"contraseña": contraseña, "puntuacion": 0}
            self.usuario_actual = usuario  # Asigna el nuevo usuario correctamente
            print(f"Usuario {usuario} registrado con éxito.")
            return True

    def mostrar_puntuacion_actual(self):
        if self.usuario_actual is None:
            print("Error: No hay usuario autenticado.")
            return

        if self.usuario_actual not in self.puntuaciones:
            print("Error: Usuario no encontrado en el ranking.")
            return

        puntuacion = self.puntuaciones[self.usuario_actual]["puntuacion"]
        print(f"{self.usuario_actual}, tu puntuación actual es: {puntuacion} puntos")

    def actualizar_puntuacion(self, puntos):
        if self.usuario_actual:
            self.puntuaciones[self.usuario_actual]["puntuacion"] += puntos
            self.guardar_datos()

    def guardar_datos(self):
        with open(self.archivo_usuarios, "w") as file:
            json.dump(self.puntuaciones, file, indent=4)

    def autenticar_usuario(self):                                                                                                       # Función para autenticar al usuario                                               
        while True:
            opcion = input("¿Tienes cuenta? (s/n): ").lower()                                                                           # Preguntar si el usuario tiene cuenta
            if opcion == "s":
                usuario = input("Usuario: ")                                                                                            # Si el usuario tiene cuenta, se le pedirá que introduzca su usuario y contraseña
                contraseña = input("Contraseña: ")
                if self.iniciar_sesion(usuario, contraseña):                                                                    # Si el usuario y la contraseña son correctos se le dará acceso al juego                                                       
                    return True
            elif opcion == "n":
                usuario = input("Elige un nombre de usuario: ")                                                                         # Si el usuario no tiene cuenta, se le pedirá que introduzca un usuario y contraseña para registrarse
                contraseña = input("Elige una contraseña: ")
                if self.registrar_usuario(usuario, contraseña):                                                                 # Si el usuario y la contraseña son correctos se le dará acceso al juego                                             
                    return True
            else:
                print("Opción no válida.")

# Lo que tiene que ver con los usuarios en conjunto:

    def mostrar_top_10(self):
        if not self.puntuaciones:
            print("No hay usuarios registrados aún.")
            return

        # Ordenar usuarios por puntuación en orden descendente
        ranking = sorted(self.puntuaciones.items(), key=lambda x: x[1]["puntuacion"], reverse=True) #Lo encontré por internet, no sabía como hacerlo

        print("\n🏆 TOP 10 USUARIOS 🏆")
        print("-" * 30)
        for i, (usuario, datos) in enumerate(ranking[:10], start=1):
            print(f"{i}. {usuario} - {datos['puntuacion']} puntos")
        print("-" * 30)
    
    def ranking_usuarios(self):
        usuario = Usuarios("DefPoke/usuarios.json")  # Cargar datos
        usuario.mostrar_top_10()  # Mostrar el ranking de usuarios
    