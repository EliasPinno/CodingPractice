
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    arrayOnePointer = 0
    arrayTwoPointer = 0
    solution = [arrayOne[0], arrayTwo[0]]
    closestDifference = abs(solution[0] - solution[1])
    while arrayOnePointer < len(arrayOne) and arrayTwoPointer < len(arrayTwo):
        currentValueOne = arrayOne[arrayOnePointer]
        currentValueTwo = arrayTwo[arrayTwoPointer]
        currentDiff = abs(currentValueOne - currentValueTwo)
        if currentDiff < closestDifference:
            closestDifference = currentDiff
            solution = [currentValueOne, currentValueTwo]
        if currentValueOne < currentValueTwo:
            arrayOnePointer += 1
        else:
            arrayTwoPointer += 1
    return solution
# O(1) space
# O(nlogn + mlogm) time? 