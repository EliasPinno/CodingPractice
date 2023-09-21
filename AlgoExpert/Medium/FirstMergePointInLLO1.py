# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Get relative depths of paths
    oneDepth = getDepthOfChild(descendantOne)
    twoDepth = getDepthOfChild(descendantTwo)
    # Align the lists so that their depths are the same by moving larger up
    # This by definition cannot miss the yca
    while oneDepth > twoDepth:
        descendantOne = descendantOne.ancestor
        oneDepth -=1
    while oneDepth < twoDepth:
        descendantTwo = descendantTwo.ancestor
        twoDepth -=1
    # Depths are aligned: step up one at a time, until you collide
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    
    return descendantOne

def getDepthOfChild(node):
    current = node
    depth = 1
    while current != None:
        depth += 1
        current = current.ancestor
    return depth
# O(n) time, O(1) space
