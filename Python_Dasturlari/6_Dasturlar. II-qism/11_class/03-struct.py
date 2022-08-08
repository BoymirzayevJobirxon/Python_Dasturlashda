# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 3. Структуры
 Вход: 
   нет 
 Результат: 
   32
   Пушкин
   Этих книг больше нет!
   Пушкин А.С. Полтава. 0 шт.
   460
"""

class TBook:
  pass

import sys

class Book: 
  pass

B = Book()
print(sys.getsizeof(B))

B.author = "Пушкин А.С."
B.title = "Полтава"
B.count = 1

fam = B.author.split()[0]
print(fam)

B.count -= 1        # одну книгу взяли 
if B.count == 0:
   print("Этих книг больше нет!")

print ( B.author, B.title + ".", B.count, "шт." )

Books = []
for i in range(100):
  Books.append(Book())
print(sys.getsizeof(Books))

