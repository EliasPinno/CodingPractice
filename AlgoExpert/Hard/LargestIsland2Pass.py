NON_LAND = 1
LAND = 0

def largestIsland(matrix):
    maxIsland = 0
    seenChar = 2
    islandSizes = {}
    # First pass: Label all the islands and their sizes
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == LAND:
                islandSize = returnDfsCount(matrix,row,col,seenChar)
                islandSizes[seenChar] = islandSize
                seenChar += 1
    # Second pass: check empty spots, see neighboring island sizes
    print(islandSizes)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == NON_LAND:
                maxIsland = max(maxIsland,sumDFSAroundSquare(matrix,row,col,islandSizes))
    return maxIsland

def isTraverseable(matrix, row, col, seenChar):
    if isAccessible(matrix,row,col):
        return matrix[row][col] != seenChar and matrix[row][col] != NON_LAND

def isAccessible(matrix, row, col):
    return row < len(matrix) and row >= 0 and col < len(matrix[row]) and col >= 0

def sumDFSAroundSquare(matrix,row,col,islandSizes):
    sum = 1
    islandSet = set()
    for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
        if isAccessible(matrix, row+i, col+j):
            if matrix[row+i][col+j] in islandSizes and matrix[row+i][col+j] not in islandSet:
                sum += islandSizes[matrix[row+i][col+j]]
                islandSet.add(matrix[row+i][col+j])
    return sum

def returnDfsCount(matrix,row,col,seenChar):
    if not isTraverseable(matrix, row, col, seenChar):
        return 0
    else:
        matrix[row][col] = seenChar
        count = 1
        for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
            count += returnDfsCount(matrix, row+i, col+j, seenChar)
        return count

# O(w*h) time and space