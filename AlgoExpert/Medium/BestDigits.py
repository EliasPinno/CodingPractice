from collections import deque

def bestDigits(number, numDigits):
    stack = deque()
    stack.append(number[0])
    for i in range(1,len(number)):
        print(list(stack))
        #print(numDigits)
        digit = number[i]
        topDigit = stack[-1]
        while digit > topDigit and len(stack) > 0 and numDigits > 0:
            numDigits -= 1
            topDigit = stack.pop()
            if topDigit >= digit: # Check before we break the loop
                stack.append(topDigit)
                numDigits += 1
        stack.append(digit)
    for i in range(numDigits):
        stack.pop()
    # Write your code here.
    return "".join(list(stack))
# O(n) time, O(n) space