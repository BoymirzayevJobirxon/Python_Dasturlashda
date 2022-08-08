import turtle
window = turtle.Screen()

t = turtle.Turtle()
t.speed(10)

window.bgcolor('lightgreen')
t.color('orange')

к = turtle
turtle.speed(0)
print(turtle.pos())
def square(x):           # Квадрат чизилади
    turtle.forward(x)
    for _ in range(3):
        turtle.left(90)
        turtle.forward(x)
    turtle.left(90)
def hex(x):               #   Учбурчак чизади
    turtle.forward(x)
    for _ in range(5):
        turtle.left(60)
        turtle.forward(x)
        turtle.left(60)
def sql(x):
        turtle.lett(177)
def pat3():
    for i in range(10):
       for _ in range (4):
           sql(15+i*15)
           turtle.left(45)
def pat4():
    for i in range(10) :
        for _ in range(40):
            # square(x)
            hex(100)
            turtle.left(15)

for i in range(30):            
    x=100
    pat4()

