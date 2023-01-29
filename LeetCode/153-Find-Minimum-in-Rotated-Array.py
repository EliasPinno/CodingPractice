class Solution:
    def findMin(self, nums: List[int]) -> int:
        totalSize = len(nums)
        sol = self.checkBetween(nums,0,totalSize-1)
        return sol
    
    def checkBetween(self, nums: List[int], left: int, right: int) -> int:
        if left == right: # We narrowed down one possible location
            return nums[left]
        elif left == right-1: # Sublist len(2): minimum must be one of these two values
            return min(nums[left], nums[left+1])
        middle = floor((right-left)/2) + left
        left_elem = nums[left]
        right_elem = nums[right]
        middle_elem = nums[middle]
        if right_elem < middle_elem: # minimum is on the right side
            return self.checkBetween(nums,middle,right)
        else: # minimum is on the left side
            return self.checkBetween(nums,left,middle)
        
# O(n) space, O(log(n)) time