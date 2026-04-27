'''
Reto de Programación Simulador de Probabilidades: Ruleta Rusa

1. Descripción del Problema: Se requiere desarrollar un programa en Python que simule un sistema de azar basado en un 
revolver de 6 recamaras. El programa debe gestionar eventos aleatorios, pausas de ejecución  para mejorar la experiencia 
de usuario y control del flujo basado en condiciones de victoria o derrota.

2. Requerimientos técnicos: el algoritmo debe cumplir con los siguientes requisitos.

1. Inicialización: Definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6.
2. Bucle de Juego: El usuario debe interactuar manualmente para girar el tambor y disparar.
3. Mecánica de Azar: En cada turno, la posición de la recamara que queda al frente al percutor debe ser aleatoria, 
   simulando el giro del tambor.
4. Condición de Derrota: Si la recamara seleccionada coincide con la de la bala, el programa termina inmediatamente.
5. Condición de Victoria: El jugador gana si logra sobrevivir a 5 intentos (ya que el sexto intento sería el fatal).
'''
# Importación de librerías: random para el azar y time para manejar pausas
import random
import time

# Encabezado visual del juego
print("="*50)
print("Bienvenido al Simulador de Ruleta Rusa")
print("="*50)

# El programa espera una acción del usuario antes de continuar
input("Poner Bala en el Tambor (Presiona Enter)")

# Lógica de preparación: Se elige un número al azar del 1 al 6 que representa 
# la posición de la bala en el tambor de un revólver de 6 espacios.
bala = random.randint(1, 6)
time.sleep(0.5) # Pausa dramática de medio segundo

# Inicialización de un acumulador para rastrear cuántas veces se ha gatillado
disparos = 0 

# Bucle principal: El juego continuará hasta que el jugador pierda o gane
while True:
    # Simulación de girar el tambor en cada ronda
    input("Girar el Tambor (Presiona Enter)")
    
    # Se genera una posición aleatoria para el percutor (la recámara que se disparará)
    recamara = random.randint(1, 6)

    input("Apuntar y Disparar (Presiona Enter)")
    time.sleep(1) # Pausa de 1 segundo para aumentar la tensión

    # Lógica de Evaluación (Condicional principal)
    # Comparamos si la posición de la bala coincide con la recámara seleccionada
    if recamara == bala:
        print("¡Bang! Has perdido. La bala estaba en la recámara número: ", bala)
        break  # Se sale del bucle 'while' porque el jugador "murió"
    else:
        # Si no coinciden, el jugador sobrevive e incrementamos el contador
        disparos += 1
        print("Has sobrevivido a este intento.")
        print("Intentos de Disparo:", disparos)

    # Condición de victoria: Si el contador llega a 5, el juego termina exitosamente
    if disparos == 5:
        print("¡Felicidades! Has ganado al sobrevivir a 5 intentos.")
        break # Se sale del bucle para finalizar el programa
    
# Mensaje final de cierre
print("="*50)
print("Fin del Juego - Gracias por jugar")
print("="*50)

'''
Explicación de la Lógica Clave
•	random.randint(1, 6): Es el motor del juego. Se usa dos veces: primero para "esconder" la bala y segundo para determinar 
    qué recámara queda frente al percutor al girar el tambor.
•	El Bucle while True: Crea un ciclo infinito que solo se detiene mediante la instrucción break. En este caso, hay dos 
    formas de romper el ciclo:
	1.	Derrota: Cuando recamara == bala.
	2.	Victoria: Cuando el contador disparos llega a 5.
•	Interactividad: El uso de input() sin asignar su valor a una variable sirve únicamente para pausar la ejecución 
    del programa, obligando al usuario a interactuar para avanzar.
•	Legibilidad: El uso de time.sleep() no afecta los datos, pero mejora la experiencia de usuario (UX) al simular el 
    tiempo que tardaría la acción en la vida real.
'''