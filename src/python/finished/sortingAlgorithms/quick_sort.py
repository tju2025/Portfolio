def part(list, start, end):
  pivot = list[start] #the pivot is initally the number at the index 'start'
  left = start + 1 
  right = end
  done = False
  #swapping allows values lower than the pivot to be on the left, and those higher than the pivot to be on the right
  while done == False:
    #iterate through list from left to right until either the left pointer crosses the right one, or the value at the left pointer exceeds the pivot value
    while left <= right and list[left] <= pivot:
      left += 1 #ul = [40, 5, 2, 88, 33, 56, 2, 10]
    #iterate through list from right to left until either the right pointer crosses the left one, or the value at the right pointer is lower than the pivot value
    while right >= left and list[right] >= pivot: 
      right -= 1 
    #when the right pointer is less than the left, there are no values where they shouldn't be - left got rid of all higher than pivot, right got rid of all lower
    if right < left:
      done = True
    else:
      #swap the values at the pointers
      temp = list[left] 
      list[left] = list[right]
      list[right] = temp
  #swap the pivot value and the value at the pointer right
  temp = list[start]
  list[start] = list[right]
  list[right] = temp
  #right is now the pivot, and so is sorted
  return right

def quicksort(list, start, end):
  if start < end: #if the first index is less than the last index
    split = part(list, start, end)
    #do the same for the sections of lists
    quicksort(list, start, split-1)
    quicksort(list, split+1, end)
  return list

ul = [40, 5, 2, 88, 33, 56, 2, 10]
ol = quicksort(ul, 0, len(ul)-1)
#The list you want sorted, the start and end of the section you want sorted
print(ol)