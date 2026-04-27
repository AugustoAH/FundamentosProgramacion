'''
Reto de Programación Simulador de Probabilidades: Ruleta Rusa

1. Descripción del Problema: Se requiere desarrollar un programa en Python que simule un sistema de azar
basado en un revolver de 6 recamaras. El programa debe gestionar eventos aleatorios, pausas de ejecución 
para mejorar la experiencia de usuario y control del flujo basado en condiciones de victoria o derrota.

2. Requerimientos técnicos:

El algoritmo debe cumplir con los siguientes requisitos:

* Inicialización: Definir una recamara ganadora (bala) de forma 
aleatoria entre 1 y 6.  (random)

* Bucle de Juego: El usuario debe interactuar manualmente (while)
para girar el tambor y disparar (time)

* Mecanica de Azar: En cada turno, la posición de la recamara que queda al frente
al percutor debe ser aleatoria, simulando el giro del tambor.

* Condición de derrota: Si la recamara seleccionada coincide con la de la 
bala, el programa termina inmediatamente.    (if)

* Condicion de Victoria: El jugador gana si logra sobrevivir a 5 intentos
(ya que el sexto intento sería el fatal). (else)
'''
import random, time

print("="*50)
print("Bienvenido al Simulador de Ruleta Rusa")
print("="*50)

input("Poner Bala en el Tambor (Presiona Enter)")
bala = random.randint(1, 6)
time.sleep(0.5)

disparos = 0 # Variable para contar los disparos realizados

while True:
    input("Girar el Tambor (Presiona Enter)")
    recamara = random.randint(1, 6)

    input("Apuntar y Disparar (Presiona Enter)")
    time.sleep(1)

    if recamara == bala:
        print("¡Bang! Has perdido. La bala estaba en la recámara " \
        "número", bala)
        break
    else:
        disparos += 1
        print("Has sobrevivido a este intento.")
        print("Intentos de Disparo:", disparos)

    if disparos == 5:
        print("¡Felicidades! Has ganado al sobrevivir a 5 intentos.")
        break
    
print("="*50)
print("Fin del Juego - Gracias por jugar")
print("="*50)