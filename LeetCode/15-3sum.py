class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        solutions = []
        for i in range(len(numsSorted)-2):
            left = i+1
            right = len(numsSorted)-1
            while left < right:
                # print("%d, %d, %d"%(i,left,right))
                value = numsSorted[i] + numsSorted[left] + numsSorted[right]
                if value == 0:
                    solutionPossible = sorted([numsSorted[i],numsSorted[left],numsSorted[right]])
                    unique = True
                    for solution in solutions:
                        isSame = True
                        for j in range(3):
                            if solution[j] != solutionPossible[j]:
                                isSame = False
                                break
                        if isSame:
                            unique = False
                            break
                    if unique:
                        solutions.append(solutionPossible)
                if value < 0:
                    left += 1
                else:
                    right -= 1
        return solutions
            
        
        
        
        
        
    
    
        