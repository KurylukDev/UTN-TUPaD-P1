
nombre = input("Ingresa tu nombre: ")


opcion = int(input("Elige una opción (1, 2 o 3):\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n"))

if opcion == 1:
    nombre_transformado = nombre.upper()  
elif opcion == 2:
    nombre_transformado = nombre.lower()  
elif opcion == 3:
    nombre_transformado = nombre.title()  
else:
    nombre_transformado = "Opción no válida"

# Imprimir el resultado
print(nombre_transformado)
