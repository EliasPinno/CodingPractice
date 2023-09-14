def binarySearch(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        targetIdx = (left + ((right-left)//2))
        value = array[targetIdx]
        if value == target:
            return targetIdx
        elif value > target:
            right = targetIdx-1
        else:
            left = targetIdx+1
    return -1

# O(logn) time, O(1) space