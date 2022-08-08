from turtle import Turtle, Screen
from math import pi, sin, cos
from random import randint, random

RADIUS = 180  # roughly the radius of a completed spiral

screen = Screen()

WIDTH, HEIGHT = screen.window_width(), screen.window_height()

turtle = Turtle(visible=False)
turtle.speed('fastest')  # because I have no patience

turtle.up()

for _ in range(2):
    x = randint(RADIUS - WIDTH//2, WIDTH//2 - RADIUS)
    y = randint(RADIUS - HEIGHT//2, HEIGHT//2 - RADIUS)
    turtle.goto(x, y)

    turtle.color(random(), random(), random())
    turtle.down()

    for i in range(200):
        t = i / 20 * pi
        dx = (1 + 5 * t) * cos(t)
        dy = (1 + 5 * t) * sin(t)

        turtle.goto(x + dx, y + dy)

    turtle.up()

screen.exitonclick()
