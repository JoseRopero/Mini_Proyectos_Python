import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

s.onkey(player.move, "Up")

game_is_one = True
while game_is_one:
    time.sleep(0.1)
    s.update()
    car_manager.create_cars()
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_one = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.meta()
        car_manager.incrementar_vel()
        scoreboard.score()


s.exitonclick()
