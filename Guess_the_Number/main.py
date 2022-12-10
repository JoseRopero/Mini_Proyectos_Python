from art import logo
import random


def elegir_numero_oculto():
    lista_numeros = []
    for numero in range(1, 101):
        lista_numeros.append(numero)
    numero = random.choice(lista_numeros)
    return numero


def adivinar_numero(numero_pc, numero_jugador):
    if numero_jugador < numero_pc:
        print("Mas alto!!!")
        print("Pruebe otra vez")
        return True
    elif numero_jugador > numero_pc:
        print("Mas bajo!!!")
        print("Pruebe otra vez")
        return True
    else:
        print("Has acertado. YOU WIN!!!")
        return False


print(logo)
print()
print("Bienvenido al juego 'Adivina el número'")
print("Estoy pensando en un número del 1 al 100.")
numero_oculto = elegir_numero_oculto()

choose_difficult = input("Elige la dificultad. Escriba 'easy' o 'hard': ")

if choose_difficult == "easy":
    intentos = 10
else:
    intentos = 5

fin_juego = True
while fin_juego and intentos > 0:
    print(f"Tienes {intentos} intentos para acertar el número")
    choose_number = int(input("Escriba el número: "))
    fin_juego = adivinar_numero(numero_oculto, choose_number)
    if fin_juego:
        intentos -= 1

if intentos == 0:
    print("Has perdido. Prueba otra vez.")
