from turtle import Turtle
from c import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.show_scores()

    def show_scores(self):
        self.clear()
        self.goto(-100, HALF_SCREEN_HEIGHT-100)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, HALF_SCREEN_HEIGHT-100)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_gets_point(self):
        self.left_score += 1
        self.show_scores()

    def right_gets_point(self):
        self.right_score += 1
        self.show_scores()
