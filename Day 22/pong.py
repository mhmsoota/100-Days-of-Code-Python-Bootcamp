from turtle import Turtle
from c import *

class Pong(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_move_to = 10
        self.y_move_to = 10

    def moveto(self):
        self.goto(self.xcor()+self.x_move_to, self.ycor()+self.y_move_to)

    def bounce_for_x(self):
        self.x_move_to *= -1
        self.moveto()

    def detect_collision_and_bounce(self, only_bounce=False):
        # Detect collision with wall
        if only_bounce:
            self.home()
            self.x_move_to *= -1
            self.x_move_to = 10
            self.y_move_to = 10
        elif self.ycor() > HALF_SCREEN_HEIGHT - 25 or self.ycor() < -HALF_SCREEN_HEIGHT + 25:
            self.y_move_to *= -1
            self.moveto()
            self.x_move_to += 5
            self.y_move_to += 5
        

