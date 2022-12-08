import random
from replit import clear
from art import logo


def reparte():
    """Retorna una carta de una lista"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)


def suma_cartas(lista_cartas):
    """Retorna la suma de cartas de una mano"""
    if sum(lista_cartas) == 21 and len(lista_cartas) == 2:  # Si en la primera mano conseguimos Blackjack.
        return 0

    if 11 in lista_cartas and sum(lista_cartas) > 21:  # Si llevamos el 'as' y la suma es más de 21, cambiamos el valor
        lista_cartas.remove(11)
        lista_cartas.append(1)

    return sum(lista_cartas)


def comparar(resultado_jugador, resultado_pc):
    """Comparamos el resultado de los dos jugadores."""

    if resultado_jugador > 21 and resultado_pc > 21:
        return "Te has pasado, PIERDES 😤"

    if resultado_jugador == resultado_pc:
        return "EMPATE 🙃"
    elif resultado_pc == 0:
        return "PIERDES, Ordenador tiene Blackjack 😱"
    elif resultado_jugador == 0:
        return "GANAS tienes Blackjack 😎"
    elif resultado_jugador > 21:
        return "Te has pasado, PIERDES 😭"
    elif resultado_pc > 21:
        return "Ordenador se ha pasado. TU GANAS 😁"
    elif resultado_jugador > resultado_pc:
        return "GANAS 😃"
    else:
        return "PIERDES 😤"


def blackjack():
    print(logo)
    print()

    mano_jugador = []
    mano_pc = []
    eleccion_boolean_jugador = True

    for _ in range(2):  # Repartimos la primera mano, 2 cartas cada uno.
        mano_jugador.append(reparte())
        mano_pc.append(reparte())

    # Iniciamos el bucle del jugador hasta que se pase o ya no quiera más cartas.
    while eleccion_boolean_jugador:
        print(f"Tus cartas son: {mano_jugador} y suman: {suma_cartas(mano_jugador)}")
        print(f"La carta de la computadora es: {mano_pc[0]}")

        # Si jugador saca Blackjack y PC también o la suma de cartas es mayor que 21 del jugador,
        # Nos salimos del bucle.
        if suma_cartas(mano_jugador) == 0 and suma_cartas(mano_pc) == 0 or suma_cartas(mano_jugador) > 21:
            eleccion_boolean_jugador = False
        # De lo contrario, seguimos jugando
        else:
            jugada = input("Escribe 'y' para pedir otra carta, escribe 'n' para pasar: ")
            if jugada == 'y':
                mano_jugador.append(reparte())
            else:
                eleccion_boolean_jugador = False

    # Una vez acabada la jugada pasamos al PC. Si no ha sacado Blackjack en la primera mano o la suma es menor que 17:
    while suma_cartas(mano_pc) != 0 and suma_cartas(mano_pc) < 17:
        mano_pc.append(reparte())

    # Cuando acaba el bucle del PC, comparamos los resultados y se decide el ganador.

    print(f"Tu mano final: {mano_jugador} y la suma: {suma_cartas(mano_jugador)}")
    print(f"La mano final del ordenador: {mano_pc} y la suma: {suma_cartas(mano_pc)}")

    # Lo meto en variables para no andar escribiendo la función dentro de la función comparar()
    resultado_jugador = suma_cartas(mano_jugador)
    resultado_pc = suma_cartas(mano_pc)

    print(comparar(resultado_jugador, resultado_pc))


while input("¿Quieres jugar una partida de Blackjack? Escriba 'y' or 'n': ") == 'y':
    clear()
    blackjack()
