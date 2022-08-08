# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 5. Сортировка структур перестановкой
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

N = len(Books)
for i in range(0,N-1):
  for j in range(N-2,i-1,-1):
    if Books[j].author > Books[j+1].author:
      Books[j], Books[j+1] = Books[j+1], Books[j]

print ( "\nПосле сортировки:" );
for b in Books:
  print ( b.author, b.title, b.count, "шт.");
               
F = open ( "books_sort.dat", "wb" )
pickle.dump ( Books, F );
F.close()
