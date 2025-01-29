class Vista:
    def __init__(self):
        pass

    def mostrar_palabra(self, pokemon, letras_usuario):
        salida = ""
        for letra in pokemon:
            if letra in letras_usuario:
                salida += f"{letra} "
            else:
                salida += "_ "
        print(salida.strip())

    def mostrar_pistas(self, intentos, pokemon_data):
        if intentos <= 4:
            print(f"Pista: Tipo principal -> {pokemon_data['tipo'][0]}")
        if intentos <= 2:
            tipo_secundario = pokemon_data["tipo"][1] if len(pokemon_data["tipo"]) > 1 else "Sin tipo secundario"
            print(f"Pista adicional: Tipo secundario -> {tipo_secundario}")
        if intentos == 1:
            print(f"Pista final: Generación -> {pokemon_data['generacion']}")

    def mostrar_letras_incorrectas(self, letras_incorrectas):
        print("Letras incorrectas: ", ", ".join(letras_incorrectas))