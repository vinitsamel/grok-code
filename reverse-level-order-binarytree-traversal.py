import queue

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse(root):
    result = []
    if root is None:
        return result
    #print (root.value)
    q = queue.Queue()
    q.put(root)

    while q.qsize() > 0:
        #print (q.qsize())
        currentLevel = []
        levelCount = q.qsize()
        for _ in range(levelCount):
            tNode = q.get()
            if tNode is not None:
                if tNode.left is not None:
                    q.put(tNode.left)
                if tNode.right is not None:
                    q.put(tNode.right)
            currentLevel.append(tNode.value)
            #print (currentLevel)
        result.insert(0, currentLevel)

    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))

main()

