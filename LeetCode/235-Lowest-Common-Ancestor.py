# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pQueue = deque()
        qQueue = deque()
        self.buildQueueRecursive(root,pQueue,p.val)
        self.buildQueueRecursive(root,qQueue,q.val)
        pQueue.popleft()
        qQueue.popleft()
        lca = root
        while len(pQueue) != 0 and len(qQueue) != 0:
            pNode = pQueue.popleft()
            qNode = qQueue.popleft()
            if(pNode != qNode):
                break
            lca = pNode
        return lca

    def buildQueueRecursive(self, node: TreeNode, queue: deque, searchVal: int):
        if node == None:
            return
        queue.append(node)
        if node.val == searchVal:
            return None
        if searchVal < node.val:
            self.buildQueueRecursive(node.left,queue,searchVal)
        else:
            self.buildQueueRecursive(node.right,queue,searchVal)
            
# Time: O(n) Space: O(n)