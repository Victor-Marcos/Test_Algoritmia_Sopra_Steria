# Clase para representar a una persona con atributos de sexo y edad
class Personas:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad

#Función para calcular el número de personas mayores de edad
def Mayores_18(PERSONAS):
    i = 0
    for persona in PERSONAS:
        if persona.edad >= 18: 
            i += 1  # 
    return i

#Función para calcular el número de personas masculinas mayores de edad
def Masculinas_Mayores_18(PERSONAS):
    i = 0
    for persona in PERSONAS:
        if persona.edad >= 18 and persona.sexo == "M":  
            i += 1  
    return i

#Función para calcular el número de personas femeninas menores de edad
def Femeninas_Menores_18(PERSONAS):
    i = 0
    for persona in PERSONAS:
        if persona.edad < 18 and persona.sexo == "F":  
            i += 1  
    return i

#Función para calcular el porcentaje de mujeres
def Porcentaje_mujeres(PERSONAS):
    i = 0
    for persona in PERSONAS:
        if persona.sexo == 'F':  
            i += 1  
        
    return (i*100)/len(PERSONAS)

#Función para crear el vector PERSONAS con los datos de las 50 personas.
def Leer_personas(n):
    PERSONAS = []
    #Bucle para recoger los 50 datos
    for i in range(n):
        #Lectura del sexo de la persona número i+1
        while True:
            sexo = input(f"Introduce el sexo de la persona {i+1} (Escriba M o F únicamente): ")
            if sexo == 'M' or sexo == 'F':
                break  # Salir del bucle si es M o F
            else:
                print("Escriba unicamente M (sexo masculino) o F (sexo femenino).")
        #Lectura de la edad de la persona número i+1
        while True:
            edad = input(f"Introduce la edad de la persona {i+1}: ")
            if edad.isdigit():
                edad = int(edad)
                break  # Salir del bucle si es un entero
            else:
                print("Escriba unicamente un número entero que haga referencia a la edad.")

        # Crear un objeto Persona y agregarlo a la lista
        persona = Personas(sexo, edad)
        PERSONAS.append(persona)
    return PERSONAS

n = 50 #Numero de personas
PERSONAS = Leer_personas(n)

Ma_18 = Mayores_18(PERSONAS)
Me_18 = n - Ma_18
M_Ma_18 = Masculinas_Mayores_18(PERSONAS)
F_Me_18 = Femeninas_Menores_18(PERSONAS)
Porcentaje_mayores_de_edad = (Ma_18*100)/len(PERSONAS)
Porcentaje_M = Porcentaje_mujeres(PERSONAS)

print(f"El número de personas mayores de edad es: {Ma_18}")
print(f"El número de personas menores de edad es: {Me_18}")

print(f"El número de hombres mayores de edad es: {M_Ma_18}")
print(f"El número de mujeres menores de edad es: {F_Me_18}")

print(f"Porcentaje de mayores de edad respecto al total: {Porcentaje_mayores_de_edad:.2f}%")
print(f"Porcentaje de mujeres respecto al total: {Porcentaje_M:.2f}%")