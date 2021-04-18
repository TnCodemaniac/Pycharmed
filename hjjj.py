
import turtle
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    s= int(num_str)

angle = 180 - 180*(10-2)/10

turtle.up

x = 0
y = 0
turtle.setpos(x,y)


numshapes = 8
for x in range(numshapes):
    turtle.color("red")
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        print (turtle.pos())
        turtle.up()
        turtle.end_fill()
