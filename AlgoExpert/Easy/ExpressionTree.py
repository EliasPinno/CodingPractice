# This is an input class. Do not edit.
ADDITION = -1
SUBTRACTION = -2
DIVISION = -3
MULTIPLICATION = -4

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value < 0:
        result =  operatorToResult(evaluateExpressionTree(tree.left), evaluateExpressionTree(tree.right), tree.value)
        print(result)
        return result
    return tree.value

def operatorToResult(a,b,operator):
    if operator == -1:
        return a+b
    if operator == -2:
        return a-b
    if operator == -3:
        return int(a/b) # a//b does NOT work for some reason
    if operator == -4:
        return a*b
# O(n) time, O(n) space