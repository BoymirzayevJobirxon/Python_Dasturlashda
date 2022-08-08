# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 4. Использование компонентов

  project_4-oop.py - программа для просмотра рисунков.
  *** Проект полностью в стиле ООП ***

"""
from simpletk import *
from tkinter import filedialog

class TImageViewer(TApplication):
  def __init__(self):
    TApplication.__init__(self, "Просмотр рисунков")
    self.position = (200, 200)
    self.size = (300, 300)
    self.panel = TPanel(self, relief="raised", height=35, bd=1)
    self.panel.align = "top"
    self.image = TImage(self, bg="white")
    self.image.align = "client"
    self.openBtn = TButton(self.panel, width=15, text="Открыть файл")
    self.openBtn.position = (5, 5)
    self.openBtn.onClick = self.selectFile
    self.centerCb = TCheckBox(self.panel,text="В центре")
    self.centerCb.position = (115, 5)
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

app.Run()