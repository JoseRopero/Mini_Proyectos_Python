# ♠️ BlackJack ♠️

Este proyecto es una implementación simple del clásico juego de BlackJack en Python. El objetivo es que el jugador se acerque lo más posible a 21 sin pasarse, compitiendo contra la computadora.

## Descripción del Juego

El juego sigue las reglas básicas de BlackJack:
1. Se reparten dos cartas al jugador y dos a la computadora.
2. El jugador puede pedir más cartas o plantarse.
3. Si el jugador o la computadora alcanza exactamente 21 en las dos primeras cartas, se considera un "BlackJack".
4. El valor de un As es flexible: puede ser 11 o 1, dependiendo de si ayuda a evitar que la suma supere 21.

Al final, el jugador y la computadora comparan sus manos para determinar el ganador.

## Archivos

- `art.py`: Contiene el logo ASCII del juego que se muestra al inicio de cada partida.
- `main.py`: El archivo principal que contiene toda la lógica del juego, desde repartir cartas hasta comparar manos y determinar el ganador.

## Funciones Principales

### `reparte()`
Retorna una carta seleccionada al azar de un mazo predeterminado. El mazo contiene cartas con valores entre 2 y 11.

### `suma_cartas(lista_cartas)`
Calcula y retorna la suma de cartas de una mano. Incluye lógica para manejar el valor del As (11 o 1) y verifica si la mano inicial es un BlackJack.

### `comparar(resultado_jugador, resultado_pc)`
Compara las manos del jugador y la computadora para determinar el ganador. Retorna un mensaje que indica el resultado (ganador o empate).

### `blackjack()`
Función principal que gestiona el flujo del juego:
- Reparte las cartas iniciales.
- Permite al jugador decidir si pide más cartas o se planta.
- Controla el turno de la computadora, que se planta si tiene 17 o más.
- Al final, compara las manos y declara el resultado.

## Ejecución

Para jugar una partida, ejecuta el archivo `main.py` en un entorno de Python. El juego permite jugar múltiples partidas sin reiniciar el script.

```bash
python main.py
```

## Ejemplo de Uso

Durante el juego, se mostrará en pantalla:

1. Las cartas y la suma del jugador.
2. La primera carta visible de la computadora.
3. Opciones para pedir otra carta o plantarse.
Al final de la partida, el juego muestra las manos finales y el resultado.

## Requisitos
Este proyecto usa la biblioteca `random` para la selección aleatoria de cartas y `replit` para limpiar la consola entre turnos. Asegúrate de tener instalada la biblioteca `replit` para una experiencia óptima.

```bash
pip install replit
```
## Notas
Este proyecto es ideal para principiantes en Python, ya que cubre temas como:

- Funciones y control de flujo (`if`, `while`, `for`)
- Manejo de listas y operadores condicionales
- Importación de módulos externos
- Disfruta del juego y buena suerte en tus partidas de BlackJack! 🃏
