import turtle, random
window = turtle.Screen()
t = turtle.Turtle()

def starfill(n,dlina):
    t.begin_fill()
    if n%2 != 0:
            for j in range(n):
                    t.forward(dlina)
                    angle = n//2*360/n
                    t.left(angle)
    t.end_fill()
t.screen.setup(700, 500)
t.screen.bgcolor('Black')
t.speed(100)
t.color('yellow')
for i in range(50):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220) 
    t.up()
    t.setposition(x,y)
    t.down
    size = random.randint(10, 20)
    vershina = random.choice([5, 7, 9,11,13,15])
    starfill(vershina,size)
   
window.mainloop()
