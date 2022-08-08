# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 15. Деревья. Вычисление арифметических выражений.
                 Хранение узлов бинарного дерева в массиве
"""
def addToTree(s, T, k):
  while k > len(T)-1:
    T.append(None)
  T[k] = s  

def priority(op):
  if op in "+-": return 1
  if op in "*/": return 2
  return 100

def lastOp(s):
  minPrt = 50
  k = -1
  for i in range(len(s)):
    if priority(s[i]) <= minPrt:
      minPrt = priority(s[i])
      k = i
  return k

def makeTree ( s, Tree, root ):
  s = s.strip()
  k = lastOp(s)
  if k < 0:
    addToTree ( s, Tree, root )
  else:
    addToTree ( s[k], Tree, root )
    makeTree ( s[:k], Tree, 2*root+1 )
    makeTree ( s[k+1:], Tree, 2*root+2 )
  
def calcTree ( Tree, root ):
  if 2*root+2 >= len(Tree) or Tree[2*root+1] == None:
    return int(Tree[root])
  else:
    n1 = calcTree ( Tree, 2*root+1 )
    n2 = calcTree ( Tree, 2*root+2 )
    if Tree[root] == "+":   res = n1 + n2
    elif Tree[root] == "-": res = n1 - n2
    elif Tree[root] == "*": res = n1 * n2
    else: res = n1 // n2
    return res 

s = input("Введите арифметическое выражение без скобок: \n" )
Tree = []
makeTree ( s, Tree, 0 )
print ( "Результат:", calcTree(Tree, 0) )
