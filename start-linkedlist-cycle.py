class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next

def getLengthofCycle(head):
    cycleLength = 0
    slowPointer = head
    slowIndex = 0
    fastPointer = head
    fastIndex = 0
    while (fastPointer and fastPointer.next) != None:
        slowPointer = slowPointer.next
        slowIndex += 1
        fastPointer = fastPointer.next.next
        fastIndex += 2
        if slowPointer == fastPointer:
            cycleLength = fastIndex - slowIndex
            break
    return cycleLength


def getStartCycleNode(head):
    cycleLength = getLengthofCycle(head)
    slowPointer = head
    fastPointer = head
    if cycleLength > 0:
        for i in range(cycleLength):
            fastPointer = fastPointer.next
        while slowPointer != fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        return slowPointer
    else:
        return None

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(getStartCycleNode(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(getStartCycleNode(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(getStartCycleNode(head).value))

main()

#TC: O(N)
#SC: O(1)