# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    if linkedList.next == None:
        return linkedList
    current = linkedList
    next = current.next
    while next != None:
        if current.value == next.value:
            next = next.next
            current.next = next
        else:
            current = next
            next = next.next
    return linkedList
# O(n) time, O(1) space