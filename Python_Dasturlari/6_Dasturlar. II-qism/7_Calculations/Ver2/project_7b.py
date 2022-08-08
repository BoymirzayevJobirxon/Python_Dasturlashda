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

  Версия 2: + использование вещественных чисел
            + использование скобок

"""
from model import Calc
from simpletk import *

app = TApplication("Калькулятор")
app.size = (200, 150)

Input = TComboBox(app, values=[], height=1)
Input.align = "top"
Input.text = "(2.3+4.2)*(5.6-2.8)"

Answers = TListBox(app)
Answers.align = "client"

def doCalc(event):
  expr = Input.text
  x = Calc(expr)
  Answers.insert(0, expr+"="+str(x))
  if not Input.findItem(expr):
    Input.addItem(expr)

Input.bind('<Key-Return>', doCalc)

app.Run()
