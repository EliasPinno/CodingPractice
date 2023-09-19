def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNonIncreasing = False
        if array[i] < array[i-1]:
            isNonDecreasing = False
    
    return isNonIncreasing or isNonDecreasing
# O(n) time, O(1) space.
# This solution is much less dumb.