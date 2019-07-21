from heapq import *

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    resulthead, resulttail = None, None
    minheap = []
    for l in lists:
        if l is not None:
            heappush(minheap, l)

    while minheap:
        minnode = heappop(minheap)
        if resulthead is None:
            resulthead = resulttail = minnode
        else:
            resulttail.next = minnode
            resulttail = resulttail.next
        if minnode.next is not None:
            heappush(minheap, minnode.next)

    return resulthead

def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next

main()