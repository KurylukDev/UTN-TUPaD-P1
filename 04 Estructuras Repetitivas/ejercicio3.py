# Solicita los dos valores
inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número: "))

# Determina menor y mayor para poder usar range correctamente
menor = min(inicio, fin)
mayor = max(inicio, fin)

# Suma los valores entre los dos números, excluyéndolos
suma = 0
for i in range(menor + 1, mayor):
    suma += i

print("La suma de los números entre", inicio, "y", fin, "es:", suma)