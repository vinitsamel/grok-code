import math

def calculateSum(arr):
    sumArr = 0
    for i in arr:
      sumArr += i
    return sumArr

def max_sub_array_of_size_k_brute(k, arr):
    max = 0
    maxStart = 0
    maxEnd = 0
    windowStart = 0
    while windowStart < (len(arr) - k):
        subTotal = calculateSum(arr[windowStart: windowStart + k])
        if subTotal > max:
            max = subTotal
            maxStart = windowStart
            maxEnd = windowStart + k
        windowStart += 1
    return arr[maxStart:maxEnd]

def max_sub_array_of_size_k(k, arr):
    windowSum, maxSum = 0, 0
    windowStart = 0
    maxStart = 0
    maxEnd = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            if windowSum > maxSum:
                maxSum = windowSum
                maxStart = windowStart
                maxEnd = windowEnd
            windowSum -= arr[windowStart]
            windowStart += 1
    return arr[maxStart:maxEnd+1]

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()