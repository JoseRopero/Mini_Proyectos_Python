from turtle import Screen
from snake import Snake
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("El juego de la serpiente")
s.tracer(0)  # Apagamos el rastreador(Para la animación de la tortuga). Hay que indicarle cunado actualizar la pantalla

snake = Snake()  # Inicializamos la serpiente que son 3 cuadrados.

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


s.exitonclick()
