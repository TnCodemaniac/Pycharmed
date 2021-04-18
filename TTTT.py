

import turtle
turtle.penup()
turtle.speed(1000000)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.write("The Game Name",move=False,  align="left", font=("Comic Sans MS", 15, "normal"))
turtle.forward(10000000)
t = turtle.Turtle()
turtle.fillcolor("cyan")
turtle.begin_fill()
t.color("blue")
t.width(10)
r =100

t.penup()
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
t.circle(r)
t.speed(100)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)


import math
from itertools import cycle
from turtle import Turtle, Screen

COLORS = cycle(['red', 'green', 'blue', 'yellow'])

def rotate_polygon(polygon, angle):

    theta = math.radians(angle)
    sin, cos = math.sin(theta), math.cos(theta)

    return [(x * cos - y * sin, x * sin + y * cos) for x, y in polygon]

def fill_polygon(turtle, polygon, color):

    turtle.color(color)

    for vertex in polygon:
        turtle.goto(vertex)

        if not turtle.filling():
            turtle.begin_fill()

    turtle.end_fill()

polygon = ((100, -28.85), (50, 57.75), (0, -28.85))

screen = Screen()

yertle = Turtle(visible=False)
yertle.penup()

for angle in range(0, 360, 30):
    rotated_polygon = rotate_polygon(polygon, angle)
    color = next(COLORS)
    fill_polygon(yertle, rotated_polygon, color)
    import turtle
    turtle.penup()
    turtle.goto(-150,150)
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
        turtle.goto(10000,100000)
screen.exitonclick()


