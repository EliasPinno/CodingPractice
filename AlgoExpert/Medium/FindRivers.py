FOUND_RIVER = 2
RIVER = 1
LAND = 0

def riverSizes(matrix):
    solution = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            answer = traverseRiver(matrix, i, j)
            if answer != 0:
                solution.append(answer)
    return solution

def traverseRiver(matrix, row, col):
    if matrix[row][col] != RIVER:
        return 0
    count = 1
    matrix[row][col] = FOUND_RIVER
    for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
        if canAccessSpot(matrix,row+i,col+j):
            count += traverseRiver(matrix,row+i,col+j)
    return count

def canAccessSpot(matrix, row, col):
    return row < len(matrix) and row >= 0 and col < len(matrix[row]) and col >= 0
