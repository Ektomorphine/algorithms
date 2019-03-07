# Insertion sorting algorithm

def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if smallest > arr[i]:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def insertionSort(arr):
  sortedArray = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    sortedArray.append(arr.pop(smallest))
  return sortedArray

print(insertionSort([2, 3, 1, 6, 78, 4]))
