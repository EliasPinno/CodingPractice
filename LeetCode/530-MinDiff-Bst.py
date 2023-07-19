# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
      myList = []
      self.getInOrderTraversal(root, myList)
      minDiff = 10**7
      for i in range(1, len(myList)):
        minDiff = min(minDiff, myList[i]-myList[i-1])
      return minDiff

    def getInOrderTraversal(self, current: Optional[TreeNode], currentList: List[TreeNode]):
      if current is None: 
        return
      self.getInOrderTraversal(current.left, currentList)
      currentList.append(current.val)
      self.getInOrderTraversal(current.right, currentList)
