from random import choice
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
turtle = Player()
cars = CarManager()
level_display = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if choice(range(5)) == 0 :
        cars.create_car()
    cars.move_towards_side()

    # Detect if turtle reached the top
    if turtle.ycor() > 250:
        level_display.update_level()
        turtle.go_to_start()
        cars.level_up()

    # Detect collisions with cars
    for car in cars.all_cars:
        if turtle.distance(car) < 40:
            level_display.end_this_game()
            game_is_on = False

screen.exitonclick()
