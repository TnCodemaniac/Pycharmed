

import turtle



def colored_star():
    turtle.speed(100)

    size = 80

    turtle.color("blue")

    turtle.width(10)


    angle = 120


    turtle.fillcolor("purple")
    turtle.begin_fill()


    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)



    turtle.end_fill()



colored_star()
turtle.end_fill()
colored_star()
turtle.penup()
turtle.left(270)
turtle.forward(100)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(40)
turtle.write("Star road", move=False, align="left", font=("Comic Sans MS", 15, "normal"))
turtle.fillcolor("yellow")
turtle.penup()
turtle.forward(1250000)



t = turtle.Turtle()
turtle.fillcolor("cyan")
turtle.begin_fill()
t.color("blue")
t.width(10)
r = 100
t.circle(r)
t.speed(100)
t.forward(10000)



t.end_fill()






