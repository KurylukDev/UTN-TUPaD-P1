import random
import statistics



numerosAleatorios = [random.randint(1, 100) for i in range(50)]

moda = statistics.mode(numerosAleatorios)
mediana = statistics.median(numerosAleatorios)
media = statistics.mean(numerosAleatorios)

if media > mediana > moda:
    sesgo = "Positivo o a la derecha"
elif media < mediana < moda:

    sesgo = "Negativo o a la izquierda"
else:
    sesgo = "Sin sesgo"
    
    print(f"Lista de numeros aleatorios: {numerosAleatorios}")
    print(f"Moda: {moda}")
    print(f"Mediana: {mediana}")    
    print(f"Media: {media}")    
    print(f"Sesgo: {sesgo}")                