import random

# Definimos el arte ASCII para cada opción
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

images = [rock, paper, scissors]

print("========================================")
print("What do you choose?")
print("  0 - Rock")
print("  1 - Paper")
print("  2 - Scissors")

user_choice = int(input("\nTu elección: "))

if user_choice >= 3 or user_choice < 0:
    print("Número inválido. ¡Pierdes por no seguir las reglas!")
else:
    # Mostrar elección del usuario
    print(f"\nYou chose {['ROCK', 'PAPER', 'SCISSORS'][user_choice]}")
    print(images[user_choice])

    print("========================================")
    print("JO!")
    print("KEN!")
    print("PO!")
    print("========================================")

    # Elección de la computadora
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {['ROCK', 'PAPER', 'SCISSORS'][computer_choice]}")
    print(images[computer_choice])

    # Lógica para determinar el ganador
    if user_choice == 0 and computer_choice == 2:
        print("Rock smashes scissors\n\nYOU WIN!")
    elif computer_choice == 0 and user_choice == 2:
        print("Rock smashes scissors\n\nYOU LOSE!")
    elif computer_choice > user_choice:
        print(f"{['Rock', 'Paper', 'Scissors'][computer_choice]} covers {['rock', 'paper', 'scissors'][user_choice]}\n\nYOU LOSE!")
    elif user_choice > computer_choice:
        print(f"{['Rock', 'Paper', 'Scissors'][user_choice]} covers {['rock', 'paper', 'scissors'][computer_choice]}\n\nYOU WIN!")
    elif computer_choice == user_choice:
        print("It's a draw!")
