# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 9. Алфавитно-частотный словарь
"""
D = {}
Fin = open ( "input_list.txt" )
while True:
  word  = Fin.readline().strip() 	
  if not word: break
  D[word] = D.get ( word, 0 ) + 1
Fin.close() 

Fout = open ( "output_list.txt", "w" )
for k in sorted(D.keys()):
  Fout.write ( "{}: {}\n".format(k, D[k]) )
Fout.close()

print ( "Данные записаны в файл output_list.txt." )


