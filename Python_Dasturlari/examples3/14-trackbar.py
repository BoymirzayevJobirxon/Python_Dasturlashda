# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  14_trackbar.py - использование ползунка

"""
from simpletk import *

def changeRGB ( event = None ):
  colorLabel.background = "#{:02X}{:02X}{:02X}".format(
                        Red.value, Green.value, Blue.value )
  Cyan.value = 255 - Red.value
  Magenta.value = 255 - Green.value
  Yellow.value = 255 - Blue.value

def changeCMY ( event = None ):
  Red.value = 255 - Cyan.value
  Green.value = 255 - Magenta.value
  Blue.value = 255 - Yellow.value
  changeRGB ( event )

app = TApplication("Использование ползунков (TTrackBar)")
app.size = (400, 350)

colorLabel = TLabel(app, text = " ", width = 200, height = 200, bg = 'black')
colorLabel.position = (150, 13)

Red = TTrackBar( app, [255, 0], width = 10, length = 200, onTrack = changeRGB )
Red.position = (10, 10)
Green = TTrackBar( app, [255, 0], width = 10, length = 200, onTrack = changeRGB )
Green.position = (50, 10)
Blue = TTrackBar( app, [255, 0], width = 10, length = 200, onTrack = changeRGB )
Blue.position = (90, 10)

labelR = TLabel(app, text = " ", width = 10, height = 10, bg = 'red')
labelR.position = (35, 220)
labelG = TLabel(app, text = " ", width = 10, height = 10, bg = 'green')
labelG.position = (75, 220)
labelB = TLabel(app, text = " ", width = 10, height = 10, bg = 'blue')
labelB.position = (115, 220)

Cyan = TTrackBar( app, [0, 255], width = 10, length = 200,
                  orient = HORIZONTAL, onTrack = changeCMY )
Cyan.value = 255
Cyan.position = (147, 220)
Magenta = TTrackBar( app, [0, 255], width = 10, length = 200,
                  orient = HORIZONTAL, onTrack = changeCMY )
Magenta.value = 255
Magenta.position = (147, 255)
Yellow = TTrackBar( app, [0, 255], width = 10, length = 200,
                  orient = HORIZONTAL, onTrack = changeCMY )
Yellow.value = 255
Yellow.position = (147, 290)

labelC = TLabel(app, text = " ", width = 10, height = 10, bg = 'cyan')
labelC.position = (357, 240)
labelM = TLabel(app, text = " ", width = 10, height = 10, bg = 'magenta')
labelM.position = (357, 275)
labelY = TLabel(app, text = " ", width = 10, height = 10, bg = 'yellow')
labelY.position = (357, 310)

app.run()


