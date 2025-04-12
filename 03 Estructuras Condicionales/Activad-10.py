hemisferio = input("¿En qué hemisferio te encuentras? (Norte o Sur): ").strip().lower()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)): 
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)): 
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)): 
        return "Verano"
    return "Otoño"

def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)): 
        return "Verano" 
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)): 
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)): 
        return "Invierno"
    return "Primavera"

estacion = estacion_sur(mes, dia) if hemisferio == "norte" else estacion_norte(mes, dia) if hemisferio == "sur" else "Hemisferio no válido"
print(f"La estación en el hemisferio {hemisferio} es: {estacion}")