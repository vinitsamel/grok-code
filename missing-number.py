def find_missing_number(arr):
    i = 0
    n = len(arr)
    while i < n:
        #print (arr[i])
        if arr[i] != i and arr[i] < n:
            temp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = temp
        else:
            i += 1
    print (arr)
    while i in range(n):
        if arr[i] != i:
            return i
    return n

def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()