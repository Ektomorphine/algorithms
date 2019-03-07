def sum(array):
  if len(array) == 0:
    return 0
  return array[0] + sum(array[1:])

print(sum([1,2,3,5,6,7,8]))
