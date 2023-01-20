from turtle import Turtle, shape

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()
    
    def go_to_start(self):
        self.showturtle()
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)
