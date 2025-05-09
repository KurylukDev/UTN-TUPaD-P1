def invertir(n):
  try:
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
  except ValueError:
    return "Entrada inválida"

num_str = input("Ingresa un número entero: ")
resultado = invertir(int(num_str))
print("Invertido:", resultado)