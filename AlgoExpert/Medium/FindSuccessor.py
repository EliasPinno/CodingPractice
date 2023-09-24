# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(h) time where h is the height of the tree
# O(1) space (no recursion!)

def findSuccessor(tree, node):
    if node.right != None:
        return getLeftMostRightChild(node)
    return getFirstParentToRight(node)
    
def getFirstParentToRight(node):
    if node == None:
        return None
    current = node
    parent = current.parent
    while parent != None and parent.right == current:
        current = parent
        parent = current.parent
    return parent
    
def getLeftMostRightChild(node):
    if node == None:
        return None
    if node.right == None:
        return node
    current = node.right
    while current.left != None:
        current = current.left
    return current
    