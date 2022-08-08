import turtle
window = turtle.Screen()
window.bgcolor('lightgreen')
turtle.setup(480,420)

t1 = turtle.Turtle()
t1.shapesize(2,2)
t1.shape('arrow')
t1.color('red','yellow')
t1.forward(200)

t2 = turtle.Turtle()
t2.shapesize(2,2)
t2.shape('turtle')
t2.color('blue','cyan')
t2.left(60)
t2.forward(200)

t3 = turtle.Turtle()
t3.shapesize(2,2)
t3.shape('circle')
t3.color('green','red')
t3.left(120)
t3.forward(200)

t4 = turtle.Turtle()
t4.shapesize(2,2)
t4.shape('square')
t4.color('violet','green')
t4.left(180)
t4.forward(200)

t5 = turtle.Turtle()
t5.shapesize(2,2)
t5.shape('triangle')
t5.color('black','violet')
t5.left(240)
t5.forward(200)

t6 = turtle.Turtle()
t6.shapesize(4,4)
t6.shape('classic')
t6.color('magenta','orange')
t6.left(300)
t6.forward(220)

window.mainloop()













