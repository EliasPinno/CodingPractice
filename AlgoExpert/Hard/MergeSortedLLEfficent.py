# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time, O(1) space
def mergeLinkedLists(headOne, headTwo):
    currentOne = headOne
    currentTwo = headTwo
    masterPointer = headOne
    if headOne.value > headTwo.value:
        masterPointer = headTwo
        currentTwo = currentTwo.next
    else:
        currentOne = currentOne.next
    solution = masterPointer
    while currentOne != None and currentTwo != None:
        if currentOne.value > currentTwo.value:
            masterPointer.next = currentTwo
            currentTwo = currentTwo.next
        else:
            masterPointer.next = currentOne
            currentOne = currentOne.next
        masterPointer = masterPointer.next
    if currentOne == None:
        masterPointer.next = currentTwo
    else:
        masterPointer.next = currentOne
    return solution
