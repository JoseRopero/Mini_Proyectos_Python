import random
import art
import listas
from replit import clear

chosen_word = random.choice(listas.disney_list_personajes).lower()  # Random para elegir la palabra de un listado

vidas = 6

print(art.logo)
print("")
print("")

display = list()  # Creamos una lista vacía que rellenaremos de líneas y espacios
for n in range(len(chosen_word)):
    if chosen_word[n] == " ":  # Si hay algún espacio en la palabra lo dejamos en su posición
        display.insert(n, " ")
    else:
        display.insert(n, "_")  # Insertamos las líneas
print(*display, sep=' ')  # Para formatear la salida de la lista
print("")

while "_" in display:
    print(f"Tienes {vidas} vidas\n")
    guess = input("Adivina la letra: ").lower()

    clear()  # Para limpiar la consola

    if guess in display:  # Cuando eliges una letra que ya se encuentra en la palabra
        print(f"Has elegido la letra '{guess}' que ya está en la palabra")

    for indice in range(len(chosen_word)):  # Si elegimos una letra correcta, la metemos en la lista
        if chosen_word[indice] == guess:
            display[indice] = guess
    print(art.stages[vidas])

    if guess not in chosen_word:  # Si es incorrecta, restamos una vida e imprimimos el muñeco
        clear()
        print(
            f"la letra '{guess}' no se encuentra en la palabra, pierdes una vida."
        )
        vidas -= 1
        print(art.stages[vidas])  # Cuando llegue a 0 las vidas, perdemos y nos salimos del bucle
        if vidas == 0:
            break

    print(*display, sep=' ')
    print("")
if vidas > 0:
    print("You win")
else:
    print("You lose")
