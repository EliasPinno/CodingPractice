# Iterative approach going from the left and right
# O(n) time, O(1) space
def threeNumberSort(array, order):
    leftVal = order[0]
    rightVal = order[2]
    leftPointer = 0
    rightPointer = len(array)-1
    # Put all the leftVal on left side
    while leftPointer < rightPointer:
        while leftPointer < len(array) and array[leftPointer] == leftVal:
            leftPointer += 1
        while rightPointer > -1 and array[rightPointer] != leftVal:
            rightPointer -= 1
        # leftPointer targets a non leftVal, rightPointer targets a leftVal
        if leftPointer < rightPointer:
            array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
    print(leftPointer)
    # Don't re assign left pointer: everything to it's left is already
    # left val
    rightPointer = len(array)-1
    # Put all rightVal elements on right side
    while leftPointer < rightPointer:
        while rightPointer > -1 and array[rightPointer] == rightVal:
            rightPointer -= 1
        while leftPointer < len(array) and array[leftPointer] != rightVal:
            leftPointer += 1
        # leftPointer targets a rightVal, rightPointer targets a non rightVal
        if leftPointer < rightPointer:
            array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
    return array
