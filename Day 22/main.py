from pong import Pong
from turtle import Screen, Turtle
from paddle import *
from c import *
from time import sleep
from score import Score

screen = Screen()
screen.setup(width=HALF_SCREEN_WIDTH, height=HALF_SCREEN_HEIGHT)
screen.bgcolor("black")
sleep(3)
screen.tracer(0)
right_paddle = Paddle((HALF_SCREEN_WIDTH-50, 0))
left_paddle = Paddle((-HALF_SCREEN_WIDTH+50, 0))
pong = Pong()
scoreboard = Score()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.05)
    pong.moveto()
    pong.detect_collision_and_bounce()
    
    
    if pong.xcor() > HALF_SCREEN_WIDTH - 25:
        pong.detect_collision_and_bounce(only_bounce=True)
        scoreboard.left_gets_point()
    elif pong.xcor() < -HALF_SCREEN_WIDTH + 25:
        pong.detect_collision_and_bounce(only_bounce=True)
        scoreboard.right_gets_point()


    #Detect collision with paddles
    if pong.distance(right_paddle)<50 and pong.xcor()>HALF_SCREEN_WIDTH-80 or pong.distance(left_paddle)<50 and pong.xcor()>-HALF_SCREEN_WIDTH+80:
        pong.bounce_for_x()

screen.exitonclick()
