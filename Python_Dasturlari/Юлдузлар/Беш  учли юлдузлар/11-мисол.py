import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('blue')

for i in range(20):
    t.forward(i * 10)
    t.right(144)
window.mainloop()
