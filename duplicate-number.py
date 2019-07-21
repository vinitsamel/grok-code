def find_duplicate(arr):
  i = 0
  while i < len(arr):
      j = arr[i] - 1
      if arr[i] != arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
      else:
          i += 1
      print (arr)

  for i in range(len(arr)):
      if arr[i] != i+1:
          return arr[i]

  return -1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()