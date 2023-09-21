from collections import deque

def balancedBrackets(string):
    stack = deque()
    bracketSet = {'(':')','[':']', '{':'}'}
    for c in string:
        if c in bracketSet.keys():
            stack.append(c)
        elif c in bracketSet.values():
            if len(stack) == 0:
                return False
            mostRecentBracket = stack.pop()
            if bracketSet[mostRecentBracket] != c:
                return False
    return len(stack) == 0
# O(n) time, O(n) space