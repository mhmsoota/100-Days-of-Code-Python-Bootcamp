from turtle import *
from random import choice, random

theturtle = Turtle()
screen = Screen()
possibleHeadings = [0, 90, 180, 270]
theturtle.pensize(10)
theturtle.speed("fastest")

# theturtle.penup()
# theturtle.goto(-200,-200)
# theturtle.pendown()

for _ in range(200):
    theturtle.pencolor(random(),random(),random())
    theturtle.seth(choice(possibleHeadings))
    theturtle.forward(30)

screen.exitonclick()