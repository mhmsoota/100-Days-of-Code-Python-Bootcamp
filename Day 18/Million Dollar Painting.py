from turtle import *
import colorgram as c
from random import choice

# rgb_colors = []
# colors = c.extract("image.jpg",40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

rgb_colors = [ (1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), 
                (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), 
                (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), 
                (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), 
                (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), 
                (145, 227, 217), (122, 193, 147), (220, 177, 216), 
                (100, 218, 229), (117, 171, 192), (79, 135, 178), 
                (252, 197, 0), (29, 84, 92), (228, 174, 166), 
                (186, 190, 201), (73, 73, 39)]

t = Turtle()
s = Screen()
s.screensize(1000, 1000)
s.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

def draw_small_circle(x, y):
    chosen_color = choice(rgb_colors)
    # t.pencolor(chosen_color)
    # t.fillcolor(chosen_color)
    t.goto(x,y)
    # t.begin_fill()
    # t.circle(20)
    # t.end_fill()
    t.dot(20, chosen_color)

for column in range (-350, -350+500, 50):
    for row in range(-350, -350+500, 50):
        draw_small_circle(row, column)
s.exitonclick( )