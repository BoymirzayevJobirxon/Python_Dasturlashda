# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 11. Вычисление постфиксной формы
 Вход: 
   нет
 Результат: 
   2
"""
#s = input("Введите выражение в постфиксной записи: ")
s = "5 15 + 4 7 + 1 - /"
data = s.split()				

stack = []					
for x in data:					
  if x in "+-*/":				
    op2 = int(stack.pop())			
    op1 = int(stack.pop())			
    if   x == "+": res = op1 + op2		
    elif x == "-": res = op1 - op2		
    elif x == "*": res = op1 * op2		
    else:         res = op1 // op2		
    stack.append ( res )			
  else:
    stack.append ( x )				
print ( stack[0] )					
