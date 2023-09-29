def invertBinaryTree(tree):
    if tree == None:
        return None
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# O(n) time
# O(d) space