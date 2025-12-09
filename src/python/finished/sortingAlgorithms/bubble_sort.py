numbers = [9, 5, 4, 15, 3, 8, 11]
numItems = len(numbers)
for i in range(0, numItems - 1):
  for j in range(0, numItems - i - 1):
    if numbers[j] > numbers[j + 1]:
      temp = numbers[j]
      numbers[j] = numbers[j+1]
      numbers[j+1] = temp
print(numbers)