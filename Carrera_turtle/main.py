from turtle import Turtle, Screen
import random

is_race_on = False
s = Screen()
s.setup(width=500, height=400)
apuesta = s.textinput(title="Elige tu apuesta", prompt="Escoge color (red, blue, orange, yellow, green, purple: ")

colores = ["red", "blue", "orange", "yellow", "green", "purple"]
positions_y = [-125, -75, -25, 25, 75, 125]
lista_turtles = []  # Aquí meteremos todas las instancias de tortugas

for indice in range(6):  # Creamos 6 tortugas
    t = Turtle(shape="turtle")
    t.color(colores[indice])
    t.penup()
    t.goto(x=-240, y=positions_y[indice])
    lista_turtles.append(t)

if apuesta:  # Cuando el usuario hace su apuesta entonces iniciamos el bucle.
    is_race_on = True

while is_race_on:
    for tortuga in lista_turtles:
        if tortuga.xcor() > 230:  # Si la tortuga supera la coordenada y=230 es la ganadora
            is_race_on = False
            ganador = tortuga.pencolor()  # Recogemos el color de la tortuga ganadora
            if ganador == apuesta:
                print(f"Has ganado, la tortuga {ganador} ha llegado primera")
            else:
                print(f"Ohhhh has perdido, la tortuga {ganador} ha llegado primera")
        distancia_aleatoria = random.randint(0, 10)
        tortuga.fd(distancia_aleatoria)

s.exitonclick()
