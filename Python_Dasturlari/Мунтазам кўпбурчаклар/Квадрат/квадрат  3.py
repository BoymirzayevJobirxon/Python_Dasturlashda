import turtle
window = turtle.Screen()
window.bgcolor('Black')
t = turtle.Turtle()
t.color('yellow')
t.speed(10)

def draw_square(m_turtle):
    for j in range(1,5):
        t.forward(100)
        t.right(90)
def draw_art():
    t.pensize(2)
    for  j in range(1,37):
        draw_square(t)
        t.right(10)
draw_art()

window.mainloop()
