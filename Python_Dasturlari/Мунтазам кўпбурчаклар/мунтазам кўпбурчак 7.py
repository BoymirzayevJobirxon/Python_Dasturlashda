import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('green')

n = 3
angle = 60

for j in range(n):
    t.forward(100)
    t.left(180-angle)

window.mainloop()
