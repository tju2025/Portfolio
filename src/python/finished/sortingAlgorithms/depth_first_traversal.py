graph = { "a": ["b", "d", "e"], "b": ["a", "c", "d"], "c": ["b", "g"], "d": ["a", "b", "e", "f"], "e":["a", "d"], "f": ["d"], "g": ["c"]}
visited = [] #empty list of visited nodes

def dfs(graph, currentvertex, visitedlist):
  visitedlist.append(currentvertex) #visit the current node
  print(visitedlist)
  for vertex in graph[currentvertex]: # for all neighbours of currentvertex
    if vertex not in visitedlist: #if they haven't been visited
      dfs(graph, vertex, visitedlist) #reccurance
  return visitedlist

traversal = dfs(graph, "a", visited)
print("Nodes visited in the order: ", traversal)

#goes down the path until it cannot go anymore, then uses backtracking
#uses a recursion stack