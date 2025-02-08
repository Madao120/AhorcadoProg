class Vista:
    def __init__(self):
        self.pistas_mostradas = []  # Guardar las pistas mostradas en pantalla

    def mostrar_palabra(self, pokemon, letras_usuario):
        salida = ""
        for letra in pokemon:
            if letra in letras_usuario:
                salida += f"{letra} "
            else:
                salida += "_ "
        print(salida.strip())

    def mostrar_pistas(self, intentos, pokemon_data, modo):
        # Reset de pistas si es una nueva palabra
        if intentos == 6:
            self.pistas_mostradas = []

        tipo_principal = pokemon_data["tipo"][0]
        tipo_secundario = pokemon_data["tipo"][1] if len(pokemon_data["tipo"]) > 1 else "Sin tipo secundario"
        generacion = pokemon_data["generacion"]

        # Verificar si el modo ya proporciona un filtro (y omitir pistas redundantes)
        omitir_tipo = modo == "2"  # Modo por Tipo
        omitir_generacion = modo == "3"  # Modo por Generación
        sin_pistas = modo == "7"  # Modo Experto

        if sin_pistas:
            return  # No mostrar pistas en modo Experto

        pistas_disponibles = []

        if not omitir_tipo:
            pistas_disponibles.append(f"Tipo principal -> {tipo_principal}")
        if not omitir_generacion:
            pistas_disponibles.append(f"Generación -> {generacion}")
        pistas_disponibles.append(f"Tipo secundario -> {tipo_secundario}")

        # Orden dinámico de pistas
        if intentos == 4 and len(self.pistas_mostradas) < 1:
            self.pistas_mostradas.append(pistas_disponibles[0])
        if intentos == 3 and len(self.pistas_mostradas) < 2 and len(pistas_disponibles) > 1:
            self.pistas_mostradas.append(pistas_disponibles[1])
        if intentos == 2 and len(self.pistas_mostradas) < 3 and len(pistas_disponibles) > 2:
            self.pistas_mostradas.append(pistas_disponibles[2])

        # Mostrar todas las pistas acumuladas
        for i, pista in enumerate(self.pistas_mostradas, start=1):
            print(f"Pista {i}: {pista}")

    def mostrar_letras_incorrectas(self, letras_incorrectas):
        print("Letras incorrectas: ", ", ".join(letras_incorrectas))


    # def mostrar_pistas(self, intentos, pokemon_data):
    #     if intentos <= 4:
    #         print(f"Pista 1: Tipo principal -> {pokemon_data['tipo'][0]}")
    #     if intentos <= 2:
    #         print(f"Pista 2: Generación -> {pokemon_data['generacion']}")

    #     if intentos == 1:
    #         tipo_secundario = pokemon_data["tipo"][1] if len(pokemon_data["tipo"]) > 1 else "Sin tipo secundario"
    #         print(f"Pista Final: Tipo secundario -> {tipo_secundario}")
            