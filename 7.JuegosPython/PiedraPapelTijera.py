'''
Reto de programación # 1: Piedra, Papel o Tijera

1. Descripción de problema
Se solicita desarrollar un programa interactivo en Python que permita a un usuario enfrentarse contra la computadora en el 
Clásico juego de Piedra, Papel o Tijera.
El programa debe ser capaz de procesar la entrada del usuario, generar una respuesta aleatoria y determinar un ganador 
basándose en las reglas tradicionales.

2. Requerimientos Técnicos

El algoritmo debe estructurarse de la siguiente manera:

* Interfaz Visual: Mostrar un encabezado decorativo utilizando métodos de cadena como .center() y multiplicación de caracteres.

* Entrada de Datos: Solicitar al usuario su elección. El programa debe ser capaz de reconocer la entrada sin importar si 
se escribe en mayúsculas o minúsculas.

* Inteligencia Aleatoria: La computadora debe elegir una opción de una lista predefinida de opciones (Piedra, Papel, Tijera) 
de forma aleatoria utilizando el módulo random.

* Logica de comparación:

Implementar las condiciones necesarias para evaluar.

1. Empate: Ambas elecciones son iguales.
2. Victoria: El usuario vence a la PC (Priedra vence a Tijera, Tijera vence a Papel, Papel vence a Piedra).
3. Derrota: La PC vence al usuario.

* Control de Flujo: El juego debe repetirse indefinidamente dentro de un blucle hasta que el usuario decida escribir 
la palabra (Salir).

Solución del Ejercicio Propuesto    

import random
import time

print("="*50)
print(" PIEDRA, PAPEL O TIJERA ".center(50, "*"))
print("="*50)

# Opciones posibles
opciones = ["piedra", "papel", "tijera"]

while True:
    # 1. Jugada del usuario
    usuario = input("\n>> Elige (piedra, papel, tijera) o 'salir': ").lower()

    if usuario == "salir":
        print("Juego terminado.")
        break

    # 2. Jugada de la PC
    pc = random.choice(opciones)
    
    print("Computadora eligiendo...")
    time.sleep(0.8)
    print(f"La PC lanzó: {pc.upper()}")

    # 3. Comparación de resultados
    if usuario == pc:
        print(">>> EMPATE")
    elif (usuario == "piedra" and pc == "tijera") or \
         (usuario == "papel" and pc == "piedra") or \
         (usuario == "tijera" and pc == "papel"):
        print(">>> ¡GANASTE! ")
    else:
        print(">>> PERDISTE")
'''

import random
import time

# Definimos el arte ASCII
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("="*50)
print(" PIEDRA, PAPEL O TIJERA ".center(50, "*"))
print("="*50)

opciones = ["piedra", "papel", "tijera"]

while True:
    usuario = input("\n>> Elige (piedra, papel, tijera) o 'salir': ").lower()

    if usuario == "salir":
        print("¡Juego terminado!")
        break

    if usuario not in opciones:
        print("Opción no válida, intenta de nuevo.")
        continue

    # Elegir imagen del usuario
    if usuario == "piedra": print(rock)
    elif usuario == "papel": print(paper)
    else: print(scissors)

    # Jugada de la PC
    pc = random.choice(opciones)
    print("Computadora eligiendo...")
    time.sleep(0.8)
    
    print(f"La PC lanzó: {pc.upper()}")
    # Elegir imagen de la PC
    if pc == "piedra": print(rock)
    elif pc == "papel": print(paper)
    else: print(scissors)

    # Lógica de resultados
    if usuario == pc:
        print(">>> EMPATE ")
    elif (usuario == "piedra" and pc == "tijera") or \
         (usuario == "papel" and pc == "piedra") or \
         (usuario == "tijera" and pc == "papel"):
        print(">>> ¡GANASTE! ")
    else:
        print(">>> PERDISTE ")
    
    print("-" * 50)