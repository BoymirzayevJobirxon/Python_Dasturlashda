from turtle import *
t = Turtle()
t.screen.setup(400, 300)
def rectangle(w, h):
    for i in range(2):
        t.left(90)
        t.fd(h)
        t.left(90)
        t.fd(w)        
rectangle(150, 50)
t.screen.exitonclick()
t.screen.mainloop()
