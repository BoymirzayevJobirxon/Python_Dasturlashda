import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('red')

n = 5
sumangle = 180*(n-2)
angle = sumangle/n 

for j in range(n):
    t.forward(100)
    t.left(180-angle)

window.mainloop()
