# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# a -> b -> c -> d ->
# <- a

def reverseLinkedList(head):
    # Handle annoying edge cases
    if head == None:
        return None
    if head.next == None:
        return head
    # Create our initial pointers
    prev = head
    current = head.next
    next = head.next.next
    # reassign your head to a tail
    prev.next = None
    while next != None:
        current.next = prev
        prev = current
        current = next
        next = next.next
    # Create the new head
    current.next = prev
    return current
# O(n) time, O(1) space