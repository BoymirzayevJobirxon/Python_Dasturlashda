# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru                                                                           .

  Глава 7. Объектно-ориентированное программирование
  Проект № 7. Модель и представление. Вычисления

  project_7.py - строковый калькулятор

  Версия 3: + использование функций abs, sqrt, sin, cos

"""
from model import Calc
from simpletk import *

app = TApplication("Калькулятор")
app.size = (300, 150)

Input = TComboBox(app, values=[], height=25)
Input.align = "top"
Input.text = "sin(1.2)*sqrt(1.7)/abs(cos(3.2))"

Answers = TListBox(app, values=[])
Answers.align = "client"

def doCalc(event):
  expr = Input.text
  x = Calc(expr)
  Answers.insert(0, expr+"="+str(x))
  if not Input.findItem(expr):
    Input.addItem(expr)

Input.bind('<Key-Return>', doCalc)

app.Run()
