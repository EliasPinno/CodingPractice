ISLAND = 1
STAY_ISLAND = 2
NONE = 0

def removeIslands(matrix):
    # Top row
    for i in range(len(matrix[0])):
        traverseIsland(matrix,0,i,ISLAND,STAY_ISLAND)
    # Left column
    for i in range(len(matrix)):
        traverseIsland(matrix,i,0,ISLAND,STAY_ISLAND)
    # BottomRow
    for i in range(len(matrix[len(matrix)-1])):
        traverseIsland(matrix,len(matrix)-1,i,ISLAND,STAY_ISLAND)
    # Right column
    for i in range(len(matrix)):
        traverseIsland(matrix,i,len(matrix[i])-1,ISLAND,STAY_ISLAND)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ISLAND:
                matrix[i][j] = NONE
            elif matrix[i][j] == STAY_ISLAND:
                matrix[i][j] = ISLAND
    return matrix

def traverseIsland(matrix, row, col, toChange, changed):
    if matrix[row][col] != ISLAND:
        return 0
    matrix[row][col] = STAY_ISLAND
    for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
        if canAccessSpot(matrix,row+i,col+j):
            traverseIsland(matrix,row+i,col+j, toChange, changed)
    
def canAccessSpot(matrix, row, col):
    return row < len(matrix) and row >= 0 and col < len(matrix[row]) and col >= 0
# O(n*m) time, O(1) space