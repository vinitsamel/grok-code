class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths(root, sum):
    allPaths = []
    findAllPathsRecursive(root, sum, [], allPaths)
    return allPaths


def findAllPathsRecursive(tNode, sum, currentPath, allPaths):
    print (1, currentPath)
    if tNode is None:
        return
    currentPath.append(tNode.val)
    if tNode.val == sum and tNode.left is None and tNode.right is None:
        allPaths.append(list(currentPath))
    else:
        findAllPathsRecursive(tNode.left, sum - tNode.val, currentPath, allPaths)
        findAllPathsRecursive(tNode.right, sum - tNode.val, currentPath, allPaths)
    print (2, currentPath)
    del currentPath[-1]
    print(3, currentPath)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()