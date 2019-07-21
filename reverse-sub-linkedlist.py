class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_sub_list(head, startPos, endPos):
    previous, current = None, head
    subEndPrevious, subEndCurrent = None, None
    curPos = 1
    while curPos <= endPos and current is not None:
        #print (curPos)
        if curPos <= startPos:
            subEndPrevious = previous
            subEndCurrent = current
            previous = current
            current = current.next
        else:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        curPos += 1
        #current.print_list()
    subEndPrevious.next = previous
    subEndCurrent.next = current
    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()