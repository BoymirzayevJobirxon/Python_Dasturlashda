# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 54. Сортировка строк
 Вход:
   пароход
   паровоз  
   пар
   Пар
   пАр
 Результат:
   Пар
   пАр
   пар
   паровоз
   пароход
"""
aS = []
print ( "Введите строки для сортировки:" )
while True:
  s1 = input()
  if s1 == "": break
  aS.append ( s1 )

aS.sort()  

for x in aS:
  print( x )


