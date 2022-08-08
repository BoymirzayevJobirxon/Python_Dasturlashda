# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 59. Обработка неизвестного количества чисел
 Вход: 
   целые числа в файле input_2.txt в текущем каталоге  
 Результат: 
   сумма чисел в файле output_2.txt в текущем каталоге    
"""
Fin = open( "input_2.txt" )

sum = 0
while True:
  s = Fin.readline()
  if not s: break
  sum += int(s)
Fin.close()

Fout = open( "output_2.txt", "w" )
Fout.write ( str(sum) )
Fout.close()

print("Результат записан в файл ""output_2.txt""" )


