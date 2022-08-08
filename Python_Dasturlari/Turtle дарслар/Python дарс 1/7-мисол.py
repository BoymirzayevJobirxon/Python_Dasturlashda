from turtle import *
t = Turtle()
t.screen.setup(450, 450)
t.up()
t.goto(-225, 0)
t.down()
t.setheading(270)
for i in range(5):
    t.circle(25, 180)
    t.begin_fill()
    t.circle(-25, 180)
    t.end_fill()
t.screen.exitonclick()
t.screen.mainloop()
