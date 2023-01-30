# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Handle cases where one or both lists are empty
        if list1 == None and list2 == None:
            return None
        elif list1 == None: 
            return list2
        elif list2 == None: 
            return list1
        # Get our inital node
        newListHead = ListNode()
        current = newListHead
        while list1 != None or list2 != None:
            current.next = self.minNodeOfLists(list1,list2)
            if current.next == list1:
                list1 = list1.next
            else:
                list2 = list2.next
            current = current.next
        return newListHead.next
    
    def minNodeOfLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        temp_max = min([list1,list2], key=attrgetter('val'))
        return temp_max

# Time: O(n). Space: O(1) (no extra space required other then a few constant vars)