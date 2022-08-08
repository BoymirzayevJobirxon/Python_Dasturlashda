# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 10. Реверс массива из файла
"""

stack = []
for s in open("input_arr.dat"):
  stack.append( int(s) )

Fout = open ( "output_arr.dat", "w" )
while len(stack) > 0:
  x = stack.pop()
  Fout.write ( str(x) + "\n" )
Fout.close()    

print ( "Результат записан в файл output_arr.dat")
