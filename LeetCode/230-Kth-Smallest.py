# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = deque()
        self.traverse(root, k, nodes)
        return nodes.pop().val

    def traverse(self, node: Optional[TreeNode], k: int, nodes: deque) -> None:
        if node != None:
            self.traverse(node.left,k,nodes)
            if len(nodes) < k:
                nodes.append(node)
                self.traverse(node.right,k,nodes)
# O(k) space, time