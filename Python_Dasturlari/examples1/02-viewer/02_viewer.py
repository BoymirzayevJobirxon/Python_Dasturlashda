# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  02_viewer.py - просмотрщик рисунков

"""
from simpletk import *
from tkinter import filedialog

app = TApplication("Просмотр рисунков")
app.position = (200, 200)
app.size = (300, 300)

panel = TPanel(app, relief="raised", height=42, bd=1)
panel.align = "top"

image = TImage(app, bg="white")
image.align = "client"
# image.picture = "flower.gif"
# image.picture = "lamplogo.jpg" # только если есть PIL

def selectFile(sender):
  fname = filedialog.askopenfilename(
     filetypes=[("Файлы GIF", "*.gif"),
                ("Все файлы", "*.*")] )
     #filetypes=[("Файлы GIF", "*.gif"),  # если есть PIL
     #           ("Файлы JPEG", "*.jpg"),
     #           ("Файлы PNG", "*.png"),
     #           ("Все файлы", "*.*")] )
  if fname:
    image.picture = fname

openBtn = TButton(panel, width=110, height = 30, text="Открыть файл")
openBtn.position = (5, 5)
openBtn.onClick = selectFile
openBtn.font = ('Helvetica', 10)

def cbChanged(sender):
  image.center = sender.checked
  image.redrawImage()

centerCb = TCheckBox(panel, text="В центре")
centerCb.position = (125, 8)
centerCb.onChange = cbChanged
centerCb.font = ('Courier New', 12)

app.run()

