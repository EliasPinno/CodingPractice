# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    length = 0
    current = linkedList
    while current != None:
        length += 1
        current = current.next
    middleNumber = length // 2 + 1
    current = linkedList
    for i in range(middleNumber-1):
        current = current.next
    return current

# O(n) time, O(1) space. Consider doing slow and fast approach?