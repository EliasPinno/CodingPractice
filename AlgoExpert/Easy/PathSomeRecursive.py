# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    solution = []
    pathSumRecursive(root, 0, solution)
    return solution    

def pathSumRecursive(node, pathSum, solution):
    if node == None:
        return None
    if node.left == None and node.right == None:
        solution.append(node.value + pathSum)
    else: # Internal node of some kind
        pathSumRecursive(node.left, node.value + pathSum, solution)
        pathSumRecursive(node.right, node.value + pathSum, solution)