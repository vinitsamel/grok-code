def remove_element(arr, key):
    keyPointer = 0
    #todo: 1 length case
    i = 0
    while i < len(arr):
        if arr[keyPointer] == key and arr[i] != key:
            temp = arr[i]
            arr[i] = arr[keyPointer]
            arr[keyPointer] = temp
            keyPointer += 1
        i += 1
    return keyPointer


def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))

main()