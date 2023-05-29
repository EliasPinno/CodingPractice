class Solution:
    def mySqrt(self, x: int) -> int:
        currentSolution = 1
        while True:
            if currentSolution*currentSolution > x:
                break
            currentSolution += 1
        return currentSolution-1
    
# Deadly simple solution: consider improving with a Binary search for a non boosted solution.