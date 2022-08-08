# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 2. Логические элементы (иерархия)

  project_2.py - начальный вариант

"""
import logelement

elNot = logelement.TNot()
elAnd = logelement.TAnd()
elAnd.link(elNot, 1)
print("  A | B | not(A&B) ");
print("-------------------");
for A in range(2):
  elAnd.In1 = bool(A)
  for B in range(2):
    elAnd.In2 = bool(B)
    print(" ", A, "|", B, "|", int(elNot.Res));
