import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

lista = [rock, paper, scissors]
eleccion = int(input("Escribe 0 para piedra, 1 para papel y 2 para tijeras:\n"))
if eleccion >= 3 or eleccion < 0:
    print("Numero incorrecto, YOU LOSE")
else:
    player = lista[eleccion]
    cpu = random.choice(lista)
    print(f"Player: {player}\n vs CPU: {cpu}")

    if player == cpu:
        print("EMPATE")
    elif player == rock and cpu == paper:
        print("YOU LOSE")
    elif player == rock and cpu == scissors:
        print("WIN")
    elif player == paper and cpu == rock:
        print("WIN")
    elif player == paper and cpu == scissors:
        print("YOU LOSE")
    elif player == scissors and cpu == rock:
        print("YOU LOSE")
    elif player == scissors and cpu == paper:
        print("WIN")
    else:
        print("Numero incorrecto, YOU LOSE")
