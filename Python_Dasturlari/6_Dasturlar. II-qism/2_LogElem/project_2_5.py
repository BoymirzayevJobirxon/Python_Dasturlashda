# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 2. Логические элементы (иерархия)

  project_2_5.py - модификация 5
     + собран дешифратор "2 в 4"

"""
from logelement import *

"""---------------------------------------------
  Класс TDecoder - дешифратор "2 в 4"
---------------------------------------------"""
class TDecoder(TLog2In):
  def __init__(self):
    TLog2In.__init__(self)
  def calc(self):
    self._res = not self.In1 and not self.In2
  def Output(self, no):
    if no == 1: return not self.In2 and self.In1
    elif no == 2: return self.In2 and not self.In1
    elif no == 3: return self.In2 and self.In1
    else: return self.Res
    
#---------------------------------------------------
# Основная программа
#---------------------------------------------------

decoder = TDecoder()
  
print(' C1 C0 | X3 X2 X1 X0');
print('---------------------');
  
for C1 in range(2):
  for C0 in range(2):
    decoder.In1 = bool(C0)
    decoder.In2 = bool(C1)
    print('  ', int(C1), '  ', int(C0),
              ' |  ', int(decoder.Output(3)),
               '  ', int(decoder.Output(2)),
               '  ', int(decoder.Output(1)),
               '  ', int(decoder.Output(0)), sep="");
