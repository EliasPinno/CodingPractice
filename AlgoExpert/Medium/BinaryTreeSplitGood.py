# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time (two passes over entire tree), O(d) space (recursion to max depth)
def splitBinaryTree(tree):
    sumOfEntireTree = sumOfSubtree(tree)
    if sumOfEntireTree % 2 != 0:
        return 0
    sum, foundTarget = solution(tree, sumOfEntireTree/2)
    if foundTarget:
        return sumOfEntireTree/2
    return 0

def solution(node, target):
    if node == None:
        return (0, False)
    leftResult, foundLeft = solution(node.left, target)
    rightResult, foundRight = solution(node.right, target)
    sumAtSpot = leftResult + rightResult + node.value
    if sumAtSpot == target:
        return (sumAtSpot, True)
    return (sumAtSpot, foundLeft or foundRight)
    
def sumOfSubtree(node):
    if node == None:
        return 0
    return node.value + sumOfSubtree(node.left) + sumOfSubtree(node.right)
    