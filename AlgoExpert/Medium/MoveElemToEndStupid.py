def moveElementToEnd(array, toMove):
    if len(array) == 0 or len(array) == 1:
        return array
    safeSwap = findNextNonTarget(len(array) - 1, array, toMove)
    idx = 0
    while idx < safeSwap:
        if array[idx] == toMove:
            swap(idx,safeSwap,array)
            safeSwap = findNextNonTarget(safeSwap, array, toMove)
        idx += 1
    return array

def swap(a,b,array):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def findNextNonTarget(idx, array, target):
    while array[idx] == target and idx >= 0:
        idx -= 1
    return idx

# O(n) time, O(1) space