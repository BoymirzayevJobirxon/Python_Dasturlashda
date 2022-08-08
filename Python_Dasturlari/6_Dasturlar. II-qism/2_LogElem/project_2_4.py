# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 2. Логические элементы (иерархия)

  project_2_4.py - модификация 4
     + собран шифратор "4 в 2"

"""
from logelement import *

"""---------------------------------------------
  Класс TCoder - шифратор "4 в 2"
---------------------------------------------"""
class TCoder:
  def __init__(self):
    self.__Or0 = TOr()
    self.__Or1 = TOr()
  def Inputs(self, In0, In1, In2, In3):
    self.__Or0.In1 = In1
    self.__Or0.In2 = In3
    self.__Or1.In1 = In2
    self.__Or1.In2 = In3
  Output0 = property(lambda x: x.__Or0.Res)
  Output1 = property(lambda x: x.__Or1.Res)
    
#---------------------------------------------------
# Основная программа
#---------------------------------------------------

coder = TCoder()

print(' X3 X2 X1 X0 | C1 C0')
print('---------------------')

for i in range(4):
  X0 = (i == 0)
  X1 = (i == 1)
  X2 = (i == 2)
  X3 = (i == 3)
  coder.Inputs(X0, X1, X2, X3)
  print('  ', int(X3), '  ', int(X2),
           '  ', int(X1), '  ', int(X0),
          ' |  ', int(coder.Output1),
           '  ', int(coder.Output0), sep="");
