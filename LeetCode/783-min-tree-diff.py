# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 100000000000000
        if root.left == None and root.right == None:
            return 100000000000000
        leftMax = self.getMax(root.left)
        rightMin = self.getMin(root.right)
        rootval = root.val
        """
        print(f"At root {rootval}")
        print(rightMin)
        print(leftMax)
        print(self.minDiffInBST(root.left))
        print(self.minDiffInBST(root.right))
        """
        
        return min((rightMin-rootval), (rootval-leftMax), self.minDiffInBST(root.left), self.minDiffInBST(root.right))

    def getMax(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return -100000000000000
        return max(root.val, self.getMax(root.right))

    def getMin(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 100000000000000
        return min(root.val, self.getMin(root.left))