import turtle   #Снаружи
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
t = turtle.Turtle()
t.color("blue")
def sqrfunc(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size = size-5
dlina = 146
while dlina > 6:
    sqrfunc(dlina)
    dlina = dlina - 20
wn.mainloop()
