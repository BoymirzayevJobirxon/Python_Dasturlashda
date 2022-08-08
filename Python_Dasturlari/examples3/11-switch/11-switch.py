# -*- coding: utf-8
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  11-switch.py - создание нового компонента TSwitch

"""
from simpletk import *

class TSwitch(TLabel):
  def __init__(self, parent, images, **kw):
    TLabel.__init__(self, parent, **kw )
    self.__images = images
    self.__state = False
    self.config (image = self.__images[0])
    TLabel.onClick.fset(self, self.__doClick)
    self.__onClick = None
    self.__onChange = None
  def __doClick(self, event):
    self.__setState(not self.__state)
  def __setState(self, newState):
    if newState != self.__state:
      self.__state = newState
      self.config (image = self.__images[self.__state])
      if self.__onChange:
         self.__onChange()
  def __setOnClick(self, func):
    self.__onClick = func
  def __setOnChange(self, func):
    self.__onChange = func
  state = property(lambda x: x.__state, __setState)
  onClick = property(lambda x: x.__onClick, __setOnClick)
  onChange = property(lambda x: x.__onChange, __setOnChange)

app = TApplication("Выключатель")
app.position = (200, 200)
app.size = (300, 100)

def showSwitchState():
  print(switch.state)

switchImages = [ PhotoImage('off.gif'),
                 PhotoImage('on.gif') ]
switchImages = [ PhotoImage('off_large.png'),
                 PhotoImage('on_large.png') ]
switch = TSwitch(app, switchImages )
switch.position = (5, 5)
switch.onChange = showSwitchState
switch.state = True

app.run()