# Feel free to add new properties and methods to the class.
from collections import deque
class MinMaxStack:
    def __init__(self):
        self.stack = deque()
        self.minMax = deque()
    
    # O(1) time
    def peek(self):
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        value = self.stack.pop()
        if value == self.getMin():
            self.minMax.popleft()
        elif value == self.getMax():
            self.minMax.pop()
        return value

    # O(1) time
    def push(self, number):
        self.stack.append(number)
        if len(self.minMax) == 0 or number >= self.getMax():
            self.minMax.append(number)
        elif number <= self.getMin():
            self.minMax.appendleft(number)
            
        # Write your code here.
        pass
    
    # O(1) time
    def getMin(self):
        return self.minMax[0]

    # O(1) time
    def getMax(self):
        return self.minMax[-1]

# O(n) space