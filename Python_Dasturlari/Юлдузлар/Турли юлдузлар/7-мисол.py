from turtle import *
t = Turtle()
t.screen.bgcolor('blue')
t.color('yellow')
t.pensize(3)
for i in range(10):
    for j in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.right(36)

t.screen.exitonclick()

