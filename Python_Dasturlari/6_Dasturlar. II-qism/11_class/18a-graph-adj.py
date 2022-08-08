# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 11 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 6.
 Программа № 18a. Графы. Использование списков смежности
 Вxод:
  нет
 Результат: 
  3 
"""
Graph = [ [],     	# фиктивный элемент
          [4], 	        # список смежности для вершины 1	
          [1,3], 	# ... для вершины 2
          [],	        # ... для вершины 3	
          [2,3,5],      # ... для вершины 4
          [3] ]         # ... для вершины 5

def pathCount ( graph, vStart, vEnd, visited = None ):  
  if vStart == vEnd: return 1
  if visited is None: visited = []
  visited.append ( vStart )
  count = 0
  for v in graph[vStart]:
    if not v in visited:
      count += pathCount ( graph, v, vEnd, visited )
  visited.pop()
  return count

print ( pathCount (Graph, 1, 3) ) 