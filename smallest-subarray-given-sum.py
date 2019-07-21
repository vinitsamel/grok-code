import math

def smallest_subarray_with_given_sum(S, arr):
    windowSum = 0
    windowStart = 0
    minLength = math.inf
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= S:
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    return minLength

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()