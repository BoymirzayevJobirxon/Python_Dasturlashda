# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 2. Длинные числа (факториал 100) 
 Вход: 
   нет 
 Результат: 
   Факториал числа 100:
   93326215443944152681...
"""
d = 1000000
A = [1]
for k in range(2,101):
  r = 0
  for i in range(len(A)):
    s = A[i]*k + r
    A[i] = s % d
    r = s // d
  if r > 0:
    A.append ( r )

h = len ( A )- 1 
print ( A[h], end = "" )
for i in range(h-1,-1,-1):
  print ( "{:06d}".format(A[i]), end = "" )

print("\n")
A = 1
for k in range(2,101):
  A = A*k
print(A)  
  