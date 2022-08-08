
from turtle import *
t = Turtle()
t.screen.setup(400, 300)
for i in range(10):
    t.fd(8)
    t.up()
    t.fd(8)
    t.down() 
t.screen.exitonclick()
t.screen.mainloop()
