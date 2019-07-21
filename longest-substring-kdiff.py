def longest_substring_with_k_distinct(str, k):
  windowStart = 0
  maxLength = 0
  maxStart = 0
  maxEnd   = 0
  tempDict = {}
  for windowEnd in range(len(str)):
    if str[windowEnd] not in tempDict.keys():
        tempDict[str[windowEnd]] = 1
    else:
        tempDict[str[windowEnd]] += 1
    if len(tempDict.keys()) > k:
        if (windowEnd - windowStart) > maxLength:
            maxLength = windowEnd - windowStart
            maxStart = windowStart
            maxEnd = windowEnd
        if tempDict[str[windowStart]] >= 1:
            tempDict[str[windowStart]] -= 1
        else:
            del(tempDict[windowStart])
        windowStart += 1
  return str[maxStart:maxEnd]

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
