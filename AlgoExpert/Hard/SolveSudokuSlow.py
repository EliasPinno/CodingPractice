MAX_DEPTH = 0

def solveSudoku(board):
    # Create sets for the board
    rowSets = [set() for _ in range(9)]
    colSets = [set() for _ in range(9)]
    squareSets = [[set() for _ in range(3)] for _ in range(3)]
    # Populate sets
    for row in range(9):
        for col in range(9):
            value = board[row][col] 
            if value != 0: # Add it to the sets
                rowBox = (row) // 3 
                colBox = (col) // 3
                rowSets[row].add(value)
                colSets[col].add(value)
                squareSets[rowBox][colBox].add(value)
    solveSudokuHelper(board,rowSets,colSets,squareSets)
    return board

def solveSudokuHelper(board,rowSets,colSets,squareSets):
    numItrDone = 0
    for i in range(9): # So we don't check assigned values too much
        for j in range(9):
            numItrDone += 1
            if board[i][j] == 0: # it is a value we can assign
                rowSet = rowSets[i]
                colSet = colSets[j]
                rowBox = (i) // 3 
                colBox = (j) // 3
                squareSet = squareSets[rowBox][colBox]
                for val in range(1,10):
                    # If we can put the val at this spot
                    if val not in rowSet and val not in colSet and val not in squareSet:
                        rowSet.add(val)
                        colSet.add(val)
                        squareSet.add(val)
                        board[i][j] = val
                        if i == 8 and j == 8: # We placed all values!
                            return True
                        hasSolution = solveSudokuHelper(board,rowSets,colSets,squareSets)
                        if hasSolution: # Our current path leads to a solution
                            return hasSolution
                        # The current placement can't lead to a solution: undo
                        rowSet.remove(val)
                        colSet.remove(val)
                        squareSet.remove(val)     
                # If we couldn't find a way to fill a zero that has a solution
                # This path is dead. Reset this square
                board[i][j] = 0
                return False
    return True
    
def printBoard(board):
    for row in board:
        print(row)
    print()

# O(numZeroes^2), O(numZeroes) space