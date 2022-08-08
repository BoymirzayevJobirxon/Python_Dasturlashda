# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 18. Графы. Кратчайшие пути.
                 Алгоритм Флойда-Уоршелла
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

P = []
for i in range(N):
  P.append([i]*N)
  P[i][i] = -1

for k in range(N):
  for i in range(N):
    for j in range(N):
      if W[i][k] + W[k][j] < W[i][j]:
        W[i][j] = W[i][k] + W[k][j]
        P[i][j] = P[k][j]
      
print ( "\nМатрица кратчайших расстояний:" );
print ( "      ", end="" );
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

print ( "\nВспомогательная матрица:");
print ( "       ", end="" );
for j in range(N):
  print ( "{:4s}".format(ASCII[j]), end="" )
print()
print ( "----"*(N+1) )
for i in range(N):
  print ( "{:2s} |".format(ASCII[i]), end="" )
  for j in range(N):
    print( "{:4d}".format(P[i][j]), end="" )
  print()

print()
for i in range(N):
  print ( "Кратчайшие маршруты из вершины {0}:".format(ASCII[i]) )
  for k in range(N):
    if k != i:
      j = k
      while j != -1:
        print ( "{:2s}".format(ASCII[j]), end="" )
        if j != i:
          print ( " <- ", end="" );
        j = P[i][j];
      print();
