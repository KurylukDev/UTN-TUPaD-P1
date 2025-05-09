def calcular_media(cantidad_numeros):

    numeros = []
    print(f"Por favor, ingresa {cantidad_numeros} números enteros:")

    for i in range(cantidad_numeros):
        while True:
            try:
                numero_str = input(f"Ingresa el número {i + 1}: ")
                numero = int(numero_str)
                numeros.append(numero)
                break  # Salir del bucle while si la entrada es válida
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

    if numeros:
        media = sum(numeros) / len(numeros)
        return media
    else:
        return None

if __name__ == "__main__":
    cantidad = 100
    media_calculada = calcular_media(cantidad)

    if media_calculada is not None:
        print(f"\nLa media de los {cantidad} números ingresados es: {media_calculada}")
    else:
        print("No se ingresaron números para calcular la media.")