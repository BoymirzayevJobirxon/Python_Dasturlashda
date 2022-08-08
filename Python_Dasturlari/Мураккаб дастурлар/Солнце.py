# Рисуем солнце и дом.
 
from tkinter import *
import turtle
turtle.bgcolor("light green")  # Цвет фона - светло зелёный
 
# Рисуем солнце с оранжевым контром и жёлтым фоном
 
turtle.color("orange", "yellow")
turtle.begin_fill()
turtle.penup()
turtle.goto(-250, 160)
turtle.pendown()
turtle.circle(45)
turtle.end_fill()
 
# Рисуем дом
# Рисуем прямоугольник с синим контуром и жёлтым фоном
turtle.color("blue", "pink")
turtle.begin_fill()
turtle.penup()
turtle.goto(85, 85)
turtle.right(90) # поворациваем на 90 градусов
turtle.pendown()
turtle.forward(120) 
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(120)
 
turtle.right(90)
turtle.forward(120)
turtle.end_fill()
 
#Рисуем крышу с синим контуром и коричневым фоном
 
turtle.color("blue", "brown")
turtle.begin_fill()
turtle.penup()
turtle.goto(108, 85)
turtle.right(225)
turtle.pendown()
turtle.forward(120)
 
turtle.left(90)
turtle.forward(120)
 
turtle.left(135) # Повернуть курсор влево на 135 градусов
turtle.forward(170)
turtle.end_fill()
 
# Рисуем окно с синим контуром и голубого цвета
 
turtle.color ("blue", "light blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(50, 50)
turtle.right(90)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()
 
# Рисуем трубу с синим контуром и серым фоном
 
turtle.color("blue", "grey")
turtle.begin_fill()
turtle.penup()
turtle.goto(50, 192)
turtle.pendown()
turtle.forward(20)
turtle.right(90)
turtle.forward(70)
turtle.right(135)
turtle.forward(30)
turtle.right(45)
turtle.forward(50)
turtle.end_fill()
 
# Выводим сообщения церного и красного цвета со шрифтом "Arial"
 
turtle.penup()
turtle.goto (-290, -150)
turtle.color ("black")
turtle.write("Иш бажарилди", font=("Arial", 18, "bold"))
turtle.goto (-100, -190)
turtle.color ("red")
turtle.write("Эътиборингиз учун рамат", font=("Arial", 18, "bold"))
turtle.done()
t.screen.exitonclick()
t.screen.mainloop()









             
