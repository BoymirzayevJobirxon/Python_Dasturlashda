# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 14. Деревья. 
                 Вычисление арифметических выражений
"""
class TNode:
  pass

def newNode( d ):
  node = TNode()
  node.data = d
  node.left = None
  node.right = None
  return node

def priority ( op ):
  if op in "+-": return 1
  if op in "*/": return 2
  return 100 

def lastOp ( s ):
  minPrt = 50   # любое между 2 и 100
  k = -1
  for i in range(len(s)):
    if priority(s[i]) <= minPrt:
      minPrt = priority(s[i])
      k = i
  return k 

def makeTree ( s ):
  k = lastOp(s)
  if k < 0:	# создать лист
    Tree = newNode ( s )
  else:	# создать узел-операцию
    Tree = newNode ( s[k] )
    Tree.left = makeTree ( s[:k] )
    Tree.right = makeTree ( s[k+1:] )
  return Tree 

def calcTree ( Tree ):
  if Tree.left == None:
    return int(Tree.data)
  else:
    n1 = calcTree ( Tree.left )
    n2 = calcTree ( Tree.right )
    if Tree.data == "+":   res = n1 + n2
    elif Tree.data == "-": res = n1 - n2
    elif Tree.data == "*": res = n1 * n2
    else: res = n1 // n2
    return res

s = input("Введите арифметическое выражение без скобок: \n" )
T = makeTree ( s );
print ( "Результат:", calcTree(T) )
