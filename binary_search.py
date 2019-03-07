def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) / 2
    guess = list[mid]
    print('low ->', low)
    print('high ->', high)
    print('mid ->', mid)
    print('guess ->', guess)
    print('=====')
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

my_list = [1, 3, 5, 7, 9]
print('Result:', binary_search(my_list, 3))
