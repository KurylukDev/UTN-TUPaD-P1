def decimal_a_binario(decimal):
    # Consigna: Convierte un número decimal entero positivo a su representación binaria.

    if decimal < 0: # Verificar si la entrada es un entero positivo
        return None # Retornar None si la entrada no es un entero positivo y se ingresa letras da error
    if decimal == 0:
        return "0"
    binario = "" # Inicializar la cadena de binario
    while decimal > 0:
        residuo = decimal % 2 # Obtener el residuo de la division y agregarlo a la cadena este residuo o es 1 o 0
        binario = str(residuo) + binario # Concatenar el residuo al inicio de la cadena
        decimal //= 2 # Dividir el decimal entre 2
    return binario # Retornar la cadena de binario

# Solicitar la entrada al usuario
numero_decimal_usuario = input("Por favor, ingresa un número decimal entero: ")

# Intentar convertir la entrada a entero (sin validación previa)
numero_decimal = int(numero_decimal_usuario)

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Mensaje de salida según el resultado
if numero_binario is not None:
    print(f"El número decimal {numero_decimal} en binario es: {numero_binario}")
else:
    print("La entrada no es un número entero positivo válido.")