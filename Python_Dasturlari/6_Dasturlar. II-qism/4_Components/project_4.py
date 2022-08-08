# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 4. Использование компонентов

  project_4.py - программа для просмотра рисунков.

"""

from simpletk import *
from tkinter import filedialog

app = TApplication("Просмотр рисунков")
app.position = (200, 200)
app.size = (300, 300)

panel = TPanel(app, relief="raised", height=35, bd=1)
panel.align = "top"

image = TImage(app, bg="white")
image.align = "client"
#image.picture = "flower.gif"

def selectFile(sender):
  fname = filedialog.askopenfilename(
     filetypes=[("Файлы GIF", "*.gif"), 
                ("Все файлы", "*.*")] )
  if fname:
    image.picture = fname

openBtn = TButton(panel, width=15, text="Открыть файл")
openBtn.position = (5, 5)
openBtn.onClick = selectFile

def cbChanged(sender):
  image.center = sender.checked
  image.redrawImage()
  
centerCb = TCheckBox(panel,text="В центре")
centerCb.position = (115, 5)
centerCb.onChange = cbChanged

app.Run()
