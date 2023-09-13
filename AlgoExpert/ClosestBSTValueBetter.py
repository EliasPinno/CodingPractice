def findClosestValueInBst(tree, target):
    current = tree
    currentClosestVal = current.value
    while current != None:
        if abs(target-current.value) < abs(target-currentClosestVal):
            currentClosestVal = current.value
        if current.value > target:
            current = current.left
        else:
            current = current.right
    return currentClosestVal


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(log(n)) time, O(1) space