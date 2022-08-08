import turtle
window = turtle.Screen()
t = turtle.Turtle()


europe = turtle.Turtle()
africa = turtle.Turtle() 
america = turtle.Turtle()
asia = turtle.Turtle()
avstralia = turtle.Turtle()

for i in [europe, africa, america, asia,avstralia]:
    i.up()
r =70   
europe.goto(-2*r,2*r)
africa.goto(0,2*r)
america.goto(2*r,2*r)
asia.goto(-r,r)
avstralia.goto(r,r)

for i in [europe, africa, america, asia,avstralia]:
    i.down()
    
europe.color('blue')
africa.color('Black')
america.color('red')
asia.color('yellow')
avstralia.color('green')

for i in [europe, africa, america, asia,avstralia]:
    i.pensize(5)
    i.circle(r)
window.mainloop()

