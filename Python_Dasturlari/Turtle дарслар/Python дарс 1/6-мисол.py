from turtle import *
t = Turtle()
t.screen.setup(400, 300)
def circ(d, r, rBig):
    for i in range(d):
        t.circle(rBig, 360 / d)
        t.dot(r, "red")
t.up()
t.goto(80, 0)
t.setheading(90)
t.down()
circ(45, 5, 100)
t.screen.exitonclick()
t.screen.mainloop()
