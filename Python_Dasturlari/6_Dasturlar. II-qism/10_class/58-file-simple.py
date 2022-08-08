# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 58. Чтение и запись в файл
 Вход: 
   целое число в файле intput_1.txt в текущем каталоге 
 Результат: 
   удвоенное число в файле output_1.txt в текущем каталоге
"""
Fin = open( "input_1.txt" )
x = int( Fin.readline().strip() )
Fin.close()

Fout = open( "output_1.txt", "w" )
Fout.write( str(2*x) )
Fout.close()
print("Результат записан в файл 'output_1.txt'" )

