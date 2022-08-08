# -*- coding: utf-8
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  intedit.py - новый компонент TIntEdit

"""
from simpletk import TEdit

class TIntEdit(TEdit):
  def __init__(self, parent, **kw):
    TEdit.__init__(self, parent, **kw)
    self.__value = 0
    self.onValidate = self.__validate
  def __validate(self):
    self.text = self.text.strip()
    if len(self.text) == 0:
      return True
    try:
      newValue = int(self.text)
      self.__value = newValue
      return True
    except:
      return False
  def __setValue(self, value):
    self.__value = value
    self.text = str(value)
  value = property(lambda x: x.__value, __setValue)