NON_LAND = 1

def largestIsland(matrix):
    maxIsland = 0
    seenChar = 2
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == NON_LAND:
                maxIsland = max(maxIsland,sumDFSAroundSquare(matrix,row,col,seenChar))
                seenChar += 1
    return maxIsland

def isTraverseable(matrix, row, col, seenChar):
    if row < len(matrix) and row >= 0 and col < len(matrix[row]) and col >= 0:
        return matrix[row][col] != seenChar and matrix[row][col] != NON_LAND

def sumDFSAroundSquare(matrix,row,col,seenChar):
    sum = 1
    for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
        sum += returnDfsCount(matrix, row+i, col+j, seenChar)
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
# O(n*m space), O((n*m)(n*m)) time