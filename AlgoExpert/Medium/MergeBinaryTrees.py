# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    if tree1 == None and tree2 == None:
        return None
    # get newNode to point at a nonNone node
    newNode = tree1
    if tree1 == None:
        return tree2
    # get correct value for currentNode
    newNode.value = returnValueOr0(tree1) + returnValueOr0(tree2)
    newNode.left = mergeBinaryTrees(returnLeftOrNone(tree1),returnLeftOrNone(tree2))
    newNode.right = mergeBinaryTrees(returnRightOrNone(tree1),returnRightOrNone(tree2))
    
    return newNode

def returnValueOr0(node):
    if node == None:
        return 0
    return node.value

def returnLeftOrNone(node):
    if node == None:
        return None
    return node.left

def returnRightOrNone(node):
    if node == None:
        return None
    return node.right
# O(n) time, O(d) space