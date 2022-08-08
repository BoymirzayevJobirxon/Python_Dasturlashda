# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  16_sqlite.py - использование базы данных sqlite3

  Утилиты командной строки для работы с sqlite3:
    https://sqlite.org/2018/sqlite-tools-win32-x86-3250200.zip
  Открытие (создание) базы данных:
    > sqlite3 phonebook.db
  Создание структуры базы данных:
  sqlite> create table contacts
            (
            id integer primary key autoincrement,
            name string not null,
            number string not null
            );
"""
import sqlite3
from simpletk import *

def execSQL ( query, params = () ):
  with sqlite3.connect( dbName ) as conn:
    cursor = conn.cursor()
    result = list(cursor.execute(query, params))
    conn.commit()
  return result

def loadTableFromBase ():
  query = 'SELECT * FROM contacts ORDER BY name desc'
  records = execSQL(query)
  table.clear()
  for row in records:
    table.appendRow( row )

def addRecord( sender ):
  query = 'INSERT INTO contacts VALUES(NULL,?, ?)'
  parameters = ( nameEdit.text, phoneEdit.text )
  execSQL( query, parameters )
  loadTableFromBase()
  nameEdit.text = ''
  phoneEdit.text = ''

def execSQLCommand( event ):
  result = execSQL(sqlMemo.text)
  print( result )
  loadTableFromBase()

dbName = "phonebook.db"

execSQL( """create table if not exists contacts
            (
            id integer primary key autoincrement,
            name string not null,
            number string not null
            );""" )

app = TApplication("База данных sqlite3")
app.size = (400, 350)

font = ('Arial', 11)
topPanel = TPanel(app, height = 52)
topPanel.align = TOP
nameLbl = TLabel(topPanel, text = "Имя", font = font)
nameLbl.position = (5, 5)
phoneLbl = TLabel(topPanel, text = "Телефон", font = font)
phoneLbl.position = (5, 25)

nameEdit = TEdit(topPanel, width = 160, font = font)
nameEdit.position = (75, 5)
phoneEdit = TEdit(topPanel, width = 160, font = font)
phoneEdit.position = (75, 25)

addImage = PhotoImage('save.gif')
addBtn = TButton(topPanel, text = " Добавить", width = 120, height = 30,
                 font = font, image = addImage )
addBtn.position = (250, 10)
addBtn.onClick = addRecord

sqlMemo = TMemo(app, height = 100)
sqlMemo.align = BOTTOM
sqlMemo.text = "select * from contacts"

sqlPanel = TPanel(app, height = 32)
sqlPanel.align = BOTTOM
lblSQL = TLabel(sqlPanel, text = 'SQL-запрос', font = font )
lblSQL.position = (5, 5)

execImage = PhotoImage('exec.gif')
sqlGoBtn = TButton(sqlPanel, text = "Go!", width = 60, height = 27,
                   font = font, image = execImage)
sqlGoBtn.position = (100, 2)
sqlGoBtn.onClick = execSQLCommand

table = TStringGrid( app, columns = ['A', 'B', 'C'],
                     oddColor = "#F0F0F0" )
table.align = CLIENT
table.font = font

  # Заголовки столбцов все сразу
table.allHeadings( ['ID', 'Имя', 'Телефон'] )

  # Настройка столбцов по номерам
table.column( "#0", minwidth = 0, width = 40 )
table.column( "#1", minwidth = 0, width = 100 )
table.column( "#2", minwidth = 0, width = 100 )

loadTableFromBase()

app.run()


