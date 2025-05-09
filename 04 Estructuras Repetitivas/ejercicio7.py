print("calcular la suma desde 0 hasta un número.")
numero_limite_str = input("Por favor, ingresa un número entero positivo: ")

try:
    numero_limite = int(numero_limite_str)

    if numero_limite < 0:
        print("Por favor, ingresa un número positivo.")
    else:
        suma = 0
        contador = 0
        while contador <= numero_limite:
            suma = suma + contador
            contador = contador + 1
        print("La suma total es:", suma)

except ValueError:
    print("¡Ups! Parece que no ingresaste un número entero válido.")