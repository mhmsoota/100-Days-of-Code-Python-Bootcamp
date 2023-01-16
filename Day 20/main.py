from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

game_snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True
screen.listen()
screen.onkey(game_snake.up, "Up")
screen.onkey(game_snake.down, "Down")
screen.onkey(game_snake.left, "Left")
screen.onkey(game_snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    game_snake.move()

    #Detect collision with food
    if game_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh()
        game_snake.extend()

    #Detect collision with wall
    if game_snake.head.xcor() > 280 or game_snake.head.xcor() < -280 or game_snake.head.ycor() > 280 or game_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    #Detect collision with tail
    for segment in game_snake.segments[1:]:
        if game_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    
screen.exitonclick()
