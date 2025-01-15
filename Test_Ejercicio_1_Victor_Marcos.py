"""
Solicitar al usuario un número entero. El programa continuará pidiendo la entrada
hasta que el usuario ingrese un valor válido de tipo entero.
"""
def LEER_NUMERO():
    while True:
        NUMERO = input("Introduzca un número entero positivo: ")
        if NUMERO.isdigit():
            NUMERO = int(NUMERO)  
            break  # Salir del bucle si es un entero
        else:
            print("Eso no es un número entero positivo. Inténtalo de nuevo.")
    return NUMERO

NUMERO = LEER_NUMERO()

#Verificamos si el número es par o impar
if  NUMERO % 2 == 0:
    #Si NUMERO es par
    while NUMERO >=0:
        print(NUMERO)
        NUMERO = NUMERO - 2
else:
    #Si NUMERO es impar
    while NUMERO >=1:
        print(NUMERO)
        NUMERO = NUMERO - 2