from turtle import *
t = Turtle()
t.screen.setup(450,450)
t.screen.bgcolor("lightgreen")
t.color('red')
t.pensize(3) 
for i in range(12):
    t.fd(8)
    t.up()
    t.fd(8)
    t.down()

t.screen.mainloop()





