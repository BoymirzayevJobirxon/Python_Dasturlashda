import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('blue')
t.color('yellow')

def star(n,dlina):
        if n%2 != 0:
                for j in range(n):
                        t.forward(dlina)
                        angle = n//2*360/n
                        t.left(angle)
def starfill(n,dlina):
    t.begin_fill()
    star(n,dlina)
    t.end_fill()
starfill(5,150)

window.mainloop()

