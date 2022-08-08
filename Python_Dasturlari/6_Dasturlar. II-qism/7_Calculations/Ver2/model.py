# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru                                                                           .

  Глава 7. Объектно-ориентированное программирование
  Проект № 7. Модель и представление. Вычисления

  model.py - модуль, выполняющий вычисления

  Версия 2: + использование вещественных чисел
            + использование скобок

"""

def priority(op):
  if op in "+-": return 1
  if op in "*/": return 2
  return 100

def lastOp(s):
  minPrt = 50
  k = -1
  nest = 0
  for i in range(len(s)):
    if s[i] == '(': nest += 1
    elif s[i] == ')': nest -= 1
    elif nest == 0 and priority(s[i]) <= minPrt:
      minPrt = priority(s[i])
      k = i
  return k

def Calc ( s):
  k = lastOp ( s )
  if k < 0:         # вся строка - число
    if s[0] == '(':
      return Calc( s[1:-1] )
    return float(s)
  else:
    n1 = Calc( s[:k] )   # левая часть
    n2 = Calc( s[k+1:] ) # правая часть
     # выполнить операцию
    if   s[k] == "+": return n1 + n2
    elif s[k] == "-": return n1 - n2
    elif s[k] == "*": return n1 * n2
    else: return n1 / n2