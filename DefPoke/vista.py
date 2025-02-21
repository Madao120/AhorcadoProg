class Vista:
    def __init__(self):
        pass

    def mostrar_palabra(self, pokemon, letras_usuario):
        palabra_oculta = "".join([letra if letra in letras_usuario else "_" for letra in pokemon])
        print("\nPalabra actual:", " ".join(palabra_oculta))
    
    def mostrar_modos(self): # Muestra los modos de juego
        print("\n📜 Zonas Safari (modos) 📜")
        print("1. Zona Clásica (Todos los Pokémon)")
        print("2. Zona por Tipo")
        print("3. Zona por Generación (Kanto, Jhoto, Hoenn, Sinnho, Unova, Kalos, Alola, Galar, Paldea)")
        print("4. Zona Doble Tipo")
        print("5. Zona Vieja (de 1º a 5º generación")
        print("6. Zona Nueva (de 6º a 9º generación)")
        print("7. Zona solo para Expertos (Sin Pistas) más puntuación")
    
    def mostrar_pistas (self,intentos, pistas, modo): # Muestra las pistas según el modo de juego excluyendo el modo 2 que tiene su propia función (los espacios luego de \n son a propósito)
        if modo == 1 or modo == 4 or modo == 5 or modo == 6 : #Modo clasico, doble tipo, populares y poco populares
            if intentos == 4 or intentos == 3:
                print (f"Pistas \n Tipo Principal: {pistas[0].capitalize()}")
            elif intentos == 2:
                print (f"Pistas \n Tipo Principal: {pistas[0].capitalize()} \n Generación: {pistas[1].capitalize()}")
            elif intentos == 1 or intentos == 0:
                print (f"Pistas \n Tipo Principal: {pistas[0].capitalize()} \n Generación: {pistas[1].capitalize()} \n Tipo Secundario: {pistas[2].capitalize()}")
        elif modo == 3: #Modo por generación ya que cambio el texto (iba a poner un if else en el print pero se iba a ver feo por que era muy largo horizontalmente)
            if intentos == 5 or intentos == 4:
                print (f"Pistas \n Generación: {pistas[0].capitalize()}")
            elif intentos == 3 or intentos == 2:
                print (f"Pistas \n Generación: {pistas[0].capitalize()} \n Tipo Principal: {pistas[1].capitalize()}")
            elif intentos == 1 or intentos == 0:
                print (f"Pistas \n Generación: {pistas[1].capitalize()} \n Tipo Principal: {pistas[0].capitalize()} \n Tipo Secundario: {pistas[2].capitalize()}")
    
    def mostrar_pistas_tipo (self, intentos, pistas, modo, tipo_modo):  #Muestra las pistas del modo 2 debido a que cambia la forma en la que se muestran las pistas
        if modo == 2: #Modo por tipo
            if intentos == 5 or intentos == 4:
                print (f"Pistas \n Primer tipo: {tipo_modo.capitalize()}")
            elif intentos == 3 or intentos == 2:
                print (f"Pistas \n Primer tipo: {tipo_modo.capitalize()} \n Generación: {pistas[1].capitalize()}")
            elif intentos == 1 or intentos == 0:
                print (f"Pistas \n Primer tipo: {tipo_modo.capitalize()} \n Generación: {pistas[1].capitalize()} \n Segundo tipo: {tipo_modo if pistas[2] == tipo_modo else pistas[2].capitalize()}")