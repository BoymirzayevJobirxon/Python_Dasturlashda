import turtle
window = turtle.Screen()
#t = turtle.Turtle()

colors=["red",  "purple", "blue","green", 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x) 
    t.left(59)

window.mainloop()
