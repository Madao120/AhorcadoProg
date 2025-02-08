class Vista:
    def __init__(self):
        pass

    def mostrar_palabra(self, pokemon, letras_usuario):
        palabra_oculta = "".join([letra if letra in letras_usuario else "_" for letra in pokemon])
        print("\nPalabra actual:", " ".join(palabra_oculta))
    
    def mostrar_modos(self):
        print("\n📜 Zonas Safari (modos) 📜")
        print("1. Zona Clásica (Todos los Pokémon)")
        print("2. Zona por Tipo")
        print("3. Zona por Generación (Kanto, Jhoto, Hoenn, Sinnho, Unova, Kalos, Alola, Galar, Paldea)")
        print("4. Zona Doble Tipo")
        print("5. Zona Vieja (de 1º a 5º generación")
        print("6. Zona Nueva (de 6º a 9º generación)")
        print("7. Zona solo para Experos (Sin Pistas) x2 puntuación")
    
    def mostrar_pistas (self,intentos, pistas, modo):
        if modo == 1 or modo == 4 or modo == 5 or modo == 6: #Modo clasico, doble tipo, populares y poco populares
            if intentos == 4 or intentos == 3:
                print (f"Pistas: \n Tipo Principal: {pistas[0]}")
            elif intentos == 2:
                print (f"Pistas: \nTipo Principal: {pistas[0]} \nGeneración: {pistas[1]}")
            elif intentos == 1 or intentos == 0:
                print (f"Pistas: \nTipo Principal: {pistas[0]} \nGeneración: {pistas[1]} \nTipo Secundario: {pistas[2]}")
        
        elif modo == 3: #Modo por generación
            if intentos == 5 or intentos == 4:
                print (f"Pistas: \n Generación: {pistas[1]}")
            elif intentos == 3 or intentos == 2:
                print (f"Pistas: \nGeneración: {pistas[1]} \nTipo Principal: {pistas[0]}")
            elif intentos == 1 or intentos == 0:
                print (f"Pistas: \nGeneración: {pistas[1]} \nTipo Principal: {pistas[0]} \nTipo Secundario: {pistas[2]}")
    
    def mostrar_pistas_tipo (self, intentos, pistas, modo, tipo_modo):
        if modo == 2: #Modo por tipo
            if intentos == 5 or intentos == 4:
                print (f"Pistas: \n Primer tipo: {tipo_modo}")
            elif intentos == 3 or intentos == 2:
                print (f"Pistas: \nTipo Principal: {tipo_modo} \nGeneración: {pistas[1]}")
            elif intentos == 1 or intentos == 0:
                print (f"Pistas: \nTipo Principal: {tipo_modo} \nGeneración: {pistas[1]} \nTipo Secundario: {tipo_modo if pistas[2] == tipo_modo else pistas[2]}")
