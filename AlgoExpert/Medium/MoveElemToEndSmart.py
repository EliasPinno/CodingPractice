def moveElementToEnd(array, toMove):
    idx = 0
    swapTarget = len(array) - 1
    while idx < swapTarget:
        # Need first condition to prevent an accidental backwards swap
        while idx < swapTarget and array[swapTarget] == toMove:
            swapTarget -= 1
        if array[idx] == toMove:
            print(idx)
            array[idx] = array[swapTarget]
            array[swapTarget] = toMove
        idx += 1
    return array
# O(n) time, O(1) space