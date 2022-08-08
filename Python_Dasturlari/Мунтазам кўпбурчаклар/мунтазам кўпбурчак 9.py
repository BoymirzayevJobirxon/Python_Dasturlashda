import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('blue')
t.speed(5)

def rightangle(n,dlina):
    sumangle = 180*(n-2)
    if sumangle%n == 0:
        angle = sumangle/n 
        for j in range(n):
            t.forward(dlina)
            t.left(180-angle)
for j in range(3,12):
    rightangle(j,50)
window.mainloop()
