# Mutating original list 

def missingNumbers(nums):
    if len(nums) == 0:
        return [1,2]
    nums.append(nums[0])
    nums.append(nums[0])
    for i in range(len(nums)):
        nums[abs(nums[i])-1] *= -1
    solution = []
    for i in range(len(nums)):
        if nums[i] > 0:
            solution.append(i+1)
    return solution

# O(n) time, O(1) space