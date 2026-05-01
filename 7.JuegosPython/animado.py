import random
import time
import os

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

# Lista para la animación
animacion = [rock, paper, scissors]
opciones = ["piedra", "papel", "tijera"]

print("="*50)
print(" PIEDRA, PAPEL O TIJERA ".center(50, "*"))
print("="*50)

while True:
    usuario = input("\n>> Elige (piedra, papel, tijera) o 'salir': ").lower()

    if usuario == "salir":
        print("¡Juego terminado!")
        break

    if usuario not in opciones:
        print("Opción no válida.")
        continue

    # --- EFECTO DE ANIMACIÓN ---
    time.sleep(0.5)
    
    for i in range(10):  # Cambiará 6 veces de imagen
        # Limpia la pantalla (cls para Windows, clear para Linux/Mac)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Muestra una imagen de la lista de animación de forma cíclica
        print(animacion[i % 3])
        time.sleep(1) # Velocidad de la animación

    # --- RESULTADO FINAL ---
    pc = random.choice(opciones)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print(f"LA PC ELIGIÓ: {pc.upper()}")
    
    if pc == "piedra": print(rock)
    elif pc == "papel": print(paper)
    else: print(scissors)
    
    print("="*50)
    print(f"TU ELEGISTE: {usuario.upper()}")

    # Lógica de ganador
    if usuario == pc:
        print("\n>>> EMPATE")
    elif (usuario == "piedra" and pc == "tijera") or \
         (usuario == "papel" and pc == "piedra") or \
         (usuario == "tijera" and pc == "papel"):
        print("\n>>> ¡GANASTE!")
    else:
        print("\n>>> PERDISTE")