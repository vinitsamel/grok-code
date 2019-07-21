class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path(root, sum):
        if root is None:
            return False

        if root.left == None and root.right == None and root.value == sum:
            return True
        else:
            return has_path(root.left, sum - root.value) or has_path(root.right, sum - root.value)


def main():
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        print("Tree has path: " + str(has_path(root, 23)))
        print("Tree has path: " + str(has_path(root, 16)))

main()