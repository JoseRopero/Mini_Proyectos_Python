from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("El juego de la serpiente")
s.tracer(0)  # Apagamos el rastreador(Para la animación de la tortuga). Hay que indicarle cunado actualizar la pantalla

scoreboard = Scoreboard()
snake = Snake()  # Inicializamos la serpiente que son 3 cuadrados.
food = Food()

s.listen()  # Para empezar a escuchar de teclado y poder mover la serpiente
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_is_one = True
while game_is_one:
    time.sleep(0.1)  # Para que el movimiento sea más lento y podamos verlo
    s.update()  # Aquí actualizamos la pantalla para que empiece a mostrar la serpiente

    snake.move()

    # Detectar la colisión con la comida.
    if snake.head.distance(food) < 15:  # Si la distancia entre los dos objetos es menor de 15, ejecuta el código.
        food.refrescar()
        snake.extender()
        scoreboard.score()

    # Detectar colisión con las paredes.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_one = False
        scoreboard.game_over()

    # Detectar colisión con la cola.
    for segmento in snake.snakes[1:]:  # Excluimos la cabeza del bucle para no comparar cabeza con cabeza.
        if snake.head.distance(segmento) < 10:  # Comparamos la cabeza con cualquier trozo de la serpiente.
            game_is_one = False
            scoreboard.game_over()


s.exitonclick()
