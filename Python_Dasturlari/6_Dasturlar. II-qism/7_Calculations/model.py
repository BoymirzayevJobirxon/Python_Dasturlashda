# -*- coding: utf-8
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  Модуль к программе 20_calculator.py - калькулятор 

"""

def priority( op ):
  if op in "+-": return 1
  if op in "*/": return 2
  return 100

def lastOp( s ):
  minPrt = 50
  k = -1
  for i in range(len(s)):
    if priority(s[i]) <= minPrt:
      minPrt = priority(s[i])
      k = i
  return k

def oper( op, n1, n2 ):
  if op == "+":   return n1 + n2
  elif op == "-": return n1 - n2
  elif op == "*": return n1 * n2
  else:           return n1 // n2

def calc ( s):
  k = lastOp ( s )
  if k < 0:         # вся строка - число
    return int(s) 
  else:
    n1 = calc( s[:k] )   # левая часть 
    n2 = calc( s[k+1:] ) # правая часть 
     # выполнить операцию 
    return oper(s[k], n1, n2)
