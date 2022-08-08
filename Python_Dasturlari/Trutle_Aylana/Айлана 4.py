import turtle
t = turtle.Turtle()
window = turtle.Screen()
t.color('blue')
t.speed(10)
for j in range(0,360,15):
    t.left(j)
    t.circle(50)
    
turtle.clear
window.mainloop()
