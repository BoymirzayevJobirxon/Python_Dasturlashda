import turtle
window = turtle.Screen()
turtle.setup(500,300)
window.bgcolor('Black')
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-130,-90)
t.pendown()
for i in range(2):
    for colours in ['red', 'magenta','blue',"cyan", 'green', 'yellow', 'white']:
        t.color(colours)
        t.pensize(3)
        t.circle(100)
        t.forward(20)
window.mainloop()
