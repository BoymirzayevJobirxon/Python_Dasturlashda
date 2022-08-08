# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 43. Сортировка выбором
 Вход: 
   1 3 5 2 4
 Результат:
   После сортировки:
   1 2 3 4 5
"""
print ( "Введите элементы массива:" )
A = list( map(int, input().split()) )
N = len(A)  

for i in range(N-1):
  nMin = i
  for j in range(i+1,N):
    if A[j] < A[nMin]:
      nMin = j
  if i!= nMin:
     A[i], A[nMin] = A[nMin], A[i]

print ( "После сортировки: " )
for x in A:
  print ( x, " ", end="", sep="" )   

