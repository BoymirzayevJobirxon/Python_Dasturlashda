# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 1a. Решето Эратосфена
 Вход: 
   нет
 Результат: 
   Простые числа от 2 до 100
"""
from math import sqrt

N = 100

N += 1
A = [True]*(N+1)

for k in range(2, int(sqrt(N))+1):
  if A[k]:
    for i in range(k*k, N, k):
      A[i] = False

print ( "Простые числа от 2 до", N-1 );
for i in range(2,N): 
  if A[i]:
    print ( i, " ", end="", sep="" )
print()




