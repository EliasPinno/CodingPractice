def findClosestValueInBst(tree, target):
    return findClosestValueInBstRecursive(tree, target)
    

def findClosestValueInBstRecursive(tree, target):
    if tree == None:
        return None
    elif tree.value == target:
        return tree.value
    elif tree.value > target:
        print("went left at ")
        print(tree.value)
        leftTreeResult = findClosestValueInBstRecursive(tree.left, target)
        if leftTreeResult != None:
            if abs(target-tree.value) < abs(target-leftTreeResult):
                return tree.value
            else:
                return leftTreeResult
        else: 
            return tree.value
    else:
        rightTreeResult = findClosestValueInBstRecursive(tree.right, target)
        if rightTreeResult != None:
            if abs(target-tree.value) < abs(target-rightTreeResult):
                return tree.value
            else:
                return rightTreeResult
        else: 
            return tree.value
            

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
