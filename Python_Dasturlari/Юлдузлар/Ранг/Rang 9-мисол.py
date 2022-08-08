import turtle, random, time
window = turtle.Screen()
def chooseRandomColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red,green, blue
bob = turtle.Turtle()
bob.color(chooseRandomColor())
bob.forward(100)
window.mainloop()
