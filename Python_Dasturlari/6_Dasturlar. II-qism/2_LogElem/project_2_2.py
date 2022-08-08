# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 2. Логические элементы (иерархия)

  project_2_2.py - модификация 2
     + собран триггер на элементах TNotOr

"""
from logelement import *

"""---------------------------------------------
  Класс TNOrTrigger - триггер на двух Not-Or
---------------------------------------------"""
class TNOrTrigger(TLog2In):
  def __init__(self):
    TLog2In.__init__(self)
    self.__NOr1 = TNotOr()
    self.__NOr2 = TNotOr()
    self._res1 = False
  def calc(self):
    self.__NOr1.In1 = self.In1
    self.__NOr2.In2 = self.In2
    self.__NOr1.In2 = self.__NOr2.Res
    self.__NOr2.In1 = self.__NOr1.Res
    self._res = self.__NOr2.Res
    self._res1 = self.__NOr1.Res
  Res1 = property(lambda x: x._res1)
    
#---------------------------------------------------
# Основная программа
#---------------------------------------------------

trigNOr = TNOrTrigger()

print(' S  R | Q !Q ')
print('-------------')

# режим хранения бита при одном состоянии 

trigNOr.In1 = True
trigNOr.In2 = False

S = False
R = False
trigNOr.In1 = S
trigNOr.In2 = R
print(" ", int(S), "  ", int(R), " | ", int(trigNOr.Res),
        '  ', int(trigNOr.Res1), sep="")

# режим хранения бита при другом состоянии 

trigNOr.In1 = False
trigNOr.In2 = True

for S in range(2):
  trigNOr.In1 = bool(S)
  for R in range(2):
    trigNOr.In2 = bool(R)
    print(" ", S, "  ", R, " | ", int(trigNOr.Res),
            '  ', int(trigNOr.Res1), sep="")
