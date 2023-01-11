from turtle import *
from random import random

tim = Turtle()
screen = Screen()


def draw_my_shape(number_of_sides):
    angle = 360/number_of_sides
    penColour = (random(), random(), random())
    tim.pencolor(penColour)
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    draw_my_shape(i)
