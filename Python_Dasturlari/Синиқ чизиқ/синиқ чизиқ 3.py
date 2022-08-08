import turtle  #Наизнанку
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5
dlina = 6
while dlina < 166:
    sqrfunc(dlina)
    dlina = dlina + 20
wn.mainloop()
