# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 61. Обработка символьных строк в файле
 Вход: данные о собаках в файле input_4.txt 
       в текущем каталоге
   <кличка> <возраст> <порода> 
 Результат: данные о собаках, которым < 5 лет, 
       в файле output_4.txt в текущем каталоге
"""
Fin = open ( "input_4.txt" )
Fout = open( "output_4.txt", "w" )

while True:
  s = Fin.readline()
  if not s: break
  age = int ( s.split()[1] )
  if age < 5:
    Fout.write ( s )

Fin.close()
Fout.close()

print("Результат записан в файл ""output_4.txt""" )
