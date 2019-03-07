# Quick sorting algorithm

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([12, 23, 45, 453, 5656523, 324, 423, 34, 3, 34, 545]))
