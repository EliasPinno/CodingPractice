# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    inOrder = inOrderTraversal(tree)        
    return inOrder[len(inOrder)-k]
    
def inOrderTraversal(tree, solution=[]):
    if tree != None:
        inOrderTraversal(tree.left,solution)
        solution.append(tree.value)
        inOrderTraversal(tree.right,solution)
        return solution
# O(n) time, O(n) space