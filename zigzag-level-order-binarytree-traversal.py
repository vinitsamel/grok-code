import queue

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    q = queue.Queue()
    result = []
    q.put(root)
    direction = 1
    while q.qsize() > 0:
        current = []
        if direction == 1:
            direction = 0
        else:
            direction == 0
            direction = 1
        for _ in range(q.qsize()):
            tNode = q.get()
            if tNode.left is not None:
                q.put(tNode.left)
            if tNode.right is not None:
                q.put(tNode.right)
            if direction == 0:
                current.append(tNode.val)
            else:
                current.insert(0, tNode.val)
            #print (current)
        result.append(current)
    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()