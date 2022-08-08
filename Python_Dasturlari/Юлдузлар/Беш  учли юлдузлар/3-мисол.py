import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('green')
t.color('yellow')
t.pensize(3)

def star(n,dlina):
        if n%2 != 0:
                for j in range(n):
                        t.forward(dlina)
                        angle = n//2*360/n
                        t.left(angle)
star(5,200)

window.mainloop()


