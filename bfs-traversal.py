import queue

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    q = queue.Queue()
    result = []
    q.put(root)
    while q.qsize() > 0:
        qlen = q.qsize()
        currentlevel = []
        for i in range(qlen):
            node = q.get()
            currentlevel.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        result.append(list(currentlevel))
    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
