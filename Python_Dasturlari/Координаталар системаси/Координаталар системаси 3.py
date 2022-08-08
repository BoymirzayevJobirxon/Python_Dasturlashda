import turtle
window = turtle.Screen()
turtle.tracer(0)
turtle.setup(700,700)
t = turtle.Turtle()
t.speed(10)



for x in range(4) :
    for у in range(6):
        t.forward(50)
        t.right(90)
        t.forward(5)
        t.backward(10)
        t.forward(5)
        t.left(90)
    t.backward(300)
    t.right(90)

t.pencolor("blue")
t.penup()
t.setpos(4,1)
t.pendown()
t.write("0", font=("Ariel",16, "bold"))

t.penup()
t.setpos(4,300)
t.pendown()
t.write("y", font=("Ariel",16, "bold"))




t.penup()
t.setpos(300, 1)
t.pendown()
t.write("x", font=("Ariel",16, "bold"))



t.penup()
t.setpos(42, -20)
b = 50
t.pendown()
for d in range(6):
    t.write(b)
    t.penup()
    t.forward(50)
    t.pendown()
    b = b + 50

t.penup()
t.left(90)
t.setpos(-25,42)
b = 50
t.pendown()
for d in range(6):
    t.write(b)
    t.penup()
    t.forward(50)
    t.pendown()
    b = b + 50

t.penup()
t.left(90)
t.setpos(-60, -20)
t.pendown()
b = -50
for r in range(6):
    t.write(b)
    t.penup()
    t.forward(50)
    t.pendown()
    b = b - 50

t.penup()
t.right(90)
t.setpos(-28,-60)
t.pendown()
b = -50
for c in range(6):
    t.write(b)
    t.penup()
    t.backward(50)
    t.pendown()
    b = b - 50
    
def circle(x,y):
    t.hideturtle()
    size = 5
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.dot(size, "red")
    t. penup ()
    t.pencolor("black")
    dx = 8*len(str(int(x)))
    t.goto(x-dx, y-8)
    t.pendown()
    t.write(int(x))
    t. penup()
    t.goto(x+10, y-8)
    t.pendown()
    t.write(int(y))
turtle.onscreenclick(circle)

window.mainloop()



window.mainloop()
