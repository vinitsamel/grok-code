class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getAllPaths(root):
    allpaths = []
    allPathsRecursive(root, [], allpaths)
    return allpaths

def allPathsRecursive(tNode, currentpath, allpaths):
    #print (tNode.value)
    if tNode is None:
        return
    #print (currentpath)
    currentpath.append(tNode.value)

    if tNode.left is None and tNode.right is None:
        allpaths.append(list(currentpath))
    else:
        allPathsRecursive(tNode.left, currentpath, allpaths)
        allPathsRecursive(tNode.right, currentpath, allpaths)
    del currentpath[-1]
    #print (currentpath)

def sumAllPaths(allpaths):
    sum = 0
    for path in allpaths:
        pathNum = 0
        for num in path:
            pathNum = (pathNum * 10) + num
        sum += pathNum
    return sum

def main():
    root = TreeNode(15)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(13)
    allpaths = getAllPaths(root)
    print (allpaths)
    print (sumAllPaths(allpaths))

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    allpaths = getAllPaths(root)
    print (allpaths)
    print (sumAllPaths(allpaths))

main()

