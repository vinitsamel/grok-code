def remove_duplicates(arr):
   leftPointer = 0
   rightPointer = leftPointer + 1
   triggerSwap = False
   while rightPointer < len(arr):
       if arr[leftPointer] < arr[rightPointer]:
           if not triggerSwap:
               leftPointer += 1
               rightPointer += 1
           else:
               leftPointer += 1
               arr[leftPointer] = arr[rightPointer]
               triggerSwap = False
       elif arr[leftPointer] == arr[rightPointer]:
           rightPointer += 1
           triggerSwap = True
   return arr[:leftPointer+1]

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()