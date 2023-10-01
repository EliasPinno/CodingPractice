def searchInSortedMatrix(matrix, target):
    length = len(matrix)
    width = len(matrix[0])
    row = 0
    col = width -1
    while row < length and col >= 0:
        elem = matrix[row][col]
        if elem == target:
            return [row,col]
        # The target cannot be in the vertical line below this
        if elem > target: 
            col -= 1
        else:
            row += 1
    return [-1,-1]
# O(n+m) time, O(1) space