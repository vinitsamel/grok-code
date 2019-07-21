class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_path(root, sequence):
    return findPathRecursive(root, sequence, [])

def findPathRecursive(root, sequence, currentPath):
    if root is not None:
        currentPath.append(root.value)
        #print (currentPath)
    else:
        return False

    if root.left is None and root.right is None:
        if currentPath == sequence:
            print (currentPath)
            print ("Match")
            return True
    else:
        retVal = findPathRecursive(root.left, sequence, currentPath)
        if retVal:
            return True

        retVal = findPathRecursive(root.right, sequence, currentPath)
        if retVal:
            return True

    print(currentPath)
    del currentPath[-1]

    if len(currentPath) == 0:
        return False


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()