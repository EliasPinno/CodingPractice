def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    memory = [[-1 for _ in range(height)] for _ in range(width)]
    memory[0][0] = 1
    return recursiveSolve(width, height, memory)

def recursiveSolve(width, height, memory):
    if width == 1 or height == 1:
        return 1 # Single Line
    if memory[width-1][height-1] != -1:
        return memory[width-1][height-1]
    memory[width-1][height-1] = recursiveSolve(width, height-1, memory) + recursiveSolve(width-1, height, memory)
    return memory[width-1][height-1]
# O((w*h)) time, O(w*h) space