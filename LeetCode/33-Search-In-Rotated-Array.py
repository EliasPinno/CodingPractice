class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchRecursive(nums,target,0,len(nums)-1)
    
    def searchRecursive(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left == right: # Narrowed down to one element
            return left if nums[left] == target else -1
        if left == right-1: # Narrowed down to two elements
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1
        # General case: narrow down interval further
        middle = floor((right-left)/2) + left
        if (nums[middle] <= target and nums[right] >= target) or (nums[middle] > nums[right] and (nums[right] >= target or nums[middle] <= target)):
            return self.searchRecursive(nums,target,middle,right)
        else:
            return self.searchRecursive(nums,target,left,middle)

# Time: O(log n) Space: O(1)
            

