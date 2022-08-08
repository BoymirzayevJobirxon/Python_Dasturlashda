# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 32. Заполнение и вывод массива
 Вход: 
   нет
 Результат:
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   [1, 4, 9, 16, 25]
   [2, 3, 5, 7, 11, 13]
   [<массив из 5 случайных значений в диапазоне [20,100]>]

"""
A = list ( range(10) )
print ( A )

A =[ i*i  for i in range(1,6)]
print ( A )

def isPrime(n): 
  count = 0
  k = 2
  while k*k <= n and n % k != 0:
    k += 1
  return k*k > n

A =[ i  for i in range(2,16) if isPrime(i)]
print ( A )

from random import randint
A = [ randint(20,100)  for x in range(5)]
print ( A )
