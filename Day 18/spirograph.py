from turtle import *
from random import random

t = Turtle()
s = Screen()
t.speed("fastest")

for angle in range(0, 360, 5):
    t.setheading(angle)
    t.pencolor(random(), random(), random())
    t.circle(100)

s.exitonclick()
