from turtle import *
from random import randint
speed(10)
penup()
goto(-250,140)
forward(100)

for step in range(15):
    write(step, align='center') #вывести число
    right(90) #повернуть направо на 90 градусов
    forward(10) #отойти от числа на 10 шагов
    pendown() #опустить перо
    forward(150) #пройти вперед 150 шагов
    penup()  #поднять перо
    backward(160) #идти назад 160 шагов
    left(90) #повернуть налево на 90 градусов forward(20)
    forward(20)
    #Добавление и настройка первой черепашки
ada = Turtle()
ada.color('red')
ada. shape('turtle')
ada.penup()
ada.goto(-160,110)
ada.pendown()

bob = Turtle()
bob.color('Blue')
bob. shape('turtle')
bob.penup()
bob.goto(-160,80)
bob.pendown()

ali = Turtle()
ali.color('Green')
ali. shape('turtle')
ali.penup()
ali.goto(-160,50)
ali.pendown()

alik = Turtle()
alik.color('Black')
alik. shape('turtle')
alik.penup()
alik.goto(-160,20)
alik.pendown()

#Перемещение черепах
for move in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    ali.forward(randint(1,5))
    alik.forward(randint(1,5))
