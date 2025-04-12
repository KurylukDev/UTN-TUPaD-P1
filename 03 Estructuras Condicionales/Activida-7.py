frase = input("Ingrese una frase o palabra: ")


if frase[-1].lower() in ["a", "e", "i", "o", "u"]:
    print("Es una vocal")
else:
    print("No es una vocal")