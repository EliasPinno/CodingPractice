# This is an input class. Do not edit.
from collections import deque

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Recursive solution. O(n) space (may have entire tree on call stack)
# O(n) time (need to test every node)
def symmetricalTree(tree):
    if tree == None:
        return True
    return symmetricalTreeRecursive(tree.left, tree.right)
    

def symmetricalTreeRecursive(leftNode,rightNode):
    # if only one of the nodes is None, return False
    if (leftNode == None) ^ (rightNode == None):
        return False
    if leftNode == rightNode: # They should both be None
        return True
    if leftNode.value == rightNode.value:
        return symmetricalTreeRecursive(leftNode.left, rightNode.right) and symmetricalTreeRecursive(leftNode.right, rightNode.left)
    return False
