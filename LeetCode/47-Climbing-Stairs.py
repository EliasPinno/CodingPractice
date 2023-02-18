class Solution:
    def __init__(self):
        self.solutionDict = {1:1, 2:2}

    def climbStairs(self, n: int) -> int:
        if n in self.solutionDict:
            return self.solutionDict[n]
        else:
            self.solutionDict[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.solutionDict[n]
    
# Time: O(n). Space: O(n)