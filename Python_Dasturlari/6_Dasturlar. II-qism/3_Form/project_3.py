# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 3. Форма и ей свойства

  project_3.py - начальный вариант

"""

from simpletk import *
from tkinter.messagebox import askokcancel

def AskOnExit(sender):
  if askokcancel("Подтверждение", 
     "Вы действительно хотите выйти из программы?"):
    app.destroy()
  
app = TApplication("Первая форма")
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)
app.onCloseQuery = AskOnExit

app.Run()



