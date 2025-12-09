def InsSort(aList):
  n = len(aList)
  for i in range(1, n):
    currentValue = aList[i]
    position = i
    while position > 0 and aList[position-1] > currentValue:
      aList[position] = aList[position-1]
      position = position - 1
    aList[position] = currentValue

list = [2, 6, 8, 5, 3, 4, 2, 9, 12, 4, 1, 2, 2]
InsSort(list)
print(list)