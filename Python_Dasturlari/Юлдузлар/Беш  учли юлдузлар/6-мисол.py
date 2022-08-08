import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('black')
t.color('yellow')

def starfill(n,dlina):
    t.begin_fill()
    if n%2 != 0:
            for j in range(n):
                    t.forward(dlina)
                    angle = n//2*360/n
                    t.left(angle)
    t.end_fill()
starfill(5,100)

window.mainloop()
