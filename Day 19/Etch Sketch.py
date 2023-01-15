from turtle import *

turtle = Turtle()
screen = Screen()


def fd():
    turtle.forward(5)


def bd():
    turtle.backward(5)


def clock():
    rn = turtle.heading()
    turtle.setheading(rn+4)


def anti_clock():
    rn = turtle.heading()
    turtle.setheading(rn-4)


def empty():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkeypress(fd, 'w')
screen.onkeypress(bd, 's')
screen.onkeypress(clock, 'd')
screen.onkeypress(anti_clock, 'a')
screen.onkeypress(empty, 'c')
screen.listen()

screen.exitonclick()
