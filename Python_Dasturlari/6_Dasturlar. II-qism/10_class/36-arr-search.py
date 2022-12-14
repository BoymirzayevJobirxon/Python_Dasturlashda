# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 36. Линейный поиск в массиве
 Вход: 
   1 2 3 4 5 
   3
 Результат:
   A[2]=3
"""
print ( "Введите элементы массива:" )
A = list( map(int, input().split()) )
N = len(A)

print ( "Что ищем? " ) 
X = int(input())

i = 0
while i < N and A[i] != X:
  i += 1
if i < N:
  print("A[", i, "]=", X, sep="")
else:
  print("Не нашли!")

