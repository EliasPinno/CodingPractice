def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    return recursiveSolve(width, height)

def recursiveSolve(width, height):
    if width == 1 or height == 1:
        return 1 # Single Line
    return recursiveSolve(width, height-1) + recursiveSolve(width-1, height)
# O(2^(w*h)) time, O(w+h) space