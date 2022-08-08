# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 56. Заполнение матрицы случайными числами
 Вход: 
   нет 
 Результат:
   <случайная матрица 3 на 4>
"""
N = 3 
M = 4

A = []
for i in range(N):
  A.append ( [0]*M )

import random
for i in range(N):
  for j in range(M):
    A[i][j] = random.randint ( 20, 80 )
    print ( "{:4d}".format(A[i][j]), end = "" )
  print()


