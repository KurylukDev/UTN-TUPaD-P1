def analizar_numeros(cantidad_numeros):
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    print(f"Por favor, ingresa {cantidad_numeros} números enteros:")

    for i in range(cantidad_numeros):
        while True:
            try:
                numero_str = input(f"Ingresa el número {i + 1}: ")
                numero = int(numero_str)
                break  # finalizar el bucle while si la entrada es válida
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    print("\n--- Análisis de los números ingresados ---")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
    print(f"Cantidad de números positivos: {positivos}")
    print(f"Cantidad de números negativos: {negativos}")

if __name__ == "__main__":
    cantidad = 100 
    analizar_numeros(cantidad)