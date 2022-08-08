# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 60. Сортировка массива из файла
 Вход: 
   массив в файле input_3.txt в текущем каталоге 
 Результат: 
   отсортированный массив в файле output_3.txt 
   в текущем каталоге
"""
Fin = open( "input_3.txt" )
s = Fin.read().split()
A = list ( map(int, s) )

A.sort()  
  
Fout = open( "output_3.txt", "w" )
for x in A:
  Fout.write ( str(x) + "\n" )
Fout.close()

print("Результат записан в файл ""output_3.txt""" )


