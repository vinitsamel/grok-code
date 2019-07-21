class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    retVal = False
    slowPointer = head
    fastPointer = head
    while (fastPointer and fastPointer.next) != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        #print (slowPointer.value, fastPointer.value)
        if (slowPointer == fastPointer):
            retVal = True
            break
    return retVal

def getCycleLength(head):
    cycleLength = 0
    slowPointer = head
    fastPointer = head
    slowPointerIndex = 0
    fastPointerIndex = 0
    while (fastPointer and fastPointer.next) != None:
        slowPointer = slowPointer.next
        slowPointerIndex += 1
        fastPointer = fastPointer.next.next
        fastPointerIndex += 2
        if (slowPointer == fastPointer):
            cycleLength = fastPointerIndex - slowPointerIndex
            break
    return cycleLength

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList has cycle Length: " + str(getCycleLength(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList has cycle Length: " + str(getCycleLength(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList has cycle Length: " + str(getCycleLength(head)))

main()
