from turtle import *
shape("turtle")
wheel=12
bgcolor("blue")
pensize(10)
pencolor("red")
goto(100,0)
for i in range(wheel):
    begin_fill() ;
    rt (90)
    fd(200)
    lt(120)
    fd (200)
    lt(120)
    fd (200)
    end_fill()
    fd (200)
exitonclick()
