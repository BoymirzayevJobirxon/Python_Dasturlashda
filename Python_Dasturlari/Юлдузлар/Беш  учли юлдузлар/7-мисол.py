
import turtle, random
window = turtle.Screen()
t = turtle.Turtle()

window.bgcolor('lightgreen')
t.color('orange')

def starfill(n,dlina):
    t.begin_fill()
    if n%2 != 0:
            for j in range(n):
                    t.forward(dlina)
                    angle = n//2*360/n
                    t.left(angle)
    t.end_fill()

for i in range(10):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220) 
    t.up()
    t.setposition(x,y)
    t.down
    starfill(5,50)

window.mainloop()
