# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 8. Калькулятор

  project_8-oop.py - вариант полностью в стиле ООП
  
"""
from simpletk import *
from int_edit import TIntEdit

class TCalculator(TApplication):
  def __init__(self):
    TApplication.__init__(self, "Калькулятор")
    self.size = (160, 192)
    self.x1 = 0
    self.x2 = 0
    self.oper = None
    self.nextNumber = False
    f = ("Courier New", 12)
    self.disp = TIntEdit(self, width=14, font=f)
    self.disp.position = (8, 8)
    bNames = ['7', '8', '9', 'C', 
         '4', '5', '6', '/',
         '1', '2', '3', '*', 
         '0', '=', '+', '-']
    btn = []
    for r in range(4):
      for c in range(4):
        k = 4*r + c
        btn.append(TButton(self, text=bNames[k], font=f, width=2))
        btn[k].position = (8+38*c, 40+38*r)
    btn[3]["fg"] = "red"    
    for k in [0, 1, 2, 
              4, 5, 6, 
              8, 9, 10, 
              12]:
      btn[k].onClick = self.doDigit    
    for k in [7, 11, 14, 15]:
      btn[k].onClick = self.doOperation    
    btn[13].onClick = self.doCalc      
    btn[3].onClick = self.doClear  

  def doClear ( self,  sender ):
    self.disp.text = ""
    self.nextNumber = False

  def doCalc ( self, sender ):
    if not self.oper: return
    self.x2 = self.disp.value
    if self.oper == "+": res = self.x1 + self.x2
    elif self.oper == "-": res = self.x1 - self.x2
    elif self.oper == "*": res = self.x1 * self.x2
    elif self.oper == "/": res = self.x1 // self.x2
    self.disp.text = str(res)
    self.nextNumber = True

  def doOperation ( self, sender ):
    self.x1 = self.disp.value
    self.oper = sender["text"]
    self.nextNumber = True

  def doDigit ( self, sender ):
    if self.nextNumber:
      self.disp.text = ""
      self.nextNumber = False
    self.disp.text = self.disp.text + sender["text"]

app = TCalculator()
app.Run()
