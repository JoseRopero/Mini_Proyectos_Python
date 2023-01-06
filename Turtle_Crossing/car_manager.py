import random
from turtle import Turtle

COLORS = ["red", "green", "yellow", "blue", "orange", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def incrementar_vel(self):
        self.car_speed += MOVE_INCREMENT
