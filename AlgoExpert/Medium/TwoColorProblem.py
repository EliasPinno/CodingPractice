from collections import deque
UNCOLORED = 0
RED = 1
BLUE = 2

def twoColorable(edges):
    n = len(edges)
    colors = [UNCOLORED]*n
    for i in range(n):
        if colors[i] == UNCOLORED: # unexplored node
            if not bfs(i,edges,colors):
                return False
    return True

def bfs(startNode, adjList, colors):
    queue = deque()
    queue.append(startNode)
    while len(queue) > 0:
        currentNode = queue.popleft()
        for neighbor in adjList[currentNode]:
            if colors[neighbor] != UNCOLORED:
                # check if the color is valid
                isLegal = isColorValid(colors[neighbor], colors[currentNode])
                if not isLegal:
                    return False
                colors[currentNode] = getOppositeColor(colors[neighbor])
            else:
                queue.append(neighbor)
        if colors[currentNode] == UNCOLORED:
            colors[currentNode] = BLUE
    return True

def getOppositeColor(color):
    if color == BLUE:
        return RED
    if color == RED:
        return BLUE

def isColorValid(color1, color2):
    if color1 == color2 and color1 != UNCOLORED:
        return False
    return True
# O(n+m) time, O(n) space where n is number of nodes, m is number of edges