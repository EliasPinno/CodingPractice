def sortStack(stack):
    if len(stack) == 0:
        return stack
    recursiveSortStack(stack)
    return stack

def removeLargestValueInStack(stack):
    if len(stack) == 1:
        return stack.pop()
    value = stack.pop()
    largestBelow = removeLargestValueInStack(stack)
    if largestBelow > value:
        stack.append(value)
        return largestBelow
    else:
        stack.append(largestBelow)
        return value

def recursiveSortStack(stack):
    largestValue = removeLargestValueInStack(stack)
    if len(stack) == 0:
        stack.append(largestValue)
    else:
        recursiveSortStack(stack)
        stack.append(largestValue)
        
# O(n^2) time, O(n) space