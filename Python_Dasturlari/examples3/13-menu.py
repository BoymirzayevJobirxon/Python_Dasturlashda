# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  13_menu.py - простая форма с меню

"""
from simpletk import *

def info():
  print('info')
def newFile( event = None ):
  print('new')
def openFile( event = None ):
  print('open')
def changeAutoSave( event = None ):
  print('changeAutoSave', autoSaveItem.value )
def changeTheme( event = None ):
  print('Theme', theme.value)
def cut( event = None ):
  print('cut')
def copy( event = None ):
  print('copy')
def paste( event = None ):
  print('paste')

app = TApplication("Форма с меню")
app.size = (300, 300)

# Верхнее меню

menu = TMenu(app)
menu.addItem( "Info", onClick = info )

# Подменю с картинками

newIcon = PhotoImage(file='new.gif')
openIcon = PhotoImage(file='open.gif')

fileMenu = menu.addSubmenu( "File" )
fileMenu.addItem( "New", onClick = newFile, accelerator = 'Ctrl+N', image = newIcon )
fileMenu.addSeparator()
fileMenu.addItem( "Open", onClick = openFile, accelerator = 'Ctrl+O', image = openIcon )

# Подменю с флажком (вкл/выкл)

prefMenu = menu.addSubmenu( "Preferences" )
autoSaveItem = prefMenu.addCheckItem( "Temp", onClick = changeAutoSave )
autoSaveItem.text = 'Autosave'
prefMenu.addSeparator()
prefMenu.text = "Customize" # изменение текста элемента меню

# Подменю с выбором одного элемента (радиокнопки)

themeMenu = prefMenu.addSubmenu( "Theme" )
theme = themeMenu.addRadioGroup(['Light', 'Night', 'Maroon'], onClick = changeTheme )
theme.value = 'Maroon'

# Всплывающее (popup) меню для редактора

edit = TMemo( app )
edit.align = "client"

popupMenu = TPopupMenu( edit )
popupMenu.addItem( "Cut", onClick = cut )
popupMenu.addItem( "Copy", onClick = copy )
popupMenu.addItem( "Paste", onClick = paste )

app.run()


