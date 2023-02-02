# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        items = deque()
        self.traverse(root,items)
        number = -1
        for i in range(k):
            number = items.popleft()
            print(number)
        return number.val

    def traverse(self, node: Optional[TreeNode], items: deque):
        if node != None:
            self.traverse(node.left,items)
            items.append(node)
            self.traverse(node.right,items)
