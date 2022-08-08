import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('yellow')
window.bgcolor('blue')
t.pensize(3)
t.speed(10)

def kvadr():
    for i in range(4):
        t.forward(80)
        t.left(90)
for j in range(12):
    kvadr()
    t.left(30)

t.screen.mainloop()
