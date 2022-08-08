import turtle
window = turtle.Screen()
turtle.setup(400,400)
t = turtle.Turtle()
t.speed(10)

t.goto(0,-20)

for i in range(313):
    t.forward(1)
    t.left(1.15)    

t.color('blue')
for i in range(313):
    t.pensize(2)
    t.forward(2)
    t.left(1.15)


    
window.mainloop()
