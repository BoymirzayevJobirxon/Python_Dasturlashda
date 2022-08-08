import turtle
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'white', 'gray']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for i in range(30):
    x = random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    у = random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    size = random.randint(10,75)
    color = random.choice(colors)
    t.penup()
    t.setpos(x,у)
    t.left(random.randint(0,360))
    t.color(color)
    t.begin_fill()
    t.pendown()
    for j in range(5):
        t.forward(size)
        t.left(225)
        t.forward(size)
        t.left(63)
    t .end_fill()
#turtle.mainloop()