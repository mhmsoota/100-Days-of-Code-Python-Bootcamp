from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(-200, 250)
        self.level = 0
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def end_this_game(self):
        self.clear()
        self.home()
        self.write(arg="Game Over", align="center", font=FONT) 