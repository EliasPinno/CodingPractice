# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    solution = []
    findKthLargestValueRecursive(tree, k, solutionContainer = solution)
    return solution[0]

def findKthLargestValueRecursive(node, k, nodesAboveRight = 0, solutionContainer = []):
    if node == None:
        return 0
    nodesBelowRight = findKthLargestValueRecursive(node.right,k,nodesAboveRight,solutionContainer)
    if len(solutionContainer) > 0:
        return 0
    location = nodesBelowRight + nodesAboveRight + 1
    if location == k:
        solutionContainer.append(node.value)
        return 0
    leftTreeResult = findKthLargestValueRecursive(node.left,k,location,solutionContainer)
    return nodesBelowRight + leftTreeResult + 1

# O(n) time, O(d) space where d is max depth of tree
# Solution uses no global pointers or values (that would make things easy)
    
