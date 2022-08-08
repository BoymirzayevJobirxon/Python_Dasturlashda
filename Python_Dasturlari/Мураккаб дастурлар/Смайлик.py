import turtle
window = turtle.Screen()
t = turtle.Turtle()

t.width(2)
#
t.up()
x = 0
y=-100
t.goto (x, y)
t.begin_fill()
t.color('#ffaa00')
t.down()
t.circle(100)

t.end_fill()
t.color('black')
t.circle(100)
t.up ()
#
x=-45
y=50
t.goto (x, y)
t.down()
t.color('#0000aa')
t.begin_fill()
t.circle(7)
t.up()
t.end_fill()
#
x=45
y=50
t.goto(x, y)
t.down()
t.color('#0000aa')
t.begin_fill()
t.circle(7)
t.up()
t.end_fill()
#
х=-55
у=-50
t.goto(х, у)
t.right(45)
t.width(3)
t.down()
t.color('#aa0000')
t.circle(80, 90)
t.up ()
#
x=0
y=50
t.goto (x, y)
t.right(135)
t.width(3)
t.down()
t.color('#000000')
t.forward(100)
window.mainloop()
