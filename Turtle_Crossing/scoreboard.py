from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.contador = 1
        self.penup()
        self.goto(-220, 265)
        self.hideturtle()
        self.write(arg=f"Score: {self.contador}", move=False, align="center", font=FONT)

    def score(self):
        self.contador += 1
        self.clear()
        self.write(arg=f"Score: {self.contador}", move=False, align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align="center", font=FONT)


