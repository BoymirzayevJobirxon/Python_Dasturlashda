# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 2. Динамическое программирование.
                 Размен монет - количество вариантов
"""
P = [1, 2, 5, 10]
MMAX = len(P)
WMAX = 100

T = []
for i in range(MMAX):
  T.append([0]*(WMAX+1))  

def RazmenPerebor ( N ): 
  count = 0;
  for i10 in range(N // P[3]+1):
    K10 = N - i10*P[3]
    for i5 in range(K10 // P[2]+1):
      K5 = N - i10*P[3] - i5*P[2]
      for i2 in range(K5 // P[1]+1):
        K2 = N - i10*P[3] - i5*P[2] -i2*P[1];
        if K2 % P[0] == 0:
          count += 1
  return count

def showTable ( P, T, N ):
  print("   ", end="")
  for w in range(N+1): 
    print("{:3d}".format(w), end="")
  print()
  for i in range(1,N+3):
    print("---", end="")
  print()
  for i in range(MMAX):
    print( "{:2d}:".format(P[i]), end="" )
    for w in range(N+1):
      print("{:3d}".format(T[i][w]) , end="")
    print()
  print()

print ( "Имеются монеты достоинством " )
for i in range(MMAX):
  if i > 0:
    if i == MMAX-1:
      print( " и ", end="" )
    else:
      print ( ", ", end="" )
  print ( P[i], end="" )
  if i == MMAX-1:
    print( " руб." )

while True:
  print ( "Введите сумму для размена (1..", 
           WMAX, "): ", sep="" );
  N = int(input())
  if 1 <= N and N <= WMAX: break

for i in range(P[0],N+1):
  T[0][i] = 1

for i in range(MMAX):
  T[i][0] = 1

for i in range(1,MMAX):
  for w in range(1,N+1):
    T[i][w] = T[i-1][w]
    if w >= P[i]:
      T[i][w] = T[i][w] + T[i][w-P[i]]

showTable(P, T, N)

print ( "Число вариантов размена:", T[MMAX-1][N] )
print ( "Проверка методом перебора... " )
print ( "  Число вариантов размена:", RazmenPerebor(N) )
