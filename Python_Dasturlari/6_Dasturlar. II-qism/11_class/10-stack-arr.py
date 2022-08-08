# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 10. Реверс массива из файла
"""

stack = []
Fin = open("input_arr.dat")
while True:
  s = Fin.readline().strip()
  if not s: break    
  stack.append( int(s) )
Fin.close()

Fout = open ( "output_arr.dat", "w" )
while len(stack) > 0:
  x = stack.pop()
  Fout.write ( str(x) + "\n" )
Fout.close()    

print ( "Результат записан в файл output_arr.dat")
