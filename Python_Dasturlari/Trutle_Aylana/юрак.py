import turtle
window = turtle.Screen()
window.bgcolor('black')
turtle.setup(400,400)
t = turtle.Turtle()
t.pensize(3)
t.speed(0)

t.color('red','pink')

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


t.begin_fill()
t.left(140)
t.forward(111.65)
curve()
t.left(120)
curve()
t.forward(111.65)
t.end_fill()
t.hideturtle()

    
window.mainloop()
