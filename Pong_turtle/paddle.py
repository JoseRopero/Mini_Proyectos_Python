from turtle import Turtle


class Paddle(Turtle):
    # En el constructor recogemos la posición de las palas para crear las dos en el main.
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

