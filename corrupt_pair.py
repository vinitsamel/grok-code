def find_corrupt_numbers(arr):
    # TODO: Write your code here
    i = 0
    while i < len(arr):
        j = arr[i]-1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    corruptPair = [-1, -1]
    for i in range(len(arr)):
        if arr[i] != i+1:
            corruptPair = [arr[i], i+1]
    return corruptPair


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))

main()

#TC O(N)
#SC O(1)