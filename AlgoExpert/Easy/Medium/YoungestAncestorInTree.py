# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    oneRoute = getRouteToTop(descendantOne)
    twoRoute = getRouteToTop(descendantTwo)
    onePointer = len(oneRoute)-2
    twoPointer = len(twoRoute)-2
    yca = topAncestor
    while onePointer >= 0 and twoPointer >= 0:
        if oneRoute[onePointer] != twoRoute[twoPointer]:
            break
        yca = oneRoute[onePointer]
        onePointer -= 1
        twoPointer -= 1
    return yca

def getRouteToTop(node):
    solution = []
    current = node
    while current != None:
        solution.append(current)
        current = current.ancestor
    return solution
# O(n) time, O(n) space where in is the number of total nodes in the tree