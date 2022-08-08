# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 13. Очередь. Заливка области
"""
def ShowMatrix(A):
  print("----------------------")
  for row in A:
    for x in row:
      print(x, " ", end="", sep="");
    print()
  print("----------------------")
  
def ShowQueue ( Q ):
  for x in Q:
    print(x, " ", sep="", end="")
  print()

Fin = open ( "input_map.dat" );
arS = Fin.readlines()
A = []
for s in arS:
  lst = s.split()
  A.append(lst)
Fin.close()
 
print ( "Исходная матрица:" )
ShowMatrix ( A );

YMAX = len(A)
XMAX = len(A[0])
NEW_COLOR = 2
x0 = 1
y0 = 0
color = A[y0][x0]

Q = []
Q.append ( (x0,y0) ) 
print ( "Изменение очереди:" )
ShowQueue ( Q );

while len(Q) > 0:	
  x, y = Q.pop(0)	
  if A[y][x] == color:	
    A[y][x] = NEW_COLOR	
    if x > 0:      Q.append( (x-1,y) )	
    if x < XMAX-1: Q.append( (x+1,y) )	
    if y > 0:      Q.append( (x,y-1) )	
    if y < YMAX-1: Q.append( (x,y+1) )
  ShowQueue ( Q );

print ( "Матрица после заливки:" )
ShowMatrix ( A );
