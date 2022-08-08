import turtle
window = turtle.Screen()

def moveUp():
    x, y = pen.position() 
    pen.setposition(x, y+5)
def moveDown():
    x, y = pen.position() 
    pen.setposition(x, y-5)
def moveLeft():
    x, y = pen.position() 
    pen.setposition(x-5, y)
def moveRight():
    x, y = pen.position() 
    pen.setposition(x+5, y)
def change():
    if pen.isvisible(): 
        pen.up()
        pen.hideturtle()
    else:
        pen.down
        pen.showturtle()

window = turtle.Screen()
pen = turtle.Turtle()


window.onkey(moveUp,"Up")
window.onkey(moveDown,"Down")
window.onkey(moveLeft,"Left")
window.onkey(moveRight,"Right")
window.onkey(change,"space")

window.listen()
window.mainloop()







