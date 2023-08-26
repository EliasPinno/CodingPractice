invalidTile = 'X'
ballTile = 'B'
emptyTile = '0'
startingBoard = [
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile],
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile],
    [ballTile,ballTile,ballTile,ballTile,ballTile,ballTile,ballTile],
    [ballTile,ballTile,ballTile,emptyTile,ballTile,ballTile,ballTile],
    [ballTile,ballTile,ballTile,ballTile,ballTile,ballTile,ballTile],
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile],
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile]]

def printBoard(board):
    for row in board:
        print(row)
    print()

def valueCopyBoard(board):
    newBoard = []
    for row in board:
        newBoard.append(row[:])
    return newBoard

