# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 29. Рекурсия. Алгоритм Евклида
 Вход: 
   14 21
 Результат:
   НОД(14,21) = 7
"""
def NOD(a, b):
  if a == 0 or b == 0:
    return a + b
  if a > b:
    return NOD ( a - b, b )
  else:
    return NOD ( a, b - a )

def NOD1(a, b):
  if a == 0 or b == 0:
    return a + b
  if a > b:
    return NOD1 ( a % b, b )
  else:
    return NOD1 ( a, b % a )

def NOD2(a,b):
  if b == 0:
    return a 
  return NOD2 ( b, a % b )

a, b = map( int, input("Введите два натуральных числа: ").split() )
print ( "НОД(", a, ",", b, ")=", NOD(a,b), sep="" )
print ( "НОД(", a, ",", b, ")=", NOD1(a,b), sep="" )
print ( "НОД(", a, ",", b, ")=", NOD2(a,b), sep="" )



