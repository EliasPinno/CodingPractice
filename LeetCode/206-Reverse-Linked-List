# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        stack = deque()
        current = head
        while current != None:
            stack.append(current)
            current=current.next
        newHead = stack.pop()
        current = newHead
        while len(stack) != 0:
            current.next = stack.pop()
            current = current.next
        current.next = None
        return newHead

# Space: O(n). Time: O(n)