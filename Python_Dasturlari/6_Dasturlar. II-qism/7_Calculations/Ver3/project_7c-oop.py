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

  Версия 3-4: + использование функций abs, sqrt, sin, cos
              + оформление в виде класса
              + запись в файл (логирование)

  *** Проект полностью в стиле ООП ***

"""
from model import Calc
from simpletk import *
from tkinter.messagebox import showerror

class TCalculator(TApplication):
  def __init__(self):
    TApplication.__init__(self, "Калькулятор")
    self.size = (300, 150)

    self.Input = TComboBox(self, values=[], height=1)
    self.Input.align = "top"
    self.Input.text = "sin(1.2)*sqrt(1.7)/abs(cos(3.2))"
    self.Input.bind('<Key-Return>', self.doCalc)

    self.Answers = TListBox(self)
    self.Answers.align = "client"

  def log(self, s):
    with open("results.txt", "a") as file:
      file.write( s+"\n")

  def doCalc(self, event):
    expr = self.Input.text
    try:
      x = Calc(expr)
      self.Answers.insert(0, expr+"="+str(x))
      if not self.Input.findItem(expr):
        self.Input.addItem(expr)
        self.log( expr+"="+str(x) )
    except:
      showerror("Ошибка", "Неверное выражение \n"+expr)
      self.log( "Неверное выражение "+expr )

app = TCalculator()
app.Run()
