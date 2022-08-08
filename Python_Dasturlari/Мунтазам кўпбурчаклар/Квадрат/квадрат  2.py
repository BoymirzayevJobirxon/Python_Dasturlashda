import turtle
window = turtle.Screen()
window.bgcolor('blue')
t = turtle.Turtle()
t.color('yellow')
t.pensize(3)
t.speed(10)
def kuadrado(size): 
  for i in range(36): #draw the circle of squares
   t.forward(size)
   t.right(90)
   t.forward(size)
   t.right(90)
   t.forward(size)
   t.right(90)
   t.forward(size)
   t.right(100)
kuadrado(100)
window.mainloop()
