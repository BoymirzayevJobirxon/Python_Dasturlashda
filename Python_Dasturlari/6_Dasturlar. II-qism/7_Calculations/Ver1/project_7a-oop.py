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

  *** Проект полностью в стиле ООП ***

"""
from model import Calc
from simpletk import *

class TCalculator(TApplication):
  def __init__(self):
    TApplication.__init__(self, "Калькулятор")
    self.size = (200, 150)

    self.Input = TComboBox(self, values=[], height=1)
    self.Input.align = "top"
    self.Input.text = "2+2"
    self.Input.bind('<Key-Return>', self.doCalc)
  
    self.Answers = TListBox(self)
    self.Answers.align = "client"

  def doCalc(self, event):
    expr = self.Input.text
    x = Calc(expr)
    self.Answers.insert(0, expr+"="+str(x))
    if not self.Input.findItem(expr):
      self.Input.addItem(expr)
    
app = TCalculator()  
app.Run()
