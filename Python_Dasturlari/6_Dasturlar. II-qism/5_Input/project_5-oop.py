# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Версия для Python 3.3.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 5. Использование компонентов

  *** Проект полностью в стиле ООП ***

"""
from simpletk import *

class TRGBcoder(TApplication):  
  def __init__(self):
    TApplication.__init__(self, "RGB-кодирование")
    self.size = (210, 90)
    self.position = (200, 200)

    f = ("MS Sans Serif", 12)
    self.lblR = TLabel(self, text="R = ", font=f )
    self.lblR.position = (5, 5)
    self.lblG = TLabel(self, text="G = ", font=f )
    self.lblG.position = (5, 30)
    self.lblB = TLabel(self, text="B = ", font=f )
    self.lblB.position = (5, 55)

    fc = ("Courier New", 16, "bold")
    self.rgbLabel = TLabel(self, text="#000000", font=fc, fg="navy" )
    self.rgbLabel.position = (100, 5)
  
    self.rgbRect = TLabel(self, text="", width =15, height = 3 )
    self.rgbRect.position = (105, 35)

    self.rEdit = TEdit(self, font=f, width=5)
    self.rEdit.position = (45, 5)
    self.rEdit.text = "123"
    self.rEdit.onChange = self.onChange

    self.gEdit = TEdit(self, font=f, width=5)
    self.gEdit.position = (45, 30)
    self.gEdit.text = "56"
    self.gEdit.onChange = self.onChange

    self.bEdit = TEdit(self, font=f, width=5)
    self.bEdit.text = "80"
    self.bEdit.position = (45, 55)
    self.bEdit.onChange = self.onChange
    
  def onChange(self, sender):
    hexColor = "?"
    bkColor = 'SystemButtonFace'
    try:
      r = int(self.rEdit.text)
      g = int(self.gEdit.text)
      b = int(self.bEdit.text)
      if r in range(256) and \
         g in range(256) and b in range(256):
        hexColor = "#{:02x}{:02x}{:02x}".format(r, g, b)
        bkColor = hexColor
    except:
      pass
    self.rgbLabel.text = hexColor
    self.rgbRect.background = bkColor

app = TRGBcoder()

app.Run()