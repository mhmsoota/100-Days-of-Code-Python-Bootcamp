from turtle import Turtle, Screen
from random import randint, choice


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# turtle1 = Turtle(shape="turtle")
# turtle1.penup()
# turtle1.goto(x = -230, y= -100)
# turtle1.color(colors[0])

# turtle2 = Turtle(shape="turtle")
# turtle2.penup()
# turtle2.goto(x = -230, y= -50)
# turtle2.color(colors[1])

# turtle3 = Turtle(shape="turtle")
# turtle3.penup()
# turtle3.goto(x = -230, y= 0)
# turtle3.color(colors[2])

# turtle4 = Turtle(shape="turtle")
# turtle4.penup()
# turtle4.goto(x = -230, y= 50)
# turtle4.color(colors[3])

# turtle5 = Turtle(shape="turtle")
# turtle5.penup()
# turtle5.goto(x = -230, y= 100)
# turtle5.color(colors[4])

y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.speed(choice([1, 3, 6, 10, 0]))
        turtle.forward(randint(10,100))
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} won the game")
            else:
                print(f"You lose! {winning_color} won the game!")
            break

screen.exitonclick()
