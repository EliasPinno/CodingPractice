# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n==1:
            return None
        else: 
            size = self.recursiveRemoveFromEnd(head,n,1)
            if size == n:
                head = head.next
            return head
    
    def recursiveRemoveFromEnd(self, node: Optional[ListNode], n: int, layer: int) -> int:
        if node.next == None: # at end Node
            return layer
        else:
            size = self.recursiveRemoveFromEnd(node.next, n, layer+1)
            if size - n == layer:
                node.next = node.next.next
            return size