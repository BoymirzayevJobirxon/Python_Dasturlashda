# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 55. Создание и вывод матриц
 Вход: 
   нет
 Результат: 
   нет
"""
N = 3
M = 4

def printMatrix ( A ):
  for i in range ( len(A) ):
    for j in range ( len(A[i]) ):
      if type(A[i][j]) == int:
        print ( "{:4d}".format(A[i][j]), end = "" )
      elif type(A[i][j]) == float:
          print ( "{:5g}".format(A[i][j]), end = "" )
      elif type(A[i][j]) == bool:
          print ( "{:4d}".format(int(A[i][j])), end = "" )
    print ()

A = [[-1, 0, 1], 
     [-1, 0, 1], 
     [0, 1, -1]]

printMatrix(A)
print()

A = []
for i in range(N):
  A.append ( [0]*M )
printMatrix(A)
print()

A = []
for i in range(N):
  A.append ( [0.1*i]*M )
printMatrix(A)
print()

A = []
for i in range(N):
  A.append ( [True]*M )
printMatrix(A)
print()

