from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",12, "bold")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.score = -1
        self.goto(0, 275)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)