# -*- coding: utf-8
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  02a_viewer.py - просмотрщик рисунков в виде одного класса

"""
from simpletk import *
from tkinter import filedialog

class TImageViewer(TApplication):
  def __init__(self):
    TApplication.__init__(self, "Просмотр рисунков")
    self.position = (200, 200)
    self.size = (300, 300)
    self.panel = TPanel(self, relief="raised", height=42, bd=1)
    self.panel.align = "top"
    self.image = TImage(self, bg="white")
    self.image.align = "client"
    self.openBtn = TButton(self.panel, width=110, height = 30, text="Открыть файл")
    self.openBtn.font = ('Helvetica', 10)
    self.openBtn.position = (5, 5)
    self.openBtn.onClick = self.selectFile
    self.centerCb = TCheckBox(self.panel,text="В центре")
    self.centerCb.position = (125, 8)
    self.centerCb.font = ('Courier New', 12)
    self.centerCb.onChange = self.cbChanged
  def selectFile(self, sender):
    fname = filedialog.askopenfilename(
       filetypes=[("Файлы GIF", "*.gif"),
                  ("Все файлы", "*.*")] )
    if fname:
      self.image.picture = fname
  def cbChanged(self, sender):
    self.image.center = sender.checked
    self.image.redrawImage()

app = TImageViewer()

app.run()