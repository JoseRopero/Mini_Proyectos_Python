from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Inicializamos dos variables para el movimiento de la bola
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebote_y(self):  # Cuando llega a una de las paredes cambiamos el eje 'y' para que disminuya.
        self.y_move *= -1

    def rebote_x(self):  # Cuando rebota en una pala cambiamos 'x' y aumentamos velocidad
        self.x_move *= -1
        self.move_speed *= 0.9

    def gol(self):
        self.home()
        self.move_speed = 0.1
        self.rebote_x()

