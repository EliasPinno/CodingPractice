from collections import deque
import math

def reversePolishNotation(tokens):
    stack = deque()
    for token in tokens:
        if isOperator(token):
            b = int(stack.pop())
            a = int(stack.pop())
            currentNumber = doOperation(a,b,token)
            stack.append(currentNumber)
        else:
            stack.append(token)
    return int(stack.pop())

def isOperator(token):
    return token in {"+","-","*","/"}

def doOperation(a,b,operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return int(a / b)
# O(n) time, O(n) space