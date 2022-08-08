# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 5a. Программы с графическим интерфейсом

  ROOM_A.py - площадь комнаты

"""
from simpletk import *
from tkinter.messagebox import askokcancel

#------------------------------------------
#  Главное окно
#------------------------------------------
app = TApplication("Площадь комнаты")
app.size = (210, 90)
app.position = (200, 200)
app.resizable = (False, False)

def AskOnExit():
  if askokcancel("Подтверждение",
     "Вы действительно хотите выйти из программы?"):
    app.destroy()
app.onCloseQuery = AskOnExit

#------------------------------------------
#  Метки
#------------------------------------------
fSans = ("MS Sans Serif", 12)
lblL = TLabel(app, text="Длина =                     м", font=fSans )
lblL.position = (5, 5)

lblW = TLabel(app, text="Ширина =                  м", font=fSans )
lblW.position = (5, 30)

lblArea = TLabel(app, text="Площадь = 1 кв. м", font=fSans, fg="navy" )
lblArea.position = (5, 55)

#------------------------------------------
#  Поля ввода
#------------------------------------------
lEdit = TEdit( app, font = fSans, width = 50 )
lEdit.position = (90, 5)
lEdit.text = "1"

wEdit = TEdit( app, font = fSans, width = 50 )
wEdit.position = (90, 30)
wEdit.text = "1"

#------------------------------------------
#  Обработчик изменений полей ввода
#------------------------------------------
def onChange(sender):
  s = "?"
  try:
    l = float(lEdit.text)
    w = float(wEdit.text)
    if l >= 0 and w >= 0:
      s = "{:0.2f}".format(l*w)
  except:
     pass
  lblArea.text = "Площадь = " + s + " кв. м"

lEdit.onChange = onChange
wEdit.onChange = onChange

app.run()
