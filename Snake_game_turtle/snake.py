from turtle import Turtle

POSICION_START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []  # Vamos a guardar los snakes para moverlos todos a la vez.
        self.crear_snake()
        self.head = self.snakes[0]

    def crear_snake(self):
        for posicion in POSICION_START:  # Creamos 3 cuadrados que forman la serpiente
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(posicion)
            self.snakes.append(snake)

    def move(self):
        # Creamos un bucle para que el último cuadrado pase a la posición del segundo y el segundo a la del primero
        # Y así sucesivamente siguiendo la cola a la cabeza que es el primero.

        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()  # Recojo las coordenadas del anterior y se las paso a la cola
            new_y = self.snakes[snake_num - 1].ycor()  # Ejem. El 3 pasa al 2, hasta que todos están encima del 1
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.fd(MOVE_SNAKE)

    # Métodos para mover la serpiente.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
