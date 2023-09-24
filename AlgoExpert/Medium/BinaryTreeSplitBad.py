from collections import deque
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(nd) time, O(d) space solution
def splitBinaryTree(tree):
    sumOfEntireTree = sumOfSubtree(tree)
    if sumOfEntireTree % 2 != 0:
        return 0
    if findSum(tree, sumOfEntireTree/2):
        return sumOfEntireTree/2
    return 0

def findSum(node, sum):
    if node == None:
        return False
    if sumOfSubtree(node) == sum:
        return True
    return findSum(node.left,sum) or findSum(node.right,sum)

def sumOfSubtree(node):
    if node == None:
        return 0
    return node.value + sumOfSubtree(node.left) + sumOfSubtree(node.right)
    