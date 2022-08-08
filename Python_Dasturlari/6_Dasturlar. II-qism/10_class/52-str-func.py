# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 52. Строки в функции
 Вход: 
   нет 
 Результат: 
   A12B.A12B.A12B
   A12B.A12B.A12B
"""

def replaceAll ( s, wOld, wNew ):
  lenOld = len(wOld)
  res = ""
  while len(s) > 0:
    p = s.find ( wOld )
    if p < 0:
      res = res + s
      return
    if p > 0:
      res = res + s[:p]    
    res = res + wNew
    if p+lenOld >= len(s):
      s = ""         
    else:
      s = s[p+lenOld:]
  return res

s = "12.12.12"
s1 = replaceAll ( s, "12", "A12B" )
print ( s1 )

s = "12.12.12"
s = s.replace ( "12", "A12B" )
print ( s )

