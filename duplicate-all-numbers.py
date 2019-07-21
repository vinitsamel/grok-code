def find_all_duplicates(arr):
    duplicateNumbers = []
    i = 0
    while i < len(arr):
      j = arr[i]-1
      if arr[i] != arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
      else:
          i += 1

    for i in range(len(arr)):
       if arr[i] != i + 1:
           duplicateNumbers.append(arr[i])
    return duplicateNumbers


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()

#TC O(N)
#SC O(1)