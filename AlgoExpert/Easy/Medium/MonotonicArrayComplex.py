def isMonotonic(array):
    # Length 2 is by definition monotonic
    if len(array) <= 2:
        return True
    if array[0] == array[len(array)-1]: 
        # To be monotonic, all elems must be the same
        for i in range(1, len(array)):
            if array[i] != array[i-1]:
                return False
        return True
    elif array[0] < array[len(array)-1]:
        # To be monotonic, all elems must be larger or equal to last
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                return False
        return True
    else:
        for i in range(1, len(array)):
            if array[i] > array[i-1]:
                return False
        return True
    pass
# O(n) time complexity, O(1) space