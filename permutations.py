import queue

def find_permutations(nums):
    q = queue.Queue()
    q.put(nums)
    result = []
    resultLookup = {}
    resultLookup[stringifyList(nums)] = 1
    result.append(nums)
    while q.qsize() > 0:
        listFromQueue = q.get()
        #print (listFromQueue)
        for i in range(len(listFromQueue)):
            for j in range(i+1, len(listFromQueue)):
                #print (resultLookup)
                newList = list(listFromQueue)
                newList[i], newList[j] = newList[j], newList[i]
                if stringifyList(newList) not in resultLookup.keys():
                    #print (stringifyList(newList))
                    resultLookup[stringifyList(newList)] = 1
                    q.put(newList)
                    result.append(newList)
    print (len(result))
    return result

def stringifyList(arr):
    return ','.join(str(x) for x in arr)


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5, 4, 6])))


main()