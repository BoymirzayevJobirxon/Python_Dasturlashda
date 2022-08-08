# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 6. Разработка компонентов

  project_6.py - программа с компонентом TIntEdit

  *** Проект полностью в стиле ООП ***
  
"""
from simpletk import *
from int_edit import TIntEdit

class TDec2Hex(TApplication):
  def __init__(self):
    TApplication.__init__(self, "Шестнадцатеричная система")
    self.size = (250, 36)
    self.position = (200, 200)
    f = ("Courier New", 14, "bold")
    self.hexLabel = TLabel(self, text="?", font=f, fg="navy" )
    self.hexLabel.position = (155, 5)
    self.decEdit = TIntEdit(self, width=12, font = f)
    self.decEdit.position = (5, 5)
    self.decEdit.text = "1001"
    self.decEdit.onChange = self.onNumChange
  def onNumChange(self, sender):
    self.hexLabel.text = "{:X}".format(sender.value)

app = TDec2Hex()
app.Run()
