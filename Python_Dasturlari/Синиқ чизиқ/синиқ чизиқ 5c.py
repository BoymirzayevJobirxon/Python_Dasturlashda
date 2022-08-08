import turtle
window = turtle.Screen()
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
sides = 5
colors = ['red', 'yellow', 'blue', 'orange',
          'green', 'purple', 'brown', 'white', 'grey', 'pink'][:sides]
for x in range(80):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)

window.mainloop()
