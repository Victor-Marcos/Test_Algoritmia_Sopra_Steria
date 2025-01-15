def Leer_HORAS_TRABAJADAS(): #Función para leer las horas trabajadas
    while True:
        HORAS_TRABAJADAS = input(f"Introduce el número de horas trabajadas: ")
        if HORAS_TRABAJADAS.isdigit(): #Comprobar si es número entero
            HORAS_TRABAJADAS = int(HORAS_TRABAJADAS) #Convertir la entrada a un número entero
            break  # Salir del bucle si es un entero
        else:
            print("Escriba unicamente un número entero que haga referencia a las horas trabajadas.")
    return HORAS_TRABAJADAS

def LEER_TARIFA(): #Función para leer la tarifa
    while True:
        TARIFA = input("Introduce la tarifa (puede ser un número decimal): ")
        if TARIFA.replace('.', '', 1).isdigit() and TARIFA.count('.') == 1:  #  #Comprobamos si es un número entero
            TARIFA = float(TARIFA) #Convertir la entrada a un número flotante
            break # Salir del bucle si es un float
        else:
            print("Por favor, introduce un número válido (puede ser decimal con punto).")
    return TARIFA

HORAS_TRABAJADAS = Leer_HORAS_TRABAJADAS()
TARIFA = LEER_TARIFA()

# Calcular el sueldo
if HORAS_TRABAJADAS <= 40:
    # Si las horas trabajadas son 40 o menos, no hay horas extras
    SUELDO = HORAS_TRABAJADAS * TARIFA
else:
    # Si las horas trabajadas son más de 40, se calculan las 40 horas con la tarifa base y las horas extras con un incremento del 50% sobre la tarifa base
    HORAS_EXTRAS = HORAS_TRABAJADAS - 40
    SUELDO = (40 * TARIFA) + HORAS_EXTRAS * TARIFA * (1 + 50/100)

print(f"El sueldo del trabajador es: {SUELDO:.2f}")
