def nodeDepths(root):
    return nodeDepthsRecursive(root, 0)
    
def nodeDepthsRecursive(node, currentDepth):
    if node == None:
        return 0
    return currentDepth + nodeDepthsRecursive(node.left, currentDepth+1) + nodeDepthsRecursive(node.right, currentDepth+1)

    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
