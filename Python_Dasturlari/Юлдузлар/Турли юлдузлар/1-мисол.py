import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('blue')
t.color('yellow')

def starfill(n,uzunlik):
    t.begin_fill()
    if n%2 != 0:
            for j in range(n):
                    t.forward(uzunlik)
                    angle = n//2*360/n
                    t.left(angle)
    t.end_fill()

starfill(7,150)

window.mainloop()
