import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color("yellow")
t.speed(6)
t.pensize(2)

def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window.bgcolor("black")
    for i in range(1,37):
        draw_square(t)
        t.right(10)
draw_art()
window.mainloop()
