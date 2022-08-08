import turtle
window = turtle.Screen()
turtle.setup(400,400)
hz = turtle.Turtle()
hz.speed(10)



# hz.shape("cat")
hz.color('green', 'yellow')

cl = ['red','green','blue','yellow']
hz.speed(50)
def drawArt(angle,d,x,y):

    hz.up()
    hz.goto(x,y)
    hz.down()
    c = 0
    for i in range(1,200):
        hz.pencolor(cl[c])
        hz.forward(d)
        hz.left(angle)
        # d = d - 2
        d = d - 1
        c = c + 1
        if(c>3):
            c = 0
# drawArt(140,100,0,0)
# drawArt(90,100,0,0)
drawArt(98,150,0,0)
