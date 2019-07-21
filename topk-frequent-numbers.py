from heapq import heappush, heappop

def find_k_frequent_numbers(nums, k):
    numfreqDict = {}
    for num in nums:
        if num in numfreqDict.keys():
            numfreqDict[num] += 1
        else:
            numfreqDict[num] = 1

    minheap = []
    for num, freq in numfreqDict.items():
        heappush(minheap, (freq, num))
        if len(minheap) > k:
            heappop(minheap)

    kfrequent = []
    while minheap:
        kfrequent.append(heappop(minheap)[1])

    return kfrequent



def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

