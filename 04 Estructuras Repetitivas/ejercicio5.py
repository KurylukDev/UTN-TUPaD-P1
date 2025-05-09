import random

numero = random.randint(0, 9)
intento = -1
intentos = 0

print("Adivina un número del 0 al 9:")
while intento != numero:
    try:
        intento = int(input())
        intentos += 1
        if intento < numero:
            print("Más alto.")
        elif intento > numero:
            print("Más bajo.")
    except ValueError:
        print("Número inválido.")

print(f"¡Adivinaste en {intentos} intentos! El número era {numero}.")