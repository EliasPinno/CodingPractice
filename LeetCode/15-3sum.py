class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        solutionDict = {}
        for i in range(len(numsSorted)-2):
            left = i+1
            right = len(numsSorted)-1
            while left < right:
                # print("%d, %d, %d"%(i,left,right))
                value = numsSorted[i] + numsSorted[left] + numsSorted[right]
                if value == 0:
                    vals = sorted([numsSorted[i],numsSorted[left],numsSorted[right]])
                    if vals[0] not in solutionDict:
                        solutionDict[vals[0]] = {vals[1]:vals[2]}
                    elif vals[1] not in solutionDict[vals[0]]:
                            solutionDict[vals[0]][vals[1]] = vals[2]
                if value < 0:
                    left += 1
                else:
                    right -= 1
        solutions = []
        for topKey in solutionDict.keys():
            for midKey in solutionDict[topKey].keys():
                solutions.append([topKey,midKey,(topKey+midKey)*(-1)])
        return solutions
# O(n^2 time), O(n) space.
# Nested dictionaries were a very bad choice for this problem: better idea:
# Just stop when you start reaching positive numbers in i
# Skip repeated values of i
# After a solution, move l and r in 1