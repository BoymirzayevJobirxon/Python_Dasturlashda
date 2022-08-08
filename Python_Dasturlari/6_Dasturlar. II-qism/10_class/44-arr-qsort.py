# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 44. Быстрая сортировка (QuickSort)
 Вход: 
   нет
 Результат:
   До сортировки:
   78 6 82 67 55 44 34
   После сортировки: 
   6 34 44 55 67 78 82
   После сортировки: 
   6 34 44 55 67 78 82
"""
import random

def qSort ( A, nStart, nEnd ):
  if nStart >= nEnd: return
  L = nStart; R = nEnd
  X = A[random.randint(L,R)] 
  while L <= R:
    while A[L] < X: L += 1  # разделение
    while A[R] > X: R -= 1
    if L <= R:
      A[L], A[R] = A[R], A[L]
      L += 1; R -= 1
  qSort ( A, nStart, R )  # рекурсивные вызовы
  qSort ( A, L, nEnd )

def qSort2 ( A ):
  if len(A) <= 1: return A	
  X = random.choice(A)  	
  B1 = [ b for b in A  if b < X ]
  BX = [ b for b in A  if b == X ]
  B2 = [ b for b in A  if b > X ]
  return qSort2(B1)+BX+qSort2(B2)	

A0 = [78, 6, 82, 67, 55, 44, 34]
N = len(A0)

A = A0[:]
print ( "До сортировки: " )
for x in A:
  print ( x, " ", end="", sep="" )   

qSort(A, 0, N-1)  

print()
print ( "После сортировки: " )
for x in A:
  print ( x, " ", end="", sep="" ) 

A = A0[:]
A = qSort2(A)  

print()
print ( "После сортировки: " )
for x in A:
  print ( x, " ", end="", sep="" ) 
