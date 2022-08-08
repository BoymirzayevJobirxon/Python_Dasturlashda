# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 1b. Решето Эратосфена.
                 Использование множеств (set)
 Вход: 
   нет
 Результат: 
   Простые числа от 2 до 100
"""
from math import sqrt

def primes(N):
  sieve = set(range(2, N))
  for i in range(2, int(math.sqrt(N))):
    if i in sieve:
      sieve -= set(range(2*i, N, i))
  return sieve

N = 100

print ( "Простые числа от 2 до", N );
for x in primes(N): 
  print ( x, " ", end="", sep="" )
print()




