from turtle import Turtle

ALINEACION = 'center'
FUENTE = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.contador = 0
        with open('data.txt') as data:
            contenido = data.read()
        self.high_score = int(contenido)
        self.goto(0, 265)
        self.hideturtle()
        self.color("white")
        self.score()

    def score(self):
        self.clear()
        self.write(arg=f"Score:  {self.contador} High Score: {self.high_score}", move=False, align=ALINEACION, font=FUENTE)

    def reset(self):
        if self.contador > self.high_score:  # Si el contador actual es la maxima puntuación
            self.high_score = self.contador  # Entonces pasará a ser high_score
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.contador = 0
        self.score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", move=False, align=ALINEACION, font=FUENTE)

    def incrementar_score(self):
        self.contador += 1
        self.clear()
        self.score()
