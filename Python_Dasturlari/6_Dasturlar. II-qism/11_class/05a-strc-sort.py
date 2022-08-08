# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 5. Сортировка структур с помощью sort
"""
import pickle

class TBook:
  pass

F = open ( "books.dat", "rb" )
Books = pickle.load(F)
F.close()

print ( "Имеющиеся данные о книгах:" );
for b in Books:
  print ( b.author, b.title, b.count, "шт.");

Books.sort ( key =  lambda x: x.author  )

print ( "\nПосле сортировки:" );
for b in Books:
  print ( b.author, b.title, b.count, "шт.");
               
F = open ( "books_sort.dat", "wb" )
pickle.dump ( Books, F );
F.close()
