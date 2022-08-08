# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 4. Структуры и файлы

"""
import pickle

class TBook:
  pass

F = open ( "books.dat", "rb" )
Books = pickle.load ( F )
F.close()
print ( "Имеющиеся данные о книгах:" );
for b in Books:
  print ( b.author, b.title, b.count, "шт.");
             
B = TBook()
print ( "\nВведите поля новой структуры:" );
B.author = input("author: ")
B.title  = input(" title: ")
B.count  = int(input(" count: "))
Books.append(B)

F = open ( "books.dat", "wb" )
pickle.dump ( Books, F );
F.close()
