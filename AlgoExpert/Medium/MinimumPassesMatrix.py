from collections import deque

def minimumPassesOfMatrix(matrix):
    # Write your code here.
    queue = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                queue.append((i,j,0))
    maxPass = 0
    while len(queue) > 0:
        row, col, currentPass = queue.popleft()
        maxPass = max(currentPass, maxPass)
        for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
            if canAccessSpot(matrix,row+i,col+j):
                if matrix[row+i][col+j] < 0:
                    matrix[row+i][col+j] = matrix[row+i][col+j]*(-1)
                    queue.append((row+i,col+j,maxPass+1))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                return -1
    return maxPass
    
def canAccessSpot(matrix, row, col):
    return row < len(matrix) and row >= 0 and col < len(matrix[row]) and col >= 0
# O(l*w) time, O(l*w) space