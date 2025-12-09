from finished.sortingAlgorithms.quick_sort import quicksort
graph = {
  "a":{"colour":"white", "neighbours":{"b":7 , "d":3}},
  "b":{"colour":"white", "neighbours":{"a":7, "c":3, "d":2, "e":6}},
  "c":{"colour":"white", "neighbours":{"b":3, "d":4, "e":1}},
  "d":{"colour":"white", "neighbours":{"a":3, "b":2, "c":4, "e":7}},
  "e":{"colour":"white", "neighbours":{"b":6, "c":1, "d":7}}
} #graph represented as nested dicts

total = 0 #to make sure they aren't done first
add = 1 #to make quicksort work
for i in graph:
  for j in graph[i]["neighbours"]:
    total += graph[i]["neighbours"][j]
for i in graph:
  graph[i]["distance"] = total + add
  add += 1
#adding edgeweights as a high number (infinite)

def dspa(graph, startVertex):
  pq = {} #priority queue
  rpq = {} #reverse priority queue
  graph[startVertex]["distance"] = 0
  print(pq, "pq initialised")
  for i in graph:
    pq[i] = graph[i]["distance"] #filling priority queue
  diff = 0.0001 #small number
  for i in pq:
    for j in pq:
      if pq[i]==pq[j] and i!=j: #changing similar values
        pq[j] += diff
        diff += 0.0001
    rpq[pq[i]] = i #creating a reverse key
  print(pq, "start of pq, needs ordering")
  print(rpq, "start of rpq")
  ul = [] #unordered list
  for i in rpq:
    ul.append(i)
  print(ul, "ul start")
  ol = quicksort(ul, 0, len(ul)-1) #sorting list
  print(ol, "ol start")
  queue = []
  for i in ol:
    queue.append(rpq[i])
  print(queue, "queue start") #creating list of nodes to be visited
  visited = []
  while len(queue) > 0:
    currentNode = queue[0]
    graph[currentNode]["colour"] = "black"
    print(graph[currentNode], currentNode, "in graph")
    queue.remove(currentNode)
    print(queue, "queue after node has been visited")
    visited.append(currentNode)
    print(visited, "visited after cn added")
    uneighbourList = [] #ul of neighbours of currentNode
    for neighbour in graph[currentNode]["neighbours"]:
      uneighbourList.append(neighbour)
    print(uneighbourList, "unlist start")
    undistanceList=[] #neighbour distance list
    for neighbour in uneighbourList:
      undistanceList.append(pq[neighbour])
    print(undistanceList, "undlist start")
    ondistanceList = quicksort(undistanceList, 0, len(undistanceList)-1)
    print(ondistanceList, "ondlist start")
    oneighbourList = []
    for distance in ondistanceList:
      oneighbourList.append(rpq[distance])
    print(oneighbourList, "onlist start")
    for neighbour in oneighbourList:
      if graph[neighbour]["colour"] != "black":
        if graph[neighbour]["colour"] == "white":
          graph[neighbour]["colour"] = "grey"
        distance = graph[currentNode]["neighbours"][neighbour] + pq[currentNode]
        print(distance, neighbour, "distance")
        if distance < pq[neighbour]:
          pq[neighbour] = distance
          print(pq, "pq after change")
          diff = 0.0001
          for i in pq:
            for j in pq:
              if pq[i]==pq[j] and i!=j: #changing similar values
                pq[j] += diff
              diff += 0.0001
            rpq[pq[i]] = i #recreating a reverse key
          print(rpq, "rpq after change")
          ul = [] #unordered list
          for i in rpq:
            ul.append(i)
          print(ul, "ul in next iteration")
          ol = quicksort(ul, 0, len(ul)-1) #sorting list
          print(ol, "ol in next iteration")
          for done in visited:
            ol.remove(done)
          queue = ol
    break
  return ""
print(dspa(graph, "a"))
  #=================================================================

#import infinity from math, use partitioning lists to sort before dealing with infinities and sorting.