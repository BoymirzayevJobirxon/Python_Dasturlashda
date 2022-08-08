import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('blue')
t.pensize(3)


for i in range(5):
    t.fd(150)
    for j in range(5):
        t.fd(50)
        t.left(144)
    t.left(144)

window.mainloop()
