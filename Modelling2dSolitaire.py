white = 'W'
black = 'B'
empty = 0
openingBoard = ['W','W','W','W','W',0,'B','B','B','B','B']
solutionBoard = ['B','B','B','B','B',0,'W','W','W','W','W']
checkedBoards = {}

def generateValidMoves(board) -> list:
    emptySpot = 0
    for i in range(len(board)):
        if(board[i] == empty):
            emptySpot = i
            break
    moves = []
    offsets = [-2,-1,1,2]
    for offset in offsets:
        if emptySpot+offset >= 0 and emptySpot+offset < len(board):
            if(board[emptySpot+offset] == white and offset < 0) or (board[emptySpot+offset] == black and offset > 0):
                moves.append((emptySpot + offset, emptySpot))
    return moves

def boardIsSolution(board) -> bool: 
    for i in range(len(board)):
        if board[i] != solutionBoard[i]:
            return False
    return True

def makeMove(move, board):
    (src,dst) = move
    srcVal = board[src]
    board[src] = board[dst]
    board[dst] = srcVal
    return board

def solution(board):
    possibleOpeningMoves = generateValidMoves(board)
    for move in possibleOpeningMoves:
        result = solutionRecursive(board,[move])
        if result != None:
            return result
    return None

def solutionRecursive(boardOrg, moveSequence):
    board = boardOrg[:] # Clone the entire board
    makeMove(moveSequence[-1], board)
    if boardIsSolution(board):
        return moveSequence
    moves = generateValidMoves(board)
    if len(moves) == 0:
        return None
    for move in moves:
        moveSequenceClone = moveSequence[:]
        moveSequenceClone.append(move)
        result = solutionRecursive(board, moveSequenceClone)
        if result != None:
            return result
    return None

def visualizeMoveSequence(boardOrg, moveSequence):
    board = boardOrg[:]
    print("Total moves in solution: " + str(len(moveSequence)))
    print("Original board: ")
    print(board)
    for move in moveSequence:
        (src,dst) = move
        print(f'Move {src} to {dst}.')
        makeMove(move,board)
        print(board)
    

visualizeMoveSequence(openingBoard, solution(openingBoard))