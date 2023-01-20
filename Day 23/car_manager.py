from player import MOVE_DISTANCE
from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.create_car()
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.goto(300, randint(-280, 280))
        self.all_cars.append(new_car)

    def move_towards_side(self):
        for car in self.all_cars:
            car.goto(car.xcor()-self.move_speed, car.ycor())

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
