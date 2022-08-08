# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 57. Сумма элементов матрицы
 Вход: 
   нет 
 Результат:
   Сумма элементов 54
"""
N = 3
M = 4

A = []
for i in range(N):
  A.append ( [0]*M )
  
for i in range(N):
  for j in range(M): 
    A[i][j] = i+j+2
    print ( "{:4d}".format(A[i][j]), end = "" )
  print()

s = 0
for i in range(N):
  for j in range(M):
    s += A[i][j]
print ( "Сумма элементов", s )



