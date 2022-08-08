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

"""

from simpletk import *
from int_edit import TIntEdit

app = TApplication("Шестнадцатеричная система")
app.size = (250, 36)
app.position = (200, 200)

f = ("Courier New", 14, "bold")
hexLabel = TLabel(app, text="?", font=f, fg="navy" )
hexLabel.position = (155, 5)

def onNumChange(sender):
  hexLabel.text = "{:X}".format(sender.value)

decEdit = TIntEdit(app, width=12, font = f)
decEdit.position = (5, 5)
decEdit.text = "1001"
decEdit.onChange = onNumChange

app.Run()
