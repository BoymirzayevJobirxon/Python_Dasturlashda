import turtle
window = turtle.Screen()
turtle.setup(400,400)
t = turtle.Turtle()
window.bgcolor('blue')
t.color('yellow')
t.speed(10)
t.pensize(2)
t.up()
t.goto(-120,-110)
t.down()

def kv(a):
    for i in range(4): 
        t.forward(a) 
        t. left (90)
n = 10	
for i in range(25):	
    kv(n) 
    n = n + 10
window.mainloop()
