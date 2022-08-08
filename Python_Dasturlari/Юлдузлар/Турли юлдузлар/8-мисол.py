from turtle import*
t = Turtle()
#t.screen.setup(450, 450)
#t.screen.bgcolor('Black')
t.speed(50)
t.pensize(2)
t.color('blue')
        
for j in range(100):
    for colours in ['violet','indigo','blue','green','blue','red']:
        t. color (colours)
        t.forward(2*j)
        t.left(150)
t.forward(50)
    
t.screen.mainloop()
