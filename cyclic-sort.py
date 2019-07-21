def cyclic_sort(arr):
    print (arr)
    i = 0
    while i < len(arr):
        if arr[i] != i+1:
            temp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
        else:
            i += 1
        #print (arr)
    return arr

def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))


main()

#TC O(N)
#SC O(1)