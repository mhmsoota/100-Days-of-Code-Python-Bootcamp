from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(20,0), (0,0), (-20,0)]



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)