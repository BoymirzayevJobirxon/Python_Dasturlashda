# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 16. Графы. Построение минимального остовного дерева графа
"""

ASCII = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
INF = 30000

def ReadWeightMatrix():
  global N, W
  Fin = open ( "input_graphs.dat" )
  N = int(Fin.readline())
  W = []  
  for i in range(N):
    row = list(map(int, Fin.readline().split()))
    W.append(row)
  Fin.close()  
  print ( "Весовая матрица графа: " )
  print ( "      ", end="" )
  for j in  range(N):
    print ( "{:4s}".format(ASCII[j]), end="" )
  print ( "\n----", "----"*N, sep="" )
  for i in range(N):
    print ( "{:2s}|".format(ASCII[i]), end="" )
    for j in range(N):
      if W[i][j] < 0:
        W[i][j] = INF
        print ( "   .", end="" )
      else:
        print ( "{:4d}".format(W[i][j]), end="" )
    print();

ReadWeightMatrix();

col = [i for i in range(N)]
ostov = []
for k in range(N-1):
    # поиск ребра с минимальным весом 
  minDist = 1e10         # очень большое число	
  for i in range(N):
    for j in range(N):
      if col[i] != col[j] and W[i][j] < minDist: 
        iMin = i 
        jMin = j 
        minDist = W[i][j]
    # добавление ребра в список выбранных 
  ostov.append ( (iMin, jMin) )
    # перекрашивание вершин 
  c = col[jMin]
  for i in range(N):
    if col[i] == c:
      col[i] = col[iMin] 

print ( "Минимальное остовное дерево графа:" )
for edge in ostov:
  print ( "(", ASCII[edge[0]], ",", ASCII[edge[1]], ")", sep="" )
