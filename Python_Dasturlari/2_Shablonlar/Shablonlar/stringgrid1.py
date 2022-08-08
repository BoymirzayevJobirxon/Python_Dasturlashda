from simpletk import *

app = TApplication("Использование таблицы (TStringGrid)")
app.size = (400, 350)

table = TStringGrid( app,
                     columns = ['A', 'B', 'C'],  # кодовые имена столбцов
                     oddColor = 'red',           # фон нечётных строк
                     evenColor = 'green'  )      # фон чётных строк
table.align = "client"

  # Заголовки столбцов по одному
table.heading( '#0', 'Name' )
table.heading( 'A', 'Apple' )    # или table.heading( '#1', 'Apple' )
table.heading( 'B', 'Samsung' )  # или table.heading( '#2', 'Samsung' )
table.heading( 'C', 'Nokia' )    # или table.heading( '#2', 'Nokia' )

  # Заголовки столбцов все сразу
table.allHeadings( ['Фамилия', 'Имя', 'Отчество', 'Телефон'] )

  # Настройка столбцов по номерам
table.column( "#0", minwidth = 0, width = 100, stretch = NO )
table.column( "#1", minwidth = 0, width = 100, stretch = NO )
table.column( "#2", minwidth = 0, width = 100 )
table.column( "#3", minwidth = 0, width = 100 )

  # Добавление строк
for i in range(5):
  table.appendRow( [str(i+1)+'-Пупкин', 'Василий', 'Алексеевич', '271-34-98'])

  # Меняем количество строк
table.rowCount = 3
table.rowCount = 8

  # Выводим значения отдельных ячеек
print( table[0, 0] )
print( table[0, 1] )
print( table[0, 2] )
print( table[0, 3] )

  # Меняем значения отдельных ячеек
table[0, 0] = 'Воронов'
table[1, 1] = 'Тимофей'
table[2, 2] = 'Петрович'

  # Вставляем строку
table.insertRow( 2, ['Семёнов', 'Кузьма', 'Мефодьевич'] )

  # Добавляем строку в коней
table.appendRow( ['Smith', 'John', 'Marta'] )

  # Изменяем строку
table.updateRow( 5, ['Романов', 'Григорий'] )

  # Удаляем строку
table.deleteRow( 2 )

  # Меняем цвета расраски
table.oddColor = '#F0F0F0'
table.evenColor = 'white'

  # Реакция на щелчок мыши
def click( event ):
  print( event.cell ) # (строка, столбец, идентификатор строки) для ячейки
  if event.cell:
    table.editCell( event.cell[0], event.cell[1] )
    #table.editCell( event.cell )
table.onClick = click

def editedCell( event ):
  print( event.cell_row ) # (строка, столбец) ячейки, где изменили значение
  print( event.cell_col )
  print( event.row_id )   # идентификатор ячейки, где изменили значение
  print( event.old_data, event.new_data ) # старое и новое значения ячейки

table.onEditedCell = editedCell

  # Очищаем таблицу
#table.clear()

app.run()


