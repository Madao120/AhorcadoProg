from juego import Juego

if __name__ == "__main__":
    juego = Juego("DefPoke/data.json", "DefPoke/usuarios.json")
    juego.jugar()