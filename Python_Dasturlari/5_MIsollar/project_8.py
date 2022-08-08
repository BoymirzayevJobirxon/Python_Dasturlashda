# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 8. Калькулятор

  project_8.py - начальный вариант

"""
from simpletk import *
from int_edit import TIntEdit

app = TApplication("Калькулятор")
app.size = (160, 192)
x1 = 0
x2 = 0
oper = None
nextNumber = False

f = ("Courier New", 12)
disp = TIntEdit(app, width=14, font=f)
disp.position = (8, 8)

b = ['7', '8', '9', 'C', 
     '4', '5', '6', '/',
     '1', '2', '3', '*', 
     '0', '=', '+', '-']

btn = []
for r in range(4):
  for c in range(4):
    k = 4*r + c
    btn.append(TButton(app, text=b[k], font=f, width=2))
    btn[k].position = (8+38*c, 40+38*r)
btn[3]["fg"] = "red"    

def doClear ( sender ):
  global nextNumber
  disp.text = ""
  print('cl>', disp.text)
  nextNumber = False

def doCalc ( sender ):
  global nextNumber, oper, x1, x2
  if not oper: return
  x2 = disp.value
  if oper == "+": res = x1 + x2
  elif oper == "-": res = x1 - x2
  elif oper == "*": res = x1 * x2
  elif oper == "/": res = x1 // x2
  disp.text = str(res)
  nextNumber = True

def doOperation ( sender ):
  global nextNumber, oper, x1
  x1 = disp.value
  oper = sender["text"]
  nextNumber = True

def doDigit ( sender ):
  global nextNumber
  if nextNumber:
    disp.text = ""
    nextNumber = False
  disp.text  = disp.text + sender["text"]

for k in [0, 1, 2, 
          4, 5, 6, 
          8, 9, 10, 
          12]:
  btn[k].onClick = doDigit

for k in [7, 11, 14, 15]:
  btn[k].onClick = doOperation

btn[13].onClick = doCalc
  
btn[3].onClick = doClear  

app.Run()
