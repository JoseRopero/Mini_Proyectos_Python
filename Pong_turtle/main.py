from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POSITION_PADDLE = [(350, 0), (-350, 0)]  # Defino las posiciones de las palas

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)
linea = Turtle("square")
linea.color("white")
linea.shapesize(stretch_wid=30, stretch_len=0.07)
medio = Turtle("circle")
medio.pencolor("white")


r_paddle = Paddle(POSITION_PADDLE[0])
l_paddle = Paddle(POSITION_PADDLE[1])
ball = Ball()
scoreboard = Scoreboard()


s.listen()
s.onkeypress(r_paddle.move_up, "Up")
s.onkeypress(r_paddle.move_down, "Down")
s.onkeypress(l_paddle.move_up, "w")
s.onkeypress(l_paddle.move_down, "s")

contador_r = 0
contador_l = 0
game_is_one = True
while contador_r <= 2 and contador_l <= 2:
    time.sleep(ball.move_speed)  # Empezamos con la velocidad del constructor.
    s.update()
    ball.move()

    # Colisión con la pared superior e inferior
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebote_y()

    # Colisión con la pala
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.rebote_x()

    # Detectar cuando sale por la derecha y suma al contador
    if ball.xcor() > 380:
        ball.gol()
        scoreboard.punto_l()
        contador_l += 1

    # Detectar cuando sale por la izquierda y suma al contador
    if ball.xcor() < -380:
        ball.gol()
        scoreboard.punto_r()
        contador_r += 1

scoreboard.game_over()
s.exitonclick()
