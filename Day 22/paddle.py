from turtle import Turtle
from c import *

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < HALF_SCREEN_HEIGHT - 50:
            self.goto(self.xcor(), self.ycor() + SPEED_OF_MOVEMENT)

    def go_down(self):
        if self.ycor() > -HALF_SCREEN_HEIGHT + 50:
            self.goto(self.xcor(), self.ycor() - SPEED_OF_MOVEMENT)