graph = {
"a": {"colour": "White", "neighbours": ["b", "d", "e"]},
"b": {"colour": "White", "neighbours": ["a", "c", "d"]},
"c": {"colour": "White", "neighbours": ["b", "g"]},
"d": {"colour": "White", "neighbours": ["a", "b", "e", "f"]},
"e": {"colour": "White", "neighbours": ["a", "d"]},
"f": {"colour": "White", "neighbours": ["d"]},
"g": {"colour": "White", "neighbours": ["c"]},
}


def bfs(graph, vertex):
  queue = [] # to be visited
  visited = []
  queue.append(vertex) #start the cycle
  while len(queue) != 0: #while queue is not empty
    currentNode = queue[0] #first item in queue
    visited.append(currentNode) #add to visited list
    queue.remove(currentNode) #remove from queue
    graph[currentNode]["colour"] = "Black" #mark as visited
    for neighbour in graph[currentNode]["neighbours"]: #for all it's neighbours
      if graph[neighbour]["colour"] == "White": #if it hasn't been marked at all
        queue.append(neighbour) #add it to the queue
        graph[neighbour]["colour"] = "Grey" #mark is as added to the queue
  return visited #final list of visited nodes


visited = bfs(graph, "a")
print("Order:", visited)