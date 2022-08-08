import turtle
window = turtle.Screen()
t = turtle.Turtle()

def circle(x,y):
    t.hideturtle()
    size = 5
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.dot(size, "red")
    t. penup ()
    t.pencolor("black")
    t.backward(40)
    t.pendown()
    print(x)
    t.write(x)
    t. penup()
    t.forward(50)
    t.pendown()
    print(y)
    t.write(y)
turtle.onscreenclick(circle)

window.mainloop()
