# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 2. Логические элементы (иерархия)

  project_2_3.py - модификация 3
     + собран триггер на элементах TNotAnd

"""
from logelement import *

"""---------------------------------------------
  Класс TNAndTrigger - триггер на двух Not-And
---------------------------------------------"""
class TNAndTrigger(TLog2In):
  def __init__(self):
    TLog2In.__init__(self)
    self.__NAnd1 = TNotAnd()
    self.__NAnd2 = TNotAnd()
    self._res1 = False
  def calc(self):
    self.__NAnd1.In1 = self.In1
    self.__NAnd2.In2 = self.In2
    self.__NAnd1.In2 = self.__NAnd2.Res
    self.__NAnd2.In1 = self.__NAnd1.Res
    self._res = self.__NAnd2.Res
    self._res1 = self.__NAnd1.Res
  Res1 = property(lambda x: x._res1)
    
#---------------------------------------------------
# Основная программа
#---------------------------------------------------

trigNAnd = TNAndTrigger()

print(' S  R | Q !Q ')
print('-------------')

# режим хранения бита при одном состоянии 

trigNAnd.In1 = False
trigNAnd.In2 = True

for S in range(2):
  trigNAnd.In1 = bool(S)
  for R in range(2):
    trigNAnd.In2 = bool(R)
    print(" ", S, "  ", R, " | ", int(trigNAnd.Res),
            '  ', int(trigNAnd.Res1), sep="")

# режим хранения бита при другом состоянии 

trigNAnd.In1 = False
trigNAnd.In2 = True

S = True
R = True
trigNAnd.In1 = S
trigNAnd.In2 = R
print(" ", int(S), "  ", int(R), " | ", int(trigNAnd.Res),
        '  ', int(trigNAnd.Res1), sep="")
