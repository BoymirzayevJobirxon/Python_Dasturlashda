# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 41. Отбор элементов по условию
 Вход: 
   5 1 2 3 4 
 Результат:
   Чётные элементы:
   2 4
"""
print ( "Введите элементы массива:" )
A = list( map(int, input().split()) )
N = len(A)  

B = []
for i in range(N):
  if A[i] % 2 == 0:
    B.append(A[i])

print ( "Чётные элементы: " )
for x in B:
  print ( x, " ", end="", sep="" )      

