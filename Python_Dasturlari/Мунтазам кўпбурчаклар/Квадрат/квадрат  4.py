import turtle
window = turtle.Screen()
turtle.speed(0)
turtle.bgcolor('black')

for i in range(5):
    for colours in ["red",  "purple", "blue","green", "yellow", "orange"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
window.mainloop()
