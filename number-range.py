def find_range(arr, key):
    start, end = 0, len(arr) - 1
    startKey, endKey = -1, -1
    while start <= end:
        mid = int((start+end)/2)
        #print (start, end, mid)
        if arr[mid] == key:
            startKey = mid
            break
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    endKey = startKey
    #print (startKey, endKey)
    while endKey < len(arr):
        if arr[endKey] != key:
            #print (arr[endKey])
            endKey -= 1
            break
        endKey += 1
        #print(startKey, endKey)
    while startKey >= 0:
        if arr[startKey] != key:
            startKey += 1
            break
        startKey -= 1
        #print(startKey, endKey)
    return [startKey, endKey]

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()
