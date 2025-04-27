def decimal_a_binario(decimal):
    # Consigna: Convierte un número decimal entero a su representación binaria.

    if not isinstance(decimal, int) or decimal < 0: # Verificar si la entrada es un entero positivo
        return None # Retornar None si la entrada no es un entero positivo
    if decimal == 0: 
        return "0" 
    binario = "" # Inicializar la cadena de binario
    while decimal > 0: 
        residuo = decimal % 2 # Obtener el residuo de la division y agregarlo a la cadena
        binario = str(residuo) + binario # Concatenar el residuo al inicio de la cadena
        decimal //= 2 # Dividir el decimal entre 2
    return binario # Retornar la cadena de binario

# Solicitar la entrada al usuario
try: 
    numero_decimal_str = input("Por favor, ingresa un número decimal entero: ")
    numero_decimal = int(numero_decimal_str) # Convertir la entrada a entero
    numero_binario = decimal_a_binario(numero_decimal) # Convertir el número decimal a binario
    
# Mensaje de salida según el resultado
    if numero_binario is not None:
        print(f"El número decimal {numero_decimal} en binario es: {numero_binario}")
    else:
        print("La entrada no es un número entero positivo válido.")
# En caso de error ejemplo el usuario ingreso letras en vez de números
except ValueError:
    print("¡Error! Ingresa un número entero válido.") 