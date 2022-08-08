# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 17. Графы. Кратчайшие пути. Алгоритм Дейкстры
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

active = [True]*N # все вершины не просмотрены
R = W[0][:]       # скопировать в R строку 0 весовой матрицы
P = [0]*N         # только прямые маршруты из вершины 0

active[0] = False
P[0] = -1

for i in range(N-1):
    # поиск новой рабочей вершины R[j] -> min  
  minDist = 1e10 # очень большое число
  for j in range(N):
    if active[j] and R[j] < minDist:
      minDist = R[j]
      kMin = j
  active[kMin] = False
    # проверка маршрутов через вершину kMin  
  for j in range(N):
    if R[kMin] + W[kMin][j] < R[j]: 
      R[j] = R[kMin] + W[kMin][j]
      P[j] = kMin

print ( "\nВспомогательные массивы:")
print ( "      ", end="" )
for i in range(N):
  print ( "{:4s}".format(ASCII[i]), end="" )
print();
print( "---"*(N+1) )
print( "R |", end="" )
for i in range(N): 
  print ( "{:4d}".format(R[i]), end="" )
print();
print( "P |", end="" )
for i in range(N):
  if P[i] < 0: 
    print ( "   .", end="" );
  else: 
    print ( "{:>4s}".format(ASCII[P[i]]), end="" )
print ();

print();
print( "Кратчайший маршрут из вершины A в вершину {:s}:".format(ASCII[N-1]) )
i = N-1
while i >= 0:
  print ( "{:2s}".format(ASCII[i]), end="" )
  if i != 0:
    print ( " <- ", end="" )
  i = P[i]
