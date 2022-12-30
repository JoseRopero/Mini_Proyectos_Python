from turtle import Turtle

ALINEACION = 'center'
FUENTE = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.contador = 0
        self.goto(0, 265)
        self.hideturtle()
        self.color("white")
        self.write(arg=f"Score:  {self.contador}", move=False, align=ALINEACION, font=FUENTE)

    def score(self):
        self.contador += 1
        self.clear()
        self.write(arg=f"Score:  {self.contador}", move=False, align=ALINEACION, font=FUENTE)

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align=ALINEACION, font=FUENTE)
