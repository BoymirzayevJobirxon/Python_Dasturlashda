import turtle
window = turtle.Screen()

t = turtle.Turtle()
t.screen.setup(450, 450)
t.shape('turtle')
t.color('red')
t.fillcolor('cyan')
t.begin_fill()
t.circle(100, 360, 5)
t.end_fill()

window.mainloop()

