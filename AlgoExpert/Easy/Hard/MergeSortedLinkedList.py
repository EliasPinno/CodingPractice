# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    finalList = []
    currentOne = headOne
    currentTwo = headTwo
    while currentOne != None or currentTwo != None:
        if currentOne == None:
            finalList.append(currentTwo.value)
            currentTwo = currentTwo.next
        elif currentTwo == None:
            finalList.append(currentOne.value)
            currentOne = currentOne.next
        else:
            if currentOne.value < currentTwo.value:
                finalList.append(currentOne.value)
                currentOne = currentOne.next
            else:
                finalList.append(currentTwo.value)
                currentTwo = currentTwo.next
    currentOne = headOne
    currentTwo = headTwo
    masterPointer = None
    if headOne.value < headTwo.value:
        masterPointer = headOne
        currentOne = currentOne.next
    else:
        masterPointer = headTwo
        currentTwo = currentTwo.next
    
    for i in range(1,len(finalList)):
        if currentOne != None and currentOne.value == finalList[i]:
            linkNode(masterPointer, currentOne)
            currentOne = currentOne.next
        else:
            linkNode(masterPointer, currentTwo)
            currentTwo = currentTwo.next
        masterPointer = masterPointer.next
        
    if headOne.value >= headTwo.value:
        return headTwo
    return headOne
def linkNode(a,b):
    print("Linking {} and {}.".format(a.value,b.value))
    a.next = b

# O(n) time, O(n) space
