# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recursiveInvert(root)
        return root
        
    def recursiveInvert(self, node: TreeNode) -> TreeNode:
        if node == None:
            return None
        left =  node.left
        right = node.right
        node.left = self.recursiveInvert(right)
        node.right = self.recursiveInvert(left)
        return node

# Time: O(n). Space: O(n)