def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print (arr)
    return arr

def selectionsort(arr):
    return arr

def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr.pop(i)
                arr.insert(j, temp)
        print (arr)
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])
    #print (leftArr, rightArr, arr)
    return merge(leftArr, rightArr, arr.copy())


def merge(leftArr, rightArr, arr):
    leftPointer, rightPointer, mergePointer = 0, 0, 0
    while leftPointer < len(leftArr) and rightPointer < len(rightArr):
        if leftArr[leftPointer] < rightArr[rightPointer]:
            arr[mergePointer] = leftArr[leftPointer]
            leftPointer += 1
        else:
            arr[mergePointer] = rightArr[rightPointer]
            rightPointer += 1
        mergePointer += 1

    while leftPointer < len(leftArr):
        arr[mergePointer] = leftArr[leftPointer]
        leftPointer += 1
        mergePointer += 1

    while rightPointer < len(rightArr):
        arr[mergePointer] = rightArr[rightPointer]
        rightPointer += 1
        mergePointer += 1
    print (arr)
    return arr



def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    i += 1
    print (arr)
    return i

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)
    return arr


def main():
    arr = [14, 5, 3, 9, 2, 12, 10, 1, 0]
    print(bubblesort(arr))
    print ('-' * 50)
    arr = [14, 5, 3, 9, 2, 12, 10, 1, 0]
    print (selectionsort(arr))
    print('-' * 50)
    arr = [14, 5, 3, 9, 2, 12, 10, 1, 0]
    print(insertionsort(arr))
    print('-' * 50)
    arr = [14, 5, 3, 9, 2, 12, 10, 1, 0]
    print(mergeSort(arr))
    print('-' * 50)
    arr = [14, 5, 3, 9, 2, 12, 10, 1, 0]
    print(quicksort(arr, 0, len(arr)-1))

main()
