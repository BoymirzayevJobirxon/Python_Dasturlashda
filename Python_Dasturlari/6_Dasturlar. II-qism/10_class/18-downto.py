# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 18. Цикл с переменной (downto)
 Вход: 
   5
 Результат:
   32 16 8 4 2
"""
M = int ( input("Введите число шагов цикла: ") )
n = 2**M
for k in range(M,0,-1):
  print ( n, " ", sep="", end="" )
  n= n // 2