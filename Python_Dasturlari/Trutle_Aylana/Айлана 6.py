
import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('lightgreen')
t.color('blue')

for i in range(10, 100, 10):
     t.circle(i) 
    
window.mainloop()
