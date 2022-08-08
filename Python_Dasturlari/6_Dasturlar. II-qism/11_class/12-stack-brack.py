# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 12. Стек. Проверка скобочных выражений
"""
L = "([{"
R = ")]}"

s = input("Введите скобочное выражение: ")
stack = []
err = False

for c in s:
  p = L.find(c)
  if p >= 0:
    stack.append(c)
  p = R.find(c)
  if p >= 0:
    if len(stack) == 0: err = True
    else:
      top = stack.pop()
      if p!= L.find(top):
        err = True
  if err: break

if len(stack) > 0: err = True

if not err:
  print ( "Выражение правильное." )
else:
  print ( "Выражение неправильное." );

