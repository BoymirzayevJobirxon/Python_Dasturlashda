# -*- coding: utf-8 -*-
"""
Библиотека SIMPLETK 
Версия 0.1

SIMPLETK - это "обертка" над стандартной библиотекой tkinter,
которая используется в языке Python для разработки приложений с
графическим интерфейсом. В ней упрощён доступ ко многим возможностям 
библиотеки tkinter, в то же время сохранена возможность использования 
всех средств tkinter.

ЛИЦЕНЗИЯ

Copyright (c) 2014, Константин Поляков
Все права защищены.

Разрешается повторное распространение и использование как в виде исходного 
кода, так и в двоичной форме, с изменениями или без, при соблюдении 
следующих условий:
  1) При повторном распространении исходного кода должно оставаться указанное 
     выше уведомление об авторском праве, этот список условий и последующий 
     отказ от гарантий.
  2) При повторном распространении двоичного кода должна сохраняться указанная 
     выше информация об авторском праве, этот список условий и последующий 
     отказ от гарантий в документации и/или в других материалах, 
     поставляемых при распространении.
  3) Ни название Организации, ни имена ее сотрудников не могут быть 
     использованы в качестве поддержки или продвижения продуктов, 
     основанных на этом ПО без предварительного письменного разрешения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ ЛЮБОГО ВИДА 
ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ 
ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ 
И НЕНАРУШЕНИЯ ПРАВ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ 
ОТВЕТСТВЕННОСТИ ПО ИСКАМ О ВОЗМЕЩЕНИИ УЩЕРБА, УБЫТКОВ ИЛИ ДРУГИХ ТРЕБОВАНИЙ 
ПО ДЕЙСТВУЮЩИМ КОНТРАКТАМ, ДЕЛИКТАМ ИЛИ ИНОМУ, ВОЗНИКШИМ ИЗ, ИМЕЮЩИМ ПРИЧИНОЙ 
ИЛИ СВЯЗАННЫМ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ПРОГРАММНОГО 
ОБЕСПЕЧЕНИЯ ИЛИ ИНЫМИ ДЕЙСТВИЯМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.
"""

__all__ = [
        'TApplication',        
        'TLabel',        
        'TButton', 
        'TCanvas', 
        'TImage',        
        'TPanel',        
        'TEdit',        
        'TMemo',
        'TListBox',        
        'TComboBox',        
        'TRadioGroup',        
        'TCheckBox',        
        'TGroupBox'
        ]

import tkinter 
from tkinter import ttk

class TApplication(tkinter.Tk):
    def __init__(self, title0):
      tkinter.Tk.__init__(self)
      self.title(title0)
      self.__size = (200, 200)
      self.__position = (200, 200)        
      self.__resizable = (True, True)
      self.__minsize = (1, 1)
      self.__maxsize = (self.winfo_screenwidth(), 
                        self.winfo_screenheight())
      self.__onCloseQuery = None
      self.protocol("WM_DELETE_WINDOW", self.__intOnCloseQuery)
    def __setGeometry (self):
      pos = self.__position
      size = self.__size
      self.geometry("{:d}x{:d}+{:d}+{:d}".format(*(size+pos)))
    def __setPosition (self, pos):
      self.__position = pos
      self.__setGeometry()      
    def __setSize (self, size):
      self.__size = size
      self.__setGeometry()      
    def __setResizable (self, value):
      self.__resizable = value
      super(TApplication,self).resizable(width=value[0], height=value[1])      
    def __setMinsize (self, value):
      self.__minsize = value
      super(TApplication,self).minsize(width=value[0], height=value[1])      
    def __setMaxsize (self, value):
      self.__maxsize = value
      super(TApplication,self).maxsize(width=value[0], height=value[1])      
    def __intOnCloseQuery(self):
      if self.__onCloseQuery:
        self.__onCloseQuery(self)
      else:
        self.destroy()  
    def __setOnCloseQuery(self, func):
      self.__onCloseQuery = func
    def Run(self):
      self.mainloop()  
    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)   
    resizable = property(lambda x: x.__resizable, __setResizable)   
    minsize = property(lambda x: x.__minsize, __setMinsize)   
    maxsize = property(lambda x: x.__maxsize, __setMaxsize)   
    onCloseQuery = property(lambda x: x.__onCloseQuery, __setOnCloseQuery)

class TPanel(tkinter.Frame):
    def __init__(self, parent, **kw):
      tkinter.Frame.__init__(self, parent, **kw)
      self.__parent = parent       
      self.__align = None
    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)          
    align = property(lambda x: x.__align, __setAlign)

class TLabel(tkinter.Label):
    def __init__(self, parent, **kw):
      tkinter.Label.__init__(self, parent, **kw)
      self.__parent = parent       
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]      
      self["height"] = size[1]      
    def __setText(self, value):
      self["text"] = value
    def __setBackground(self, value):
      self["bg"] = value
    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)   
    text = property(lambda x: x["text"], __setText)
    background = property(lambda x: x["bg"], __setBackground)

class TButton(tkinter.Button):
    def __init__(self, parent, **kw):
      tkinter.Button.__init__(self, parent, **kw)
      self.__parent = parent       
      self.__position = (0, 0)
      self.__onClick = None
      self["command"] = self.__intOnClick
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    def __intOnClick(self):
      if self.__onClick:
        self.__onClick(self)  
    def __setOnClick(self, func):
      self.__onClick = func
    position = property(lambda x: x.__position, __setPosition)
    onClick = property(lambda x: x.__onClick, __setOnClick)

class TCheckBox(tkinter.Checkbutton):
    def __init__(self, parent, **kw):
      self.__var = tkinter.IntVar()
      tkinter.Checkbutton.__init__(self, parent, **kw)
      self["onvalue"] = 1        
      self["offvalue"] = 0        
      self["variable"] = self.__var
      self.__parent = parent       
      self.__position = (0, 0)
      self.__onChange = None
      self["command"] = self.__intOnChange
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    def __setChecked (self, value):
      if self.__var != value:  
        self.__var = int(value)      
        if self.__onChange:
          self.__onChange()
    def __intOnChange(self):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func
    position = property(lambda x: x.__position, __setPosition)
    checked = property(lambda x: x.__var.get() == 1, __setChecked)
    onChange = property(lambda x: x.__onChange, __setOnChange)

class TCanvas(tkinter.Canvas):
    def __init__(self, parent, **kw):
      tkinter.Canvas.__init__(self, parent, **kw)
      self.__parent = parent       
      self.__position = (0, 0)
    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)          
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    
class TImage(TCanvas):
    def __init__(self, parent, **kw):
      TCanvas.__init__(self, parent, **kw)
      self.__parent = parent       
      self.__position = (0, 0)
      self.__center = tkinter.NO
      self.__picture = None
      self.bind("<Configure>", self.__onResize)
    def __onResize(self, ev):
      self.redrawImage()
    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)          
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    def redrawImage(self):
      self.delete("all")
      pic = self.__picture
      if pic:          
        x0, y0 = 0, 0
        if self.__center:
          self.update()
          x0 = max( 0, (self.winfo_width()-pic.width())//2 )   
          y0 = max( 0, (self.winfo_height()-pic.height())//2 )  
        try: 
          self.create_image(x0, y0, anchor=tkinter.NW, image=pic)
        except: pass
    def __setCenter (self, value):
      if self.__center != value:
        self.__center = value
        self.redrawImage()
    def __setPicture (self, fName):
      try:
        self.__picture = tkinter.PhotoImage(file = fName)
        self.redrawImage()
      except:
        self.delete("all")
    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    center = property(lambda x: x.__center == 1, __setCenter)
    picture = property(lambda x: x.__picture, __setPicture)    
    
class TEdit(tkinter.Entry):
    def __init__(self, parent, **kw):
      tkinter.Entry.__init__(self, parent, **kw)
      self.__parent = parent       
      self.__position = (0, 0)
      self.__onChange = None
      self.__onValidate = None
      self.__var = tkinter.StringVar()
      self["textvariable"] = self.__var
      self.__text = self.__var.get()
      self.__var.trace("w", self.__trace)
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    def __trace(self, *args):
      valid = tkinter.YES  
      if self.__onValidate:
        valid = self.__onValidate()
      if valid:
        self.__text = self.__var.get()  
        if self.__onChange:
          self.__onChange(self)
      else:
        self.__var.set(self.__text)  
    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange: 
        self.__onChange(self)
    def __setOnValidate(self, func):
      self.__onValidate = func
    def __setText(self, value):
      self.__var.set(value)
      self.update()
      if self.__onChange:
        self.__onChange(self)
    position = property(lambda x: x.__position, __setPosition)
    text = property(lambda x: x.__var.get(), __setText)
    onChange = property(lambda x: x.__onChange, __setOnChange)
    onValidate = property(lambda x: x.__onValidate, __setOnValidate)
    
class TComboBox(ttk.Combobox):
  def __init__(self, parent, **kw):
    ttk.Combobox.__init__(self, parent, **kw)
    self.__parent = parent       
    self.__position = (0, 0)
  def __setPosition (self, pos):
    self.__position = pos
    self.place( x = self.__position[0], y = self.__position[1] )
  def __setAlign(self, align):
    self.__align = align
    if align == tkinter.TOP  or  align == tkinter.BOTTOM:
      self.pack(side=align, fill=tkinter.X)
    elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
      self.pack(side=align, fill=tkinter.Y)
    elif align == "client":
      self.pack(fill=tkinter.BOTH, expand=tkinter.YES)        
  def __setText(self, value):
    self.set(value)
    self.update()
  def findItem(self, value):
    if not self["values"]:
      return False
    else:
      return value in self["values"]
  def addItem(self, value):
    if not self["values"]:
      self["values"] = (value,)
    else:
      self["values"] = self["values"] + (value,)    
  position = property(lambda x: x.__position, __setPosition)
  align = property(lambda x: x.__align, __setAlign)
  text = property(lambda x: x.get(), __setText)

class TListBox(tkinter.Listbox):
  def __init__(self, parent, **kw):
    self.__panel = TPanel(parent)
    tkinter.Listbox.__init__(self, self.__panel, **kw)
    self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
    self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    self.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    self.__sbar.config(command=self.yview)
    self.configure(yscrollcommand=self.__sbar.set)
    self.__position = (0, 0)
  def __setPosition (self, pos):
    self.__position = pos
    self.__panel.place( x = self.__position[0], y = self.__position[1] )
  def __setAlign(self, align):
    self.__align = align
    if align == tkinter.TOP  or  align == tkinter.BOTTOM:
      self.__panel.pack(side=align, fill=tkinter.X)
    elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
      self.__panel.pack(side=align, fill=tkinter.Y)
    elif align == "client":
      self.__panel.pack(fill=tkinter.BOTH, expand=tkinter.YES)
  position = property(lambda x: x.__position, __setPosition)
  align = property(lambda x: x.__align, __setAlign)

class TRadioGroup(TPanel):
    def __init__(self, parent, items, **kw):
      self.__parent = parent       
      self.__var = tkinter.StringVar()
      TPanel.__init__(self, parent, **kw)
      for text, code in items:
        btn = tkinter.Radiobutton(self, text=text,
            variable=self.__var, value=code)
        btn.pack(anchor=tkinter.W)      
      if len(items):  
        self.__var.set(items[0][1])   
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__align = None
    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )
    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)          
    def __setSelected (self, value):
      self.__var.set(pos)
    position = property(lambda x: x.__position, __setPosition)
    align = property(lambda x: x.__align, __setAlign)
    selected = property(lambda x: x.__var.get(), __setSelected)
    
class TGroupBox(tkinter.LabelFrame):
  def __init__(self, parent, **kw):
    tkinter.LabelFrame.__init__(self, parent, **kw)
    
class TMemo(tkinter.Text):
  def __init__(self, parent, **kw):
    self.__panel = TPanel(parent)
    tkinter.Text.__init__(self, self.__panel, **kw)
    self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
    self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    self.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    self.__sbar.config(command=self.yview)
    self.configure(yscrollcommand=self.__sbar.set)
    self.__position = (0, 0)
  def __setPosition (self, pos):
    self.__position = pos
    self.__panel.place( x = self.__position[0], y = self.__position[1] )
  def __setAlign(self, align):
    self.__align = align
    if align == tkinter.TOP  or  align == tkinter.BOTTOM:
      self.__panel.pack(side=align, fill=tkinter.X)
    elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
      self.__panel.pack(side=align, fill=tkinter.Y)
    elif align == "client":
      self.__panel.pack(fill=tkinter.BOTH, expand=tkinter.YES)
  align = property(lambda x: x.__align, __setAlign)
  position = property(lambda x: x.__position, __setPosition)
    