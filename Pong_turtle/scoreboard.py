from turtle import Turtle

ALINEACION = 'center'
FUENTE = ('Courier', 60, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.contador_r = 0
        self.contador_l = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 220)
        self.write(arg=f"{self.contador_r}", move=False, align=ALINEACION, font=FUENTE)
        self.goto(-100, 220)
        self.write(arg=f"{self.contador_l}", move=False, align=ALINEACION, font=FUENTE)

    def punto_l(self):
        self.contador_l += 1
        self.update_score()

    def punto_r(self):
        self.contador_r += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align=ALINEACION, font=FUENTE)
