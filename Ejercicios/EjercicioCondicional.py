'''
</>  Reto código

Objetivo: Crear un programa que determine la categoría de edad de una persona

Crea un programa que solicite la edad de una persona y determine su categoría según las siguientes reglas:

    Si la edad es menor que 0, mostrar "Edad no válida"
    Si la edad está entre 0 y 12, mostrar "Infante"
    Si la edad está entre 13 y 17, mostrar "Adolescente"
    Si la edad está entre 18 y 64, mostrar "Adulto"
    Si la edad es 65 o mayor, mostrar "Adulto mayor"

Utiliza una estructura if-elif-else para implementar esta lógica. El programa debe solicitar la edad con la función input() y convertirla a 
entero antes de evaluarla.

Solución:
'''
# Solicitar la edad al usuario
entrada = input("Por favor, ingresa tu edad: ")

# Convertir la entrada a entero
# Nota: Usamos un bloque try-except por si el usuario ingresa algo que no sea un número
try:
    edad = int(entrada)

    # Lógica de categorización con if-elif-else
    if edad < 0:
        print("Edad no válida")
    elif edad <= 12:
        print("Infante")
    elif edad <= 17:
        print("Adolescente")
    elif edad <= 64:
        print("Adulto")
    else:
        print("Adulto mayor")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")

#Otra Solucion 

# Programa para determinar la categoría de edad de una persona
# Solicitar la edad al usuario
try:
    edad = int(input("Por favor, ingresa tu edad: "))
    
    # Determinar la categoría según la edad
    if edad < 0:
        print("Edad no válida")
    elif edad <= 12:
        print("Infante")
    elif edad <= 17:
        print("Adolescente")
    elif edad <= 64:
        print("Adulto")
    else:
        print("Adulto mayor")
        
except ValueError:
    print("Error: Debes ingresar un número entero.")