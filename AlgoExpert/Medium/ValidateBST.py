import sys

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateNode(tree)

def validateNode(node, lowerBound = -sys.maxsize, upperBound = sys.maxsize):
    if node == None:
        return True
    elif node.value < lowerBound or node.value >= upperBound:
        return False
    else:
        return validateNode(node.left, lowerBound, node.value) and validateNode(node.right, node.value, upperBound)
# O(n) time (must check every node), O(d) space where d is the depth of the tree