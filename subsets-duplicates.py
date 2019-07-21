def find_subsets(nums):
    subsets = []
    subsets.append([])
    nums.sort()
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            newset = list(subsets[j])
            newset.append(nums[i])
            subsets.append(newset)
    return subsets


def main():
  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))

#TC O(N)
#SC O(N)

main()