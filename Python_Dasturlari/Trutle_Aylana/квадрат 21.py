from turtle import *
speed(0)
bgcolor('black')
pensize(3)
for x in range(15):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        color(colours)
        left(12)
        for j in range(4):
            forward(200)
            left(90)
exitonclick()
        
