numero = int(input("número entero: "))

# Usamos la función abs() para contar correctamente los dígitos aunque el número sea negativo
contador_digitos = len(str(abs(numero)))

print("El número tiene", contador_digitos, "dígito(s).")