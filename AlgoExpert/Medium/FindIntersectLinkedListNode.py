# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(headOne, headTwo):
    length1 = getLinkedListLength(headOne)
    length2 = getLinkedListLength(headTwo)
    currentOne = headOne
    currentTwo = headTwo
    if length1 > length2:
        currentOne = movePointerNForward(currentOne, length1-length2)
    else:
        currentTwo = movePointerNForward(currentTwo, length2-length1)
    while currentOne != None:
        if currentOne == currentTwo:
            return currentOne
        currentOne = currentOne.next
        currentTwo = currentTwo.next
    return None

def getLinkedListLength(head):
    current = head
    length = 1
    while current.next != None:
        current = current.next
        length += 1
    return length
    
def movePointerNForward(node,n):
    while n > 0:
        node = node.next
        n -= 1
    return node
# O(n+m) time, O(1) space