from juego import Juego

if __name__ == "__main__":
    juego = Juego("NewPoke/data.json", "NewPoke/usuarios.json")
    juego.jugar()