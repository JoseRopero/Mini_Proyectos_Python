from art import logo, vs
from game_data import data
import random
from replit import clear


def random_eleccion(datos):
    """Elegir un diccionario aleatorio de la lista data"""
    indice = random.randint(0, 49)
    return datos[indice]


def comparar(datoA, datoB):
    if datoA['follower_count'] > datoB['follower_count']:
        return True
    else:
        return False


def game():
    contador = 0
    opcionA = random_eleccion(data)
    opcionB = random_eleccion(data)

    end_game = True
    while end_game:

        print(logo)
        if contador > 0:  # Para que empiece a imprimir el contador desde que acertamos la primera.
            print(f"Muy bien!! Tu resultado: {contador}")

        print(
            f"Compare A: {opcionA['name']}, a {opcionA['description']}, from {opcionA['country']}")

        print(vs)

        print(
            f"Contra B: {opcionB['name']}, a {opcionB['description']}, from {opcionB['country']}")

        eleccion_jugador = input("Quién tiene mas followers? Escribe 'A' o 'B': ").lower()

        clear()

        if eleccion_jugador == 'a':
            boolean = comparar(opcionA, opcionB)
            if boolean:  # Si la verdadera es la 'a' solo cambiamos la opcion B.
                contador += 1
                opcionB = random_eleccion(data)
            else:
                print(f"Lo siento, has perdido. Resultado final: {contador}")
                return
        elif eleccion_jugador == 'b':
            boolean = comparar(opcionB, opcionA)
            if boolean:
                contador += 1
                opcionA = opcionB  # Si la verdadera es la 'b', la cambiamos para que sea la opcion A
                opcionB = random_eleccion(data)  # Y la opcion 'b' elegimos otro aleatorio a comparar.
            else:
                print(f"Lo siento, has perdido. Resultado final: {contador}")
                return
        else:
            print("Elija la opcion correcta")


game()
